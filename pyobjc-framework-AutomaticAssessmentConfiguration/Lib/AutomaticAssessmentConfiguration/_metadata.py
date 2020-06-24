# This file is generated by objective.metadata
#
# Last update: Thu Jun 25 00:10:32 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$AEAssessmentErrorDomain$"""
enums = """$AEAssessmentErrorUnknown@1$AEAutocorrectModeNone@0$AEAutocorrectModePunctuation@2$AEAutocorrectModeSpelling@1$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"AEAssessmentConfiguration",
        b"allowsAccessibilitySpeech",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"allowsActivityContinuation",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"allowsContinuousPathKeyboard",
        {"retval": {"type": b"Z"}},
    )
    r(b"AEAssessmentConfiguration", b"allowsDictation", {"retval": {"type": b"Z"}})
    r(
        b"AEAssessmentConfiguration",
        b"allowsKeyboardShortcuts",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"allowsPasswordAutoFill",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"allowsPredictiveKeyboard",
        {"retval": {"type": b"Z"}},
    )
    r(b"AEAssessmentConfiguration", b"allowsSpellCheck", {"retval": {"type": b"Z"}})
    r(
        b"AEAssessmentConfiguration",
        b"setAllowsAccessibilitySpeech:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"setAllowsActivityContinuation:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"setAllowsContinuousPathKeyboard:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"setAllowsDictation:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"setAllowsKeyboardShortcuts:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"setAllowsPasswordAutoFill:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"setAllowsPredictiveKeyboard:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AEAssessmentConfiguration",
        b"setAllowsSpellCheck:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AEAssessmentSession",
        b"beginSessionWithConfiguration:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"AEAssessmentSession",
        b"endWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"AEAssessmentSession",
        b"invalidationHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                }
            }
        },
    )
    r(b"AEAssessmentSession", b"isActive", {"retval": {"type": "Z"}})
    r(
        b"AEAssessmentSession",
        b"setInvalidationHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"NSObject",
        b"assessmentSession:failedToBeginWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"assessmentSession:wasInterruptedWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"assessmentSessionDidBegin:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"assessmentSessionDidEnd:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
