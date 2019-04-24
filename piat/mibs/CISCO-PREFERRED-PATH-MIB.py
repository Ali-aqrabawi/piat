#
# PySNMP MIB module CISCO-PREFERRED-PATH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-PREFERRED-PATH-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:28:24 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VsanIndex, FcAddressId = mibBuilder.importSymbols("CISCO-ST-TC", "VsanIndex", "FcAddressId")
notifyVsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "notifyVsanIndex")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, ObjectIdentity, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, MibIdentifier, iso, Counter32, Unsigned32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "ObjectIdentity", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "MibIdentifier", "iso", "Counter32", "Unsigned32", "Counter64", "IpAddress")
TextualConvention, StorageType, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "TruthValue", "RowStatus", "DisplayString")
ciscoPrefPathMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 592))
ciscoPrefPathMIB.setRevisions(('2006-10-26 14:44',))
if mibBuilder.loadTexts: ciscoPrefPathMIB.setLastUpdated('200610261444Z')
if mibBuilder.loadTexts: ciscoPrefPathMIB.setOrganization('Cisco Systems Inc.')
ciscoPrefPathMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 592, 0))
ciscoPrefPathMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 592, 1))
ciscoPrefPathMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 592, 2))
ciscoPrefPathConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1))
ciscoPrefPathInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2))
class CiscoPrefPathFcAddrMask(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("full", 1), ("domainArea", 2), ("domain", 3), ("noMask", 4))

class CiscoPrefPathStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("active", 2), ("pending", 3), ("deleted", 4), ("changed", 5))

class CiscoPrefPathIvrNextHopVsanId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4093)

