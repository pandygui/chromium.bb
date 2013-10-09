/*
 * Copyright (C) 2009 Google Inc. All rights reserved.
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

#include "config.h"
#include "bindings/v8/BindingState.h"

#include "bindings/v8/ScriptController.h"
#include "bindings/v8/V8Binding.h"
#include "core/page/DOMWindow.h"
#include "core/page/Frame.h"
#include "wtf/StdLibExtras.h"

namespace WebCore {

BindingState* BindingState::instance()
{
    DEFINE_STATIC_LOCAL(BindingState, bindingStateForV8, ());
    return &bindingStateForV8;
}

static v8::Handle<v8::Context> activeContext()
{
    v8::Handle<v8::Context> context = v8::Context::GetCalling();
    if (!context.IsEmpty() && DOMWrapperWorld::contextHasCorrectPrototype(context))
        return context;
    // Unfortunately, when processing script from a plug-in, we might not
    // have a calling context. In those cases, we fall back to the
    // entered context.
    return v8::Context::GetEntered();
}

DOMWindow* activeDOMWindow(BindingState*)
{
    return toDOMWindow(activeContext());
}

DOMWindow* firstDOMWindow(BindingState*)
{
    return toDOMWindow(v8::Context::GetEntered());
}

Document* currentDocument(BindingState*)
{
    return toDOMWindow(v8::Context::GetCurrent())->document();
}

void printErrorMessageForFrame(Frame* frame, const String& message)
{
    if (!frame)
        return;
    frame->document()->domWindow()->printErrorMessage(message);
}

}
