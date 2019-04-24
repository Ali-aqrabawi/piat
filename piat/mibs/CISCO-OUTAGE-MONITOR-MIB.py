#
# PySNMP MIB module CISCO-OUTAGE-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-OUTAGE-MONITOR-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:41:14 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Bits, Integer32, Gauge32, IpAddress, ObjectIdentity, Counter64, MibIdentifier, NotificationType, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Bits", "Integer32", "Gauge32", "IpAddress", "ObjectIdentity", "Counter64", "MibIdentifier", "NotificationType", "Counter32", "iso")
TextualConvention, DisplayString, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "DateAndTime")
ciscoOutageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 280))
ciscoOutageMIB.setRevisions(('2005-08-22 00:00', '2002-09-09 00:00',))
if mibBuilder.loadTexts: ciscoOutageMIB.setLastUpdated('200508220000Z')
if mibBuilder.loadTexts: ciscoOutageMIB.setOrganization('Cisco Systems, Inc.')
ciscoOutageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 1))
cOutageBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1))
cOutageHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2))
cOutageDescription = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3))
cOutageMonObject = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4))
cOutageCpmMapping = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5))
cOutageRmtMapping = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6))
cOutageLntMapping = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 7))
class OutageMonObjectType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("interface", 1), ("physicalEntity", 2), ("swProcess", 3), ("remoteObject", 4), ("logicalEntity", 5))

cOutageApplVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageApplVersion.setStatus('current')
cOutageNotificationsSent = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1, 2), Counter32()).setUnits('notifications').setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageNotificationsSent.setStatus('current')
cOutageNotificationsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOutageNotificationsEnabled.setStatus('current')
cOutageNotificationFilterEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOutageNotificationFilterEnabled.setStatus('current')
cOutageFilteredEvents = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageFilteredEvents.setStatus('current')
cOutageHistTableSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 1), Unsigned32().clone(100)).setUnits('entries').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOutageHistTableSize.setStatus('current')
cOutageHistMsgsFlushed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 2), Counter32()).setUnits('messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageHistMsgsFlushed.setStatus('current')
cOutageHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3), )
if mibBuilder.loadTexts: cOutageHistoryTable.setStatus('current')
cOutageHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageEventIndex"))
if mibBuilder.loadTexts: cOutageHistoryEntry.setStatus('current')
cOutageEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cOutageEventIndex.setStatus('current')
cOutageEventObjectType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 2), OutageMonObjectType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageEventObjectType.setStatus('current')
cOutageEventMonObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageEventMonObjectIndex.setStatus('current')
cOutageEventTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageEventTypeIndex.setStatus('current')
cOutageEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageEventTime.setStatus('current')
cOutageEventInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageEventInterval.setStatus('current')
cOutageEventTypeMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3, 1), )
if mibBuilder.loadTexts: cOutageEventTypeMapTable.setStatus('current')
cOutageEventTypeMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTypeMapIndex"))
if mibBuilder.loadTexts: cOutageEventTypeMapEntry.setStatus('current')
cOutageEventTypeMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cOutageEventTypeMapIndex.setStatus('current')
cOutageEventTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageEventTypeName.setStatus('current')
cOutageEventTypeDescrText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageEventTypeDescrText.setStatus('current')
cOutageObjectTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1), )
if mibBuilder.loadTexts: cOutageObjectTable.setStatus('current')
cOutageObjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageObjectType"), (0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageMonitoredObjectIndex"))
if mibBuilder.loadTexts: cOutageObjectEntry.setStatus('current')
cOutageObjectType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 1), OutageMonObjectType())
if mibBuilder.loadTexts: cOutageObjectType.setStatus('current')
cOutageMonitoredObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cOutageMonitoredObjectIndex.setStatus('current')
cOutageCurrentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageCurrentStatus.setStatus('current')
cOutageAOTSinceMeasureStarted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageAOTSinceMeasureStarted.setStatus('current')
cOutageNAFSinceMeasureStarted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageNAFSinceMeasureStarted.setStatus('current')
cOutageRecordingStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageRecordingStartTime.setStatus('current')
cOutageCpmMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5, 1), )
if mibBuilder.loadTexts: cOutageCpmMapTable.setStatus('current')
cOutageCpmMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5, 1, 1), ).setIndexNames((0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageCpmMapIndex"))
if mibBuilder.loadTexts: cOutageCpmMapEntry.setStatus('current')
cOutageCpmMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cOutageCpmMapIndex.setStatus('current')
cOutageCpmCPUTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageCpmCPUTotalIndex.setStatus('current')
cOutageCpmProcessPID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageCpmProcessPID.setStatus('current')
cOutageRemoteObjMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1), )
if mibBuilder.loadTexts: cOutageRemoteObjMapTable.setStatus('current')
cOutageRemoteObjMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1, 1), ).setIndexNames((0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageRemoteObjMapIndex"))
if mibBuilder.loadTexts: cOutageRemoteObjMapEntry.setStatus('current')
cOutageRemoteObjMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cOutageRemoteObjMapIndex.setStatus('current')
cOutageRemoteObjIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageRemoteObjIDType.setStatus('current')
cOutageRemoteObjID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageRemoteObjID.setStatus('current')
cOutageRemoteObjDescrText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageRemoteObjDescrText.setStatus('current')
cOutageLogicalObjMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 7, 1), )
if mibBuilder.loadTexts: cOutageLogicalObjMapTable.setStatus('current')
cOutageLogicalObjMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 7, 1, 1), ).setIndexNames((0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageLogicalObjMapIndex"))
if mibBuilder.loadTexts: cOutageLogicalObjMapEntry.setStatus('current')
cOutageLogicalObjMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 7, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cOutageLogicalObjMapIndex.setStatus('current')
cOutageLogicalObjDescrText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 7, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOutageLogicalObjDescrText.setStatus('current')
ciscoOutageMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 2))
ciscoOutageMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 2, 0))
ciscoOutageEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 280, 2, 0, 1)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventObjectType"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventMonObjectIndex"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTypeIndex"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTime"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventInterval"))
if mibBuilder.loadTexts: ciscoOutageEvent.setStatus('current')
ciscoOutageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 3))
ciscoOutageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 1))
ciscoOutageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2))
ciscoOutageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 1, 1)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "ciscoOutageBasicGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoEventHistoryGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoEventDescrGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoObjectOutageGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoCpmMappingGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoRmtMappingGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoOutageNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOutageMIBCompliance = ciscoOutageMIBCompliance.setStatus('deprecated')
ciscoOutageMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 1, 2)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "ciscoOutageBasicGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoEventHistoryGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoEventDescrGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoObjectOutageGroupRev"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoCpmMappingGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoRmtMappingGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoLntMappingGroup"), ("CISCO-OUTAGE-MONITOR-MIB", "ciscoOutageNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOutageMIBComplianceRev1 = ciscoOutageMIBComplianceRev1.setStatus('current')
ciscoOutageBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 1)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "cOutageApplVersion"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageNotificationsSent"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageNotificationsEnabled"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageNotificationFilterEnabled"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageFilteredEvents"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOutageBasicGroup = ciscoOutageBasicGroup.setStatus('current')
ciscoEventHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 2)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "cOutageHistTableSize"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageHistMsgsFlushed"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventObjectType"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventMonObjectIndex"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTypeIndex"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTime"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEventHistoryGroup = ciscoEventHistoryGroup.setStatus('current')
ciscoEventDescrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 3)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTypeName"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTypeDescrText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEventDescrGroup = ciscoEventDescrGroup.setStatus('current')
ciscoObjectOutageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 4)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "cOutageCurrentStatus"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageAOTSinceMeasureStarted"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageNAFSinceMeasureStarted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoObjectOutageGroup = ciscoObjectOutageGroup.setStatus('deprecated')
ciscoCpmMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 5)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "cOutageCpmCPUTotalIndex"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageCpmProcessPID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpmMappingGroup = ciscoCpmMappingGroup.setStatus('current')
ciscoRmtMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 6)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "cOutageRemoteObjIDType"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageRemoteObjID"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageRemoteObjDescrText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmtMappingGroup = ciscoRmtMappingGroup.setStatus('current')
ciscoOutageNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 7)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "ciscoOutageEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOutageNotificationsGroup = ciscoOutageNotificationsGroup.setStatus('current')
ciscoObjectOutageGroupRev = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 8)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "cOutageCurrentStatus"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageRecordingStartTime"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageAOTSinceMeasureStarted"), ("CISCO-OUTAGE-MONITOR-MIB", "cOutageNAFSinceMeasureStarted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoObjectOutageGroupRev = ciscoObjectOutageGroupRev.setStatus('current')
ciscoLntMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 9)).setObjects(("CISCO-OUTAGE-MONITOR-MIB", "cOutageLogicalObjDescrText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLntMappingGroup = ciscoLntMappingGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-OUTAGE-MONITOR-MIB", cOutageHistoryEntry=cOutageHistoryEntry, cOutageRemoteObjDescrText=cOutageRemoteObjDescrText, cOutageMonitoredObjectIndex=cOutageMonitoredObjectIndex, ciscoOutageMIBCompliance=ciscoOutageMIBCompliance, ciscoOutageMIBCompliances=ciscoOutageMIBCompliances, ciscoOutageBasicGroup=ciscoOutageBasicGroup, cOutageCpmMapping=cOutageCpmMapping, cOutageEventMonObjectIndex=cOutageEventMonObjectIndex, cOutageCurrentStatus=cOutageCurrentStatus, cOutageRecordingStartTime=cOutageRecordingStartTime, cOutageEventTypeMapIndex=cOutageEventTypeMapIndex, cOutageHistMsgsFlushed=cOutageHistMsgsFlushed, ciscoOutageMIBObjects=ciscoOutageMIBObjects, cOutageCpmMapTable=cOutageCpmMapTable, ciscoOutageNotificationsGroup=ciscoOutageNotificationsGroup, ciscoEventDescrGroup=ciscoEventDescrGroup, cOutageCpmCPUTotalIndex=cOutageCpmCPUTotalIndex, cOutageCpmProcessPID=cOutageCpmProcessPID, OutageMonObjectType=OutageMonObjectType, ciscoEventHistoryGroup=ciscoEventHistoryGroup, cOutageCpmMapEntry=cOutageCpmMapEntry, cOutageRemoteObjIDType=cOutageRemoteObjIDType, cOutageApplVersion=cOutageApplVersion, ciscoLntMappingGroup=ciscoLntMappingGroup, cOutageNotificationsSent=cOutageNotificationsSent, cOutageAOTSinceMeasureStarted=cOutageAOTSinceMeasureStarted, cOutageLogicalObjMapEntry=cOutageLogicalObjMapEntry, ciscoOutageEvent=ciscoOutageEvent, ciscoRmtMappingGroup=ciscoRmtMappingGroup, cOutageEventTypeDescrText=cOutageEventTypeDescrText, ciscoOutageMIBGroups=ciscoOutageMIBGroups, cOutageHistoryTable=cOutageHistoryTable, cOutageLogicalObjMapTable=cOutageLogicalObjMapTable, cOutageNotificationsEnabled=cOutageNotificationsEnabled, ciscoObjectOutageGroup=ciscoObjectOutageGroup, cOutageMonObject=cOutageMonObject, cOutageEventIndex=cOutageEventIndex, cOutageRemoteObjMapIndex=cOutageRemoteObjMapIndex, cOutageRemoteObjID=cOutageRemoteObjID, cOutageEventTypeMapTable=cOutageEventTypeMapTable, cOutageObjectEntry=cOutageObjectEntry, cOutageRemoteObjMapEntry=cOutageRemoteObjMapEntry, cOutageRemoteObjMapTable=cOutageRemoteObjMapTable, PYSNMP_MODULE_ID=ciscoOutageMIB, ciscoOutageMIB=ciscoOutageMIB, cOutageEventTypeIndex=cOutageEventTypeIndex, cOutageBasicInfo=cOutageBasicInfo, cOutageDescription=cOutageDescription, ciscoOutageMIBConformance=ciscoOutageMIBConformance, cOutageEventTypeMapEntry=cOutageEventTypeMapEntry, cOutageFilteredEvents=cOutageFilteredEvents, ciscoOutageMIBNotificationPrefix=ciscoOutageMIBNotificationPrefix, ciscoObjectOutageGroupRev=ciscoObjectOutageGroupRev, cOutageEventInterval=cOutageEventInterval, cOutageLntMapping=cOutageLntMapping, cOutageEventObjectType=cOutageEventObjectType, cOutageEventTypeName=cOutageEventTypeName, cOutageCpmMapIndex=cOutageCpmMapIndex, cOutageLogicalObjDescrText=cOutageLogicalObjDescrText, cOutageRmtMapping=cOutageRmtMapping, cOutageNAFSinceMeasureStarted=cOutageNAFSinceMeasureStarted, cOutageHistTableSize=cOutageHistTableSize, cOutageLogicalObjMapIndex=cOutageLogicalObjMapIndex, cOutageNotificationFilterEnabled=cOutageNotificationFilterEnabled, cOutageObjectType=cOutageObjectType, cOutageHistory=cOutageHistory, ciscoCpmMappingGroup=ciscoCpmMappingGroup, ciscoOutageMIBComplianceRev1=ciscoOutageMIBComplianceRev1, ciscoOutageMIBNotifications=ciscoOutageMIBNotifications, cOutageObjectTable=cOutageObjectTable, cOutageEventTime=cOutageEventTime)
