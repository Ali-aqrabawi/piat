#
# PySNMP MIB module CISCO-ST-TC (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-ST-TC
# Produced by pysmi-0.3.4 at Sun Apr 21 23:47:38 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, Bits, ModuleIdentity, TimeTicks, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Gauge32, Unsigned32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Bits", "ModuleIdentity", "TimeTicks", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Gauge32", "Unsigned32", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
storageTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 4))
storageTextualConventions.setRevisions(('2012-08-08 00:00', '2011-07-26 00:00', '2010-12-24 00:00', '2008-05-16 00:00', '2005-12-17 00:00', '2004-05-18 00:00', '2003-09-26 00:00', '2003-08-07 00:00', '2002-10-04 00:00', '2002-09-24 00:00',))
if mibBuilder.loadTexts: storageTextualConventions.setLastUpdated('201208080000Z')
if mibBuilder.loadTexts: storageTextualConventions.setOrganization('Cisco Systems, Inc.')
class VsanIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class DomainId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 239)

class DomainIdOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 239)

class FcAddressId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class FcNameId(TextualConvention, OctetString):
    reference = 'Fibre Channel Framing and Signaling (FC-FS) Rev 1.70 - Section 14 Name_Indentifier Formats.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class FcNameIdOrZero(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )
class FcClassOfServices(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("classF", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4), ("class5", 5), ("class6", 6))

class FcPortTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("auto", 1), ("fPort", 2), ("flPort", 3), ("ePort", 4), ("bPort", 5), ("fxPort", 6), ("sdPort", 7), ("tlPort", 8), ("nPort", 9), ("nlPort", 10), ("nxPort", 11), ("tePort", 12), ("fvPort", 13), ("portOperDown", 14), ("stPort", 15), ("npPort", 16), ("tfPort", 17), ("tnpPort", 18))

class FcPortTxTypes(TextualConvention, Integer32):
    reference = 'IEEE Std 802.3-2005 carrier sense multiple access with collision detection (CSMA/CD) access method and physical layer specification.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("unknown", 1), ("longWaveLaser", 2), ("shortWaveLaser", 3), ("longWaveLaserCostReduced", 4), ("electrical", 5), ("tenGigBaseSr", 6), ("tenGigBaseLr", 7), ("tenGigBaseEr", 8), ("tenGigBaseLx4", 9), ("tenGigBaseSw", 10), ("tenGigBaseLw", 11), ("tenGigBaseEw", 12))

class FcPortModuleTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("gbic", 3), ("embedded", 4), ("glm", 5), ("gbicWithSerialID", 6), ("gbicWithoutSerialID", 7), ("sfpWithSerialID", 8), ("sfpWithoutSerialID", 9), ("xfp", 10), ("x2Short", 11), ("x2Medium", 12), ("x2Tall", 13), ("xpakShort", 14), ("xpakMedium", 15), ("xpakTall", 16), ("xenpak", 17), ("sfpDwdm", 18), ("qsfp", 19), ("x2Dwdm", 20))

class FcIfSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("auto", 1), ("oneG", 2), ("twoG", 3), ("fourG", 4), ("autoMaxTwoG", 5), ("eightG", 6), ("autoMaxFourG", 7), ("tenG", 8), ("autoMaxEightG", 9), ("sixteenG", 10), ("autoMaxSixteenG", 11))

class PortMemberList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class FcAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(3, 3), ValueSizeConstraint(8, 8), )
class FcAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("wwn", 1), ("fcid", 2))

class InterfaceOperMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("auto", 1), ("fPort", 2), ("flPort", 3), ("ePort", 4), ("bPort", 5), ("fxPort", 6), ("sdPort", 7), ("tlPort", 8), ("nPort", 9), ("nlPort", 10), ("nxPort", 11), ("tePort", 12), ("fvPort", 13), ("portOperDown", 14), ("stPort", 15), ("mgmtPort", 16), ("ipsPort", 17), ("evPort", 18), ("npPort", 19), ("tfPort", 20), ("tnpPort", 21))

class FcIfServiceStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2))

class FcIfSfpDiagLevelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("normal", 2), ("lowWarning", 3), ("lowAlarm", 4), ("highWarning", 5), ("highAlarm", 6))

mibBuilder.exportSymbols("CISCO-ST-TC", FcPortTxTypes=FcPortTxTypes, FcIfSpeed=FcIfSpeed, FcAddressId=FcAddressId, FcNameIdOrZero=FcNameIdOrZero, FcClassOfServices=FcClassOfServices, FcIfSfpDiagLevelType=FcIfSfpDiagLevelType, FcIfServiceStateType=FcIfServiceStateType, VsanIndex=VsanIndex, FcNameId=FcNameId, FcAddress=FcAddress, FcPortModuleTypes=FcPortModuleTypes, FcPortTypes=FcPortTypes, PortMemberList=PortMemberList, DomainId=DomainId, storageTextualConventions=storageTextualConventions, PYSNMP_MODULE_ID=storageTextualConventions, DomainIdOrZero=DomainIdOrZero, InterfaceOperMode=InterfaceOperMode, FcAddressType=FcAddressType)
