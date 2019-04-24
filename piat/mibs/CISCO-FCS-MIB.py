#
# PySNMP MIB module CISCO-FCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-FCS-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:33:43 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
FcGs3RejectReasonCode, = mibBuilder.importSymbols("CISCO-NS-MIB", "FcGs3RejectReasonCode")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcAddressId, FcNameId, FcPortModuleTypes, FcPortTxTypes, VsanIndex, DomainIdOrZero, FcPortTypes = mibBuilder.importSymbols("CISCO-ST-TC", "FcAddressId", "FcNameId", "FcPortModuleTypes", "FcPortTxTypes", "VsanIndex", "DomainIdOrZero", "FcPortTypes")
TimeIntervalSec, ListIndex, ListIndexOrZero = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec", "ListIndex", "ListIndexOrZero")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
FcList, = mibBuilder.importSymbols("CISCO-ZS-MIB", "FcList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Gauge32, MibIdentifier, Counter32, ObjectIdentity, NotificationType, iso, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Gauge32", "MibIdentifier", "Counter32", "ObjectIdentity", "NotificationType", "iso", "Bits", "Integer32")
TruthValue, DisplayString, RowStatus, TextualConvention, TimeStamp, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention", "TimeStamp", "TestAndIncr")
ciscoFcsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 297))
ciscoFcsMIB.setRevisions(('2004-02-19 00:00', '2003-08-20 00:00', '2002-12-18 00:00', '2002-10-07 00:00',))
if mibBuilder.loadTexts: ciscoFcsMIB.setLastUpdated('200402190000Z')
if mibBuilder.loadTexts: ciscoFcsMIB.setOrganization('Cisco Systems Inc.')
ciscoFcsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 297, 1))
fcsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 297, 2))
fcsConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1))
fcsStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2))
fcsInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 3))
fcsNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 4))
fcsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 4, 0))
class CreatedBy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("createdByMgmt", 1), ("learnedviaGS3", 2))

class FcIeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("switch", 3), ("hub", 4), ("bridge", 5))

class FcPortState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("online", 2), ("offline", 3), ("testing", 4), ("fault", 5), ("other", 6))

class FcPlatformType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("gateway", 3), ("converter", 4), ("hostBusAdapter", 5), ("swProxyAgent", 6), ("storageDevice", 7), ("host", 8), ("storageSubSys", 9), ("module", 10), ("swDriver", 11), ("storageAccessDev", 12))

class FcFcsRejReasonExplanation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("noAdditionalExplanation", 1), ("invNameIdForIEOrPort", 2), ("ieListNotAvailable", 3), ("ieTypeNotAvailable", 4), ("domainIdNotAvailable", 5), ("mgmtIdNotAvailable", 6), ("fabNameNotAvailable", 7), ("ielogNameNotAvailable", 8), ("mgmtAddrListNotAvailable", 9), ("ieInfoListNotAvailable", 10), ("portListNotAvailable", 11), ("portTypeNotAvailable", 12), ("phyPortNumNotAvailable", 13), ("attPortNameListNotAvailable", 14), ("portStateNotAvailable", 15), ("unableToRegIELogName", 16), ("platformNameNoExist", 17), ("platformNameAlreadyExists", 18), ("platformNodeNameNoExists", 19), ("platformNodeNameAlreadyExists", 20))

