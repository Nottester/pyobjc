# This file is generated by objective.metadata
#
# Last update: Sat Jun 27 17:49:31 2020
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
constants = """$ICButtonTypeCopy$ICButtonTypeMail$ICButtonTypePrint$ICButtonTypeScan$ICButtonTypeTransfer$ICButtonTypeWeb$ICCameraDeviceCanAcceptPTPCommands$ICCameraDeviceCanDeleteAllFiles$ICCameraDeviceCanDeleteOneFile$ICCameraDeviceCanReceiveFile$ICCameraDeviceCanSyncClock$ICCameraDeviceCanTakePicture$ICCameraDeviceCanTakePictureUsingShutterReleaseOnCamera$ICCameraDeviceSupportsFastPTP$ICCameraDeviceSupportsHEIF$ICDeleteAfterSuccessfulDownload$ICDeleteCanceled$ICDeleteErrorCanceled$ICDeleteErrorDeviceMissing$ICDeleteErrorFileMissing$ICDeleteErrorReadOnly$ICDeleteFailed$ICDeleteSuccessful$ICDeviceCanEjectOrDisconnect$ICDeviceLocationDescriptionBluetooth$ICDeviceLocationDescriptionFireWire$ICDeviceLocationDescriptionMassStorage$ICDeviceLocationDescriptionUSB$ICDownloadSidecarFiles$ICDownloadsDirectoryURL$ICEnumerationChronologicalOrder$ICErrorDomain$ICImageSourceShouldCache$ICImageSourceThumbnailMaxPixelSize$ICLocalizedStatusNotificationKey$ICOverwrite$ICSaveAsFilename$ICSavedAncillaryFiles$ICSavedFilename$ICScannerStatusRequestsOverviewScan$ICScannerStatusWarmUpDone$ICScannerStatusWarmingUp$ICStatusCodeKey$ICStatusNotificationKey$ICTransportTypeBluetooth$ICTransportTypeExFAT$ICTransportTypeFireWire$ICTransportTypeMassStorage$ICTransportTypeTCPIP$ICTransportTypeUSB$ICTruncateAfterSuccessfulDownload$"""
enums = """$ICDeviceLocationTypeBluetooth@2048$ICDeviceLocationTypeBonjour@1024$ICDeviceLocationTypeLocal@256$ICDeviceLocationTypeMaskBluetooth@2048$ICDeviceLocationTypeMaskBonjour@1024$ICDeviceLocationTypeMaskLocal@256$ICDeviceLocationTypeMaskRemote@65024$ICDeviceLocationTypeMaskShared@512$ICDeviceLocationTypeShared@512$ICDeviceTypeCamera@1$ICDeviceTypeMaskCamera@1$ICDeviceTypeMaskScanner@2$ICDeviceTypeScanner@2$ICEXIFOrientation1@1$ICEXIFOrientation2@2$ICEXIFOrientation3@3$ICEXIFOrientation4@4$ICEXIFOrientation5@5$ICEXIFOrientation6@6$ICEXIFOrientation7@7$ICEXIFOrientation8@8$ICLegacyReturnCodeCannotYieldDevice@-9909$ICLegacyReturnCodeCommunicationErr@-9900$ICLegacyReturnCodeDataTypeNotFoundErr@-9910$ICLegacyReturnCodeDeviceAlreadyOpenErr@-9914$ICLegacyReturnCodeDeviceGUIDNotFoundErr@-9916$ICLegacyReturnCodeDeviceIOServicePathNotFoundErr@-9917$ICLegacyReturnCodeDeviceInternalErr@-9912$ICLegacyReturnCodeDeviceInvalidParamErr@-9913$ICLegacyReturnCodeDeviceLocationIDNotFoundErr@-9915$ICLegacyReturnCodeDeviceMemoryAllocationErr@-9911$ICLegacyReturnCodeDeviceNotFoundErr@-9901$ICLegacyReturnCodeDeviceNotOpenErr@-9902$ICLegacyReturnCodeDeviceUnsupportedErr@-9918$ICLegacyReturnCodeExtensionInternalErr@-9920$ICLegacyReturnCodeFileCorruptedErr@-9903$ICLegacyReturnCodeFrameworkInternalErr@-9919$ICLegacyReturnCodeIOPendingErr@-9904$ICLegacyReturnCodeIndexOutOfRangeErr@-9907$ICLegacyReturnCodeInvalidObjectErr@-9905$ICLegacyReturnCodeInvalidPropertyErr@-9906$ICLegacyReturnCodeInvalidSessionErr@-9921$ICLegacyReturnCodePropertyTypeNotFoundErr@-9908$ICMediaPresentationConvertedAssets@1$ICMediaPresentationOriginalAssets@2$ICReturnCodeDeleteOffset@-21150$ICReturnCodeDeviceConnection@-21400$ICReturnCodeDeviceOffset@-21350$ICReturnCodeDownloadOffset@-21100$ICReturnCodeExFATOffset@-21200$ICReturnCodeMetadataOffset@-21050$ICReturnCodeObjectCouldNotBeRead@-21448$ICReturnCodeObjectDataEmpty@-21447$ICReturnCodeObjectDataOffsetInvalid@-21449$ICReturnCodeObjectDataRequestTooLarge@-21446$ICReturnCodeObjectDoesNotExist@-21450$ICReturnCodeObjectOffset@-21450$ICReturnCodePTPOffset@-21250$ICReturnCodeSystemOffset@-21300$ICReturnCodeThumbnailOffset@-21000$ICReturnCommunicationTimedOut@-9923$ICReturnConnectionClosedSessionSuddenly@-21349$ICReturnConnectionDriverExited@-21350$ICReturnConnectionEjectFailed@-21346$ICReturnConnectionEjectedSuddenly@-21348$ICReturnConnectionFailedToOpen@-21345$ICReturnConnectionFailedToOpenDevice@-21344$ICReturnConnectionSessionAlreadyOpen@-21347$ICReturnDeleteFilesCanceled@-9942$ICReturnDeleteFilesFailed@-9941$ICReturnDeviceCommandGeneralFailure@-9955$ICReturnDeviceCouldNotPair@-9951$ICReturnDeviceCouldNotUnpair@-9952$ICReturnDeviceFailedToCloseSession@-9928$ICReturnDeviceFailedToCompleteTransfer@-9956$ICReturnDeviceFailedToOpenSession@-9927$ICReturnDeviceFailedToSendData@-9957$ICReturnDeviceFailedToTakePicture@-9944$ICReturnDeviceIsBusyEnumerating@-9954$ICReturnDeviceIsPasscodeLocked@-9943$ICReturnDeviceNeedsCredentials@-9953$ICReturnDeviceSoftwareInstallationCanceled@-9948$ICReturnDeviceSoftwareInstallationCompleted@-9947$ICReturnDeviceSoftwareInstallationFailed@-9949$ICReturnDeviceSoftwareIsBeingInstalled@-9946$ICReturnDeviceSoftwareNotAvailable@-9950$ICReturnDeviceSoftwareNotInstalled@-9945$ICReturnDownloadCanceled@-9937$ICReturnDownloadFailed@-9934$ICReturnDownloadFileWritable@-21099$ICReturnDownloadPathInvalid@-21100$ICReturnErrorDeviceEjected@-21300$ICReturnExFATVolumeInvalid@21200$ICReturnFailedToCompletePassThroughCommand@-9936$ICReturnFailedToCompleteSendMessageRequest@-9940$ICReturnFailedToDisabeTethering@-9939$ICReturnFailedToEnabeTethering@-9938$ICReturnInvalidParam@-9922$ICReturnMetadataAlreadyFetching@-20149$ICReturnMetadataCanceled@-20148$ICReturnMetadataInvalid@-20147$ICReturnMetadataNotAvailable@-20150$ICReturnMultiErrorDictionary@-30000$ICReturnPTPFailedToSendCommand@-21250$ICReturnPTPNotAuthorizedToSendCommand@-21249$ICReturnReceivedUnsolicitedScannerErrorInfo@-9933$ICReturnReceivedUnsolicitedScannerStatusInfo@-9932$ICReturnScanOperationCanceled@-9924$ICReturnScannerFailedToCompleteOverviewScan@-9930$ICReturnScannerFailedToCompleteScan@-9931$ICReturnScannerFailedToSelectFunctionalUnit@-9929$ICReturnScannerInUseByLocalUser@-9925$ICReturnScannerInUseByRemoteUser@-9926$ICReturnSessionNotOpened@-9958$ICReturnSuccess@0$ICReturnThumbnailAlreadyFetching@-20999$ICReturnThumbnailCanceled@-20098$ICReturnThumbnailInvalid@-20097$ICReturnThumbnailNotAvailable@-21000$ICReturnUploadFailed@-9935$ICScannerBitDepth16Bits@16$ICScannerBitDepth1Bit@1$ICScannerBitDepth8Bits@8$ICScannerColorDataFormatTypeChunky@0$ICScannerColorDataFormatTypePlanar@1$ICScannerDocumentType10@25$ICScannerDocumentType10R@67$ICScannerDocumentType110@72$ICScannerDocumentType11R@69$ICScannerDocumentType12R@70$ICScannerDocumentType135@76$ICScannerDocumentType2A0@18$ICScannerDocumentType3R@61$ICScannerDocumentType4A0@17$ICScannerDocumentType4R@62$ICScannerDocumentType5R@63$ICScannerDocumentType6R@64$ICScannerDocumentType8R@65$ICScannerDocumentTypeA0@19$ICScannerDocumentTypeA1@20$ICScannerDocumentTypeA2@21$ICScannerDocumentTypeA3@11$ICScannerDocumentTypeA4@1$ICScannerDocumentTypeA5@5$ICScannerDocumentTypeA6@13$ICScannerDocumentTypeA7@22$ICScannerDocumentTypeA8@23$ICScannerDocumentTypeA9@24$ICScannerDocumentTypeAPSC@74$ICScannerDocumentTypeAPSH@73$ICScannerDocumentTypeAPSP@75$ICScannerDocumentTypeB5@2$ICScannerDocumentTypeBusinessCard@53$ICScannerDocumentTypeC0@44$ICScannerDocumentTypeC1@45$ICScannerDocumentTypeC10@51$ICScannerDocumentTypeC2@46$ICScannerDocumentTypeC3@47$ICScannerDocumentTypeC4@14$ICScannerDocumentTypeC5@15$ICScannerDocumentTypeC6@16$ICScannerDocumentTypeC7@48$ICScannerDocumentTypeC8@49$ICScannerDocumentTypeC9@50$ICScannerDocumentTypeDefault@0$ICScannerDocumentTypeE@60$ICScannerDocumentTypeISOB0@26$ICScannerDocumentTypeISOB1@27$ICScannerDocumentTypeISOB10@33$ICScannerDocumentTypeISOB2@28$ICScannerDocumentTypeISOB3@12$ICScannerDocumentTypeISOB4@6$ICScannerDocumentTypeISOB5@29$ICScannerDocumentTypeISOB6@7$ICScannerDocumentTypeISOB7@30$ICScannerDocumentTypeISOB8@31$ICScannerDocumentTypeISOB9@32$ICScannerDocumentTypeJISB0@34$ICScannerDocumentTypeJISB1@35$ICScannerDocumentTypeJISB10@43$ICScannerDocumentTypeJISB2@36$ICScannerDocumentTypeJISB3@37$ICScannerDocumentTypeJISB4@38$ICScannerDocumentTypeJISB6@39$ICScannerDocumentTypeJISB7@40$ICScannerDocumentTypeJISB8@41$ICScannerDocumentTypeJISB9@42$ICScannerDocumentTypeLF@78$ICScannerDocumentTypeMF@77$ICScannerDocumentTypeS10R@68$ICScannerDocumentTypeS12R@71$ICScannerDocumentTypeS8R@66$ICScannerDocumentTypeUSExecutive@10$ICScannerDocumentTypeUSLedger@9$ICScannerDocumentTypeUSLegal@4$ICScannerDocumentTypeUSLetter@3$ICScannerDocumentTypeUSStatement@52$ICScannerFeatureTypeBoolean@2$ICScannerFeatureTypeEnumeration@0$ICScannerFeatureTypeRange@1$ICScannerFeatureTypeTemplate@3$ICScannerFunctionalUnitStateOverviewScanInProgress@4$ICScannerFunctionalUnitStateReady@1$ICScannerFunctionalUnitStateScanInProgress@2$ICScannerFunctionalUnitTypeDocumentFeeder@3$ICScannerFunctionalUnitTypeFlatbed@0$ICScannerFunctionalUnitTypeNegativeTransparency@2$ICScannerFunctionalUnitTypePositiveTransparency@1$ICScannerMeasurementUnitCentimeters@1$ICScannerMeasurementUnitInches@0$ICScannerMeasurementUnitPicas@2$ICScannerMeasurementUnitPixels@5$ICScannerMeasurementUnitPoints@3$ICScannerMeasurementUnitTwips@4$ICScannerPixelDataTypeBW@0$ICScannerPixelDataTypeCIEXYZ@8$ICScannerPixelDataTypeCMY@4$ICScannerPixelDataTypeCMYK@5$ICScannerPixelDataTypeGray@1$ICScannerPixelDataTypePalette@3$ICScannerPixelDataTypeRGB@2$ICScannerPixelDataTypeYUV@6$ICScannerPixelDataTypeYUVK@7$ICScannerTransferModeFileBased@0$ICScannerTransferModeMemoryBased@1$"""
misc.update({"ICRunLoopMode": "com.apple.ImageCaptureCore"})
aliases = {
    "ICReturnCodeObjectDoesNotExist": "ICReturnCodeObjectOffset",
    "ICReturnFailedToDisableTethering": "ICReturnFailedToDisabeTethering",
    "ICReturnPTPFailedToSendCommand": "ICReturnCodeDownloadOffset",
    "ICReturnDownloadPathInvalid": "ICReturnCodeDownloadOffset",
    "ICRect": "NSRect",
    "ICReturnDeviceIsAccessRestrictedAppleDevice": "ICReturnDeviceIsPasscodeLocked",
    "ICPoint": "NSPoint",
    "ICReturnFailedToEnableTethering": "ICReturnFailedToEnabeTethering",
    "ICSize": "NSSize",
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"ICCameraDevice", b"batteryLevelAvailable", {"retval": {"type": "Z"}})
    r(b"ICCameraDevice", b"iCloudPhotosEnabled", {"retval": {"type": b"Z"}})
    r(b"ICCameraDevice", b"isAccessRestrictedAppleDevice", {"retval": {"type": "Z"}})
    r(b"ICCameraDevice", b"isEjectable", {"retval": {"type": b"Z"}})
    r(b"ICCameraDevice", b"isLocked", {"retval": {"type": b"Z"}})
    r(
        b"ICCameraDevice",
        b"requestDeleteFiles:deleteFailed:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"ICCameraDevice",
        b"requestDownloadFile:options:downloadDelegate:didDownloadSelector:contextInfo:",
        {"arguments": {5: {"sel_of_type": b"v@:@@@^v"}}},
    )
    r(
        b"ICCameraDevice",
        b"requestReadDataFromFile:atOffset:length:readDelegate:didReadDataSelector:contextInfo:",
        {"arguments": {6: {"sel_of_type": b"v@:@@@^v"}}},
    )
    r(
        b"ICCameraDevice",
        b"requestSendPTPCommand:outData:completion:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"ICCameraDevice",
        b"requestSendPTPCommand:outData:sendCommandDelegate:didSendCommandSelector:contextInfo:",
        {"arguments": {5: {"sel_of_type": b"v@:@@@@^v"}}},
    )
    r(
        b"ICCameraDevice",
        b"requestUploadFile:options:uploadDelegate:didUploadSelector:contextInfo:",
        {"arguments": {5: {"sel_of_type": b"v@:@@^v"}}},
    )
    r(
        b"ICCameraDevice",
        b"setPtpEventHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"ICCameraDevice",
        b"setTetheredCaptureEnabled:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"ICCameraDevice", b"tetheredCaptureEnabled", {"retval": {"type": "Z"}})
    r(b"ICCameraFile", b"burstFavorite", {"retval": {"type": b"Z"}})
    r(b"ICCameraFile", b"burstPicked", {"retval": {"type": b"Z"}})
    r(b"ICCameraFile", b"firstPicked", {"retval": {"type": b"Z"}})
    r(b"ICCameraFile", b"highFramerate", {"retval": {"type": b"Z"}})
    r(
        b"ICCameraFile",
        b"requestDownloadWithOptions:completion:",
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
        b"ICCameraFile",
        b"requestMetadataDictionaryWithOptions:completion:",
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
        b"ICCameraFile",
        b"requestReadDataAtOffset:length:completion:",
        {
            "arguments": {
                4: {
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
        b"ICCameraFile",
        b"requestThumbnailDataWithOptions:completion:",
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
    r(b"ICCameraFile", b"timeLapse", {"retval": {"type": b"Z"}})
    r(b"ICCameraItem", b"isInTemporaryStore", {"retval": {"type": "Z"}})
    r(b"ICCameraItem", b"isLocked", {"retval": {"type": "Z"}})
    r(b"ICCameraItem", b"isRaw", {"retval": {"type": "Z"}})
    r(
        b"ICCameraItem",
        b"wasAddedAfterContentCatalogCompleted",
        {"retval": {"type": "Z"}},
    )
    r(b"ICDevice", b"hasConfigurableWiFiInterface", {"retval": {"type": "Z"}})
    r(b"ICDevice", b"hasOpenSession", {"retval": {"type": "Z"}})
    r(b"ICDevice", b"isRemote", {"retval": {"type": "Z"}})
    r(b"ICDevice", b"isShared", {"retval": {"type": "Z"}})
    r(
        b"ICDevice",
        b"requestCloseSessionWithOptions:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"ICDevice",
        b"requestEjectWithCompletion:",
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
        b"ICDevice",
        b"requestOpenSessionWithOptions:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"ICDevice",
        b"requestSendMessage:outData:maxReturnedDataSize:sendMessageDelegate:didSendMessageSelector:contextInfo:",
        {"arguments": {6: {"sel_of_type": b"v@:I@@^v"}}},
    )
    r(b"ICDeviceBrowser", b"isBrowsing", {"retval": {"type": "Z"}})
    r(b"ICScannerBandData", b"isBigEndian", {"retval": {"type": "Z"}})
    r(b"ICScannerFeatureBoolean", b"setValue:", {"arguments": {2: {"type": "Z"}}})
    r(b"ICScannerFeatureBoolean", b"value", {"retval": {"type": "Z"}})
    r(
        b"ICScannerFunctionalUnit",
        b"acceptsThresholdForBlackAndWhiteScanning",
        {"retval": {"type": "Z"}},
    )
    r(b"ICScannerFunctionalUnit", b"canPerformOverviewScan", {"retval": {"type": "Z"}})
    r(b"ICScannerFunctionalUnit", b"overviewScanInProgress", {"retval": {"type": "Z"}})
    r(b"ICScannerFunctionalUnit", b"scanInProgress", {"retval": {"type": "Z"}})
    r(
        b"ICScannerFunctionalUnit",
        b"setUsesThresholdForBlackAndWhiteScanning:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"ICScannerFunctionalUnit",
        b"usesThresholdForBlackAndWhiteScanning",
        {"retval": {"type": "Z"}},
    )
    r(
        b"ICScannerFunctionalUnitDocumentFeeder",
        b"documentLoaded",
        {"retval": {"type": "Z"}},
    )
    r(
        b"ICScannerFunctionalUnitDocumentFeeder",
        b"duplexScanningEnabled",
        {"retval": {"type": "Z"}},
    )
    r(
        b"ICScannerFunctionalUnitDocumentFeeder",
        b"reverseFeederPageOrder",
        {"retval": {"type": "Z"}},
    )
    r(
        b"ICScannerFunctionalUnitDocumentFeeder",
        b"setDuplexScanningEnabled:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"ICScannerFunctionalUnitDocumentFeeder",
        b"supportsDuplexScanning",
        {"retval": {"type": "Z"}},
    )
    r(
        b"NSObject",
        b"cameraDevice:didAddItem:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:didAddItems:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:didCompleteDeleteFilesWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:didReceiveMetadata:forItem:error:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:didReceiveMetadataForItem:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:didReceivePTPEvent:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:didReceiveThumbnail:forItem:error:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"^{CGImage=}"},
                4: {"type": b"@"},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:didReceiveThumbnailForItem:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:didRemoveItem:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:didRemoveItems:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:didRenameItems:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:shouldGetMetadataOfItem:",
        {
            "required": False,
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDevice:shouldGetThumbnailOfItem:",
        {
            "required": False,
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"cameraDeviceDidChangeCapability:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"cameraDeviceDidEnableAccessRestriction:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"cameraDeviceDidRemoveAccessRestriction:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"device:didCloseSessionWithError:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"device:didEjectWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"device:didEncounterError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"device:didOpenSessionWithError:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"device:didReceiveButtonPress:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"device:didReceiveCustomNotification:data:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"device:didReceiveStatusInformation:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"deviceBrowser:deviceDidChangeName:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"deviceBrowser:deviceDidChangeSharingState:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"deviceBrowser:didAddDevice:moreComing:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": "Z"}},
        },
    )
    r(
        b"NSObject",
        b"deviceBrowser:didRemoveDevice:moreGoing:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": "Z"}},
        },
    )
    r(
        b"NSObject",
        b"deviceBrowser:requestsSelectDevice:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"deviceBrowserDidEnumerateLocalDevices:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"deviceDidBecomeReady:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"deviceDidBecomeReadyWithCompleteContentCatalog:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"deviceDidChangeName:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"deviceDidChangeSharingState:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"didDownloadFile:error:options:contextInfo:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": "^v"},
            },
        },
    )
    r(
        b"NSObject",
        b"didReceiveDownloadProgressForFile:downloadedBytes:maxBytes:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"q"}, 4: {"type": b"q"}},
        },
    )
    r(
        b"NSObject",
        b"didRemoveDevice:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"scannerDevice:didCompleteOverviewScanWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"scannerDevice:didCompleteScanWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"scannerDevice:didScanToBandData:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"scannerDevice:didScanToURL:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"scannerDevice:didScanToURL:data:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"scannerDevice:didSelectFunctionalUnit:error:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"scannerDeviceDidBecomeAvailable:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {
    "ICReturnCodeObjectDataEmpty": "ICReturnCodeObjectOffset-3",
    "ICReturnCodeObjectCouldNotBeRead": "ICReturnCodeObjectOffset-2",
    "ICReturnCodeObjectDataOffsetInvalid": "ICReturnCodeObjectOffset-1",
}

# END OF FILE
