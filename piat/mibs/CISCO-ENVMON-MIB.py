#
# PySNMP MIB module CISCO-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-ENVMON-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:47:08 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Gauge32, iso, ModuleIdentity, MibIdentifier, Bits, Counter32, TimeTicks, Counter64, Unsigned32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Gauge32", "iso", "ModuleIdentity", "MibIdentifier", "Bits", "Counter32", "TimeTicks", "Counter64", "Unsigned32", "Integer32", "NotificationType")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoEnvMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 13))
ciscoEnvMonMIB.setRevisions(('2003-12-01 00:00', '2003-11-25 00:00', '2002-10-15 00:00', '2002-07-17 00:00', '2002-02-04 00:00', '2001-08-30 00:00', '2001-08-16 00:00', '2001-05-07 00:00', '2000-01-31 00:00', '1998-10-22 00:00', '1998-08-05 00:00', '1996-11-12 00:00', '1995-08-15 00:00', '1995-03-13 00:00',))
if mibBuilder.loadTexts: ciscoEnvMonMIB.setLastUpdated('200312010000Z')
if mibBuilder.loadTexts: ciscoEnvMonMIB.setOrganization('Cisco Systems, Inc.')
class CiscoEnvMonState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("shutdown", 4), ("notPresent", 5), ("notFunctioning", 6))

class CiscoSignedGauge(TextualConvention, Integer32):
    status = 'current'

ciscoEnvMonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 13, 1))
ciscoEnvMonPresent = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("oldAgs", 1), ("ags", 2), ("c7000", 3), ("ci", 4), ("cAccessMon", 6), ("cat6000", 7), ("ubr7200", 8), ("cat4000", 9), ("c10000", 10), ("osr7600", 11), ("c7600", 12), ("c37xx", 13), ("other", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonPresent.setStatus('current')
ciscoEnvMonVoltageStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2), )
if mibBuilder.loadTexts: ciscoEnvMonVoltageStatusTable.setStatus('current')
ciscoEnvMonVoltageStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1), ).setIndexNames((0, "CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusIndex"))
if mibBuilder.loadTexts: ciscoEnvMonVoltageStatusEntry.setStatus('current')
ciscoEnvMonVoltageStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ciscoEnvMonVoltageStatusIndex.setStatus('current')
ciscoEnvMonVoltageStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonVoltageStatusDescr.setStatus('current')
ciscoEnvMonVoltageStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 3), CiscoSignedGauge()).setUnits('millivolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonVoltageStatusValue.setStatus('current')
ciscoEnvMonVoltageThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 4), Integer32()).setUnits('millivolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonVoltageThresholdLow.setStatus('current')
ciscoEnvMonVoltageThresholdHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 5), Integer32()).setUnits('millivolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonVoltageThresholdHigh.setStatus('current')
ciscoEnvMonVoltageLastShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 6), Integer32()).setUnits('millivolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonVoltageLastShutdown.setStatus('current')
ciscoEnvMonVoltageState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 2, 1, 7), CiscoEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonVoltageState.setStatus('current')
ciscoEnvMonTemperatureStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3), )
if mibBuilder.loadTexts: ciscoEnvMonTemperatureStatusTable.setStatus('current')
ciscoEnvMonTemperatureStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1), ).setIndexNames((0, "CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusIndex"))
if mibBuilder.loadTexts: ciscoEnvMonTemperatureStatusEntry.setStatus('current')
ciscoEnvMonTemperatureStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ciscoEnvMonTemperatureStatusIndex.setStatus('current')
ciscoEnvMonTemperatureStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonTemperatureStatusDescr.setStatus('current')
ciscoEnvMonTemperatureStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 3), Gauge32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonTemperatureStatusValue.setStatus('current')
ciscoEnvMonTemperatureThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 4), Integer32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonTemperatureThreshold.setStatus('current')
ciscoEnvMonTemperatureLastShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 5), Integer32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonTemperatureLastShutdown.setStatus('current')
ciscoEnvMonTemperatureState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 3, 1, 6), CiscoEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonTemperatureState.setStatus('current')
ciscoEnvMonFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 4), )
if mibBuilder.loadTexts: ciscoEnvMonFanStatusTable.setStatus('current')
ciscoEnvMonFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 4, 1), ).setIndexNames((0, "CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusIndex"))
if mibBuilder.loadTexts: ciscoEnvMonFanStatusEntry.setStatus('current')
ciscoEnvMonFanStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ciscoEnvMonFanStatusIndex.setStatus('current')
ciscoEnvMonFanStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonFanStatusDescr.setStatus('current')
ciscoEnvMonFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 4, 1, 3), CiscoEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonFanState.setStatus('current')
ciscoEnvMonSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5), )
if mibBuilder.loadTexts: ciscoEnvMonSupplyStatusTable.setStatus('current')
ciscoEnvMonSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5, 1), ).setIndexNames((0, "CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusIndex"))
if mibBuilder.loadTexts: ciscoEnvMonSupplyStatusEntry.setStatus('current')
ciscoEnvMonSupplyStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ciscoEnvMonSupplyStatusIndex.setStatus('current')
ciscoEnvMonSupplyStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonSupplyStatusDescr.setStatus('current')
ciscoEnvMonSupplyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5, 1, 3), CiscoEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonSupplyState.setStatus('current')
ciscoEnvMonSupplySource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("ac", 2), ("dc", 3), ("externalPowerSupply", 4), ("internalRedundant", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonSupplySource.setStatus('current')
ciscoEnvMonAlarmContacts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 13, 1, 6), Bits().clone(namedValues=NamedValues(("minorVisual", 0), ("majorVisual", 1), ("criticalVisual", 2), ("minorAudible", 3), ("majorAudible", 4), ("criticalAudible", 5), ("input", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoEnvMonAlarmContacts.setStatus('current')
ciscoEnvMonMIBNotificationEnables = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 13, 2))
ciscoEnvMonEnableShutdownNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoEnvMonEnableShutdownNotification.setStatus('current')
ciscoEnvMonEnableVoltageNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoEnvMonEnableVoltageNotification.setStatus('deprecated')
ciscoEnvMonEnableTemperatureNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoEnvMonEnableTemperatureNotification.setStatus('deprecated')
ciscoEnvMonEnableFanNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoEnvMonEnableFanNotification.setStatus('deprecated')
ciscoEnvMonEnableRedundantSupplyNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoEnvMonEnableRedundantSupplyNotification.setStatus('deprecated')
ciscoEnvMonEnableStatChangeNotif = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 13, 2, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoEnvMonEnableStatChangeNotif.setStatus('current')
ciscoEnvMonMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 13, 3))
ciscoEnvMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0))
ciscoEnvMonShutdownNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 1))
if mibBuilder.loadTexts: ciscoEnvMonShutdownNotification.setStatus('current')
ciscoEnvMonVoltageNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 2)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusValue"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"))
if mibBuilder.loadTexts: ciscoEnvMonVoltageNotification.setStatus('deprecated')
ciscoEnvMonTemperatureNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 3)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusValue"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"))
if mibBuilder.loadTexts: ciscoEnvMonTemperatureNotification.setStatus('deprecated')
ciscoEnvMonFanNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 4)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonFanState"))
if mibBuilder.loadTexts: ciscoEnvMonFanNotification.setStatus('deprecated')
ciscoEnvMonRedundantSupplyNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 5)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyState"))
if mibBuilder.loadTexts: ciscoEnvMonRedundantSupplyNotification.setStatus('deprecated')
ciscoEnvMonVoltStatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 6)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusValue"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"))
if mibBuilder.loadTexts: ciscoEnvMonVoltStatusChangeNotif.setStatus('current')
ciscoEnvMonTempStatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 7)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusValue"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"))
if mibBuilder.loadTexts: ciscoEnvMonTempStatusChangeNotif.setStatus('current')
ciscoEnvMonFanStatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 8)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonFanState"))
if mibBuilder.loadTexts: ciscoEnvMonFanStatusChangeNotif.setStatus('current')
ciscoEnvMonSuppStatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 13, 3, 0, 9)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyState"))
if mibBuilder.loadTexts: ciscoEnvMonSuppStatusChangeNotif.setStatus('current')
ciscoEnvMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 13, 4))
ciscoEnvMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 1))
ciscoEnvMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2))
ciscoEnvMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 1, 1)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonMIBCompliance = ciscoEnvMonMIBCompliance.setStatus('deprecated')
ciscoEnvMonMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 1, 2)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonMIBGroupRev"), ("CISCO-ENVMON-MIB", "ciscoEnvMonMIBNotifGroup"), ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableStatChangeGroup"), ("CISCO-ENVMON-MIB", "ciscoEnvMonStatChangeNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonMIBComplianceRev1 = ciscoEnvMonMIBComplianceRev1.setStatus('current')
ciscoEnvMonMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 1)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonPresent"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusValue"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageThresholdLow"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageThresholdHigh"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageLastShutdown"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusValue"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureThreshold"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureLastShutdown"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"), ("CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonFanState"), ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyState"), ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplySource"), ("CISCO-ENVMON-MIB", "ciscoEnvMonAlarmContacts"), ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableShutdownNotification"), ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableVoltageNotification"), ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableTemperatureNotification"), ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableFanNotification"), ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableRedundantSupplyNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonMIBGroup = ciscoEnvMonMIBGroup.setStatus('deprecated')
ciscoEnvMonMIBGroupRev = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 2)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonPresent"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusValue"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageThresholdLow"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageThresholdHigh"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageLastShutdown"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusValue"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureThreshold"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureLastShutdown"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"), ("CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonFanState"), ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplyState"), ("CISCO-ENVMON-MIB", "ciscoEnvMonSupplySource"), ("CISCO-ENVMON-MIB", "ciscoEnvMonAlarmContacts"), ("CISCO-ENVMON-MIB", "ciscoEnvMonEnableShutdownNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonMIBGroupRev = ciscoEnvMonMIBGroupRev.setStatus('current')
ciscoEnvMonEnableStatChangeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 3)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonEnableStatChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonEnableStatChangeGroup = ciscoEnvMonEnableStatChangeGroup.setStatus('current')
ciscoEnvMonMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 4)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonShutdownNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonMIBNotifGroup = ciscoEnvMonMIBNotifGroup.setStatus('current')
ciscoEnvMonStatChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 5)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltStatusChangeNotif"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTempStatusChangeNotif"), ("CISCO-ENVMON-MIB", "ciscoEnvMonFanStatusChangeNotif"), ("CISCO-ENVMON-MIB", "ciscoEnvMonSuppStatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonStatChangeNotifGroup = ciscoEnvMonStatChangeNotifGroup.setStatus('current')
ciscoEnvMonMIBMiscNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 13, 4, 2, 6)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageNotification"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureNotification"), ("CISCO-ENVMON-MIB", "ciscoEnvMonFanNotification"), ("CISCO-ENVMON-MIB", "ciscoEnvMonRedundantSupplyNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonMIBMiscNotifGroup = ciscoEnvMonMIBMiscNotifGroup.setStatus('deprecated')
mibBuilder.exportSymbols("CISCO-ENVMON-MIB", ciscoEnvMonVoltageState=ciscoEnvMonVoltageState, ciscoEnvMonTemperatureThreshold=ciscoEnvMonTemperatureThreshold, ciscoEnvMonVoltageThresholdHigh=ciscoEnvMonVoltageThresholdHigh, ciscoEnvMonMIBNotifications=ciscoEnvMonMIBNotifications, ciscoEnvMonFanNotification=ciscoEnvMonFanNotification, ciscoEnvMonSupplyStatusIndex=ciscoEnvMonSupplyStatusIndex, ciscoEnvMonMIBNotificationPrefix=ciscoEnvMonMIBNotificationPrefix, ciscoEnvMonEnableStatChangeNotif=ciscoEnvMonEnableStatChangeNotif, ciscoEnvMonSupplyStatusDescr=ciscoEnvMonSupplyStatusDescr, ciscoEnvMonStatChangeNotifGroup=ciscoEnvMonStatChangeNotifGroup, ciscoEnvMonTempStatusChangeNotif=ciscoEnvMonTempStatusChangeNotif, ciscoEnvMonFanStatusDescr=ciscoEnvMonFanStatusDescr, ciscoEnvMonEnableFanNotification=ciscoEnvMonEnableFanNotification, ciscoEnvMonEnableShutdownNotification=ciscoEnvMonEnableShutdownNotification, ciscoEnvMonSupplyStatusTable=ciscoEnvMonSupplyStatusTable, ciscoEnvMonMIBCompliances=ciscoEnvMonMIBCompliances, ciscoEnvMonVoltageStatusDescr=ciscoEnvMonVoltageStatusDescr, CiscoSignedGauge=CiscoSignedGauge, ciscoEnvMonVoltageLastShutdown=ciscoEnvMonVoltageLastShutdown, ciscoEnvMonFanStatusIndex=ciscoEnvMonFanStatusIndex, ciscoEnvMonMIBNotificationEnables=ciscoEnvMonMIBNotificationEnables, ciscoEnvMonMIBComplianceRev1=ciscoEnvMonMIBComplianceRev1, ciscoEnvMonVoltStatusChangeNotif=ciscoEnvMonVoltStatusChangeNotif, CiscoEnvMonState=CiscoEnvMonState, ciscoEnvMonTemperatureStatusDescr=ciscoEnvMonTemperatureStatusDescr, ciscoEnvMonSuppStatusChangeNotif=ciscoEnvMonSuppStatusChangeNotif, ciscoEnvMonMIBGroupRev=ciscoEnvMonMIBGroupRev, ciscoEnvMonPresent=ciscoEnvMonPresent, ciscoEnvMonTemperatureState=ciscoEnvMonTemperatureState, ciscoEnvMonEnableVoltageNotification=ciscoEnvMonEnableVoltageNotification, ciscoEnvMonVoltageStatusIndex=ciscoEnvMonVoltageStatusIndex, ciscoEnvMonSupplySource=ciscoEnvMonSupplySource, ciscoEnvMonRedundantSupplyNotification=ciscoEnvMonRedundantSupplyNotification, ciscoEnvMonEnableStatChangeGroup=ciscoEnvMonEnableStatChangeGroup, ciscoEnvMonVoltageNotification=ciscoEnvMonVoltageNotification, ciscoEnvMonObjects=ciscoEnvMonObjects, ciscoEnvMonVoltageStatusValue=ciscoEnvMonVoltageStatusValue, ciscoEnvMonMIBMiscNotifGroup=ciscoEnvMonMIBMiscNotifGroup, ciscoEnvMonFanStatusEntry=ciscoEnvMonFanStatusEntry, ciscoEnvMonVoltageThresholdLow=ciscoEnvMonVoltageThresholdLow, ciscoEnvMonTemperatureStatusTable=ciscoEnvMonTemperatureStatusTable, ciscoEnvMonMIBGroup=ciscoEnvMonMIBGroup, ciscoEnvMonMIB=ciscoEnvMonMIB, ciscoEnvMonShutdownNotification=ciscoEnvMonShutdownNotification, ciscoEnvMonFanStatusChangeNotif=ciscoEnvMonFanStatusChangeNotif, ciscoEnvMonFanState=ciscoEnvMonFanState, ciscoEnvMonMIBNotifGroup=ciscoEnvMonMIBNotifGroup, PYSNMP_MODULE_ID=ciscoEnvMonMIB, ciscoEnvMonMIBConformance=ciscoEnvMonMIBConformance, ciscoEnvMonSupplyStatusEntry=ciscoEnvMonSupplyStatusEntry, ciscoEnvMonEnableRedundantSupplyNotification=ciscoEnvMonEnableRedundantSupplyNotification, ciscoEnvMonTemperatureStatusEntry=ciscoEnvMonTemperatureStatusEntry, ciscoEnvMonTemperatureLastShutdown=ciscoEnvMonTemperatureLastShutdown, ciscoEnvMonVoltageStatusEntry=ciscoEnvMonVoltageStatusEntry, ciscoEnvMonTemperatureNotification=ciscoEnvMonTemperatureNotification, ciscoEnvMonSupplyState=ciscoEnvMonSupplyState, ciscoEnvMonEnableTemperatureNotification=ciscoEnvMonEnableTemperatureNotification, ciscoEnvMonVoltageStatusTable=ciscoEnvMonVoltageStatusTable, ciscoEnvMonMIBGroups=ciscoEnvMonMIBGroups, ciscoEnvMonAlarmContacts=ciscoEnvMonAlarmContacts, ciscoEnvMonTemperatureStatusValue=ciscoEnvMonTemperatureStatusValue, ciscoEnvMonMIBCompliance=ciscoEnvMonMIBCompliance, ciscoEnvMonTemperatureStatusIndex=ciscoEnvMonTemperatureStatusIndex, ciscoEnvMonFanStatusTable=ciscoEnvMonFanStatusTable)
