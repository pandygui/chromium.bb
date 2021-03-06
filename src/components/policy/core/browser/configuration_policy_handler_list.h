// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef COMPONENTS_POLICY_CORE_BROWSER_CONFIGURATION_POLICY_HANDLER_LIST_H_
#define COMPONENTS_POLICY_CORE_BROWSER_CONFIGURATION_POLICY_HANDLER_LIST_H_

#include <vector>

#include "base/callback.h"
#include "base/macros.h"
#include "base/memory/scoped_ptr.h"
#include "components/policy/core/common/policy_details.h"
#include "components/policy/policy_export.h"

class PrefValueMap;

namespace policy {

class ConfigurationPolicyHandler;
class PolicyErrorMap;
struct PolicyHandlerParameters;
class PolicyMap;
struct PolicyToPreferenceMapEntry;
class Schema;

// Converts policies to their corresponding preferences by applying a list of
// ConfigurationPolicyHandler objects. This includes error checking and
// cleaning up policy values for displaying.
class POLICY_EXPORT ConfigurationPolicyHandlerList {
 public:
  typedef base::Callback<void(PolicyHandlerParameters*)>
      PopulatePolicyHandlerParametersCallback;

  explicit ConfigurationPolicyHandlerList(
      const PopulatePolicyHandlerParametersCallback& parameters_callback,
      const GetChromePolicyDetailsCallback& details_callback);
  ~ConfigurationPolicyHandlerList();

  // Adds a policy handler to the list.
  void AddHandler(scoped_ptr<ConfigurationPolicyHandler> handler);

  // Translates |policies| to their corresponding preferences in |prefs|.
  // Any errors found while processing the policies are stored in |errors|.
  // |prefs| or |errors| can be NULL, and won't be filled in that case.
  void ApplyPolicySettings(const PolicyMap& policies,
                           PrefValueMap* prefs,
                           PolicyErrorMap* errors) const;

  // Converts sensitive policy values to others more appropriate for displaying.
  void PrepareForDisplaying(PolicyMap* policies) const;

 private:
  std::vector<ConfigurationPolicyHandler*> handlers_;
  const PopulatePolicyHandlerParametersCallback parameters_callback_;
  const GetChromePolicyDetailsCallback details_callback_;

  DISALLOW_COPY_AND_ASSIGN(ConfigurationPolicyHandlerList);
};

// Callback with signature of BuildHandlerList(), to be used in constructor of
// BrowserPolicyConnector.
typedef base::Callback<scoped_ptr<ConfigurationPolicyHandlerList>(
    const Schema&)> HandlerListFactory;

}  // namespace policy

#endif  // COMPONENTS_POLICY_CORE_BROWSER_CONFIGURATION_POLICY_HANDLER_LIST_H_
