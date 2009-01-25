from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSXMLParser (TestCase):
    def testConstants(self):
        self.assertEquals(NSXMLParserInternalError, 1)
        self.assertEquals(NSXMLParserOutOfMemoryError, 2)
        self.assertEquals(NSXMLParserDocumentStartError, 3)
        self.assertEquals(NSXMLParserEmptyDocumentError, 4)
        self.assertEquals(NSXMLParserPrematureDocumentEndError, 5)
        self.assertEquals(NSXMLParserInvalidHexCharacterRefError, 6)
        self.assertEquals(NSXMLParserInvalidDecimalCharacterRefError, 7)
        self.assertEquals(NSXMLParserInvalidCharacterRefError, 8)
        self.assertEquals(NSXMLParserInvalidCharacterError, 9)
        self.assertEquals(NSXMLParserCharacterRefAtEOFError, 10)
        self.assertEquals(NSXMLParserCharacterRefInPrologError, 11)
        self.assertEquals(NSXMLParserCharacterRefInEpilogError, 12)
        self.assertEquals(NSXMLParserCharacterRefInDTDError, 13)
        self.assertEquals(NSXMLParserEntityRefAtEOFError, 14)
        self.assertEquals(NSXMLParserEntityRefInPrologError, 15)
        self.assertEquals(NSXMLParserEntityRefInEpilogError, 16)
        self.assertEquals(NSXMLParserEntityRefInDTDError, 17)
        self.assertEquals(NSXMLParserParsedEntityRefAtEOFError, 18)
        self.assertEquals(NSXMLParserParsedEntityRefInPrologError, 19)
        self.assertEquals(NSXMLParserParsedEntityRefInEpilogError, 20)
        self.assertEquals(NSXMLParserParsedEntityRefInInternalSubsetError, 21)
        self.assertEquals(NSXMLParserEntityReferenceWithoutNameError, 22)
        self.assertEquals(NSXMLParserEntityReferenceMissingSemiError, 23)
        self.assertEquals(NSXMLParserParsedEntityRefNoNameError, 24)
        self.assertEquals(NSXMLParserParsedEntityRefMissingSemiError, 25)
        self.assertEquals(NSXMLParserUndeclaredEntityError, 26)
        self.assertEquals(NSXMLParserUnparsedEntityError, 28)
        self.assertEquals(NSXMLParserEntityIsExternalError, 29)
        self.assertEquals(NSXMLParserEntityIsParameterError, 30)
        self.assertEquals(NSXMLParserUnknownEncodingError, 31)
        self.assertEquals(NSXMLParserEncodingNotSupportedError, 32)
        self.assertEquals(NSXMLParserStringNotStartedError, 33)
        self.assertEquals(NSXMLParserStringNotClosedError, 34)
        self.assertEquals(NSXMLParserNamespaceDeclarationError, 35)
        self.assertEquals(NSXMLParserEntityNotStartedError, 36)
        self.assertEquals(NSXMLParserEntityNotFinishedError, 37)
        self.assertEquals(NSXMLParserLessThanSymbolInAttributeError, 38)
        self.assertEquals(NSXMLParserAttributeNotStartedError, 39)
        self.assertEquals(NSXMLParserAttributeNotFinishedError, 40)
        self.assertEquals(NSXMLParserAttributeHasNoValueError, 41)
        self.assertEquals(NSXMLParserAttributeRedefinedError, 42)
        self.assertEquals(NSXMLParserLiteralNotStartedError, 43)
        self.assertEquals(NSXMLParserLiteralNotFinishedError, 44)
        self.assertEquals(NSXMLParserCommentNotFinishedError, 45)
        self.assertEquals(NSXMLParserProcessingInstructionNotStartedError, 46)
        self.assertEquals(NSXMLParserProcessingInstructionNotFinishedError, 47)
        self.assertEquals(NSXMLParserNotationNotStartedError, 48)
        self.assertEquals(NSXMLParserNotationNotFinishedError, 49)
        self.assertEquals(NSXMLParserAttributeListNotStartedError, 50)
        self.assertEquals(NSXMLParserAttributeListNotFinishedError, 51)
        self.assertEquals(NSXMLParserMixedContentDeclNotStartedError, 52)
        self.assertEquals(NSXMLParserMixedContentDeclNotFinishedError, 53)
        self.assertEquals(NSXMLParserElementContentDeclNotStartedError, 54)
        self.assertEquals(NSXMLParserElementContentDeclNotFinishedError, 55)
        self.assertEquals(NSXMLParserXMLDeclNotStartedError, 56)
        self.assertEquals(NSXMLParserXMLDeclNotFinishedError, 57)
        self.assertEquals(NSXMLParserConditionalSectionNotStartedError, 58)
        self.assertEquals(NSXMLParserConditionalSectionNotFinishedError, 59)
        self.assertEquals(NSXMLParserExternalSubsetNotFinishedError, 60)
        self.assertEquals(NSXMLParserDOCTYPEDeclNotFinishedError, 61)
        self.assertEquals(NSXMLParserMisplacedCDATAEndStringError, 62)
        self.assertEquals(NSXMLParserCDATANotFinishedError, 63)
        self.assertEquals(NSXMLParserMisplacedXMLDeclarationError, 64)
        self.assertEquals(NSXMLParserSpaceRequiredError, 65)
        self.assertEquals(NSXMLParserSeparatorRequiredError, 66)
        self.assertEquals(NSXMLParserNMTOKENRequiredError, 67)
        self.assertEquals(NSXMLParserNAMERequiredError, 68)
        self.assertEquals(NSXMLParserPCDATARequiredError, 69)
        self.assertEquals(NSXMLParserURIRequiredError, 70)
        self.assertEquals(NSXMLParserPublicIdentifierRequiredError, 71)
        self.assertEquals(NSXMLParserLTRequiredError, 72)
        self.assertEquals(NSXMLParserGTRequiredError, 73)
        self.assertEquals(NSXMLParserLTSlashRequiredError, 74)
        self.assertEquals(NSXMLParserEqualExpectedError, 75)
        self.assertEquals(NSXMLParserTagNameMismatchError, 76)
        self.assertEquals(NSXMLParserUnfinishedTagError, 77)
        self.assertEquals(NSXMLParserStandaloneValueError, 78)
        self.assertEquals(NSXMLParserInvalidEncodingNameError, 79)
        self.assertEquals(NSXMLParserCommentContainsDoubleHyphenError, 80)
        self.assertEquals(NSXMLParserInvalidEncodingError, 81)
        self.assertEquals(NSXMLParserExternalStandaloneEntityError, 82)
        self.assertEquals(NSXMLParserInvalidConditionalSectionError, 83)
        self.assertEquals(NSXMLParserEntityValueRequiredError, 84)
        self.assertEquals(NSXMLParserNotWellBalancedError, 85)
        self.assertEquals(NSXMLParserExtraContentError, 86)
        self.assertEquals(NSXMLParserInvalidCharacterInEntityError, 87)
        self.assertEquals(NSXMLParserParsedEntityRefInInternalError, 88)
        self.assertEquals(NSXMLParserEntityRefLoopError, 89)
        self.assertEquals(NSXMLParserEntityBoundaryError, 90)
        self.assertEquals(NSXMLParserInvalidURIError, 91)
        self.assertEquals(NSXMLParserURIFragmentError, 92)
        self.assertEquals(NSXMLParserNoDTDError, 94)
        self.assertEquals(NSXMLParserDelegateAbortedParseError, 512)


if __name__ == "__main__":
    main()