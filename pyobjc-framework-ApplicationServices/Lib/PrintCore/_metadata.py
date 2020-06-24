# This file is generated by objective.metadata
#
# Last update: Thu Jun 25 00:07:48 2020
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
misc.update(
    {
        "PMPaperMargins": objc.createStructType(
            "PMPaperMargins", b"{PMRect=dddd}", ["top", "left", "bottom", "right"]
        ),
        "PMResolution": objc.createStructType(
            "PMResolution", b"{PMResolution=dd}", ["hRes", "vRes"]
        ),
        "PMLanguageInfo": objc.createStructType(
            "PMLanguageInfo",
            b"{PMLanguageInfo=[33C][33C][33C]}",
            ["level", "version", "release"],
        ),
        "PMRect": objc.createStructType(
            "PMRect", b"{PMRect=dddd}", ["top", "left", "bottom", "right"]
        ),
    }
)
constants = """$$"""
enums = """$kAllPPDDomains@1$kCUPSPPDDomain@6$kLocalPPDDomain@3$kNetworkPPDDomain@4$kPMAllocationFailure@-108$kPMBorderDoubleHairline@2$kPMBorderDoubleThickline@4$kPMBorderSingleHairline@1$kPMBorderSingleThickline@3$kPMCMYKColorSpaceModel@3$kPMCVMSymbolNotFound@-9662$kPMCancel@128$kPMCloseFailed@-9785$kPMColorSpaceModelCount@4$kPMCoverPageAfter@3$kPMCoverPageBefore@2$kPMCoverPageNone@1$kPMCreateMessageFailed@-9620$kPMDataFormatXMLCompressed@2$kPMDataFormatXMLDefault@0$kPMDataFormatXMLMinimal@1$kPMDeleteSubTicketFailed@-9585$kPMDestinationFax@3$kPMDestinationFile@2$kPMDestinationInvalid@0$kPMDestinationPreview@4$kPMDestinationPrinter@1$kPMDestinationProcessPDF@5$kPMDevNColorSpaceModel@4$kPMDocumentNotFound@-9644$kPMDontSwitchPDEError@-9531$kPMDuplexNoTumble@2$kPMDuplexNone@1$kPMDuplexTumble@3$kPMEditRequestFailed@-9544$kPMFeatureNotInstalled@-9533$kPMFileOrDirOperationFailed@-9634$kPMFontNameTooLong@-9704$kPMFontNotFound@-9703$kPMGeneralCGError@-9705$kPMGeneralError@-30870$kPMGrayColorSpaceModel@1$kPMHideInlineItems@0$kPMIOAttrNotAvailable@-9787$kPMIOMSymbolNotFound@-9661$kPMInternalError@-30870$kPMInvalidAllocator@-30890$kPMInvalidCVMContext@-9665$kPMInvalidCalibrationTarget@-30898$kPMInvalidConnection@-30887$kPMInvalidFileType@-30895$kPMInvalidIOMContext@-9664$kPMInvalidIndex@-30882$kPMInvalidItem@-30892$kPMInvalidJobID@-9666$kPMInvalidJobTemplate@-30885$kPMInvalidKey@-30888$kPMInvalidLookupSpec@-9542$kPMInvalidObject@-30896$kPMInvalidPBMRef@-9540$kPMInvalidPDEContext@-9530$kPMInvalidPMContext@-9663$kPMInvalidPageFormat@-30876$kPMInvalidPaper@-30897$kPMInvalidParameter@-50$kPMInvalidPreset@-30899$kPMInvalidPrintSession@-30879$kPMInvalidPrintSettings@-30875$kPMInvalidPrinter@-30880$kPMInvalidPrinterAddress@-9780$kPMInvalidPrinterInfo@-30886$kPMInvalidReply@-30894$kPMInvalidState@-9706$kPMInvalidSubTicket@-9584$kPMInvalidTicket@-30891$kPMInvalidType@-30893$kPMInvalidValue@-30889$kPMItemIsLocked@-9586$kPMJobBusy@-9642$kPMJobCanceled@-9643$kPMJobGetTicketBadFormatError@-9672$kPMJobGetTicketReadError@-9673$kPMJobManagerAborted@-9671$kPMJobNotFound@-9641$kPMJobStreamEndError@-9670$kPMJobStreamOpenFailed@-9668$kPMJobStreamReadFailed@-9669$kPMKeyNotFound@-9589$kPMKeyNotUnique@-9590$kPMKeyOrValueNotFound@-9623$kPMLandscape@2$kPMLastErrorCodeToMakeMaintenanceOfThisListEasier@-9799$kPMLayoutBottomTopLeftRight@7$kPMLayoutBottomTopRightLeft@8$kPMLayoutLeftRightBottomTop@2$kPMLayoutLeftRightTopBottom@1$kPMLayoutRightLeftBottomTop@4$kPMLayoutRightLeftTopBottom@3$kPMLayoutTopBottomLeftRight@5$kPMLayoutTopBottomRightLeft@6$kPMLockIgnored@-30878$kPMMessagingError@-9624$kPMNoDefaultItem@-9500$kPMNoDefaultPrinter@-30872$kPMNoDefaultSettings@-9501$kPMNoError@0$kPMNoPrinterJobID@-9667$kPMNoSelectedPrinters@-9541$kPMNoSuchEntry@-30874$kPMNotImplemented@-30873$kPMObjectInUse@-30881$kPMOpenFailed@-9781$kPMOutOfScope@-30871$kPMPMSymbolNotFound@-9660$kPMPageToPaperMappingNone@1$kPMPageToPaperMappingScaleToFit@2$kPMPaperTypeCoated@2$kPMPaperTypeGlossy@4$kPMPaperTypePlain@1$kPMPaperTypePremium@3$kPMPaperTypeTShirt@6$kPMPaperTypeTransparency@5$kPMPaperTypeUnknown@0$kPMPermissionError@-9636$kPMPluginNotFound@-9701$kPMPluginRegisterationFailed@-9702$kPMPortrait@1$kPMPrBrowserNoUI@-9545$kPMPrintAllPages@-1$kPMPrinterIdle@3$kPMPrinterProcessing@4$kPMPrinterStopped@5$kPMQualityBest@13$kPMQualityDraft@4$kPMQualityHighest@15$kPMQualityInkSaver@1$kPMQualityLowest@0$kPMQualityNormal@8$kPMQualityPhoto@11$kPMQueueAlreadyExists@-9639$kPMQueueJobFailed@-9640$kPMQueueNotFound@-9638$kPMRGBColorSpaceModel@2$kPMReadFailed@-9782$kPMReadGotZeroData@-9788$kPMReverseLandscape@4$kPMReversePortrait@3$kPMScalingCenterOnImgArea@6$kPMScalingCenterOnPaper@5$kPMScalingPinBottomLeft@3$kPMScalingPinBottomRight@4$kPMScalingPinTopLeft@1$kPMScalingPinTopRight@2$kPMServerAlreadyRunning@-9631$kPMServerAttributeRestricted@-9633$kPMServerCommunicationFailed@-9621$kPMServerNotFound@-9630$kPMServerSuspended@-9632$kPMShowDefaultInlineItems@32768$kPMShowInlineCopies@1$kPMShowInlineOrientation@8$kPMShowInlinePageRange@2$kPMShowInlinePageRangeWithSelection@64$kPMShowInlinePaperSize@4$kPMShowInlineScale@128$kPMShowPageAttributesPDE@256$kPMSimplexTumble@4$kPMStatusFailed@-9784$kPMStringConversionFailure@-30883$kPMSubTicketNotFound@-9583$kPMSyncRequestFailed@-9543$kPMTemplateIsLocked@-9588$kPMTicketIsLocked@-9587$kPMTicketTypeNotFound@-9580$kPMUnableToFindProcess@-9532$kPMUnexpectedImagingError@-9707$kPMUnknownColorSpaceModel@0$kPMUnknownDataType@-9591$kPMUnknownMessage@-9637$kPMUnlocked@0$kPMUnsupportedConnection@-9786$kPMUpdateTicketFailed@-9581$kPMUserOrGroupNotFound@-9635$kPMValidateTicketFailed@-9582$kPMValueOutOfRange@-30877$kPMWriteFailed@-9783$kPMXMLParseError@-30884$kSystemPPDDomain@2$kUserPPDDomain@5$"""
misc.update(
    {
        "kPMNoPrintSettings": None,
        "kPMMirrorStr": b"mirror",
        "kPMFaxCoverSheetMessageStr": b"faxCoverSheetMessage",
        "kPMUseOptionalAccountIDStr": b"com.apple.print.PrintSettings.PMUseOptionalAccountID",
        "kPMSecondaryPaperFeedStr": b"com.apple.print.PrintSettings.PMSecondaryPaperFeed",
        "kPMTotalSidesImagedStr": b"com.apple.print.PrintSettings.PMTotalSidesImaged",
        "kPMSchedulerPDEKindID": "com.apple.print.pde.SchedulerKind",
        "kPMServerLocal": None,
        "kPMJobPINPDEKindID": "com.apple.print.pde.jobPIN",
        "kPMPageToPaperMappingTypeStr": b"com.apple.print.PageToPaperMappingType",
        "SUMMARY_DISPLAY_ORDER": "Summary, Display, Order",
        "kPMColorPDEKindID": "com.apple.print.pde.ColorKind",
        "kPMBorderTypeStr": b"com.apple.print.PrintSettings.PMBorderType",
        "kPMPrinterFeaturesPDEKindID": "com.apple.print.pde.PrinterFeaturesKind",
        "kPMGraphicsContextCoreGraphics": "com.apple.graphicscontext.coregraphics",
        "kPMColorSyncProfileIDStr": b"com.apple.print.PrintSettings.PMColorSyncProfileID",
        "kPMFaxToneDialingStr": b"faxToneDialing",
        "kPDFWorkflowItemsKey": "items",
        "kPMCoverPagePDEKindID": "com.apple.print.pde.CoverPageKind",
        "kPMFaxSubjectLabelStr": b"faxSubjectLabel",
        "kGeneralPageSetupDialogTypeIDStr": "6E6ED964-B738-11D3-952F-0050E4603277",
        "kPMCopiesAndPagesPDEKindID": "com.apple.print.pde.CopiesAndPagesKind",
        "kAppPageSetupDialogTypeIDStr": "B9A0DA98-E57F-11D3-9E83-0050E4603277",
        "kPMDocumentFormatDefault": "com.apple.documentformat.default",
        "kPDFWorkflowDisplayNameKey": "displayName",
        "kPMNoPageFormat": None,
        "kPMImagingOptionsPDEKindID": "com.apple.print.pde.ImagingOptionsKind",
        "kPDFWorkflowModifiedKey": "wasModifiedInline",
        "kPMPrintSelectionOnlyStr": b"com.apple.print.PrintSettings.PMPrintSelectionOnly",
        "kPMDestinationPrinterIDStr": b"DestinationPrinterID",
        "kPMJobPriorityStr": b"com.apple.print.PrintSettings.PMJobPriority",
        "kPMLayoutTileOrientationStr": b"com.apple.print.PrintSettings.PMLayoutTileOrientation",
        "kPrinterModuleTypeIDStr": "BDB091F4-E57F-11D3-B5CC-0050E4603277",
        "kPMInkPDEKindID": "com.apple.print.pde.InkKind",
        "kPMSandboxCompatiblePDEs": "PMSandboxCompatiblePDEs",
        "kPMPrimaryPaperFeedStr": b"com.apple.print.PrintSettings.PMPrimaryPaperFeed",
        "kPMFaxUseSoundStr": b"faxUseSound",
        "kPMPSErrorHandlerStr": b"com.apple.print.PrintSettings.PMPSErrorHandler",
        "kPMTotalBeginPagesStr": b"com.apple.print.PrintSettings.PMTotalBeginPages",
        "kPMBorderStr": b"com.apple.print.PrintSettings.PMBorder",
        "kPMGraphicsContextDefault": "com.apple.graphicscontext.default",
        "kPMPrintSelectionTitleKey": "com.apple.printSelection.title",
        "kDialogExtensionIntfIDStr": "A996FD7E-B738-11D3-8519-0050E4603277",
        "kPMInlineWorkflowStr": b"inlineWorkflow",
        "kPMLayoutColumnsStr": b"com.apple.print.PrintSettings.PMLayoutColumns",
        "kPMPageSetStr": b"page-set",
        "kPMFaxModemPDEKindID": "com.apple.print.pde.FaxModemKind",
        "kPMPageToPaperMediaNameStr": b"com.apple.print.PageToPaperMappingMediaName",
        "kPMPageAttributesKindID": "com.apple.print.pde.PageAttributesKind",
        "kPMLayoutNUpStr": b"com.apple.print.PrintSettings.PMLayoutNUp",
        "kPMLayoutPDEKindID": "com.apple.print.pde.LayoutUserOptionKind",
        "kAppPrintDialogTypeIDStr": "BCB07250-E57F-11D3-8CA6-0050E4603277",
        "kPMUseOptionalPINStr": b"com.apple.print.PrintSettings.PMUseOptionalPIN",
        "kPMErrorHandlingPDEKindID": "com.apple.print.pde.ErrorHandlingKind",
        "kPMApplicationColorMatchingStr": b"AP_ApplicationColorMatching",
        "kPMPresetGraphicsTypeAll": "All",
        "kPMCopyCollateStr": b"com.apple.print.PrintSettings.PMCopyCollate",
        "kPMPSTraySwitchStr": b"com.apple.print.PrintSettings.PMPSTraySwitch",
        "kPMOutputFilenameStr": b"com.apple.print.PrintSettings.PMOutputFilename",
        "kPMUnsupportedPDEKindID": "com.apple.print.pde.UnsupportedPDEKind",
        "kPMCustomProfilePathStr": b"PMCustomProfilePath",
        "kPMLayoutDirectionStr": b"com.apple.print.PrintSettings.PMLayoutDirection",
        "kPMFaxCoverPagePDEKindID": "com.apple.print.pde.FaxCoverPageKind",
        "kPMFaxSheetsLabelStr": b"faxSheetsLabel",
        "kPMFaxToLabelStr": b"faxToLabel",
        "kPMFaxWaitForDialToneStr": b"faxWaitForDialTone",
        "kGeneralPrintDialogTypeIDStr": "C1BF838E-B72A-11D3-9644-0050E4603277",
        "kPMJobStateStr": b"com.apple.print.PrintSettings.PMJobState",
        "kPMLayoutRowsStr": b"com.apple.print.PrintSettings.PMLayoutRows",
        "kPMDocumentFormatPDF": "application/pdf",
        "kPMOutputOptionsPDEKindID": "com.apple.print.pde.OutputOptionsKind",
        "kPDFWorkflowItemURLKey": "itemURL",
        "kPMPPDDescriptionType": "PMPPDDescriptionType",
        "kPMPresetGraphicsTypeNone": "None",
        "kPMCopiesStr": b"com.apple.print.PrintSettings.PMCopies",
        "kPMPresetGraphicsTypeGeneral": "General",
        "kPMColorMatchingModeStr": b"AP_ColorMatchingMode",
        "kAppPrintThumbnailTypeIDStr": "9320FE03-B5D5-11D5-84D1-003065D6135E",
        "kPMFaxAddressesPDEKindID": "com.apple.print.pde.FaxAddressesKind",
        "kPMFitToPageStr": b"fit-to-page",
        "kPMFaxSubjectStr": b"faxSubject",
        "kPMPresetGraphicsTypeKey": "com.apple.print.preset.graphicsType",
        "kPMCustomPaperSizePDEKindID": "com.apple.print.pde.CustomPaperSizeKind",
        "kPMJobHoldUntilTimeStr": b"com.apple.print.PrintSettings.PMJobHoldUntilTime",
        "kPMCoverPageStr": b"com.apple.print.PrintSettings.PMCoverPage",
        "kPMDuplexPDEKindID": "com.apple.print.pde.DuplexKind",
        "kPMFaxDateLabelStr": b"faxDateLabel",
        "kPMPageToPaperMappingAllowScalingUpStr": b"com.apple.print.PageToPaperMappingAllowScalingUp",
        "kPMFaxNumberStr": b"phone",
        "kPMCoverPageSourceStr": b"com.apple.print.PrintSettings.PMCoverPageSource",
        "kPMDestinationTypeStr": b"com.apple.print.PrintSettings.PMDestinationType",
        "kPMFaxPrefixStr": b"faxPrefix",
        "kPMVendorColorMatchingStr": b"AP_VendorColorMatching",
        "kPMPriorityPDEKindID": "com.apple.print.pde.PriorityKind",
        "kPMPaperSourcePDEKindID": "com.apple.print.pde.PaperSourceKind",
        "kPMPaperFeedPDEKindID": "com.apple.print.pde.PaperFeedKind",
        "kPMUniPrinterPDEKindID": "com.apple.print.pde.UniPrinterKind",
        "kPMColorMatchingPDEKindID": "com.apple.print.pde.ColorMatchingKind",
        "kPMFaxFromLabelStr": b"faxFromLabel",
        "kPMMediaQualityPDEKindID": "com.apple.print.pde.MediaQualityPDEKind",
        "kPMDocumentFormatPostScript": "application/postscript",
        "kPMPresetGraphicsTypePhoto": "Photo",
        "kPMDuplexingStr": b"com.apple.print.PrintSettings.PMDuplexing",
        "kPMPaperHandlingPDEKindID": "com.apple.print.pde.PaperHandlingKind",
        "kPMFaxToStr": b"faxTo",
        "kPMSummaryPanelKindID": "com.apple.print.pde.SummaryKind",
        "kPMRotationScalingPDEKindID": "com.apple.print.pde.RotationScalingKind",
        "kPMPDFEffectsPDEKindID": "com.apple.print.pde.PDFEffects",
        "kPMOutputOrderStr": b"OutputOrder",
        "kPMFaxCoverSheetStr": b"faxCoverSheet",
    }
)
functions = {
    "PMSetPageRange": (b"i^{OpaquePMPrintSettings=}II",),
    "PMPaperGetPPDPaperName": (
        b"i^{OpaquePMPaper=}^^{__CFString=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMGetCopies": (
        b"i^{OpaquePMPrintSettings=}^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPrinterGetOutputResolution": (
        b"i^{OpaquePMPrinter=}^{OpaquePMPrintSettings=}^{PMResolution=dd}",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "PMPrinterCopyPresets": (
        b"i^{OpaquePMPrinter=}^^{__CFArray=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMGetLastPage": (
        b"i^{OpaquePMPrintSettings=}^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPaperGetWidth": (
        b"i^{OpaquePMPaper=}^d",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMGetPageFormatPaper": (
        b"i^{OpaquePMPageFormat=}^^{OpaquePMPaper=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPrinterIsDefault": (b"Z^{OpaquePMPrinter=}",),
    "PMGetPageFormatExtendedData": (
        b"i^{OpaquePMPageFormat=}I^I^v",
        "",
        {
            "arguments": {
                2: {"type_modifier": "N"},
                3: {"c_array_length_in_arg": 2, "type_modifier": "o"},
            }
        },
    ),
    "PMPaperCreateLocalizedName": (
        b"i^{OpaquePMPaper=}^{OpaquePMPrinter=}^^{__CFString=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMSessionError": (b"i^{OpaquePMPrintSession=}",),
    "PMPresetGetAttributes": (
        b"i^{OpaquePMPreset=}^^{__CFDictionary=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPrinterGetPaperList": (
        b"i^{OpaquePMPrinter=}^^{__CFArray=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSessionCopyDestinationFormat": (
        b"i^{OpaquePMPrintSession=}^{OpaquePMPrintSettings=}^^{__CFString=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMPrinterSendCommand": (
        b"i^{OpaquePMPrinter=}^{__CFString=}^{__CFString=}^{__CFDictionary=}",
    ),
    "PMPrinterIsPostScriptPrinter": (
        b"i^{OpaquePMPrinter=}^Z",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSessionCreatePrinterList": (
        b"i^{OpaquePMPrintSession=}^^{__CFArray=}^q^^{OpaquePMPrinter=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {"already_cfretained": True, "type_modifier": "o"},
                2: {"type_modifier": "o"},
                3: {"type_modifier": "o"},
            },
        },
    ),
    "PMGetFirstPage": (
        b"i^{OpaquePMPrintSettings=}^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMWorkflowSubmitPDFWithSettings": (
        b"i^{__CFURL=}^{OpaquePMPrintSettings=}^{__CFURL=}",
    ),
    "PMCGImageCreateWithEPSDataProvider": (
        b"^{CGImage=}^{CGDataProvider=}^{CGImage=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "PMPrintSettingsCopyAsDictionary": (
        b"i^{OpaquePMPrintSettings=}^^{__CFDictionary=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMPrinterPrintWithProvider": (
        b"i^{OpaquePMPrinter=}^{OpaquePMPrintSettings=}^{OpaquePMPageFormat=}^{__CFString=}^{CGDataProvider=}",
    ),
    "PMGetPageRange": (
        b"i^{OpaquePMPrintSettings=}^I^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}, 2: {"type_modifier": "o"}}},
    ),
    "PMSessionEndPageNoDialog": (b"i^{OpaquePMPrintSession=}",),
    "PMGetOrientation": (
        b"i^{OpaquePMPageFormat=}^S",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPageFormatCreateWithDataRepresentation": (
        b"i^{__CFData=}^^{OpaquePMPageFormat=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"type_modifier": "o"}},
        },
    ),
    "PMGetCollate": (
        b"i^{OpaquePMPrintSettings=}^Z",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPresetCreatePrintSettings": (
        b"i^{OpaquePMPreset=}^{OpaquePMPrintSession=}^^{OpaquePMPrintSettings=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"type_modifier": "o"}},
        },
    ),
    "PMSetCollate": (b"i^{OpaquePMPrintSettings=}Z",),
    "PMPrinterIsRemote": (
        b"i^{OpaquePMPrinter=}^Z",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPrintSettingsGetJobName": (
        b"i^{OpaquePMPrintSettings=}^^{__CFString=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSetDuplex": (b"i^{OpaquePMPrintSettings=}I",),
    "PMPrinterGetMimeTypes": (
        b"i^{OpaquePMPrinter=}^{OpaquePMPrintSettings=}^^{__CFArray=}",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "PMPrinterIsPostScriptCapable": (b"Z^{OpaquePMPrinter=}",),
    "PMPrintSettingsSetJobName": (b"i^{OpaquePMPrintSettings=}^{__CFString=}",),
    "PMSessionCopyOutputFormatList": (
        b"i^{OpaquePMPrintSession=}S^^{__CFArray=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMSetPageFormatExtendedData": (
        b"i^{OpaquePMPageFormat=}II^v",
        "",
        {"arguments": {3: {"c_array_length_in_arg": 2, "type_modifier": "n"}}},
    ),
    "PMPrinterCreateFromPrinterID": (
        b"^{OpaquePMPrinter=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "PMPrinterIsFavorite": (b"Z^{OpaquePMPrinter=}",),
    "PMPrintSettingsCreateWithDataRepresentation": (
        b"i^{__CFData=}^^{OpaquePMPrintSettings=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"type_modifier": "o"}},
        },
    ),
    "PMPageFormatCreateDataRepresentation": (
        b"i^{OpaquePMPageFormat=}^^{__CFData=}I",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMSessionDefaultPageFormat": (b"i^{OpaquePMPrintSession=}^{OpaquePMPageFormat=}",),
    "PMCopyPrintSettings": (
        b"i^{OpaquePMPrintSettings=}^{OpaquePMPrintSettings=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "PMPrinterGetCommInfo": (
        b"i^{OpaquePMPrinter=}^Z^Z",
        "",
        {"arguments": {1: {"type_modifier": "o"}, 2: {"type_modifier": "o"}}},
    ),
    "PMPrinterGetLocation": (b"^{__CFString=}^{OpaquePMPrinter=}",),
    "PMPageFormatGetPrinterID": (
        b"i^{OpaquePMPageFormat=}^^{__CFString=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMRetain": (b"i^v",),
    "PMSessionGetCGGraphicsContext": (
        b"i^{OpaquePMPrintSession=}^^{CGContext=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSessionSetCurrentPMPrinter": (b"i^{OpaquePMPrintSession=}^{OpaquePMPrinter=}",),
    "PMPrinterGetID": (b"^{__CFString=}^{OpaquePMPrinter=}",),
    "PMPaperIsCustom": (b"Z^{OpaquePMPaper=}",),
    "PMGetUnadjustedPageRect": (
        b"i^{OpaquePMPageFormat=}^{PMRect=dddd}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSetOrientation": (b"i^{OpaquePMPageFormat=}SZ",),
    "PMCreateGenericPrinter": (
        b"i^^{OpaquePMPrinter=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"type_modifier": "o"}},
        },
    ),
    "PMGetAdjustedPaperRect": (
        b"i^{OpaquePMPageFormat=}^{PMRect=dddd}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMCopyLocalizedPPD": (
        b"i^{__CFURL=}^^{__CFURL=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMPaperGetID": (
        b"i^{OpaquePMPaper=}^^{__CFString=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPaperGetHeight": (
        b"i^{OpaquePMPaper=}^d",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPrinterCopyDeviceURI": (
        b"i^{OpaquePMPrinter=}^^{__CFURL=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMPaperCreateCustom": (
        b"i^{OpaquePMPrinter=}^{__CFString=}^{__CFString=}dd^{PMRect=dddd}^^{OpaquePMPaper=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {5: {"type_modifier": "n"}, 6: {"type_modifier": "o"}},
        },
    ),
    "PMSessionEndDocumentNoDialog": (b"i^{OpaquePMPrintSession=}",),
    "PMServerCreatePrinterList": (
        b"i^{OpaquePMServer=}^^{__CFArray=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMPrinterGetDriverCreator": (
        b"i^{OpaquePMPrinter=}^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSessionCopyDestinationLocation": (
        b"i^{OpaquePMPrintSession=}^{OpaquePMPrintSettings=}^^{__CFURL=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMPrinterGetIndexedPrinterResolution": (
        b"i^{OpaquePMPrinter=}I^{PMResolution=dd}",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "PMSessionCreatePageFormatList": (
        b"i^{OpaquePMPrintSession=}^{OpaquePMPrinter=}^^{__CFArray=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMPrinterCopyHostName": (
        b"i^{OpaquePMPrinter=}^^{__CFString=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMSetScale": (b"i^{OpaquePMPageFormat=}d",),
    "PMPrinterPrintWithFile": (
        b"i^{OpaquePMPrinter=}^{OpaquePMPrintSettings=}^{OpaquePMPageFormat=}^{__CFString=}^{__CFURL=}",
    ),
    "PMSessionSetDataInSession": (b"i^{OpaquePMPrintSession=}^{__CFString=}@",),
    "PMPaperGetPrinterID": (
        b"i^{OpaquePMPaper=}^^{__CFString=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSessionValidatePrintSettings": (
        b"i^{OpaquePMPrintSession=}^{OpaquePMPrintSettings=}^Z",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "PMPaperGetMargins": (
        b"i^{OpaquePMPaper=}^{PMRect=dddd}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPrinterCopyState": (
        b"i^{OpaquePMPrinter=}^^{__CFDictionary=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMPrintSettingsGetValue": (
        b"i^{OpaquePMPrintSettings=}^{__CFString=}^@",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "PMCreatePageFormat": (
        b"i^^{OpaquePMPageFormat=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"type_modifier": "o"}},
        },
    ),
    "PMSessionBeginPageNoDialog": (
        b"i^{OpaquePMPrintSession=}^{OpaquePMPageFormat=}^{PMRect=dddd}",
    ),
    "PMPrinterGetLanguageInfo": (
        b"i^{OpaquePMPrinter=}^{PMLanguageInfo=[33C][33C][33C]}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSetLastPage": (b"i^{OpaquePMPrintSettings=}IZ",),
    "PMCopyPPDData": (
        b"i^{__CFURL=}^^{__CFData=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMSessionGetDataFromSession": (
        b"i^{OpaquePMPrintSession=}^{__CFString=}^@",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "PMPrintSettingsCreateDataRepresentation": (
        b"i^{OpaquePMPrintSettings=}^^{__CFData=}I",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMPrinterGetDriverReleaseInfo": (
        b"i^{OpaquePMPrinter=}^{VersRec={NumVersion=CCCC}s[256C][256C]}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSessionSetError": (b"i^{OpaquePMPrintSession=}i",),
    "PMSessionSetDestination": (
        b"i^{OpaquePMPrintSession=}^{OpaquePMPrintSettings=}S^{__CFString=}^{__CFURL=}",
    ),
    "PMSessionBeginCGDocumentNoDialog": (
        b"i^{OpaquePMPrintSession=}^{OpaquePMPrintSettings=}^{OpaquePMPageFormat=}",
    ),
    "PMSessionGetDestinationType": (
        b"i^{OpaquePMPrintSession=}^{OpaquePMPrintSettings=}^S",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "PMCreateSession": (
        b"i^^{OpaquePMPrintSession=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"type_modifier": "o"}},
        },
    ),
    "PMServerLaunchPrinterBrowser": (b"i^{OpaquePMServer=}^{__CFDictionary=}",),
    "PMCopyPageFormat": (
        b"i^{OpaquePMPageFormat=}^{OpaquePMPageFormat=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "PMPrinterGetName": (b"^{__CFString=}^{OpaquePMPrinter=}",),
    "PMCopyAvailablePPDs": (
        b"iS^^{__CFArray=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMSessionDefaultPrintSettings": (
        b"i^{OpaquePMPrintSession=}^{OpaquePMPrintSettings=}",
    ),
    "PMPrinterWritePostScriptToURL": (
        b"i^{OpaquePMPrinter=}^{OpaquePMPrintSettings=}^{OpaquePMPageFormat=}^{__CFString=}^{__CFURL=}^{__CFURL=}",
    ),
    "PMPrinterSetDefault": (b"i^{OpaquePMPrinter=}",),
    "PMPrinterSetOutputResolution": (
        b"i^{OpaquePMPrinter=}^{OpaquePMPrintSettings=}^{PMResolution=dd}",
        "",
        {"arguments": {2: {"type_modifier": "n"}}},
    ),
    "PMPrinterGetState": (
        b"i^{OpaquePMPrinter=}^S",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMWorkflowSubmitPDFWithOptions": (
        b"i^{__CFURL=}^{__CFString=}^c^{__CFURL=}",
        "",
        {"arguments": {2: {"c_array_delimited_by_null": True, "type_modifier": "n"}}},
    ),
    "PMGetScale": (
        b"i^{OpaquePMPageFormat=}^d",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSetFirstPage": (b"i^{OpaquePMPrintSettings=}IZ",),
    "PMWorkflowCopyItems": (
        b"i^^{__CFArray=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMGetAdjustedPageRect": (
        b"i^{OpaquePMPageFormat=}^{PMRect=dddd}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPrinterCopyDescriptionURL": (
        b"i^{OpaquePMPrinter=}^{__CFString=}^^{__CFURL=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMCreatePrintSettings": (
        b"i^^{OpaquePMPrintSettings=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"type_modifier": "o"}},
        },
    ),
    "PMPrintSettingsSetValue": (b"i^{OpaquePMPrintSettings=}^{__CFString=}@Z",),
    "PMGetDuplex": (
        b"i^{OpaquePMPrintSettings=}^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPrinterGetMakeAndModelName": (
        b"i^{OpaquePMPrinter=}^^{__CFString=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPresetCopyName": (
        b"i^{OpaquePMPreset=}^^{__CFString=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMSessionGetCurrentPrinter": (
        b"i^{OpaquePMPrintSession=}^^{OpaquePMPrinter=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMPrinterGetPrinterResolutionCount": (
        b"i^{OpaquePMPrinter=}^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSetCopies": (b"i^{OpaquePMPrintSettings=}IZ",),
    "PMGetUnadjustedPaperRect": (
        b"i^{OpaquePMPageFormat=}^{PMRect=dddd}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "PMSessionValidatePageFormat": (
        b"i^{OpaquePMPrintSession=}^{OpaquePMPageFormat=}^Z",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "PMPrintSettingsCopyKeys": (
        b"i^{OpaquePMPrintSettings=}^^{__CFArray=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "PMCreatePageFormatWithPMPaper": (
        b"i^^{OpaquePMPageFormat=}^{OpaquePMPaper=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"type_modifier": "o"}},
        },
    ),
    "PMRelease": (b"i^v",),
}
aliases = {
    "kPMPrintTimeAEType": "cLongDateTime",
    "kPMDontWantData": "objc.NULL",
    "kPMNoReference": "objc.NULL",
    "kPMLastPageAEType": "typeSInt32",
    "kPMFeatureAEType": "typeAEList",
    "kPMDestinationTypeDefault": "kPMDestinationPrinter",
    "kPMAllocationFailure": "memFullErr",
    "kPMNoError": "noErr",
    "kPMInternalError": "kPMGeneralError",
    "kPMPDFWorkFlowAEType": "typeUTF8Text",
    "kPMFaxNumberAEType": "typeChar",
    "kPMErrorHandlingAEType": "typeEnumerated",
    "kPMSaveAsPDFAEType": "typeFileURL",
    "kPMDuplexDefault": "kPMDuplexNone",
    "kPMDontWantBoolean": "objc.NULL",
    "kPMTargetPrinterAEType": "typeChar",
    "kPMCollateAEType": "typeBoolean",
    "kPMCopieAEType": "typeSInt32",
    "kPMFirstPageAEType": "typeSInt32",
    "kPMLayoutDownAEType": "typeSInt32",
    "kPMNoData": "objc.NULL",
    "kPMDontWantSize": "objc.NULL",
    "kPMSaveAsPSAEType": "typeFileURL",
    "kPMPresetAEType": "typeUTF8Text",
    "kPMLayoutAcrossAEType": "typeSInt32",
    "kPMInvalidParameter": "paramErr",
}
misc.update(
    {
        "PMPrintSettings": objc.createOpaquePointerType(
            "PMPrintSettings", b"^{OpaquePMPrintSettings}"
        ),
        "PMPrintSession": objc.createOpaquePointerType(
            "PMPrintSession", b"^{OpaquePMPrintSession}"
        ),
        "PMPageFormat": objc.createOpaquePointerType(
            "PMPageFormat", b"^{OpaquePMPageFormat}"
        ),
        "PMPaper": objc.createOpaquePointerType("PMPaper", b"^{OpaquePMPaper}"),
        "PMPreset": objc.createOpaquePointerType("PMPreset", b"^{OpaquePMPreset}"),
        "PMPrinter": objc.createOpaquePointerType("PMPrinter", b"^{OpaquePMPrinter}"),
        "PMServer": objc.createOpaquePointerType("PMServer", b"^{OpaquePMServer}"),
    }
)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"NSObject", b"initWithBundle:", {"retval": {"type": "Z"}})
    r(b"NSObject", b"printWindowWillClose:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"NSObject",
        b"restoreValuesAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"saveValuesAndReturnError:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(b"NSObject", b"shouldHide", {"retval": {"type": "Z"}})
    r(b"NSObject", b"shouldPrint", {"retval": {"type": "Z"}})
    r(b"NSObject", b"shouldShowHelp", {"retval": {"type": "Z"}})
    r(b"NSObject", b"willChangePPDOptionKeyValue:ppdChoice:", {"retval": {"type": "Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {
    "kPMLayoutTileOrientationKey": "kPMLayoutTileOrientationStr.decode('utf-8')",
    "kPMColorSyncProfileIDKey": "kPMColorSyncProfileIDStr.decode('utf-8')",
    "kPMFaxSheetsLabelKey": "kPMFaxSheetsLabelStr.decode('utf-8')",
    "kPMUseOptionalAccountIDKey": "kPMUseOptionalAccountIDStr.decode('utf-8')",
    "kPMJobPriorityKey": "kPMJobPriorityStr.decode('utf-8')",
    "kPMLayoutNUpKey": "kPMLayoutNUpStr.decode('utf-8')",
    "kPMCoverPageDefault": "(kPMCoverPageNone)",
    "kPMPSTraySwitchKey": "kPMPSTraySwitchStr.decode('utf-8')",
    "kPMColorMatchingModeKey": "kPMColorMatchingModeStr.decode('utf-8')",
    "kPMJobStateKey": "kPMJobStateStr.decode('utf-8')",
    "kPMPrintSelectionOnlyKey": "kPMPrintSelectionOnlyStr.decode('utf-8')",
    "kPMFaxNumberKey": "kPMFaxNumberStr.decode('utf-8')",
    "kPMLayoutRowsKey": "kPMLayoutRowsStr.decode('utf-8')",
    "kPMFitToPageKey": "kPMFitToPageStr.decode('utf-8')",
    "kPMDestinationPrinterIDKey": "kPMDestinationPrinterIDStr.decode('utf-8')",
    "kPMFaxDateLabelKey": "kPMFaxDateLabelStr.decode('utf-8')",
    "kPMFaxSubjectLabelKey": "kPMFaxSubjectLabelStr.decode('utf-8')",
    "kPMBorderTypeKey": "kPMBorderTypeStr.decode('utf-8')",
    "kPMUseOptionalPINKey": "kPMUseOptionalPINStr.decode('utf-8')",
    "kPMFaxSubjectKey": "kPMFaxSubjectStr.decode('utf-8')",
    "kPMTotalSidesImagedKey": "kPMTotalSidesImagedStr.decode('utf-8')",
    "kPMPageSetKey": "CFSTR(kPMPageSetStr)",
    "kPMCoverPageKey": "kPMCoverPageStr.decode('utf-8')",
    "kPMFaxFromLabelKey": "kPMFaxFromLabelStr.decode('utf-8')",
    "kPMSecondaryPaperFeedKey": "kPMSecondaryPaperFeedStr.decode('utf-8')",
    "kPMFaxWaitForDialToneKey": "kPMFaxWaitForDialToneStr.decode('utf-8')",
    "kPMLayoutDirectionKey": "kPMLayoutDirectionStr.decode('utf-8')",
    "kPMDestinationTypeKey": "kPMDestinationTypeStr.decode('utf-8')",
    "kPMDuplexingKey": "kPMDuplexingStr.decode('utf-8')",
    "kPMCopiesKey": "kPMCopiesStr.decode('utf-8')",
    "kPMVendorColorMatching": "kPMVendorColorMatchingStr.decode('utf-8')",
    "kPMFaxPrefixKey": "kPMFaxPrefixStr.decode('utf-8')",
    "kPMFaxCoverSheetMessageKey": "kPMFaxCoverSheetMessageStr.decode('utf-8')",
    "kPMFaxToLabelKey": "kPMFaxToLabelStr.decode('utf-8')",
    "kPMFaxToneDialingKey": "kPMFaxToneDialingStr.decode('utf-8')",
    "kPMPrimaryPaperFeedKey": "kPMPrimaryPaperFeedStr.decode('utf-8')",
    "kPMCoverPageSourceKey": "kPMCoverPageSourceStr.decode('utf-8')",
    "kPMOutputFilenameKey": "kPMOutputFilenameStr.decode('utf-8')",
    "kPMOutputOrderKey": "CFSTR(kPMOutputOrderStr)",
    "kPMCopyCollateKey": "kPMCopyCollateStr.decode('utf-8')",
    "kPMInlineWorkflowKey": "kPMInlineWorkflowStr.decode('utf-8')",
    "kPMPageToPaperMappingAllowScalingUpKey": "CFSTR(kPMPageToPaperMappingAllowScalingUpStr)",
    "kPMFaxUseSoundKey": "kPMFaxUseSoundStr.decode('utf-8')",
    "kPMBorderKey": "kPMBorderStr.decode('utf-8')",
    "kPMFaxToKey": "kPMFaxToStr.decode('utf-8')",
    "kPMApplicationColorMatching": "kPMApplicationColorMatchingStr.decode('utf-8')",
    "kPMFaxCoverSheetKey": "kPMFaxCoverSheetStr.decode('utf-8')",
    "kPMJobHoldUntilTimeKey": "kPMJobHoldUntilTimeStr.decode('utf-8')",
    "kPMMirrorKey": "CFSTR(kPMMirrorStr)",
    "kPMLayoutColumnsKey": "kPMLayoutColumnsStr.decode('utf-8')",
    "kPMTotalBeginPagesKey": "kPMTotalBeginPagesStr.decode('utf-8')",
    "kPMPageToPaperMediaNameKey": "CFSTR(kPMPageToPaperMediaNameStr)",
    "kPMCustomProfilePathKey": "kPMCustomProfilePathStr.decode('utf-8')",
    "kPMPSErrorHandlerKey": "kPMPSErrorHandlerStr.decode('utf-8')",
    "kPMPageToPaperMappingTypeKey": "CFSTR(kPMPageToPaperMappingTypeStr)",
}

# END OF FILE
