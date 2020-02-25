"""
Python mapping for the AutomaticAssessmentConfiguration framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import objc
import sys
import Foundation

from AutomaticAssessmentConfiguration import _metadata


sys.modules["AutomaticAssessmentConfiguration"] = mod = objc.ObjCLazyModule(
    "AutomaticAssessmentConfiguration",
    "com.apple.AutomaticAssessmentConfiguration",
    objc.pathForFramework("/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (Foundation,),
)

import AutomaticAssessmentConfiguration
import objc
AutomaticAssessmentConfiguration.AEAssessmentSession = objc.lookUpClass('AutomaticAssessmentConfiguration.AEAssessmentSession')
AutomaticAssessmentConfiguration.AEAssessmentConfiguration = objc.lookUpClass('AutomaticAssessmentConfiguration.AEAssessmentConfiguration')

import sys

del sys.modules["AutomaticAssessmentConfiguration._metadata"]