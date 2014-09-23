/*
 * Copyright (C) 2011 Google Inc. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *
 *     * Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above
 * copyright notice, this list of conditions and the following disclaimer
 * in the documentation and/or other materials provided with the
 * distribution.
 *     * Neither the name of Google Inc. nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef InspectorPageAgent_h
#define InspectorPageAgent_h


#include "InspectorFrontend.h"
#include "core/inspector/InspectorBaseAgent.h"
#include "modules/geolocation/GeolocationPosition.h"
#include "wtf/HashMap.h"
#include "wtf/text/WTFString.h"

namespace WebCore {

class Resource;
class DOMWrapperWorld;
class Document;
class DocumentLoader;
class Frame;
class GraphicsContext;
class GraphicsLayer;
class InjectedScriptManager;
class InspectorClient;
class InspectorOverlay;
class InstrumentingAgents;
class IntSize;
class KURL;
class LayoutRect;
class Page;
class RenderObject;
class SharedBuffer;
class StyleResolver;

typedef String ErrorString;

class InspectorPageAgent : public InspectorBaseAgent<InspectorPageAgent>, public InspectorBackendDispatcher::PageCommandHandler {
    WTF_MAKE_NONCOPYABLE(InspectorPageAgent);
public:
    enum ResourceType {
        DocumentResource,
        StylesheetResource,
        ImageResource,
        Font,
        ScriptResource,
        XHRResource,
        WebSocketResource,
        OtherResource
    };

    static PassOwnPtr<InspectorPageAgent> create(InstrumentingAgents*, Page*, InspectorCompositeState*, InjectedScriptManager*, InspectorClient*, InspectorOverlay*);

    static bool cachedResourceContent(Resource*, String* result, bool* base64Encoded);
    static bool sharedBufferContent(PassRefPtr<SharedBuffer>, const String& textEncodingName, bool withBase64Encode, String* result);

    static PassRefPtr<SharedBuffer> resourceData(Frame*, const KURL&, String* textEncodingName);
    static Resource* cachedResource(Frame*, const KURL&);
    static TypeBuilder::Page::ResourceType::Enum resourceTypeJson(ResourceType);
    static ResourceType cachedResourceType(const Resource&);
    static TypeBuilder::Page::ResourceType::Enum cachedResourceTypeJson(const Resource&);

    // Page API for InspectorFrontend
    virtual void enable(ErrorString*);
    virtual void disable(ErrorString*);
    virtual void addScriptToEvaluateOnLoad(ErrorString*, const String& source, String* result);
    virtual void removeScriptToEvaluateOnLoad(ErrorString*, const String& identifier);
    virtual void reload(ErrorString*, const bool* optionalIgnoreCache, const String* optionalScriptToEvaluateOnLoad, const String* optionalScriptPreprocessor);
    virtual void navigate(ErrorString*, const String& url);
    virtual void getNavigationHistory(ErrorString*, int*, RefPtr<TypeBuilder::Array<TypeBuilder::Page::NavigationEntry> >&);
    virtual void navigateToHistoryEntry(ErrorString*, int);
    virtual void getCookies(ErrorString*, RefPtr<TypeBuilder::Array<TypeBuilder::Page::Cookie> >& cookies);
    virtual void deleteCookie(ErrorString*, const String& cookieName, const String& url);
    virtual void getResourceTree(ErrorString*, RefPtr<TypeBuilder::Page::FrameResourceTree>&);
    virtual void getResourceContent(ErrorString*, const String& frameId, const String& url, String* content, bool* base64Encoded);
    virtual void searchInResource(ErrorString*, const String& frameId, const String& url, const String& query, const bool* optionalCaseSensitive, const bool* optionalIsRegex, RefPtr<TypeBuilder::Array<TypeBuilder::Page::SearchMatch> >&);
    virtual void setDocumentContent(ErrorString*, const String& frameId, const String& html);
    virtual void setDeviceMetricsOverride(ErrorString*, int width, int height, double deviceScaleFactor, bool emulateViewport, bool fitWindow, const bool* optionalTextAutosizing, const double* optionalFontScaleFactor);
    virtual void setShowPaintRects(ErrorString*, bool show);
    virtual void setShowDebugBorders(ErrorString*, bool show);
    virtual void setShowFPSCounter(ErrorString*, bool show);
    virtual void setContinuousPaintingEnabled(ErrorString*, bool enabled);
    virtual void setShowScrollBottleneckRects(ErrorString*, bool show);
    virtual void getScriptExecutionStatus(ErrorString*, PageCommandHandler::Result::Enum*);
    virtual void setScriptExecutionDisabled(ErrorString*, bool);
    virtual void setGeolocationOverride(ErrorString*, const double*, const double*, const double*);
    virtual void clearGeolocationOverride(ErrorString*);
    virtual void setDeviceOrientationOverride(ErrorString*, double, double, double);
    virtual void clearDeviceOrientationOverride(ErrorString*);
    virtual void setTouchEmulationEnabled(ErrorString*, bool);
    virtual void setEmulatedMedia(ErrorString*, const String&);
    virtual void captureScreenshot(ErrorString*, const String* format, const int* quality, const int* maxWidth, const int* maxHeight, String* data, RefPtr<TypeBuilder::Page::ScreencastFrameMetadata>& out_metadata);
    virtual void canScreencast(ErrorString*, bool*);
    virtual void startScreencast(ErrorString*, const String* format, const int* quality, const int* maxWidth, const int* maxHeight);
    virtual void stopScreencast(ErrorString*);
    virtual void handleJavaScriptDialog(ErrorString*, bool accept, const String* promptText);
    virtual void queryUsageAndQuota(WebCore::ErrorString*, const WTF::String&, WTF::RefPtr<WebCore::TypeBuilder::Page::Quota>&, WTF::RefPtr<WebCore::TypeBuilder::Page::Usage>&);
    virtual void setShowViewportSizeOnResize(ErrorString*, bool show, const bool* showGrid);

    // Geolocation override helper.
    GeolocationPosition* overrideGeolocationPosition(GeolocationPosition*);

    // Text autosizing override helpers.
    bool overrideTextAutosizing(bool);
    // Note: This is used by Settings::deviceScaleAdjustment to calculate the overridden device scale adjustment.
    float overrideFontScaleFactor(float);

    // InspectorInstrumentation API
    void didClearWindowObjectInWorld(Frame*, DOMWrapperWorld*);
    void domContentLoadedEventFired(Frame*);
    void loadEventFired(Frame*);
    void didCommitLoad(Frame*, DocumentLoader*);
    void frameAttachedToParent(Frame*);
    void frameDetachedFromParent(Frame*);
    void loaderDetachedFromFrame(DocumentLoader*);
    void frameStartedLoading(Frame*);
    void frameStoppedLoading(Frame*);
    void frameScheduledNavigation(Frame*, double delay);
    void frameClearedScheduledNavigation(Frame*);
    void willRunJavaScriptDialog(const String& message);
    void didRunJavaScriptDialog();
    bool applyViewportStyleOverride(StyleResolver*);
    void applyEmulatedMedia(String*);
    void didPaint(RenderObject*, const GraphicsLayer*, GraphicsContext*, const LayoutRect&);
    void didLayout(RenderObject*);
    void didScroll();
    void didResizeMainFrame();
    void didRecalculateStyle();
    void scriptsEnabled(bool isEnabled);

    // Inspector Controller API
    virtual void setFrontend(InspectorFrontend*);
    virtual void clearFrontend();
    virtual void restore();

    void webViewResized(const IntSize&);

    // Cross-agents API
    Page* page() { return m_page; }
    Frame* mainFrame();
    String createIdentifier();
    Frame* frameForId(const String& frameId);
    String frameId(Frame*);
    bool hasIdForFrame(Frame*) const;
    String loaderId(DocumentLoader*);
    Frame* findFrameWithSecurityOrigin(const String& originRawString);
    Frame* assertFrame(ErrorString*, const String& frameId);
    String scriptPreprocessorSource() { return m_scriptPreprocessorSource; }
    const AtomicString& resourceSourceMapURL(const String& url);
    bool deviceMetricsOverrideEnabled();
    static DocumentLoader* assertDocumentLoader(ErrorString*, Frame*);

private:
    static void resourceContent(ErrorString*, Frame*, const KURL&, String* result, bool* base64Encoded);

    InspectorPageAgent(InstrumentingAgents*, Page*, InspectorCompositeState*, InjectedScriptManager*, InspectorClient*, InspectorOverlay*);
    bool deviceMetricsChanged(int width, int height, double deviceScaleFactor, bool emulateViewport, bool fitWindow, double fontScaleFactor, bool textAutosizing);
    void updateViewMetrics(int width, int height, double deviceScaleFactor, bool emulateViewport, bool fitWindow);
    void updateTouchEventEmulationInPage(bool);
    bool forceCompositingMode(ErrorString*);

    static bool dataContent(const char* data, unsigned size, const String& textEncodingName, bool withBase64Encode, String* result);

    PassRefPtr<TypeBuilder::Page::Frame> buildObjectForFrame(Frame*);
    PassRefPtr<TypeBuilder::Page::FrameResourceTree> buildObjectForFrameTree(Frame*);
    Page* m_page;
    InjectedScriptManager* m_injectedScriptManager;
    InspectorClient* m_client;
    InspectorFrontend::Page* m_frontend;
    InspectorOverlay* m_overlay;
    long m_lastScriptIdentifier;
    String m_pendingScriptToEvaluateOnLoadOnce;
    String m_scriptToEvaluateOnLoadOnce;
    String m_pendingScriptPreprocessor;
    String m_scriptPreprocessorSource;
    HashMap<Frame*, String> m_frameToIdentifier;
    HashMap<String, Frame*> m_identifierToFrame;
    HashMap<DocumentLoader*, String> m_loaderToIdentifier;
    bool m_enabled;
    bool m_geolocationOverridden;
    bool m_ignoreScriptsEnabledNotification;
    bool m_deviceMetricsOverridden;
    bool m_emulateViewportEnabled;
    RefPtr<GeolocationPosition> m_geolocationPosition;
    RefPtr<GeolocationPosition> m_platformGeolocationPosition;
};


} // namespace WebCore


#endif // !defined(InspectorPagerAgent_h)