class CiscoPrefPathPreferenceLevel(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

cPrefPathRouteMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1), )
if mibBuilder.loadTexts: cPrefPathRouteMapTable.setStatus('current')
cPrefPathRouteMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"))
if mibBuilder.loadTexts: cPrefPathRouteMapEntry.setStatus('current')
cPrefPathRouteMapVsanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 1), VsanIndex())
if mibBuilder.loadTexts: cPrefPathRouteMapVsanIndex.setStatus('current')
cPrefPathRouteMapRouteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)))
if mibBuilder.loadTexts: cPrefPathRouteMapRouteIndex.setStatus('current')
cPrefPathRouteMapIntfPrefStrict = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cPrefPathRouteMapIntfPrefStrict.setStatus('current')
cPrefPathRouteMapRouteActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cPrefPathRouteMapRouteActive.setStatus('current')
cPrefPathRouteMapActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cPrefPathRouteMapActive.setStatus('deprecated')
cPrefPathRouteMapStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 6), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cPrefPathRouteMapStorageType.setStatus('current')
cPrefPathRouteMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cPrefPathRouteMapRowStatus.setStatus('current')
cPrefPathRouteMapGlobalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 2), )
if mibBuilder.loadTexts: cPrefPathRouteMapGlobalTable.setStatus('current')
cPrefPathRouteMapGlobalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"))
if mibBuilder.loadTexts: cPrefPathRouteMapGlobalEntry.setStatus('current')
cPrefPathRouteMapGlobalActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("partial", 2), ("none", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cPrefPathRouteMapGlobalActive.setStatus('current')
cPrefPathRouteMapMatchTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3), )
if mibBuilder.loadTexts: cPrefPathRouteMapMatchTable.setStatus('current')
cPrefPathRouteMapMatchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcAddr"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcAddrMask"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcIntf"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchDstAddr"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchDstAddrMask"))
if mibBuilder.loadTexts: cPrefPathRouteMapMatchEntry.setStatus('current')
cPrefPathRMapMatchSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 1), FcAddressId())
if mibBuilder.loadTexts: cPrefPathRMapMatchSrcAddr.setStatus('current')
cPrefPathRMapMatchSrcAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 2), CiscoPrefPathFcAddrMask())
if mibBuilder.loadTexts: cPrefPathRMapMatchSrcAddrMask.setStatus('current')
cPrefPathRMapMatchSrcIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 3), InterfaceIndexOrZero())
if mibBuilder.loadTexts: cPrefPathRMapMatchSrcIntf.setStatus('current')
cPrefPathRMapMatchDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 4), FcAddressId())
if mibBuilder.loadTexts: cPrefPathRMapMatchDstAddr.setStatus('current')
cPrefPathRMapMatchDstAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 5), CiscoPrefPathFcAddrMask())
if mibBuilder.loadTexts: cPrefPathRMapMatchDstAddrMask.setStatus('current')
cPrefPathRMapMatchRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cPrefPathRMapMatchRowStatus.setStatus('current')
cPrefPathRouteMapSetTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4), )
if mibBuilder.loadTexts: cPrefPathRouteMapSetTable.setStatus('current')
cPrefPathRouteMapSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIntfPref"))
if mibBuilder.loadTexts: cPrefPathRouteMapSetEntry.setStatus('current')
cPrefPathRMapSetIntfPref = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4, 1, 1), CiscoPrefPathPreferenceLevel())
if mibBuilder.loadTexts: cPrefPathRMapSetIntfPref.setStatus('current')
cPrefPathRMapSetIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cPrefPathRMapSetIntf.setStatus('current')
cPrefPathRMapSetIvrNextHopVsanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4, 1, 3), CiscoPrefPathIvrNextHopVsanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cPrefPathRMapSetIvrNextHopVsanId.setStatus('current')
cPrefPathRMapSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cPrefPathRMapSetRowStatus.setStatus('current')
cPrefPathRouteMapInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 1), )
if mibBuilder.loadTexts: cPrefPathRouteMapInfoTable.setStatus('current')
cPrefPathRouteMapInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"))
if mibBuilder.loadTexts: cPrefPathRouteMapInfoEntry.setStatus('current')
cPrefPathRMapSelectedPref = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 1, 1, 1), CiscoPrefPathPreferenceLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cPrefPathRMapSelectedPref.setStatus('current')
cPrefPathRMapSelectedIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cPrefPathRMapSelectedIntf.setStatus('current')
cPrefPathRMapSelIvrNextHopVsanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 1, 1, 3), CiscoPrefPathIvrNextHopVsanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cPrefPathRMapSelIvrNextHopVsanId.setStatus('current')
cPrefPathRouteMapMatchInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 2), )
if mibBuilder.loadTexts: cPrefPathRouteMapMatchInfoTable.setStatus('current')
cPrefPathRouteMapMatchInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcAddr"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcAddrMask"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcIntf"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchDstAddr"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchDstAddrMask"))
if mibBuilder.loadTexts: cPrefPathRouteMapMatchInfoEntry.setStatus('current')
cPrefPathRMapMatchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 2, 1, 1), CiscoPrefPathStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cPrefPathRMapMatchStatus.setStatus('current')
cPrefPathRouteMapSetInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 3), )
if mibBuilder.loadTexts: cPrefPathRouteMapSetInfoTable.setStatus('current')
cPrefPathRouteMapSetInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"), (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIntfPref"))
if mibBuilder.loadTexts: cPrefPathRouteMapSetInfoEntry.setStatus('current')
cPrefPathRouteMapSetInfoIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cPrefPathRouteMapSetInfoIntf.setStatus('current')
cPrefPathRouteMapSetInfoIvrNextHopVId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 3, 1, 2), CiscoPrefPathIvrNextHopVsanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cPrefPathRouteMapSetInfoIvrNextHopVId.setStatus('current')
cPrefPathRouteMapSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 3, 1, 3), CiscoPrefPathStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cPrefPathRouteMapSetStatus.setStatus('current')
cPrefPathHwFailureNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cPrefPathHwFailureNotifEnable.setStatus('current')
ciscoPrefPathHWFailureNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 592, 0, 1)).setObjects(("CISCO-VSAN-MIB", "notifyVsanIndex"))
if mibBuilder.loadTexts: ciscoPrefPathHWFailureNotify.setStatus('current')
ciscoPrefPathMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 1))
ciscoPrefPathMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2))
ciscoPrefPathMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 1, 1)).setObjects(("CISCO-PREFERRED-PATH-MIB", "ciscoPrefPathConfigGroup"), ("CISCO-PREFERRED-PATH-MIB", "ciscoPrefPathInfoGroup"), ("CISCO-PREFERRED-PATH-MIB", "ciscoPrefPathNotifyGroup"), ("CISCO-PREFERRED-PATH-MIB", "ciscoPrefPathNotifyConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrefPathMIBCompliance = ciscoPrefPathMIBCompliance.setStatus('deprecated')
ciscoPrefPathMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 1, 2)).setObjects(("CISCO-PREFERRED-PATH-MIB", "ciscoPrefPathConfigGroupRev1"), ("CISCO-PREFERRED-PATH-MIB", "ciscoPrefPathInfoGroup"), ("CISCO-PREFERRED-PATH-MIB", "ciscoPrefPathNotifyGroup"), ("CISCO-PREFERRED-PATH-MIB", "ciscoPrefPathNotifyConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrefPathMIBComplianceRev1 = ciscoPrefPathMIBComplianceRev1.setStatus('current')
ciscoPrefPathConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2, 1)).setObjects(("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIntf"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIvrNextHopVsanId"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapIntfPrefStrict"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteActive"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapActive"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapStorageType"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRowStatus"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchRowStatus"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrefPathConfigGroup = ciscoPrefPathConfigGroup.setStatus('deprecated')
ciscoPrefPathInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2, 2)).setObjects(("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSelectedPref"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSelectedIntf"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSelIvrNextHopVsanId"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchStatus"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapSetInfoIntf"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapSetInfoIvrNextHopVId"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapSetStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrefPathInfoGroup = ciscoPrefPathInfoGroup.setStatus('current')
ciscoPrefPathNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2, 3)).setObjects(("CISCO-PREFERRED-PATH-MIB", "ciscoPrefPathHWFailureNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrefPathNotifyGroup = ciscoPrefPathNotifyGroup.setStatus('current')
ciscoPrefPathNotifyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2, 4)).setObjects(("CISCO-PREFERRED-PATH-MIB", "cPrefPathHwFailureNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrefPathNotifyConfigGroup = ciscoPrefPathNotifyConfigGroup.setStatus('current')
ciscoPrefPathConfigGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2, 5)).setObjects(("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapGlobalActive"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIntf"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIvrNextHopVsanId"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapIntfPrefStrict"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteActive"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapStorageType"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRowStatus"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchRowStatus"), ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrefPathConfigGroupRev1 = ciscoPrefPathConfigGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-PREFERRED-PATH-MIB", cPrefPathRMapMatchDstAddrMask=cPrefPathRMapMatchDstAddrMask, cPrefPathHwFailureNotifEnable=cPrefPathHwFailureNotifEnable, ciscoPrefPathConfigGroup=ciscoPrefPathConfigGroup, PYSNMP_MODULE_ID=ciscoPrefPathMIB, cPrefPathRouteMapMatchInfoEntry=cPrefPathRouteMapMatchInfoEntry, cPrefPathRouteMapMatchTable=cPrefPathRouteMapMatchTable, CiscoPrefPathPreferenceLevel=CiscoPrefPathPreferenceLevel, cPrefPathRMapMatchSrcAddrMask=cPrefPathRMapMatchSrcAddrMask, cPrefPathRMapMatchSrcAddr=cPrefPathRMapMatchSrcAddr, cPrefPathRouteMapGlobalActive=cPrefPathRouteMapGlobalActive, cPrefPathRouteMapIntfPrefStrict=cPrefPathRouteMapIntfPrefStrict, cPrefPathRMapSetIvrNextHopVsanId=cPrefPathRMapSetIvrNextHopVsanId, cPrefPathRMapSelIvrNextHopVsanId=cPrefPathRMapSelIvrNextHopVsanId, ciscoPrefPathMIBComplianceRev1=ciscoPrefPathMIBComplianceRev1, cPrefPathRouteMapTable=cPrefPathRouteMapTable, cPrefPathRouteMapGlobalTable=cPrefPathRouteMapGlobalTable, cPrefPathRouteMapMatchEntry=cPrefPathRouteMapMatchEntry, cPrefPathRMapMatchSrcIntf=cPrefPathRMapMatchSrcIntf, ciscoPrefPathConfiguration=ciscoPrefPathConfiguration, cPrefPathRMapSetRowStatus=cPrefPathRMapSetRowStatus, cPrefPathRouteMapGlobalEntry=cPrefPathRouteMapGlobalEntry, ciscoPrefPathMIBNotifs=ciscoPrefPathMIBNotifs, cPrefPathRMapSelectedIntf=cPrefPathRMapSelectedIntf, ciscoPrefPathInformation=ciscoPrefPathInformation, CiscoPrefPathStatus=CiscoPrefPathStatus, cPrefPathRouteMapStorageType=cPrefPathRouteMapStorageType, ciscoPrefPathMIBCompliance=ciscoPrefPathMIBCompliance, cPrefPathRouteMapActive=cPrefPathRouteMapActive, cPrefPathRouteMapSetInfoIntf=cPrefPathRouteMapSetInfoIntf, ciscoPrefPathMIB=ciscoPrefPathMIB, ciscoPrefPathNotifyConfigGroup=ciscoPrefPathNotifyConfigGroup, cPrefPathRouteMapRouteActive=cPrefPathRouteMapRouteActive, cPrefPathRouteMapRouteIndex=cPrefPathRouteMapRouteIndex, cPrefPathRMapSetIntfPref=cPrefPathRMapSetIntfPref, cPrefPathRMapMatchStatus=cPrefPathRMapMatchStatus, cPrefPathRouteMapEntry=cPrefPathRouteMapEntry, cPrefPathRouteMapSetStatus=cPrefPathRouteMapSetStatus, ciscoPrefPathHWFailureNotify=ciscoPrefPathHWFailureNotify, ciscoPrefPathMIBConform=ciscoPrefPathMIBConform, ciscoPrefPathNotifyGroup=ciscoPrefPathNotifyGroup, cPrefPathRouteMapInfoTable=cPrefPathRouteMapInfoTable, cPrefPathRouteMapSetInfoEntry=cPrefPathRouteMapSetInfoEntry, ciscoPrefPathConfigGroupRev1=ciscoPrefPathConfigGroupRev1, cPrefPathRouteMapSetInfoIvrNextHopVId=cPrefPathRouteMapSetInfoIvrNextHopVId, cPrefPathRouteMapInfoEntry=cPrefPathRouteMapInfoEntry, ciscoPrefPathMIBCompliances=ciscoPrefPathMIBCompliances, cPrefPathRMapSetIntf=cPrefPathRMapSetIntf, cPrefPathRouteMapMatchInfoTable=cPrefPathRouteMapMatchInfoTable, cPrefPathRouteMapSetInfoTable=cPrefPathRouteMapSetInfoTable, cPrefPathRouteMapSetEntry=cPrefPathRouteMapSetEntry, ciscoPrefPathInfoGroup=ciscoPrefPathInfoGroup, CiscoPrefPathFcAddrMask=CiscoPrefPathFcAddrMask, cPrefPathRouteMapSetTable=cPrefPathRouteMapSetTable, CiscoPrefPathIvrNextHopVsanId=CiscoPrefPathIvrNextHopVsanId, cPrefPathRouteMapRowStatus=cPrefPathRouteMapRowStatus, ciscoPrefPathMIBGroups=ciscoPrefPathMIBGroups, cPrefPathRouteMapVsanIndex=cPrefPathRouteMapVsanIndex, ciscoPrefPathMIBObjects=ciscoPrefPathMIBObjects, cPrefPathRMapSelectedPref=cPrefPathRMapSelectedPref, cPrefPathRMapMatchDstAddr=cPrefPathRMapMatchDstAddr, cPrefPathRMapMatchRowStatus=cPrefPathRMapMatchRowStatus)