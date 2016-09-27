// Copyright (c) 2009 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "ui/base/win/mouse_wheel_util.h"

#include <windowsx.h>

#include "base/auto_reset.h"
#include "ui/base/view_prop.h"
#include "ui/gfx/win/hwnd_util.h"

namespace ui {

// Property used to indicate the HWND supports having mouse wheel messages
// rerouted to it.
static const char* const kHWNDSupportMouseWheelRerouting =
    "__HWND_MW_REROUTE_OK";

static bool IsBlpwtk1Window(HWND window) {
  char buf[MAX_PATH];
  int len = ::GetWindowTextA(window, buf, MAX_PATH-1);
  buf[len] = 0;
  if (0 == strncmp(buf, "WebkitCtrl ", 11)) {
    return true;
  }
  return false;
}

static bool WindowSupportsRerouteMouseWheel(HWND window) {
  while (GetWindowLong(window, GWL_STYLE) & WS_CHILD) {
    if (!IsWindow(window))
      break;

    if (ViewProp::GetValue(window, kHWNDSupportMouseWheelRerouting) != NULL) {
      return true;
    }

    // SHEZ: If this is a blpwtk1 window, then it supports rerouting mouse
    // SHEZ: wheel.
    if (IsBlpwtk1Window(window)) {
      return true;
    }

    window = GetParent(window);
  }
  return false;
}

static bool IsCompatibleWithMouseWheelRedirection(HWND window) {
  std::wstring class_name = gfx::GetClassName(window);
  // Mousewheel redirection to comboboxes is a surprising and
  // undesireable user behavior.
  return !(class_name == L"ComboBox" ||
           class_name == L"ComboBoxEx32");
}

static bool CanRedirectMouseWheelFrom(HWND window) {
  std::wstring class_name = gfx::GetClassName(window);

  // Older Thinkpad mouse wheel drivers create a window under mouse wheel
  // pointer. Detect if we are dealing with this window. In this case we
  // don't need to do anything as the Thinkpad mouse driver will send
  // mouse wheel messages to the right window.
  if ((class_name == L"Syn Visual Class") ||
     (class_name == L"SynTrackCursorWindowClass"))
    return false;

  return true;
}

static bool IsInsideBlpwtk1Window(HWND window) {
  while (GetWindowLong(window, GWL_STYLE) & WS_CHILD) {
    if (!IsWindow(window))
      break;

    if (IsBlpwtk1Window(window)) {
      return true;
    }

    window = GetParent(window);
  }
  return false;
}

ViewProp* SetWindowSupportsRerouteMouseWheel(HWND hwnd) {
  return new ViewProp(hwnd, kHWNDSupportMouseWheelRerouting,
                      reinterpret_cast<HANDLE>(true));
}

bool RerouteMouseWheel(HWND window, WPARAM w_param, LPARAM l_param, bool reroute_to_any_related_window) {
  // Since this is called from a subclass for every window, we can get
  // here recursively. This will happen if, for example, a control
  // reflects wheel scroll messages to its parent. Bail out if we got
  // here recursively.
  static bool recursion_break = false;
  if (recursion_break)
    return false;
  // Check if this window's class has a bad interaction with rerouting.
  if (!IsCompatibleWithMouseWheelRedirection(window))
    return false;

  DWORD current_process = GetCurrentProcessId();
  POINT wheel_location = { GET_X_LPARAM(l_param), GET_Y_LPARAM(l_param) };
  HWND window_under_wheel = WindowFromPoint(wheel_location);

  if (!CanRedirectMouseWheelFrom(window_under_wheel))
    return false;

  // Find the lowest Chrome window in the hierarchy that can be the
  // target of mouse wheel redirection.
  while (window != window_under_wheel) {
    // If window_under_wheel is not a valid Chrome window, then return true to
    // suppress further processing of the message.
    if (!::IsWindow(window_under_wheel))
      return true;
    DWORD wheel_window_process = 0;
    GetWindowThreadProcessId(window_under_wheel, &wheel_window_process);
    if (current_process != wheel_window_process) {
      if (IsChild(window, window_under_wheel)) {
        // If this message is reflected from a child window in a different
        // process (happens with out of process windowed plugins) then
        // we don't want to reroute the wheel message.
        // SHEZ: Except, if that window happens to be our blpwtk1 window.
        if (!IsInsideBlpwtk1Window(window_under_wheel)) {
          return false;
        }
      } else {
        if (!reroute_to_any_related_window ||
            (GetAncestor(window, GA_ROOTOWNER) != GetAncestor(window_under_wheel, GA_ROOTOWNER))) {
          // The wheel is scrolling over an unrelated window. Make sure that we
          // have marked that window as supporting mouse wheel rerouting.
          // Otherwise, we cannot send random WM_MOUSEWHEEL messages to arbitrary
          // windows. So just drop the message.
          if (!WindowSupportsRerouteMouseWheel(window_under_wheel))
            return true;
        }
      }
    }

    // If the child window is transparent, then it is not interested in
    // receiving wheel events.
    if (IsChild(window, window_under_wheel) &&
        ::GetWindowLong(
            window_under_wheel, GWL_EXSTYLE) & WS_EX_TRANSPARENT) {
      return false;
    }

    // window_under_wheel is a Chrome window.  If allowed, redirect.
    if (IsCompatibleWithMouseWheelRedirection(window_under_wheel)) {
      base::AutoReset<bool> auto_reset_recursion_break(&recursion_break, true);
      SendMessage(window_under_wheel, WM_MOUSEWHEEL, w_param, l_param);
      return true;
    }
    // If redirection is disallowed, try the parent.
    window_under_wheel = GetAncestor(window_under_wheel, GA_PARENT);
  }
  // If we traversed back to the starting point, we should process
  // this message normally; return false.
  return false;
}

}  // namespace ui