fcsVsanDiscoverySpinLock = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcsVsanDiscoverySpinLock.setStatus('current')
fcsVsanDiscoveryName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcsVsanDiscoveryName.setStatus('current')
fcsVsanDiscoveryList2k = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 3), FcList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcsVsanDiscoveryList2k.setStatus('current')
fcsVsanDiscoveryList4k = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 4), FcList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcsVsanDiscoveryList4k.setStatus('current')
fcsStartDiscovery = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("startDiscovery", 1), ("noOp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcsStartDiscovery.setStatus('current')
fcsDiscoveryStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 6), )
if mibBuilder.loadTexts: fcsDiscoveryStatusTable.setStatus('current')
fcsDiscoveryStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: fcsDiscoveryStatusEntry.setStatus('current')
fcsDiscoveryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inProgress", 1), ("completed", 2), ("databaseInvalid", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsDiscoveryStatus.setStatus('current')
fcsDiscoveryCompleteTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 6, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsDiscoveryCompleteTime.setStatus('current')
fcsVsanDiscoveryTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 7), TimeIntervalSec().subtype(subtypeSpec=ValueRangeConstraint(300, 1800)).clone(900)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcsVsanDiscoveryTimeOut.setStatus('current')
fcsDiscoveryInvalidateCache2k = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 8), FcList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcsDiscoveryInvalidateCache2k.setStatus('current')
fcsDiscoveryInvalidateCache4k = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 9), FcList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcsDiscoveryInvalidateCache4k.setStatus('current')
fcsIeNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 489472))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsIeNumber.setStatus('current')
fcsIeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11), )
if mibBuilder.loadTexts: fcsIeTable.setStatus('current')
fcsIeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FCS-MIB", "fcsIeName"))
if mibBuilder.loadTexts: fcsIeEntry.setStatus('current')
fcsIeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 1), FcNameId())
if mibBuilder.loadTexts: fcsIeName.setStatus('current')
fcsIeType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 2), FcIeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsIeType.setStatus('current')
fcsIeDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 3), DomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsIeDomainId.setStatus('current')
fcsIeMgmtId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 4), FcAddressId().clone(hexValue="000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsIeMgmtId.setStatus('current')
fcsIeFabricName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 5), FcNameId().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsIeFabricName.setStatus('current')
fcsIeLogicalName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsIeLogicalName.setStatus('current')
fcsIeMgmtAddrListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 7), ListIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsIeMgmtAddrListIndex.setStatus('current')
fcsIeInfoList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsIeInfoList.setStatus('current')
fcsIePortListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 9), ListIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsIePortListIndex.setStatus('current')
fcsMgmtAddrListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12), )
if mibBuilder.loadTexts: fcsMgmtAddrListTable.setStatus('current')
fcsMgmtAddrListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1), ).setIndexNames((0, "CISCO-FCS-MIB", "fcsMgmtAddrListIndex"), (0, "CISCO-FCS-MIB", "fcsMgmtAddrIndex"))
if mibBuilder.loadTexts: fcsMgmtAddrListEntry.setStatus('current')
fcsMgmtAddrListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1, 1), ListIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fcsMgmtAddrListIndex.setStatus('current')
fcsMgmtAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fcsMgmtAddrIndex.setStatus('current')
fcsMgmtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcsMgmtAddr.setStatus('current')
fcsMgmtAddrConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1, 4), CreatedBy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsMgmtAddrConfigSource.setStatus('current')
fcsMgmtAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcsMgmtAddrRowStatus.setStatus('current')
fcsPortListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 13), )
if mibBuilder.loadTexts: fcsPortListTable.setStatus('current')
fcsPortListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 13, 1), ).setIndexNames((0, "CISCO-FCS-MIB", "fcsPortListIndex"), (0, "CISCO-FCS-MIB", "fcsPortName"))
if mibBuilder.loadTexts: fcsPortListEntry.setStatus('current')
fcsPortListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 13, 1, 1), ListIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPortListIndex.setStatus('current')
fcsPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPortNumber.setStatus('current')
fcsPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15), )
if mibBuilder.loadTexts: fcsPortTable.setStatus('current')
fcsPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FCS-MIB", "fcsPortName"))
if mibBuilder.loadTexts: fcsPortEntry.setStatus('current')
fcsPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 1), FcNameId())
if mibBuilder.loadTexts: fcsPortName.setStatus('current')
fcsPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 2), FcPortTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPortType.setStatus('current')
fcsPortTXType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 3), FcPortTxTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPortTXType.setStatus('current')
fcsPortModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 4), FcPortModuleTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPortModuleType.setStatus('current')
fcsPortPhyPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPortPhyPortNum.setStatus('current')
fcsPortAttachPortNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 6), ListIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPortAttachPortNameIndex.setStatus('current')
fcsPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 7), FcPortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPortState.setStatus('current')
fcsAttachPortNameListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 16), )
if mibBuilder.loadTexts: fcsAttachPortNameListTable.setStatus('current')
fcsAttachPortNameListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 16, 1), ).setIndexNames((0, "CISCO-FCS-MIB", "fcsAttachPortNameListIndex"), (0, "CISCO-FCS-MIB", "fcsAttachPortName"))
if mibBuilder.loadTexts: fcsAttachPortNameListEntry.setStatus('current')
fcsAttachPortNameListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 16, 1, 1), ListIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fcsAttachPortNameListIndex.setStatus('current')
fcsAttachPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 16, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsAttachPortName.setStatus('current')
fcsPlatformNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPlatformNumber.setStatus('current')
fcsPlatformTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18), )
if mibBuilder.loadTexts: fcsPlatformTable.setStatus('current')
fcsPlatformEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FCS-MIB", "fcsPlatformIndex"))
if mibBuilder.loadTexts: fcsPlatformEntry.setStatus('current')
fcsPlatformIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fcsPlatformIndex.setStatus('current')
fcsPlatformName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcsPlatformName.setStatus('current')
fcsPlatformType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 3), FcPlatformType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcsPlatformType.setStatus('current')
fcsPlatformNodeNameListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 4), ListIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcsPlatformNodeNameListIndex.setStatus('current')
fcsPlatformMgmtAddrListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 5), ListIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcsPlatformMgmtAddrListIndex.setStatus('current')
fcsPlatformConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 6), CreatedBy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPlatformConfigSource.setStatus('current')
fcsPlatformValidation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("validate", 1), ("noop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcsPlatformValidation.setStatus('current')
fcsPlatformValidationResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("success", 1), ("inProgress", 2), ("nameInvalid", 3), ("nodeInvalid", 4), ("failure", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsPlatformValidationResult.setStatus('current')
fcsPlatformRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcsPlatformRowStatus.setStatus('current')
fcsNodeNameListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19), )
if mibBuilder.loadTexts: fcsNodeNameListTable.setStatus('current')
fcsNodeNameListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19, 1), ).setIndexNames((0, "CISCO-FCS-MIB", "fcsNodeNameListIndex"), (0, "CISCO-FCS-MIB", "fcsNodeName"))
if mibBuilder.loadTexts: fcsNodeNameListEntry.setStatus('current')
fcsNodeNameListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19, 1, 1), ListIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fcsNodeNameListIndex.setStatus('current')
fcsNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19, 1, 2), FcNameId())
if mibBuilder.loadTexts: fcsNodeName.setStatus('current')
fcsNodeNameConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19, 1, 3), CreatedBy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsNodeNameConfigSource.setStatus('current')
fcsNodeNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcsNodeNameRowStatus.setStatus('current')
fcsTotalRejects = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsTotalRejects.setStatus('current')
fcsStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2), )
if mibBuilder.loadTexts: fcsStatsTable.setStatus('current')
fcsStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: fcsStatsEntry.setStatus('current')
fcsRxGetReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsRxGetReqs.setStatus('current')
fcsTxGetReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsTxGetReqs.setStatus('current')
fcsRxRegReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsRxRegReqs.setStatus('current')
fcsTxRegReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsTxRegReqs.setStatus('current')
fcsRxDeregReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsRxDeregReqs.setStatus('current')
fcsTxDeregReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsTxDeregReqs.setStatus('current')
fcsTxRscns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsTxRscns.setStatus('current')
fcsRxRscns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsRxRscns.setStatus('current')
fcsRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsRejects.setStatus('current')
fcsRejReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 3, 1), FcGs3RejectReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsRejReasonCode.setStatus('current')
fcsRejReasonCodeExplanation = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 3, 2), FcFcsRejReasonExplanation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsRejReasonCodeExplanation.setStatus('current')
fcsMgmtAddrChangeVsanIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 3, 3), VsanIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fcsMgmtAddrChangeVsanIndex.setStatus('current')
fcsMgmtAddrChangeIeName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 3, 4), FcNameId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fcsMgmtAddrChangeIeName.setStatus('current')
fcsReqRejNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 20), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcsReqRejNotifyEnable.setStatus('current')
fcsDiscoveryCompleteNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 21), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcsDiscoveryCompleteNotifyEnable.setStatus('current')
fcsReqRejNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 4, 0, 1)).setObjects(("CISCO-FCS-MIB", "fcsRejReasonCode"), ("CISCO-FCS-MIB", "fcsRejReasonCodeExplanation"))
if mibBuilder.loadTexts: fcsReqRejNotify.setStatus('current')
fcsDiscoveryCompleteNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 4, 0, 2)).setObjects(("CISCO-FCS-MIB", "fcsVsanDiscoveryName"))
if mibBuilder.loadTexts: fcsDiscoveryCompleteNotify.setStatus('current')
fcsMgmtAddrChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 4, 0, 3)).setObjects(("CISCO-FCS-MIB", "fcsMgmtAddrChangeVsanIndex"), ("CISCO-FCS-MIB", "fcsMgmtAddrChangeIeName"))
if mibBuilder.loadTexts: fcsMgmtAddrChangeNotify.setStatus('current')
fcsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 1))
fcsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2))
fcsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 1, 1)).setObjects(("CISCO-FCS-MIB", "fcsConfigurationGroup"), ("CISCO-FCS-MIB", "fcsStatisticsGroup"), ("CISCO-FCS-MIB", "fcsNotificationControlGroup"), ("CISCO-FCS-MIB", "fcsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcsMIBCompliance = fcsMIBCompliance.setStatus('deprecated')
fcsMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 1, 2)).setObjects(("CISCO-FCS-MIB", "fcsConfigurationGroup"), ("CISCO-FCS-MIB", "fcsStatisticsGroup"), ("CISCO-FCS-MIB", "fcsNotificationControlGroupRev1"), ("CISCO-FCS-MIB", "fcsNotificationGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcsMIBComplianceRev1 = fcsMIBComplianceRev1.setStatus('current')
fcsConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 1)).setObjects(("CISCO-FCS-MIB", "fcsVsanDiscoverySpinLock"), ("CISCO-FCS-MIB", "fcsVsanDiscoveryName"), ("CISCO-FCS-MIB", "fcsVsanDiscoveryList2k"), ("CISCO-FCS-MIB", "fcsVsanDiscoveryList4k"), ("CISCO-FCS-MIB", "fcsStartDiscovery"), ("CISCO-FCS-MIB", "fcsDiscoveryStatus"), ("CISCO-FCS-MIB", "fcsDiscoveryCompleteTime"), ("CISCO-FCS-MIB", "fcsVsanDiscoveryTimeOut"), ("CISCO-FCS-MIB", "fcsDiscoveryInvalidateCache2k"), ("CISCO-FCS-MIB", "fcsDiscoveryInvalidateCache4k"), ("CISCO-FCS-MIB", "fcsIeNumber"), ("CISCO-FCS-MIB", "fcsIeType"), ("CISCO-FCS-MIB", "fcsIeDomainId"), ("CISCO-FCS-MIB", "fcsIeMgmtId"), ("CISCO-FCS-MIB", "fcsIeFabricName"), ("CISCO-FCS-MIB", "fcsIeLogicalName"), ("CISCO-FCS-MIB", "fcsIeMgmtAddrListIndex"), ("CISCO-FCS-MIB", "fcsIeInfoList"), ("CISCO-FCS-MIB", "fcsIePortListIndex"), ("CISCO-FCS-MIB", "fcsMgmtAddr"), ("CISCO-FCS-MIB", "fcsMgmtAddrConfigSource"), ("CISCO-FCS-MIB", "fcsMgmtAddrRowStatus"), ("CISCO-FCS-MIB", "fcsPortListIndex"), ("CISCO-FCS-MIB", "fcsPortNumber"), ("CISCO-FCS-MIB", "fcsPortType"), ("CISCO-FCS-MIB", "fcsPortTXType"), ("CISCO-FCS-MIB", "fcsPortModuleType"), ("CISCO-FCS-MIB", "fcsPortPhyPortNum"), ("CISCO-FCS-MIB", "fcsPortAttachPortNameIndex"), ("CISCO-FCS-MIB", "fcsPortState"), ("CISCO-FCS-MIB", "fcsAttachPortName"), ("CISCO-FCS-MIB", "fcsPlatformNumber"), ("CISCO-FCS-MIB", "fcsPlatformName"), ("CISCO-FCS-MIB", "fcsPlatformType"), ("CISCO-FCS-MIB", "fcsPlatformNodeNameListIndex"), ("CISCO-FCS-MIB", "fcsPlatformMgmtAddrListIndex"), ("CISCO-FCS-MIB", "fcsPlatformConfigSource"), ("CISCO-FCS-MIB", "fcsPlatformValidation"), ("CISCO-FCS-MIB", "fcsPlatformValidationResult"), ("CISCO-FCS-MIB", "fcsPlatformRowStatus"), ("CISCO-FCS-MIB", "fcsNodeNameConfigSource"), ("CISCO-FCS-MIB", "fcsNodeNameRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcsConfigurationGroup = fcsConfigurationGroup.setStatus('current')
fcsStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 2)).setObjects(("CISCO-FCS-MIB", "fcsTotalRejects"), ("CISCO-FCS-MIB", "fcsRxGetReqs"), ("CISCO-FCS-MIB", "fcsTxGetReqs"), ("CISCO-FCS-MIB", "fcsRxRegReqs"), ("CISCO-FCS-MIB", "fcsTxRegReqs"), ("CISCO-FCS-MIB", "fcsRxDeregReqs"), ("CISCO-FCS-MIB", "fcsTxDeregReqs"), ("CISCO-FCS-MIB", "fcsTxRscns"), ("CISCO-FCS-MIB", "fcsRxRscns"), ("CISCO-FCS-MIB", "fcsRejects"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcsStatisticsGroup = fcsStatisticsGroup.setStatus('current')
fcsNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 3)).setObjects(("CISCO-FCS-MIB", "fcsReqRejNotifyEnable"), ("CISCO-FCS-MIB", "fcsRejReasonCode"), ("CISCO-FCS-MIB", "fcsRejReasonCodeExplanation"), ("CISCO-FCS-MIB", "fcsDiscoveryCompleteNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcsNotificationControlGroup = fcsNotificationControlGroup.setStatus('deprecated')
fcsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 4)).setObjects(("CISCO-FCS-MIB", "fcsReqRejNotify"), ("CISCO-FCS-MIB", "fcsDiscoveryCompleteNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcsNotificationGroup = fcsNotificationGroup.setStatus('deprecated')
fcsNotificationGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 5)).setObjects(("CISCO-FCS-MIB", "fcsReqRejNotify"), ("CISCO-FCS-MIB", "fcsDiscoveryCompleteNotify"), ("CISCO-FCS-MIB", "fcsMgmtAddrChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcsNotificationGroupRev1 = fcsNotificationGroupRev1.setStatus('current')
fcsNotificationControlGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 6)).setObjects(("CISCO-FCS-MIB", "fcsReqRejNotifyEnable"), ("CISCO-FCS-MIB", "fcsRejReasonCode"), ("CISCO-FCS-MIB", "fcsRejReasonCodeExplanation"), ("CISCO-FCS-MIB", "fcsDiscoveryCompleteNotifyEnable"), ("CISCO-FCS-MIB", "fcsMgmtAddrChangeVsanIndex"), ("CISCO-FCS-MIB", "fcsMgmtAddrChangeIeName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcsNotificationControlGroupRev1 = fcsNotificationControlGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-FCS-MIB", fcsMgmtAddrListEntry=fcsMgmtAddrListEntry, fcsIeMgmtAddrListIndex=fcsIeMgmtAddrListIndex, fcsVsanDiscoveryName=fcsVsanDiscoveryName, fcsTxRegReqs=fcsTxRegReqs, fcsIeMgmtId=fcsIeMgmtId, fcsRxGetReqs=fcsRxGetReqs, fcsTotalRejects=fcsTotalRejects, FcPlatformType=FcPlatformType, fcsVsanDiscoveryList4k=fcsVsanDiscoveryList4k, fcsNodeNameListTable=fcsNodeNameListTable, fcsIeName=fcsIeName, PYSNMP_MODULE_ID=ciscoFcsMIB, fcsRxRegReqs=fcsRxRegReqs, fcsStartDiscovery=fcsStartDiscovery, fcsIeFabricName=fcsIeFabricName, fcsPlatformNodeNameListIndex=fcsPlatformNodeNameListIndex, ciscoFcsMIB=ciscoFcsMIB, fcsPlatformTable=fcsPlatformTable, fcsPortEntry=fcsPortEntry, fcsDiscoveryStatusTable=fcsDiscoveryStatusTable, fcsPlatformIndex=fcsPlatformIndex, fcsInformation=fcsInformation, fcsMgmtAddrListTable=fcsMgmtAddrListTable, fcsIeLogicalName=fcsIeLogicalName, fcsStatsEntry=fcsStatsEntry, fcsRxRscns=fcsRxRscns, fcsNotificationControlGroup=fcsNotificationControlGroup, fcsPortName=fcsPortName, ciscoFcsMIBObjects=ciscoFcsMIBObjects, fcsStats=fcsStats, fcsMIBCompliance=fcsMIBCompliance, fcsPlatformMgmtAddrListIndex=fcsPlatformMgmtAddrListIndex, fcsTxRscns=fcsTxRscns, fcsPlatformEntry=fcsPlatformEntry, fcsMgmtAddrChangeVsanIndex=fcsMgmtAddrChangeVsanIndex, fcsPortListTable=fcsPortListTable, fcsAttachPortNameListTable=fcsAttachPortNameListTable, fcsPlatformValidationResult=fcsPlatformValidationResult, fcsNodeNameConfigSource=fcsNodeNameConfigSource, fcsIeInfoList=fcsIeInfoList, fcsAttachPortName=fcsAttachPortName, fcsNodeNameListIndex=fcsNodeNameListIndex, FcFcsRejReasonExplanation=FcFcsRejReasonExplanation, fcsPortTXType=fcsPortTXType, fcsStatisticsGroup=fcsStatisticsGroup, fcsNotificationControlGroupRev1=fcsNotificationControlGroupRev1, fcsPortListIndex=fcsPortListIndex, fcsPlatformName=fcsPlatformName, fcsNodeNameListEntry=fcsNodeNameListEntry, fcsMgmtAddrListIndex=fcsMgmtAddrListIndex, fcsMIBGroups=fcsMIBGroups, fcsAttachPortNameListEntry=fcsAttachPortNameListEntry, fcsAttachPortNameListIndex=fcsAttachPortNameListIndex, fcsIeEntry=fcsIeEntry, fcsMIBComplianceRev1=fcsMIBComplianceRev1, fcsPlatformRowStatus=fcsPlatformRowStatus, fcsRxDeregReqs=fcsRxDeregReqs, fcsMgmtAddrChangeNotify=fcsMgmtAddrChangeNotify, CreatedBy=CreatedBy, fcsDiscoveryCompleteTime=fcsDiscoveryCompleteTime, fcsConfiguration=fcsConfiguration, fcsPortState=fcsPortState, fcsPlatformNumber=fcsPlatformNumber, fcsMgmtAddr=fcsMgmtAddr, fcsDiscoveryStatus=fcsDiscoveryStatus, fcsVsanDiscoverySpinLock=fcsVsanDiscoverySpinLock, fcsIeNumber=fcsIeNumber, fcsMgmtAddrIndex=fcsMgmtAddrIndex, fcsDiscoveryCompleteNotify=fcsDiscoveryCompleteNotify, fcsVsanDiscoveryList2k=fcsVsanDiscoveryList2k, fcsMgmtAddrConfigSource=fcsMgmtAddrConfigSource, fcsTxDeregReqs=fcsTxDeregReqs, fcsIePortListIndex=fcsIePortListIndex, fcsNodeName=fcsNodeName, fcsDiscoveryCompleteNotifyEnable=fcsDiscoveryCompleteNotifyEnable, FcPortState=FcPortState, fcsPortAttachPortNameIndex=fcsPortAttachPortNameIndex, fcsPortType=fcsPortType, FcIeType=FcIeType, fcsConfigurationGroup=fcsConfigurationGroup, fcsPortListEntry=fcsPortListEntry, fcsNotifications=fcsNotifications, fcsRejects=fcsRejects, fcsDiscoveryInvalidateCache2k=fcsDiscoveryInvalidateCache2k, fcsMgmtAddrRowStatus=fcsMgmtAddrRowStatus, fcsPlatformConfigSource=fcsPlatformConfigSource, fcsPortNumber=fcsPortNumber, fcsReqRejNotify=fcsReqRejNotify, fcsIeTable=fcsIeTable, fcsDiscoveryInvalidateCache4k=fcsDiscoveryInvalidateCache4k, fcsNotification=fcsNotification, fcsPortPhyPortNum=fcsPortPhyPortNum, fcsReqRejNotifyEnable=fcsReqRejNotifyEnable, fcsTxGetReqs=fcsTxGetReqs, fcsDiscoveryStatusEntry=fcsDiscoveryStatusEntry, fcsIeType=fcsIeType, fcsMgmtAddrChangeIeName=fcsMgmtAddrChangeIeName, fcsNodeNameRowStatus=fcsNodeNameRowStatus, fcsPortTable=fcsPortTable, fcsRejReasonCodeExplanation=fcsRejReasonCodeExplanation, fcsPlatformType=fcsPlatformType, fcsRejReasonCode=fcsRejReasonCode, fcsStatsTable=fcsStatsTable, fcsMIBCompliances=fcsMIBCompliances, fcsMIBConformance=fcsMIBConformance, fcsNotificationGroupRev1=fcsNotificationGroupRev1, fcsPortModuleType=fcsPortModuleType, fcsNotificationGroup=fcsNotificationGroup, fcsVsanDiscoveryTimeOut=fcsVsanDiscoveryTimeOut, fcsPlatformValidation=fcsPlatformValidation, fcsIeDomainId=fcsIeDomainId)
