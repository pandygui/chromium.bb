/*
 * Copyright (C) 2013 Bloomberg Finance L.P.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

#include <blpwtk2_toolkitimpl.h>

#include <blpwtk2_statics.h>
#include <blpwtk2_constants.h>
#include <blpwtk2_browserthread.h>
#include <blpwtk2_browsercontextimpl.h>
#include <blpwtk2_browsercontextimplmanager.h>
#include <blpwtk2_inprocessrenderer.h>
#include <blpwtk2_inprocessrendererhost.h>
#include <blpwtk2_browsermainrunner.h>
#include <blpwtk2_mainmessagepump.h>
#include <blpwtk2_processclientimpl.h>
#include <blpwtk2_processhostimpl.h>
#include <blpwtk2_products.h>
#include <blpwtk2_profilecreateparams.h>
#include <blpwtk2_profileproxy.h>
#include <blpwtk2_webviewcreateparams.h>
#include <blpwtk2_webviewimpl.h>
#include <blpwtk2_webviewproxy.h>

#include <base/command_line.h>
#include <base/file_util.h>
#include <base/files/file_enumerator.h>
#include <base/message_loop.h>
#include <base/path_service.h>
#include <base/synchronization/waitable_event.h>
#include <base/threading/thread_restrictions.h>
#include <chrome/common/chrome_paths.h>
#include <content/public/app/content_main_runner.h>
#include <content/public/app/startup_helper_win.h>  // for InitializeSandboxInfo
#include <content/public/common/content_switches.h>
#include <content/browser/web_contents/web_contents_view_win.h>
#include <ipc/ipc_channel.h>
#include <sandbox/win/src/win_utils.h>

#include <TlHelp32.h>  // for CreateToolhelp32Snapshot

extern HANDLE g_instDLL;  // set in DllMain

namespace blpwtk2 {

static base::MessagePump* messagePumpForUIFactory()
{
    if (Statics::isInApplicationMainThread()) {
        return new MainMessagePump();
    }

    return new base::MessagePumpForUI();
}

static bool loadRunningProcessIds(std::set<int>* pids)
{
    HANDLE hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hProcessSnap == INVALID_HANDLE_VALUE) {
        return false;
    }

    PROCESSENTRY32 pe32;
    pe32.dwSize = sizeof(PROCESSENTRY32);
    if (!Process32First(hProcessSnap, &pe32)) {
        CloseHandle(hProcessSnap);
        return false;
    }

    do {
        pids->insert(pe32.th32ProcessID);
    } while (Process32Next(hProcessSnap, &pe32));

    CloseHandle(hProcessSnap);
    return true;
}

// Returns true if 'dirName' matches the pattern "<prefix><number>_<number>"
// for any prefix in 'prefixes'.  If so, load the first <number> into 'pid'.
static bool isScopedDir(const std::wstring& dirName,
                        const std::vector<std::wstring>& prefixes,
                        int *pid)
{
    const wchar_t* dirNameC = dirName.c_str();
    for (std::size_t i = 0; i < prefixes.size(); ++i) {
        if (prefixes[i].length() >= dirName.length()) {
            continue;
        }
        if (0 != wcsncmp(dirNameC, prefixes[i].data(), prefixes[i].length())) {
            continue;
        }
        const wchar_t* pidStart = dirNameC + prefixes[i].length();
        if (!iswdigit(*pidStart)) {
            continue;
        }
        *pid = *pidStart - '0';
        const wchar_t* pidEnd = pidStart + 1;
        while (iswdigit(*pidEnd)) {
            *pid *= 10;
            *pid += *pidEnd - '0';
            ++pidEnd;
        }
        if (*pidEnd != '_') {
            continue;
        }
        const wchar_t* randStart = pidEnd + 1;
        if (!iswdigit(*randStart)) {
            continue;
        }
        const wchar_t* randEnd = randStart + 1;
        while (iswdigit(*randEnd)) {
            ++randEnd;
        }
        if (*randEnd != 0) {
            continue;
        }
        return true;
    }
    return false;
}

static void deleteTemporaryScopedDirs()
{
    std::set<int> pids;
    if (!loadRunningProcessIds(&pids)) {
        return;
    }

    base::FilePath tempPath;
    if (!file_util::GetTempDir(&tempPath)) {
        return;
    }

    std::vector<std::wstring> prefixes;
    prefixes.push_back(L"scoped_dir");
    prefixes.push_back(L"scoped_dir_");
    prefixes.push_back(L"blpwtk2_");

    int count = 0;
    base::FileEnumerator enumerator(
        tempPath,
        false,
        base::FileEnumerator::DIRECTORIES);
    for (base::FilePath path = enumerator.Next(); !path.empty(); path = enumerator.Next()) {
        std::wstring baseName = path.BaseName().value();
        int pid;
        if (isScopedDir(baseName, prefixes, &pid)) {
            if (pids.end() == pids.find(pid)) {
                file_util::Delete(path, true);
                ++count;
                if (count == 100) {
                    // There are thousands of these directories currently in
                    // people's TEMP.  We'll just delete a 100 of them at a
                    // time, and over time, they will all be gone.
                    // This is so that blpwtk2 doesn't take a really really
                    // long time to startup the first time this function is
                    // called.
                    return;
                }
            }
        }
    }
}

static ToolkitImpl* g_instance = 0;

ToolkitImpl* ToolkitImpl::instance()
{
    return g_instance;
}

ToolkitImpl::ToolkitImpl(const StringRef& dictionaryPath,
                         bool pluginDiscoveryEnabled)
: d_threadsStarted(false)
, d_threadsStopped(false)
, d_defaultProfile(0)
, d_mainDelegate(false, pluginDiscoveryEnabled)
, d_dictionaryPath(dictionaryPath.data(), dictionaryPath.length())
{
    DCHECK(!g_instance);
    g_instance = this;

    deleteTemporaryScopedDirs();

    d_mainDelegate.setRendererInfoMap(&d_rendererInfoMap);
    base::MessageLoop::InitMessagePumpForUIFactory(&messagePumpForUIFactory);
}

ToolkitImpl::~ToolkitImpl()
{
    DCHECK(!d_threadsStarted || d_threadsStopped);
    DCHECK(g_instance);
    g_instance = 0;
}

void ToolkitImpl::startupThreads()
{
    DCHECK(!d_threadsStarted);

    content::InitializeSandboxInfo(&d_sandboxInfo);
    d_mainRunner.reset(content::ContentMainRunner::Create());
    int rc = d_mainRunner->Initialize((HINSTANCE)g_instDLL, &d_sandboxInfo, &d_mainDelegate);
    DCHECK(-1 == rc);  // it returns -1 for success!!

    if (!d_dictionaryPath.empty()) {
        base::ThreadRestrictions::ScopedAllowIO allowIO;
        PathService::Override(chrome::DIR_APP_DICTIONARIES, base::FilePath::FromUTF8Unsafe(d_dictionaryPath));
    }

    if (Statics::isRendererMainThreadMode()) {
        new base::MessageLoop(base::MessageLoop::TYPE_UI);
        content::WebContentsViewWin::disableHookOnRoot();
        d_browserThread.reset(new BrowserThread(&d_sandboxInfo));
    }
    else {
        DCHECK(Statics::isOriginalThreadMode());
        d_browserMainRunner.reset(new BrowserMainRunner(&d_sandboxInfo));
    }

    InProcessRenderer::init();
    MainMessagePump::current()->init();

    if (Statics::isRendererMainThreadMode()) {
        std::string channelId = IPC::Channel::GenerateVerifiedChannelID(BLPWTK2_VERSION);

        d_browserThread->messageLoop()->PostTask(
            FROM_HERE,
            base::Bind(&ToolkitImpl::createInProcessHost,
                       base::Unretained(this),
                       channelId));
        d_browserThread->sync();  // TODO: remove this sync
        d_inProcessClient.reset(
            new ProcessClientImpl(channelId,
                                  InProcessRenderer::ipcTaskRunner()));
    }

    d_threadsStarted = true;
}

void ToolkitImpl::shutdownThreads()
{
    DCHECK(!d_threadsStopped);
    DCHECK(d_threadsStarted);

    if (d_defaultProfile) {
        d_defaultProfile->destroy();
        d_defaultProfile = 0;
    }

    if (Statics::isRendererMainThreadMode()) {
        d_inProcessClient.reset();
        d_browserThread->messageLoop()->PostTask(
            FROM_HERE,
            base::Bind(&ToolkitImpl::destroyInProcessHost,
                       base::Unretained(this)));

        d_browserThread->sync();  // make sure any WebView::destroy has been
                                  // handled by the browser-main thread
    }

    MainMessagePump::current()->cleanup();
    InProcessRenderer::cleanup();

    if (Statics::isRendererMainThreadMode()) {
        delete base::MessageLoop::current();
        d_browserThread.reset();
    }
    else {
        DCHECK(Statics::isOriginalThreadMode());
        d_browserMainRunner.reset();
    }

    d_mainRunner->Shutdown();
    d_mainRunner.reset();

    sandbox::CallOnExitHandlers();

    d_threadsStopped = true;
}

void ToolkitImpl::setRendererUsesInProcessPlugins(int renderer)
{
    d_rendererInfoMap.setRendererUsesInProcessPlugins(renderer);
}

void ToolkitImpl::registerPlugin(const char* pluginPath)
{
    d_mainDelegate.registerPlugin(pluginPath);
}

Profile* ToolkitImpl::createProfile(const ProfileCreateParams& params)
{
    DCHECK(Statics::isInApplicationMainThread());
    DCHECK(Statics::isRendererMainThreadMode()
        || Statics::isOriginalThreadMode());

    if (!d_threadsStarted) {
        startupThreads();
    }

    std::string dataDir(params.dataDir().data(), params.dataDir().length());
    if (Statics::isRendererMainThreadMode()) {
        return new ProfileProxy(d_inProcessClient.get(),
                                Statics::getUniqueRoutingId(),
                                dataDir,
                                params.diskCacheEnabled());
    }
    else {
        DCHECK(Statics::isOriginalThreadMode());
        DCHECK(Statics::browserContextImplManager);
        return Statics::browserContextImplManager->createBrowserContextImpl(
            dataDir,
            params.diskCacheEnabled());
    }
}

bool ToolkitImpl::hasDevTools()
{
    DCHECK(Statics::isInApplicationMainThread());
    return Statics::hasDevTools;
}

void ToolkitImpl::destroy()
{
    DCHECK(Statics::isInApplicationMainThread());
    DCHECK(0 == Statics::numProfiles);
    if (d_threadsStarted) {
        shutdownThreads();
    }
    delete this;
}

WebView* ToolkitImpl::createWebView(NativeView parent,
                                    WebViewDelegate* delegate,
                                    const WebViewCreateParams& params)
{
    DCHECK(Statics::isInApplicationMainThread());
    DCHECK(Statics::isRendererMainThreadMode()
        || Statics::isOriginalThreadMode());

    if (!d_threadsStarted) {
        startupThreads();
    }

    Profile* profile = params.profile();
    if (!profile) {
        if (!d_defaultProfile) {
            d_defaultProfile = createProfile(ProfileCreateParams(""));
        }
        profile = d_defaultProfile;
    }

    bool singleProcess = CommandLine::ForCurrentProcess()->HasSwitch(switches::kSingleProcess);
    // Enforce in-process renderer if "--single-process" is specified on the
    // command line.  This is useful for debugging.
    int rendererAffinity = singleProcess ? Constants::IN_PROCESS_RENDERER
                                         : params.rendererAffinity();

    DCHECK(singleProcess ||
           rendererAffinity == Constants::ANY_OUT_OF_PROCESS_RENDERER ||
           d_rendererInfoMap.dcheckProfileForRenderer(rendererAffinity, profile));

    if (Statics::isRendererMainThreadMode()) {
        DCHECK(d_browserThread.get());

        ProfileProxy* profileProxy = static_cast<ProfileProxy*>(profile);
        return new WebViewProxy(d_inProcessClient.get(),
                                Statics::getUniqueRoutingId(),
                                profileProxy,
                                delegate,
                                parent,
                                rendererAffinity,
                                params.initiallyVisible(),
                                params.takeFocusOnMouseDown());
    }
    else if (Statics::isOriginalThreadMode()) {
        BrowserContextImpl* browserContext =
            static_cast<BrowserContextImpl*>(profile);
        int hostAffinity =
            d_browserMainRunner->obtainHostAffinity(browserContext,
                                                    rendererAffinity,
                                                    &d_rendererInfoMap);
        return new WebViewImpl(delegate,
                               parent,
                               browserContext,
                               hostAffinity,
                               params.initiallyVisible(),
                               params.takeFocusOnMouseDown());
    }

    NOTREACHED();
    return 0;
}

void ToolkitImpl::onRootWindowPositionChanged(gfx::NativeView root)
{
    DCHECK(Statics::isInApplicationMainThread());
    if (d_threadsStarted && Statics::isRendererMainThreadMode()) {
        DCHECK(d_browserThread);
        d_browserThread->messageLoop()->PostTask(FROM_HERE,
            base::Bind(&content::WebContentsViewWin::onRootWindowPositionChanged, root));
    }
}

void ToolkitImpl::onRootWindowSettingChange(gfx::NativeView root)
{
    DCHECK(Statics::isInApplicationMainThread());
    if (d_threadsStarted && Statics::isRendererMainThreadMode()) {
        DCHECK(d_browserThread);
        d_browserThread->messageLoop()->PostTask(FROM_HERE,
            base::Bind(&content::WebContentsViewWin::onRootWindowSettingChange, root));
    }
}

bool ToolkitImpl::preHandleMessage(const NativeMsg* msg)
{
    DCHECK(Statics::isInApplicationMainThread());
    DCHECK(PumpMode::MANUAL == Statics::pumpMode);
    if (d_threadsStarted) {
        return MainMessagePump::current()->preHandleMessage(*msg);
    }
    return false;
}

void ToolkitImpl::postHandleMessage(const NativeMsg* msg)
{
    DCHECK(Statics::isInApplicationMainThread());
    DCHECK(PumpMode::MANUAL == Statics::pumpMode);
    if (d_threadsStarted) {
        MainMessagePump::current()->postHandleMessage(*msg);
    }
}

void ToolkitImpl::createInProcessHost(const std::string& channelId)
{
    DCHECK(Statics::isInBrowserMainThread());
    d_inProcessHost.reset(new ProcessHostImpl(channelId,
                                              &d_rendererInfoMap,
                                              d_browserThread->mainRunner()));
}

void ToolkitImpl::destroyInProcessHost()
{
    DCHECK(Statics::isInBrowserMainThread());
    d_inProcessHost.reset();
}

}  // close namespace blpwtk2

