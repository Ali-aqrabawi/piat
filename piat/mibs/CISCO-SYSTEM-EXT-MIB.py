#
# PySNMP MIB module CISCO-SYSTEM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-SYSTEM-EXT-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:44:00 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, EntPhysicalIndexOrZero = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec", "EntPhysicalIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32, IpAddress, Unsigned32, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32", "IpAddress", "Unsigned32", "iso", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "DateAndTime")
ciscoSystemExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 305))
ciscoSystemExtMIB.setRevisions(('2016-07-19 00:00', '2016-06-07 00:00', '2015-08-19 00:00', '2007-08-06 00:00', '2006-11-29 00:00', '2006-09-25 00:00', '2005-11-09 00:00', '2005-06-14 00:00', '2004-04-19 00:00', '2003-05-02 00:00', '2003-03-02 00:00', '2002-11-19 00:00', '2002-10-04 00:00',))
if mibBuilder.loadTexts: ciscoSystemExtMIB.setLastUpdated('201606140000Z')
if mibBuilder.loadTexts: ciscoSystemExtMIB.setOrganization('Cisco Systems Inc.')
ciscoSystemExtMIBNotifsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 0))
ciscoSystemExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1))
ciscoSystemExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 2))
ciscoSysInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1))
ciscoSysErrorGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2))
ciscoHaGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3))
ciscoSwFailureGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4))
ciscoSwFailureNotifControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 5))
ciscoSystemSwitchingModeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 6))
ciscoSystemMaintModeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7))
ciscoSystemMaintModeNotifControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 8))
ciscoSystemReloadGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 9))
class CseHaRestartReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 1), ("ungracefulExit", 2), ("otherSignal", 3), ("sigterm", 4), ("softwareUpgrade", 5), ("configUpdate", 6), ("configRemove", 7), ("shutdown", 8), ("aborted", 9), ("heartbeatFailure", 10), ("userTerminate", 11), ("gracefulExit", 12), ("noCallHomeFailure", 13), ("serviceTimeout", 14))

class CiscoMaintModeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("maintenance", 2), ("unplannedMaint", 3))

cseSysCPUUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysCPUUtilization.setStatus('current')
cseSysMemoryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysMemoryUtilization.setStatus('current')
cseSysConfLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysConfLastChange.setStatus('current')
cseSysAutoSync = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sync", 1), ("noSync", 2))).clone('noSync')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cseSysAutoSync.setStatus('current')
cseSysAutoSyncState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inProgress", 1), ("succeeded", 2), ("failed", 3), ("notStarted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysAutoSyncState.setStatus('current')
cseWriteErase = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("eraseAll", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cseWriteErase.setStatus('current')
cseSysConsolePortStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("notConnected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysConsolePortStatus.setStatus('current')
cseSysTelnetServiceActivation = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cseSysTelnetServiceActivation.setStatus('current')
cseSysFIPSModeActivation = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cseSysFIPSModeActivation.setStatus('current')
cseSysUpTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 10), TimeIntervalSec()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysUpTime.setStatus('current')
cseSnmpErrorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1), )
if mibBuilder.loadTexts: cseSnmpErrorTable.setStatus('current')
cseSnmpErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorAddressType"), (0, "CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorAddress"), (0, "CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorRequestId"))
if mibBuilder.loadTexts: cseSnmpErrorEntry.setStatus('current')
cseSnmpErrorAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cseSnmpErrorAddressType.setStatus('current')
cseSnmpErrorAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: cseSnmpErrorAddress.setStatus('current')
cseSnmpErrorRequestId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cseSnmpErrorRequestId.setStatus('current')
cseSnmpErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSnmpErrorCode.setStatus('current')
cseSnmpErrorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSnmpErrorDescription.setStatus('current')
cseHaRestartReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 2), CseHaRestartReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cseHaRestartReason.setStatus('current')
cseHaRestartStateless = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 3), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cseHaRestartStateless.setStatus('current')
cseHaRestartService = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cseHaRestartService.setStatus('current')
cseHaShutDownReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cseHaShutDownReason.setStatus('current')
cseSwCorePath = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSwCorePath.setStatus('current')
cseSwCoresTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2), )
if mibBuilder.loadTexts: cseSwCoresTable.setStatus('current')
cseSwCoresEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1), ).setIndexNames((0, "CISCO-SYSTEM-EXT-MIB", "cseSwCoresModule"), (0, "CISCO-SYSTEM-EXT-MIB", "cseSwCoresProcName"), (0, "CISCO-SYSTEM-EXT-MIB", "cseSwCoresInstance"))
if mibBuilder.loadTexts: cseSwCoresEntry.setStatus('current')
cseSwCoresModule = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 1), EntPhysicalIndexOrZero())
if mibBuilder.loadTexts: cseSwCoresModule.setStatus('current')
cseSwCoresProcName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cseSwCoresProcName.setStatus('current')
cseSwCoresInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cseSwCoresInstance.setStatus('current')
cseSwCoresPID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSwCoresPID.setStatus('current')
cseSwCoresTimeCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSwCoresTimeCreated.setStatus('current')
cseSwCoresSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSwCoresSlotNum.setStatus('current')
cseSwCoresFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSwCoresFileName.setStatus('current')
ciscoSystemSwitchingModeAdmin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("notApplicable", 2), ("nexus3000", 3), ("nexus9000", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoSystemSwitchingModeAdmin.setStatus('current')
ciscoSystemSwitchingModeOper = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("notApplicable", 2), ("nexus3000", 3), ("nexus9000", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSystemSwitchingModeOper.setStatus('current')
cseMaintModeState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 1), CiscoMaintModeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseMaintModeState.setStatus('current')
cseSystemReloadPending = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 9, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSystemReloadPending.setStatus('current')
ciscoSwFailureNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 5, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoSwFailureNotifEnable.setStatus('current')
ciscoSystemNormalModeNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 8, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoSystemNormalModeNotifEnable.setStatus('current')
ciscoSystemMaintModeNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 8, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoSystemMaintModeNotifEnable.setStatus('current')
cseHaNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5))
cseHaNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5, 0))
cseHaRestartNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5, 0, 1)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseHaRestartReason"), ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartService"), ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartStateless"))
if mibBuilder.loadTexts: cseHaRestartNotify.setStatus('current')
cseShutDownNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5, 0, 2)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseHaShutDownReason"))
if mibBuilder.loadTexts: cseShutDownNotify.setStatus('current')
cseFailNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3))
cseFailNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3, 0))
cseFailSwCoreNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3, 0, 1))
if mibBuilder.loadTexts: cseFailSwCoreNotify.setStatus('current')
cseFailSwCoreNotifyExtended = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3, 0, 2)).setObjects(("SNMPv2-MIB", "sysName"), ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresFileName"), ("CISCO-SYSTEM-EXT-MIB", "cseSwCorePath"), ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresPID"))
if mibBuilder.loadTexts: cseFailSwCoreNotifyExtended.setStatus('current')
cseMaintModeNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2))
cseMaintModeNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2, 0))
cseNormalModeChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2, 0, 1)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseMaintModeState"))
if mibBuilder.loadTexts: cseNormalModeChangeNotify.setStatus('current')
cseMaintModeChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2, 0, 2)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseMaintModeState"))
if mibBuilder.loadTexts: cseMaintModeChangeNotify.setStatus('current')
ciscoSystemExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1))
ciscoSystemExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2))
ciscoSystemExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 1)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBCompliance = ciscoSystemExtMIBCompliance.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 2)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev1 = ciscoSystemExtMIBComplianceRev1.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 3)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev2 = ciscoSystemExtMIBComplianceRev2.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 4)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev3 = ciscoSystemExtMIBComplianceRev3.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 5)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev4 = ciscoSystemExtMIBComplianceRev4.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 6)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev5 = ciscoSystemExtMIBComplianceRev5.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 7)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup3"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev6 = ciscoSystemExtMIBComplianceRev6.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 8)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoFIPSGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev7 = ciscoSystemExtMIBComplianceRev7.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 9)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev3"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoFIPSGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev8 = ciscoSystemExtMIBComplianceRev8.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 11)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev3"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoFIPSGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemSwitchingModeObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev9 = ciscoSystemExtMIBComplianceRev9.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 12)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev3"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoFIPSGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemSwitchingModeObjectsGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemMaintModeObjectsGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemMaintModeNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev10 = ciscoSystemExtMIBComplianceRev10.setStatus('current')
ciscoSystemExtInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 1)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysCPUUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysMemoryUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysConfLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoGroup = ciscoSystemExtInfoGroup.setStatus('deprecated')
ciscoSystemExtErrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 2)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorCode"), ("CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtErrorGroup = ciscoSystemExtErrorGroup.setStatus('current')
ciscoSystemExtHaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 3)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseHaRestartReason"), ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartService"), ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartStateless"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtHaGroup = ciscoSystemExtHaGroup.setStatus('current')
ciscoSystemExtNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 4)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseHaRestartNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtNotificationGroup = ciscoSystemExtNotificationGroup.setStatus('current')
ciscoSystemExtInfoGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 5)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysCPUUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysMemoryUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysConfLastChange"), ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSync"), ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSyncState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoGroupRev1 = ciscoSystemExtInfoGroupRev1.setStatus('deprecated')
ciscoSystemExtInfoGroupOptional = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 6)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseWriteErase"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoGroupOptional = ciscoSystemExtInfoGroupOptional.setStatus('current')
ciscoSystemExtSwFailureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 7)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSwCorePath"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtSwFailureGroup = ciscoSystemExtSwFailureGroup.setStatus('current')
ciscoSystemExtInfoGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 8)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysConsolePortStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoGroupRev2 = ciscoSystemExtInfoGroupRev2.setStatus('current')
ciscoSystemExtSwFailureGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 9)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSwCoresPID"), ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresTimeCreated"), ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresSlotNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtSwFailureGroup2 = ciscoSystemExtSwFailureGroup2.setStatus('current')
ciscoSystemExtNotificationGroupSup1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 10)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseShutDownNotify"), ("CISCO-SYSTEM-EXT-MIB", "cseFailSwCoreNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtNotificationGroupSup1 = ciscoSystemExtNotificationGroupSup1.setStatus('current')
ciscoSystemExtHaGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 11)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseHaShutDownReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtHaGroupRev1 = ciscoSystemExtHaGroupRev1.setStatus('current')
ciscoSystemExtInfoTelnetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 12)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysTelnetServiceActivation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoTelnetGroup = ciscoSystemExtInfoTelnetGroup.setStatus('current')
ciscoSystemExtNotificationGroupSup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 13)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseFailSwCoreNotifyExtended"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtNotificationGroupSup2 = ciscoSystemExtNotificationGroupSup2.setStatus('current')
ciscoSystemExtSwFailureGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 14)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSwCoresFileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtSwFailureGroup3 = ciscoSystemExtSwFailureGroup3.setStatus('current')
ciscoSystemExtSwFailureControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 15)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSwFailureNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtSwFailureControlGroup = ciscoSystemExtSwFailureControlGroup.setStatus('current')
ciscoSystemExtInfoFIPSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 16)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysFIPSModeActivation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoFIPSGroup = ciscoSystemExtInfoFIPSGroup.setStatus('current')
ciscoSystemExtInfoGroupRev3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 17)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysCPUUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysMemoryUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysConfLastChange"), ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSync"), ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSyncState"), ("CISCO-SYSTEM-EXT-MIB", "cseSysUpTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoGroupRev3 = ciscoSystemExtInfoGroupRev3.setStatus('current')
ciscoSystemSwitchingModeObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 18)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemSwitchingModeAdmin"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemSwitchingModeOper"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemSwitchingModeObjectsGroup = ciscoSystemSwitchingModeObjectsGroup.setStatus('current')
ciscoSystemMaintModeObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 19)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseMaintModeState"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemNormalModeNotifEnable"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemMaintModeNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemMaintModeObjectsGroup = ciscoSystemMaintModeObjectsGroup.setStatus('current')
ciscoSystemMaintModeNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 20)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseNormalModeChangeNotify"), ("CISCO-SYSTEM-EXT-MIB", "cseMaintModeChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemMaintModeNotificationGroup = ciscoSystemMaintModeNotificationGroup.setStatus('current')
ciscoSystemReloadObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 21)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSystemReloadPending"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemReloadObjectsGroup = ciscoSystemReloadObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSTEM-EXT-MIB", ciscoSystemExtMIBObjects=ciscoSystemExtMIBObjects, ciscoSystemExtMIBComplianceRev7=ciscoSystemExtMIBComplianceRev7, cseSysAutoSyncState=cseSysAutoSyncState, cseSwCoresTimeCreated=cseSwCoresTimeCreated, cseHaRestartReason=cseHaRestartReason, ciscoSystemExtInfoGroupRev2=ciscoSystemExtInfoGroupRev2, ciscoSystemMaintModeNotificationGroup=ciscoSystemMaintModeNotificationGroup, ciscoSystemReloadObjectsGroup=ciscoSystemReloadObjectsGroup, cseSysTelnetServiceActivation=cseSysTelnetServiceActivation, cseFailNotificationPrefix=cseFailNotificationPrefix, ciscoSystemSwitchingModeAdmin=ciscoSystemSwitchingModeAdmin, ciscoSystemExtNotificationGroupSup1=ciscoSystemExtNotificationGroupSup1, ciscoSystemExtMIBNotifsPrefix=ciscoSystemExtMIBNotifsPrefix, cseFailSwCoreNotify=cseFailSwCoreNotify, ciscoSystemExtSwFailureControlGroup=ciscoSystemExtSwFailureControlGroup, ciscoSystemExtMIBComplianceRev6=ciscoSystemExtMIBComplianceRev6, CseHaRestartReason=CseHaRestartReason, ciscoSystemExtMIBComplianceRev2=ciscoSystemExtMIBComplianceRev2, ciscoSystemSwitchingModeOper=ciscoSystemSwitchingModeOper, cseSysCPUUtilization=cseSysCPUUtilization, cseMaintModeState=cseMaintModeState, cseHaNotificationPrefix=cseHaNotificationPrefix, cseNormalModeChangeNotify=cseNormalModeChangeNotify, cseWriteErase=cseWriteErase, ciscoSystemExtInfoTelnetGroup=ciscoSystemExtInfoTelnetGroup, cseFailSwCoreNotifyExtended=cseFailSwCoreNotifyExtended, cseSnmpErrorRequestId=cseSnmpErrorRequestId, cseHaNotification=cseHaNotification, ciscoSystemSwitchingModeGroup=ciscoSystemSwitchingModeGroup, ciscoSystemExtNotificationGroup=ciscoSystemExtNotificationGroup, ciscoSwFailureNotifEnable=ciscoSwFailureNotifEnable, cseSnmpErrorCode=cseSnmpErrorCode, ciscoSystemExtMIBCompliances=ciscoSystemExtMIBCompliances, cseSnmpErrorEntry=cseSnmpErrorEntry, ciscoSwFailureGroup=ciscoSwFailureGroup, ciscoSystemMaintModeNotifEnable=ciscoSystemMaintModeNotifEnable, cseFailNotification=cseFailNotification, ciscoSystemExtMIBComplianceRev9=ciscoSystemExtMIBComplianceRev9, ciscoSwFailureNotifControl=ciscoSwFailureNotifControl, cseSwCoresTable=cseSwCoresTable, cseSwCoresSlotNum=cseSwCoresSlotNum, cseSysFIPSModeActivation=cseSysFIPSModeActivation, ciscoSystemReloadGroup=ciscoSystemReloadGroup, PYSNMP_MODULE_ID=ciscoSystemExtMIB, cseSwCoresFileName=cseSwCoresFileName, ciscoHaGroup=ciscoHaGroup, cseSnmpErrorTable=cseSnmpErrorTable, CiscoMaintModeState=CiscoMaintModeState, cseSwCorePath=cseSwCorePath, cseShutDownNotify=cseShutDownNotify, ciscoSystemExtMIBComplianceRev3=ciscoSystemExtMIBComplianceRev3, cseSysAutoSync=cseSysAutoSync, cseSwCoresProcName=cseSwCoresProcName, ciscoSystemExtInfoGroupRev1=ciscoSystemExtInfoGroupRev1, ciscoSysInfoGroup=ciscoSysInfoGroup, ciscoSystemExtInfoGroup=ciscoSystemExtInfoGroup, cseSnmpErrorDescription=cseSnmpErrorDescription, cseSnmpErrorAddress=cseSnmpErrorAddress, ciscoSystemExtMIBGroups=ciscoSystemExtMIBGroups, cseHaShutDownReason=cseHaShutDownReason, ciscoSystemExtHaGroupRev1=ciscoSystemExtHaGroupRev1, ciscoSystemExtMIBComplianceRev4=ciscoSystemExtMIBComplianceRev4, cseSwCoresPID=cseSwCoresPID, ciscoSystemExtInfoFIPSGroup=ciscoSystemExtInfoFIPSGroup, cseSnmpErrorAddressType=cseSnmpErrorAddressType, ciscoSystemExtMIBComplianceRev5=ciscoSystemExtMIBComplianceRev5, ciscoSystemExtMIBConformance=ciscoSystemExtMIBConformance, cseMaintModeChangeNotify=cseMaintModeChangeNotify, ciscoSystemExtNotificationGroupSup2=ciscoSystemExtNotificationGroupSup2, ciscoSystemExtMIBCompliance=ciscoSystemExtMIBCompliance, cseSysMemoryUtilization=cseSysMemoryUtilization, cseSwCoresEntry=cseSwCoresEntry, ciscoSystemExtMIBComplianceRev1=ciscoSystemExtMIBComplianceRev1, cseSysConsolePortStatus=cseSysConsolePortStatus, ciscoSystemSwitchingModeObjectsGroup=ciscoSystemSwitchingModeObjectsGroup, ciscoSystemMaintModeNotifControl=ciscoSystemMaintModeNotifControl, cseSwCoresModule=cseSwCoresModule, ciscoSystemMaintModeObjectsGroup=ciscoSystemMaintModeObjectsGroup, cseHaRestartStateless=cseHaRestartStateless, cseMaintModeNotificationPrefix=cseMaintModeNotificationPrefix, cseHaRestartNotify=cseHaRestartNotify, ciscoSystemExtMIB=ciscoSystemExtMIB, ciscoSystemExtSwFailureGroup=ciscoSystemExtSwFailureGroup, cseSystemReloadPending=cseSystemReloadPending, ciscoSystemMaintModeGroup=ciscoSystemMaintModeGroup, ciscoSystemExtHaGroup=ciscoSystemExtHaGroup, cseSysUpTime=cseSysUpTime, ciscoSystemExtErrorGroup=ciscoSystemExtErrorGroup, ciscoSystemNormalModeNotifEnable=ciscoSystemNormalModeNotifEnable, cseMaintModeNotification=cseMaintModeNotification, ciscoSystemExtInfoGroupOptional=ciscoSystemExtInfoGroupOptional, ciscoSystemExtSwFailureGroup3=ciscoSystemExtSwFailureGroup3, ciscoSystemExtSwFailureGroup2=ciscoSystemExtSwFailureGroup2, cseHaRestartService=cseHaRestartService, ciscoSystemExtInfoGroupRev3=ciscoSystemExtInfoGroupRev3, ciscoSystemExtMIBComplianceRev10=ciscoSystemExtMIBComplianceRev10, cseSwCoresInstance=cseSwCoresInstance, ciscoSysErrorGroup=ciscoSysErrorGroup, ciscoSystemExtMIBComplianceRev8=ciscoSystemExtMIBComplianceRev8, cseSysConfLastChange=cseSysConfLastChange)
