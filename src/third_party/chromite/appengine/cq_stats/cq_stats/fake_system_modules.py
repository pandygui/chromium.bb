# Copyright 2015 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Fake out system python modules that are not available on AE.

Chromite imports some standard python modules that are not available on the
restricted sandbox environment on appengine. Fake out this modules such that
imports don't break, but any attempt to use the modules blows up obviously.
"""

from __future__ import print_function

import os


FAKE_HOMEDIR = '/tmp/an_obviously_non_existent_home_dir'
def _expanduser(_):
  """A fake implementation of os.path.expanduser.

  os.path.expanduser needs to import 'pwd' that is not available on appengine.
  In fact, the concept of HOMEDIR doesn't make sense at all. So, patch it to
  return a safe fake path. If we try to use it anywhere, it will fail obviously.
  """
  return FAKE_HOMEDIR


# Importing this module has the side effect of patching all of the following
# library modules / classes / functions.
os.path.expanduser = _expanduser
