#
# PySNMP MIB module CISCO-ITP-RT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-ITP-RT-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:41:35 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
CItpTcRouteTableName, CItpTcTableLoadStatus, CItpTcPointCode, CItpTcQos, CItpTcLinksetId = mibBuilder.importSymbols("CISCO-ITP-TC-MIB", "CItpTcRouteTableName", "CItpTcTableLoadStatus", "CItpTcPointCode", "CItpTcQos", "CItpTcLinksetId")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, NotificationType, iso, Bits, Counter64, Unsigned32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "NotificationType", "iso", "Bits", "Counter64", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Gauge32", "IpAddress")
TruthValue, TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "TimeStamp")
ciscoItpRtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 228))
ciscoItpRtMIB.setRevisions(('2003-07-10 00:00', '2002-01-07 00:00', '2001-08-29 00:00',))
if mibBuilder.loadTexts: ciscoItpRtMIB.setLastUpdated('200307100000Z')
if mibBuilder.loadTexts: ciscoItpRtMIB.setOrganization('Cisco Systems, Inc.')
cItpRouteNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 228, 0))
cItpRtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 228, 1))
cItpRtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 228, 2))
cItpRtScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1))
cItpRtTables = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2))
cItpRtNotificationsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 3))
cItpRtConfigLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cItpRtConfigLastChanged.setStatus('deprecated')
cItpRtConfigLoad = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cItpRtConfigLoad.setStatus('deprecated')
cItpRtConfigLoadStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 3), CItpTcTableLoadStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cItpRtConfigLoadStatus.setStatus('deprecated')
cItpRtStateChangeCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cItpRtStateChangeCount.setStatus('deprecated')
cItpRtStateChangeNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cItpRtStateChangeNotifEnabled.setStatus('deprecated')
cItpRtChangeNotifDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cItpRtChangeNotifDelayTime.setStatus('deprecated')
cItpRtMaxDynamicRoutes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cItpRtMaxDynamicRoutes.setStatus('deprecated')
cItpRtChangeNotifWindowTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 900)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cItpRtChangeNotifWindowTime.setStatus('deprecated')
cItpRtChangeNotifMaxPerWindow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 9000)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cItpRtChangeNotifMaxPerWindow.setStatus('deprecated')
cItpRouteTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1), )
if mibBuilder.loadTexts: cItpRouteTable.setStatus('deprecated')
cItpRouteTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-ITP-RT-MIB", "cItpRouteTableName"), (0, "CISCO-ITP-RT-MIB", "cItpRouteDpc"), (0, "CISCO-ITP-RT-MIB", "cItpRouteMask"), (0, "CISCO-ITP-RT-MIB", "cItpRouteDestLsCost"), (0, "CISCO-ITP-RT-MIB", "cItpRouteDestLinkset"))
if mibBuilder.loadTexts: cItpRouteTableEntry.setStatus('deprecated')
cItpRouteTableName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 1), CItpTcRouteTableName())
if mibBuilder.loadTexts: cItpRouteTableName.setStatus('deprecated')
cItpRouteDpc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 2), CItpTcPointCode())
if mibBuilder.loadTexts: cItpRouteDpc.setStatus('deprecated')
cItpRouteDestLsCost = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)))
if mibBuilder.loadTexts: cItpRouteDestLsCost.setStatus('deprecated')
cItpRouteDestLinkset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 4), CItpTcLinksetId())
if mibBuilder.loadTexts: cItpRouteDestLinkset.setStatus('deprecated')
cItpRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215)))
if mibBuilder.loadTexts: cItpRouteMask.setStatus('deprecated')
cItpRouteQos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 6), CItpTcQos()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cItpRouteQos.setStatus('deprecated')
cItpRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("available", 2), ("restricted", 3), ("unavailable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cItpRouteStatus.setStatus('deprecated')
cItpRouteNonAdjStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("allowed", 2), ("restricted", 3), ("prohibited", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cItpRouteNonAdjStatus.setStatus('deprecated')
cItpRtNotifInfoSuppressedFlag = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 3, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cItpRtNotifInfoSuppressedFlag.setStatus('deprecated')
cItpRtNotifInfoStateChanges = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 3, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 480))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cItpRtNotifInfoStateChanges.setStatus('deprecated')
cItpRouteStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 228, 0, 1)).setObjects(("CISCO-ITP-RT-MIB", "cItpRtStateChangeCount"), ("CISCO-ITP-RT-MIB", "cItpRtNotifInfoSuppressedFlag"), ("CISCO-ITP-RT-MIB", "cItpRtNotifInfoStateChanges"))
if mibBuilder.loadTexts: cItpRouteStateChange.setStatus('deprecated')
cItpRtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 1))
cItpRtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 2))
cItpRtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 1, 1)).setObjects(("CISCO-ITP-RT-MIB", "cItpRtScalarGroup"), ("CISCO-ITP-RT-MIB", "cItpRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cItpRtMIBCompliance = cItpRtMIBCompliance.setStatus('deprecated')
cItpRtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 1, 2)).setObjects(("CISCO-ITP-RT-MIB", "cItpRtScalarGroup"), ("CISCO-ITP-RT-MIB", "cItpRouteGroup"), ("CISCO-ITP-RT-MIB", "cItpRtNotificationsGroup"), ("CISCO-ITP-RT-MIB", "cItpRtScalarGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cItpRtMIBComplianceRev1 = cItpRtMIBComplianceRev1.setStatus('deprecated')
cItpRtScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 2, 1)).setObjects(("CISCO-ITP-RT-MIB", "cItpRtConfigLastChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cItpRtScalarGroup = cItpRtScalarGroup.setStatus('deprecated')
cItpRouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 2, 2)).setObjects(("CISCO-ITP-RT-MIB", "cItpRouteQos"), ("CISCO-ITP-RT-MIB", "cItpRouteStatus"), ("CISCO-ITP-RT-MIB", "cItpRouteNonAdjStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cItpRouteGroup = cItpRouteGroup.setStatus('deprecated')
cItpRtNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 2, 3)).setObjects(("CISCO-ITP-RT-MIB", "cItpRouteStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cItpRtNotificationsGroup = cItpRtNotificationsGroup.setStatus('deprecated')
cItpRtScalarGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 2, 4)).setObjects(("CISCO-ITP-RT-MIB", "cItpRtConfigLoad"), ("CISCO-ITP-RT-MIB", "cItpRtConfigLoadStatus"), ("CISCO-ITP-RT-MIB", "cItpRtStateChangeCount"), ("CISCO-ITP-RT-MIB", "cItpRtStateChangeNotifEnabled"), ("CISCO-ITP-RT-MIB", "cItpRtChangeNotifDelayTime"), ("CISCO-ITP-RT-MIB", "cItpRtMaxDynamicRoutes"), ("CISCO-ITP-RT-MIB", "cItpRtChangeNotifWindowTime"), ("CISCO-ITP-RT-MIB", "cItpRtChangeNotifMaxPerWindow"), ("CISCO-ITP-RT-MIB", "cItpRtNotifInfoSuppressedFlag"), ("CISCO-ITP-RT-MIB", "cItpRtNotifInfoStateChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cItpRtScalarGroupRev1 = cItpRtScalarGroupRev1.setStatus('deprecated')
mibBuilder.exportSymbols("CISCO-ITP-RT-MIB", cItpRtNotificationsGroup=cItpRtNotificationsGroup, cItpRtNotificationsInfo=cItpRtNotificationsInfo, cItpRouteDpc=cItpRouteDpc, cItpRtChangeNotifWindowTime=cItpRtChangeNotifWindowTime, cItpRtConfigLastChanged=cItpRtConfigLastChanged, cItpRtMIBCompliance=cItpRtMIBCompliance, cItpRtMIBConformance=cItpRtMIBConformance, cItpRouteStatus=cItpRouteStatus, cItpRtConfigLoadStatus=cItpRtConfigLoadStatus, PYSNMP_MODULE_ID=ciscoItpRtMIB, cItpRouteQos=cItpRouteQos, cItpRouteDestLsCost=cItpRouteDestLsCost, ciscoItpRtMIB=ciscoItpRtMIB, cItpRouteNotifications=cItpRouteNotifications, cItpRtConfigLoad=cItpRtConfigLoad, cItpRouteNonAdjStatus=cItpRouteNonAdjStatus, cItpRtStateChangeNotifEnabled=cItpRtStateChangeNotifEnabled, cItpRouteMask=cItpRouteMask, cItpRtMIBComplianceRev1=cItpRtMIBComplianceRev1, cItpRtScalars=cItpRtScalars, cItpRouteTable=cItpRouteTable, cItpRouteTableEntry=cItpRouteTableEntry, cItpRouteDestLinkset=cItpRouteDestLinkset, cItpRtScalarGroup=cItpRtScalarGroup, cItpRtChangeNotifMaxPerWindow=cItpRtChangeNotifMaxPerWindow, cItpRtMIBGroups=cItpRtMIBGroups, cItpRtNotifInfoSuppressedFlag=cItpRtNotifInfoSuppressedFlag, cItpRtMaxDynamicRoutes=cItpRtMaxDynamicRoutes, cItpRouteGroup=cItpRouteGroup, cItpRtChangeNotifDelayTime=cItpRtChangeNotifDelayTime, cItpRtMIBObjects=cItpRtMIBObjects, cItpRtMIBCompliances=cItpRtMIBCompliances, cItpRtStateChangeCount=cItpRtStateChangeCount, cItpRouteTableName=cItpRouteTableName, cItpRtNotifInfoStateChanges=cItpRtNotifInfoStateChanges, cItpRtTables=cItpRtTables, cItpRouteStateChange=cItpRouteStateChange, cItpRtScalarGroupRev1=cItpRtScalarGroupRev1)