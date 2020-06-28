# This file is generated by objective.metadata
#
# Last update: Sat Jun 27 18:36:28 2020
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
constants = """$NSAddedPersistentStoresKey$NSAffectedObjectsErrorKey$NSAffectedStoresErrorKey$NSBinaryExternalRecordType$NSBinaryStoreInsecureDecodingCompatibilityOption$NSBinaryStoreSecureDecodingClasses$NSBinaryStoreType$NSCoreDataCoreSpotlightExporter$NSCoreDataVersionNumber@d$NSDeletedObjectIDsKey$NSDeletedObjectsKey$NSDetailedErrorsKey$NSEntityNameInPathKey$NSErrorMergePolicy$NSExternalRecordExtensionOption$NSExternalRecordsDirectoryOption$NSExternalRecordsFileFormatOption$NSIgnorePersistentStoreVersioningOption$NSInMemoryStoreType$NSInferMappingModelAutomaticallyOption$NSInsertedObjectIDsKey$NSInsertedObjectsKey$NSInvalidatedAllObjectsKey$NSInvalidatedObjectIDsKey$NSInvalidatedObjectsKey$NSManagedObjectContextDidMergeChangesObjectIDsNotification$NSManagedObjectContextDidSaveNotification$NSManagedObjectContextDidSaveObjectIDsNotification$NSManagedObjectContextObjectsDidChangeNotification$NSManagedObjectContextQueryGenerationKey$NSManagedObjectContextWillSaveNotification$NSMergeByPropertyObjectTrumpMergePolicy$NSMergeByPropertyStoreTrumpMergePolicy$NSMigratePersistentStoresAutomaticallyOption$NSMigrationDestinationObjectKey$NSMigrationEntityMappingKey$NSMigrationEntityPolicyKey$NSMigrationManagerKey$NSMigrationPropertyMappingKey$NSMigrationSourceObjectKey$NSModelPathKey$NSObjectURIKey$NSOverwriteMergePolicy$NSPersistentCloudKitContainerEventChangedNotification$NSPersistentCloudKitContainerEventUserInfoKey$NSPersistentHistoryTokenKey$NSPersistentHistoryTrackingKey$NSPersistentStoreConnectionPoolMaxSizeKey$NSPersistentStoreCoordinatorStoresDidChangeNotification$NSPersistentStoreCoordinatorStoresWillChangeNotification$NSPersistentStoreCoordinatorWillRemoveStoreNotification$NSPersistentStoreDidImportUbiquitousContentChangesNotification$NSPersistentStoreFileProtectionKey$NSPersistentStoreForceDestroyOption$NSPersistentStoreOSCompatibility$NSPersistentStoreRebuildFromUbiquitousContentOption$NSPersistentStoreRemoteChangeNotification$NSPersistentStoreRemoteChangeNotificationPostOptionKey$NSPersistentStoreRemoveUbiquitousMetadataOption$NSPersistentStoreSaveConflictsErrorKey$NSPersistentStoreTimeoutOption$NSPersistentStoreURLKey$NSPersistentStoreUbiquitousContainerIdentifierKey$NSPersistentStoreUbiquitousContentNameKey$NSPersistentStoreUbiquitousContentURLKey$NSPersistentStoreUbiquitousPeerTokenOption$NSPersistentStoreUbiquitousTransitionTypeKey$NSReadOnlyPersistentStoreOption$NSRefreshedObjectIDsKey$NSRefreshedObjectsKey$NSRemovedPersistentStoresKey$NSRollbackMergePolicy$NSSQLiteAnalyzeOption$NSSQLiteErrorDomain$NSSQLiteManualVacuumOption$NSSQLitePragmasOption$NSSQLiteStoreType$NSStoreModelVersionHashesKey$NSStoreModelVersionIdentifiersKey$NSStorePathKey$NSStoreTypeKey$NSStoreUUIDInPathKey$NSStoreUUIDKey$NSUUIDChangedPersistentStoresKey$NSUpdatedObjectIDsKey$NSUpdatedObjectsKey$NSValidateXMLStoreOption$NSValidationKeyErrorKey$NSValidationObjectErrorKey$NSValidationPredicateErrorKey$NSValidationValueErrorKey$NSXMLExternalRecordType$NSXMLStoreType$"""
enums = """$NSAddEntityMappingType@2$NSBatchDeleteRequestType@7$NSBatchDeleteResultTypeCount@2$NSBatchDeleteResultTypeObjectIDs@1$NSBatchDeleteResultTypeStatusOnly@0$NSBatchInsertRequestResultTypeCount@2$NSBatchInsertRequestResultTypeObjectIDs@1$NSBatchInsertRequestResultTypeStatusOnly@0$NSBatchInsertRequestType@5$NSBatchUpdateRequestType@6$NSBinaryDataAttributeType@1000$NSBooleanAttributeType@800$NSCascadeDeleteRule@2$NSConfinementConcurrencyType@0$NSCopyEntityMappingType@4$NSCoreDataError@134060$NSCoreDataVersionNumber10_10@526.0$NSCoreDataVersionNumber10_10_2@526.1$NSCoreDataVersionNumber10_10_3@526.2$NSCoreDataVersionNumber10_11@640.0$NSCoreDataVersionNumber10_11_3@641.3$NSCountResultType@4$NSCustomEntityMappingType@1$NSDateAttributeType@900$NSDecimalAttributeType@400$NSDenyDeleteRule@3$NSDictionaryResultType@2$NSDoubleAttributeType@500$NSEntityMigrationPolicyError@134170$NSErrorMergePolicyType@0$NSExternalRecordImportError@134200$NSFetchIndexElementTypeBinary@0$NSFetchIndexElementTypeRTree@1$NSFetchRequestExpressionType@50$NSFetchRequestType@1$NSFetchedResultsChangeDelete@2$NSFetchedResultsChangeInsert@1$NSFetchedResultsChangeMove@3$NSFetchedResultsChangeUpdate@4$NSFloatAttributeType@600$NSInferredMappingModelError@134190$NSInteger16AttributeType@100$NSInteger32AttributeType@200$NSInteger64AttributeType@300$NSMainQueueConcurrencyType@2$NSManagedObjectConstraintMergeError@133021$NSManagedObjectConstraintValidationError@1551$NSManagedObjectContextLockingError@132000$NSManagedObjectExternalRelationshipError@133010$NSManagedObjectIDResultType@1$NSManagedObjectMergeError@133020$NSManagedObjectReferentialIntegrityError@133000$NSManagedObjectResultType@0$NSManagedObjectValidationError@1550$NSMergeByPropertyObjectTrumpMergePolicyType@2$NSMergeByPropertyStoreTrumpMergePolicyType@1$NSMigrationCancelledError@134120$NSMigrationConstraintViolationError@134111$NSMigrationError@134110$NSMigrationManagerDestinationStoreError@134160$NSMigrationManagerSourceStoreError@134150$NSMigrationMissingMappingModelError@134140$NSMigrationMissingSourceModelError@134130$NSNoActionDeleteRule@0$NSNullifyDeleteRule@1$NSObjectIDAttributeType@2000$NSOverwriteMergePolicyType@3$NSPersistentCloudKitContainerEventResultTypeCountEvents@1$NSPersistentCloudKitContainerEventResultTypeEvents@0$NSPersistentCloudKitContainerEventTypeExport@2$NSPersistentCloudKitContainerEventTypeImport@1$NSPersistentCloudKitContainerEventTypeSetup@0$NSPersistentCloudKitContainerSchemaInitializationOptionsDryRun@2$NSPersistentCloudKitContainerSchemaInitializationOptionsNone@0$NSPersistentCloudKitContainerSchemaInitializationOptionsPrintSchema@4$NSPersistentHistoryChangeTypeDelete@2$NSPersistentHistoryChangeTypeInsert@0$NSPersistentHistoryChangeTypeUpdate@1$NSPersistentHistoryResultTypeChangesOnly@4$NSPersistentHistoryResultTypeCount@2$NSPersistentHistoryResultTypeObjectIDs@1$NSPersistentHistoryResultTypeStatusOnly@0$NSPersistentHistoryResultTypeTransactionsAndChanges@5$NSPersistentHistoryResultTypeTransactionsOnly@3$NSPersistentHistoryTokenExpiredError@134301$NSPersistentStoreCoordinatorLockingError@132010$NSPersistentStoreIncompatibleSchemaError@134020$NSPersistentStoreIncompatibleVersionHashError@134100$NSPersistentStoreIncompleteSaveError@134040$NSPersistentStoreInvalidTypeError@134000$NSPersistentStoreOpenError@134080$NSPersistentStoreOperationError@134070$NSPersistentStoreSaveConflictsError@134050$NSPersistentStoreSaveError@134030$NSPersistentStoreTimeoutError@134090$NSPersistentStoreTypeMismatchError@134010$NSPersistentStoreUbiquitousTransitionTypeAccountAdded@1$NSPersistentStoreUbiquitousTransitionTypeAccountRemoved@2$NSPersistentStoreUbiquitousTransitionTypeContentRemoved@3$NSPersistentStoreUbiquitousTransitionTypeInitialImportCompleted@4$NSPersistentStoreUnsupportedRequestTypeError@134091$NSPrivateQueueConcurrencyType@1$NSRemoveEntityMappingType@3$NSRollbackMergePolicyType@4$NSSQLiteError@134180$NSSaveRequestType@2$NSSnapshotEventMergePolicy@64$NSSnapshotEventRefresh@32$NSSnapshotEventRollback@16$NSSnapshotEventUndoDeletion@4$NSSnapshotEventUndoInsertion@2$NSSnapshotEventUndoUpdate@8$NSStatusOnlyResultType@0$NSStringAttributeType@700$NSTransformEntityMappingType@5$NSTransformableAttributeType@1800$NSURIAttributeType@1200$NSUUIDAttributeType@1100$NSUndefinedAttributeType@0$NSUndefinedEntityMappingType@0$NSUpdatedObjectIDsResultType@1$NSUpdatedObjectsCountResultType@2$NSValidationDateTooLateError@1630$NSValidationDateTooSoonError@1640$NSValidationInvalidDateError@1650$NSValidationInvalidURIError@1690$NSValidationMissingMandatoryPropertyError@1570$NSValidationMultipleErrorsError@1560$NSValidationNumberTooLargeError@1610$NSValidationNumberTooSmallError@1620$NSValidationRelationshipDeniedDeleteError@1600$NSValidationRelationshipExceedsMaximumCountError@1590$NSValidationRelationshipLacksMinimumCountError@1580$NSValidationStringPatternMatchingError@1680$NSValidationStringTooLongError@1660$NSValidationStringTooShortError@1670$"""
misc.update(
    {
        "NSCoreDataVersionNumber10_10_3": 526.2,
        "NSCoreDataVersionNumber10_10_2": 526.1,
        "NSCoreDataVersionNumber_iPhoneOS_3_2": 310.2,
        "NSCoreDataVersionNumber_iPhoneOS_3_1": 248.0,
        "NSCoreDataVersionNumber10_7_2": 358.12,
        "NSCoreDataVersionNumber10_11_3": 641.3,
        "NSCoreDataVersionNumber10_7_4": 358.14,
        "NSCoreDataVersionNumber_iPhoneOS_9_3": 641.6,
        "NSCoreDataVersionNumber_iPhoneOS_9_2": 641.4,
        "NSCoreDataVersionNumber10_8": 407.5,
        "NSCoreDataVersionNumber10_9": 481.0,
        "NSCoreDataVersionNumber10_5_3": 186.0,
        "NSCoreDataVersionNumber10_6": 246.0,
        "NSCoreDataVersionNumber10_7": 358.4,
        "NSCoreDataVersionNumber10_4": 46.0,
        "NSCoreDataVersionNumber10_5": 185.0,
        "NSCoreDataVersionNumber10_8_2": 407.7,
        "NSCoreDataVersionNumber10_10": 526.0,
        "NSCoreDataVersionNumber10_11": 640.0,
        "NSCoreDataVersionNumber10_6_3": 251.0,
        "NSCoreDataVersionNumber10_6_2": 250.0,
        "NSCoreDataVersionNumber10_4_3": 77.0,
        "NSCoreDataVersionNumber10_7_3": 358.13,
        "NSCoreDataVersionNumber10_9_2": 481.1,
        "NSCoreDataVersionNumber10_9_3": 481.3,
        "NSCoreDataVersionNumber_iPhoneOS_5_0": 386.1,
        "NSCoreDataVersionNumber_iPhoneOS_5_1": 386.5,
        "NSCoreDataVersionNumber_iPhoneOS_8_3": 519.15,
        "NSCoreDataVersionNumber_iPhoneOS_8_0": 519.0,
        "NSCoreDataVersionNumber_iPhoneOS_7_0": 479.1,
        "NSCoreDataVersionNumber_iPhoneOS_7_1": 479.3,
        "NSCoreDataVersionNumber_iPhoneOS_3_0": 241.0,
        "NSCoreDataVersionNumber_iPhoneOS_6_1": 419.1,
        "NSCoreDataVersionNumber_iPhoneOS_6_0": 419.0,
        "NSCoreDataVersionNumber_iPhoneOS_9_0": 640.0,
        "NSCoreDataVersionNumber_iPhoneOS_4_3": 320.17,
        "NSCoreDataVersionNumber_iPhoneOS_4_2": 320.15,
        "NSCoreDataVersionNumber_iPhoneOS_4_1": 320.11,
        "NSCoreDataVersionNumber_iPhoneOS_4_0": 320.5,
    }
)
aliases = {"COREDATA_PRIVATE_EXTERN": "__private_extern__"}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSAsynchronousFetchRequest",
        b"completionBlock",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                }
            }
        },
    )
    r(
        b"NSAsynchronousFetchRequest",
        b"initWithFetchRequest:completionBlock:",
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
        b"NSAtomicStore",
        b"load:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NSAtomicStore",
        b"save:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NSAttributeDescription",
        b"allowsExternalBinaryDataStorage",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"NSAttributeDescription",
        b"preservesValueInHistoryOnDeletion",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"NSAttributeDescription",
        b"setAllowsExternalBinaryDataStorage:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"NSAttributeDescription",
        b"setPreservesValueInHistoryOnDeletion:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"NSBatchInsertRequest",
        b"batchInsertRequestWithEntityName:dictionaryHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"NSBatchInsertRequest",
        b"batchInsertRequestWithEntityName:managedObjectHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"NSBatchInsertRequest",
        b"initWithEntity:dictionaryHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"NSBatchInsertRequest",
        b"initWithEntity:managedObjectHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"NSBatchInsertRequest",
        b"setDictionaryHandler:",
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
        b"NSBatchInsertRequest",
        b"setManagedObjectHandler:",
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
    r(b"NSBatchUpdateRequest", b"includesSubentities", {"retval": {"type": b"Z"}})
    r(
        b"NSBatchUpdateRequest",
        b"setIncludesSubentities:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"NSCoreDataCoreSpotlightDelegate",
        b"searchableIndex:reindexAllSearchableItemsWithAcknowledgementHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"NSCoreDataCoreSpotlightDelegate",
        b"searchableIndex:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(b"NSEntityDescription", b"isAbstract", {"retval": {"type": "Z"}})
    r(b"NSEntityDescription", b"isKindOfEntity:", {"retval": {"type": "Z"}})
    r(b"NSEntityDescription", b"setAbstract:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"NSEntityMigrationPolicy",
        b"beginEntityMapping:manager:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSEntityMigrationPolicy",
        b"createDestinationInstancesForSourceInstance:entityMapping:manager:error:",
        {"retval": {"type": "Z"}, "arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"NSEntityMigrationPolicy",
        b"createRelationshipsForDestinationInstance:entityMapping:manager:error:",
        {"retval": {"type": "Z"}, "arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"NSEntityMigrationPolicy",
        b"endEntityMapping:manager:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSEntityMigrationPolicy",
        b"endInstanceCreationForEntityMapping:manager:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSEntityMigrationPolicy",
        b"endRelationshipCreationForEntityMapping:manager:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSEntityMigrationPolicy",
        b"performCustomValidationForEntityMapping:manager:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(b"NSFetchIndexElementDescription", b"isAscending", {"retval": {"type": "Z"}})
    r(
        b"NSFetchIndexElementDescription",
        b"setAscending:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"NSFetchRequest", b"execute:", {"arguments": {2: {"type_modifier": b"o"}}})
    r(b"NSFetchRequest", b"includesPendingChanges", {"retval": {"type": "Z"}})
    r(b"NSFetchRequest", b"includesPropertyValues", {"retval": {"type": "Z"}})
    r(b"NSFetchRequest", b"includesSubentities", {"retval": {"type": "Z"}})
    r(b"NSFetchRequest", b"returnsDistinctResults", {"retval": {"type": "Z"}})
    r(b"NSFetchRequest", b"returnsObjectsAsFaults", {"retval": {"type": "Z"}})
    r(
        b"NSFetchRequest",
        b"setIncludesPendingChanges:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSFetchRequest",
        b"setIncludesPropertyValues:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"NSFetchRequest", b"setIncludesSubentities:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"NSFetchRequest",
        b"setReturnsDistinctResults:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSFetchRequest",
        b"setReturnsObjectsAsFaults:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSFetchRequest",
        b"setShouldRefreshRefetchedObjects:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"NSFetchRequest", b"shouldRefreshRefetchedObjects", {"retval": {"type": b"Z"}})
    r(
        b"NSFetchRequestExpression",
        b"expressionForFetch:context:countOnly:",
        {"arguments": {4: {"type": "Z"}}},
    )
    r(b"NSFetchRequestExpression", b"isCountOnlyRequest", {"retval": {"type": "Z"}})
    r(
        b"NSFetchedResultsController",
        b"performFetch:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NSIncrementalStore",
        b"executeRequest:withContext:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSIncrementalStore",
        b"loadMetadata:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NSIncrementalStore",
        b"newValueForRelationship:forObjectWithID:withContext:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"NSIncrementalStore",
        b"newValuesForObjectWithID:withContext:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSIncrementalStore",
        b"obtainPermanentIDsForObjects:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSManagedObject",
        b"contextShouldIgnoreUnmodeledPropertyChanges",
        {"retval": {"type": b"Z"}},
    )
    r(b"NSManagedObject", b"hasChanges", {"retval": {"type": b"Z"}})
    r(b"NSManagedObject", b"hasFaultForRelationshipNamed:", {"retval": {"type": "Z"}})
    r(b"NSManagedObject", b"hasPersistentChangedValues", {"retval": {"type": "Z"}})
    r(b"NSManagedObject", b"isDeleted", {"retval": {"type": "Z"}})
    r(b"NSManagedObject", b"isFault", {"retval": {"type": "Z"}})
    r(b"NSManagedObject", b"isInserted", {"retval": {"type": "Z"}})
    r(b"NSManagedObject", b"isUpdated", {"retval": {"type": "Z"}})
    r(b"NSManagedObject", b"observationInfo", {"retval": {"type": "^v"}})
    r(b"NSManagedObject", b"setObservationInfo:", {"arguments": {2: {"type": "^v"}}})
    r(
        b"NSManagedObject",
        b"validateForDelete:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NSManagedObject",
        b"validateForInsert:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NSManagedObject",
        b"validateForUpdate:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NSManagedObject",
        b"validateValue:forKey:error:",
        {
            "retval": {"type": "Z"},
            "arguments": {2: {"type_modifier": b"N"}, 4: {"type_modifier": b"o"}},
        },
    )
    r(
        b"NSManagedObjectContext",
        b"automaticallyMergesChangesFromParent",
        {"retval": {"type": "Z"}},
    )
    r(
        b"NSManagedObjectContext",
        b"countForFetchRequest:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"executeFetchRequest:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"executeRequest:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"existingObjectWithID:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"NSManagedObjectContext", b"hasChanges", {"retval": {"type": "Z"}})
    r(
        b"NSManagedObjectContext",
        b"observeValueForKeyPath:ofObject:change:context:",
        {"arguments": {5: {"type": "^v"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"obtainPermanentIDsForObjects:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"performBlock:",
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
        b"NSManagedObjectContext",
        b"performBlockAndWait:",
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
        b"NSManagedObjectContext",
        b"propagatesDeletesAtEndOfEvent",
        {"retval": {"type": "Z"}},
    )
    r(
        b"NSManagedObjectContext",
        b"refreshObject:mergeChanges:",
        {"arguments": {3: {"type": "Z"}}},
    )
    r(b"NSManagedObjectContext", b"retainsRegisteredObjects", {"retval": {"type": "Z"}})
    r(
        b"NSManagedObjectContext",
        b"save:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"setAutomaticallyMergesChangesFromParent:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"setPropagatesDeletesAtEndOfEvent:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"setQueryGenerationFromToken:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"setRetainsRegisteredObjects:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"setShouldDeleteInaccessibleFaults:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSManagedObjectContext",
        b"shouldDeleteInaccessibleFaults",
        {"retval": {"type": "Z"}},
    )
    r(
        b"NSManagedObjectContext",
        b"shouldHandleInaccessibleFault:forObjectID:triggeredByProperty:",
        {"retval": {"type": "Z"}},
    )
    r(b"NSManagedObjectContext", b"tryLock", {"retval": {"type": "Z"}})
    r(b"NSManagedObjectID", b"isTemporaryID", {"retval": {"type": "Z"}})
    r(
        b"NSManagedObjectModel",
        b"isConfiguration:compatibleWithStoreMetadata:",
        {"retval": {"type": "Z"}},
    )
    r(
        b"NSMappingModel",
        b"inferredMappingModelForSourceModel:destinationModel:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSMergePolicy",
        b"resolveConflicts:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSMergePolicy",
        b"resolveConstraintConflicts:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSMergePolicy",
        b"resolveOptimisticLockingVersionConflicts:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSMigrationManager",
        b"migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:",
        {"retval": {"type": "Z"}, "arguments": {9: {"type_modifier": b"o"}}},
    )
    r(
        b"NSMigrationManager",
        b"setUsesStoreSpecificMigrationManager:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"NSMigrationManager",
        b"usesStoreSpecificMigrationManager",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"NSObject",
        b"controller:didChangeContentWithDifference:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"controller:didChangeContentWithSnapshot:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"controller:didChangeObject:atIndexPath:forChangeType:newIndexPath:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": sel32or64(b"I", b"Q")},
                6: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"controller:didChangeSection:atIndex:forChangeType:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": sel32or64(b"I", b"Q")},
                5: {"type": sel32or64(b"I", b"Q")},
            },
        },
    )
    r(
        b"NSObject",
        b"controller:sectionIndexTitleForSectionName:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"controllerDidChangeContent:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"controllerWillChangeContent:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"indexTitle", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"name", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"numberOfObjects", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"objects", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSPersistentCloudKitContainer",
        b"initializeCloudKitSchemaWithOptions:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"NSPersistentCloudKitContainerEvent", b"succeeded", {"retval": {"type": b"Z"}})
    r(
        b"NSPersistentContainer",
        b"loadPersistentStoresWithCompletionHandler:",
        {
            "arguments": {
                2: {
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
        b"NSPersistentContainer",
        b"performBackgroundTask:",
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
    r(b"NSPersistentStore", b"isReadOnly", {"retval": {"type": "Z"}})
    r(b"NSPersistentStore", b"loadMetadata", {"retval": {"type": "Z"}})
    r(
        b"NSPersistentStore",
        b"loadMetadata:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStore",
        b"metadataForPersistentStoreWithURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStore",
        b"migrationManagerClass",
        {"retval": {"type_modifier": b"o"}},
    )
    r(
        b"NSPersistentStore",
        b"setMetadata:forPersistentStoreWithURL:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(b"NSPersistentStore", b"setReadOnly:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"NSPersistentStoreCoordinator",
        b"addPersistentStoreWithDescription:completionHandler:",
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
        b"NSPersistentStoreCoordinator",
        b"addPersistentStoreWithType:configuration:URL:options:error:",
        {"arguments": {6: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"destroyPersistentStoreAtURL:withType:options:error:",
        {"retval": {"type": "Z"}, "arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"executeRequest:withContext:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"importStoreWithIdentifier:fromExternalRecordsDirectory:toURL:options:withType:error:",
        {"arguments": {7: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"metadataForPersistentStoreOfType:URL:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"metadataForPersistentStoreOfType:URL:options:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"metadataForPersistentStoreWithURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"migratePersistentStore:toURL:options:withType:error:",
        {"arguments": {6: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"performBlock:",
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
        b"NSPersistentStoreCoordinator",
        b"performBlockAndWait:",
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
        b"NSPersistentStoreCoordinator",
        b"removePersistentStore:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"removeUbiquitousContentAndPersistentStoreAtURL:options:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:",
        {"retval": {"type": "Z"}, "arguments": {7: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"setMetadata:forPersistentStoreOfType:URL:error:",
        {"retval": {"type": "Z"}, "arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"setMetadata:forPersistentStoreOfType:URL:options:error:",
        {"retval": {"type": "Z"}, "arguments": {6: {"type_modifier": b"o"}}},
    )
    r(
        b"NSPersistentStoreCoordinator",
        b"setURL:forPersistentStore:",
        {"retval": {"type": "Z"}},
    )
    r(b"NSPersistentStoreCoordinator", b"tryLock", {"retval": {"type": "Z"}})
    r(b"NSPersistentStoreDescription", b"isReadOnly", {"retval": {"type": "Z"}})
    r(
        b"NSPersistentStoreDescription",
        b"setReadOnly:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSPersistentStoreDescription",
        b"setShouldAddStoreAsynchronously:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSPersistentStoreDescription",
        b"setShouldInferMappingModelAutomatically:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSPersistentStoreDescription",
        b"setShouldMigrateStoreAutomatically:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSPersistentStoreDescription",
        b"shouldAddStoreAsynchronously",
        {"retval": {"type": "Z"}},
    )
    r(
        b"NSPersistentStoreDescription",
        b"shouldInferMappingModelAutomatically",
        {"retval": {"type": "Z"}},
    )
    r(
        b"NSPersistentStoreDescription",
        b"shouldMigrateStoreAutomatically",
        {"retval": {"type": "Z"}},
    )
    r(b"NSPropertyDescription", b"isIndexed", {"retval": {"type": "Z"}})
    r(b"NSPropertyDescription", b"isIndexedBySpotlight", {"retval": {"type": "Z"}})
    r(b"NSPropertyDescription", b"isOptional", {"retval": {"type": "Z"}})
    r(b"NSPropertyDescription", b"isStoredInExternalRecord", {"retval": {"type": "Z"}})
    r(b"NSPropertyDescription", b"isTransient", {"retval": {"type": "Z"}})
    r(b"NSPropertyDescription", b"setIndexed:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"NSPropertyDescription",
        b"setIndexedBySpotlight:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"NSPropertyDescription", b"setOptional:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"NSPropertyDescription",
        b"setStoredInExternalRecord:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"NSPropertyDescription", b"setTransient:", {"arguments": {2: {"type": "Z"}}})
    r(b"NSRelationshipDescription", b"isOrdered", {"retval": {"type": b"Z"}})
    r(b"NSRelationshipDescription", b"isToMany", {"retval": {"type": "Z"}})
    r(b"NSRelationshipDescription", b"setOrdered:", {"arguments": {2: {"type": b"Z"}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
