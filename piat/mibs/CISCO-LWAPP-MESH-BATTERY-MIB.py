#
# PySNMP MIB module CISCO-LWAPP-MESH-BATTERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-LWAPP-MESH-BATTERY-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:34:04 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cLApName, cLApSysMacAddress = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApName", "cLApSysMacAddress")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, Unsigned32, ObjectIdentity, ModuleIdentity, MibIdentifier, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, TimeTicks, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "TimeTicks", "IpAddress", "Bits")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoLwappMeshBatteryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 620))
ciscoLwappMeshBatteryMIB.setRevisions(('2010-09-08 00:00', '2007-02-27 00:00',))
if mibBuilder.loadTexts: ciscoLwappMeshBatteryMIB.setLastUpdated('201009080000Z')
if mibBuilder.loadTexts: ciscoLwappMeshBatteryMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappMeshBatteryMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 0))
ciscoLwappMeshBatteryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 1))
ciscoLwappMeshBatteryMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 2))
ciscoLwappMeshBatteryInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1))
ciscoLwappMeshBatteryNotifControlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 2))
clMeshNodeBatteryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1), )
if mibBuilder.loadTexts: clMeshNodeBatteryTable.setStatus('current')
clMeshNodeBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"))
if mibBuilder.loadTexts: clMeshNodeBatteryEntry.setStatus('current')
clMeshNodeBatteryModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryModelName.setStatus('current')
clMeshNodeBatteryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("normal", 2), ("overloaded", 3), ("low", 4), ("acfail", 5), ("replace", 6), ("missing", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryStatus.setStatus('current')
clMeshNodeBatteryChargingState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("charging", 3), ("discharging", 4), ("charged", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryChargingState.setStatus('deprecated')
clMeshNodeBatteryChargingLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 4), Integer32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryChargingLevel.setStatus('current')
clMeshNodeBatteryRemainingCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 5), Unsigned32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryRemainingCapacity.setStatus('deprecated')
clMeshNodeBatterySwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatterySwVersion.setStatus('current')
clMeshNodeBatterySerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatterySerialNumber.setStatus('current')
clMeshNodeBatteryInputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 8), Unsigned32()).setUnits('milliVolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryInputVoltage.setStatus('current')
clMeshNodeBatteryOutputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 9), Unsigned32()).setUnits('milliVolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryOutputVoltage.setStatus('current')
clMeshNodeBatteryOutputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 10), Unsigned32()).setUnits('milliWatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryOutputPower.setStatus('current')
clMeshNodeBatteryInternalVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 11), Unsigned32()).setUnits('milliVolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryInternalVoltage.setStatus('current')
clMeshNodeBatteryTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 12), Integer32()).setUnits('degree Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryTemperature.setStatus('current')
clMeshNodeBatteryCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 13), Unsigned32()).setUnits('milliAmps').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryCurrent.setStatus('deprecated')
clMeshNodeBatteryCurrentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 14), Integer32()).setUnits('milliAmps').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBatteryCurrentValue.setStatus('current')
clMeshBatteryAlarmEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshBatteryAlarmEnabled.setStatus('current')
ciscoLwappMeshBatteryAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 620, 0, 1)).setObjects(("CISCO-LWAPP-AP-MIB", "cLApName"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"))
if mibBuilder.loadTexts: ciscoLwappMeshBatteryAlarm.setStatus('current')
ciscoLwappMeshBatteryMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1))
ciscoLwappMeshBatteryMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2))
ciscoLwappMeshBatteryMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1, 1)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryInfoGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsConfigGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryMIBCompliance = ciscoLwappMeshBatteryMIBCompliance.setStatus('deprecated')
ciscoLwappMeshBatteryMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1, 2)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsConfigGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryInfoGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryMIBComplianceRev1 = ciscoLwappMeshBatteryMIBComplianceRev1.setStatus('deprecated')
ciscoLwappMeshBatteryMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1, 3)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsConfigGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryNotifsGroup"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryInfoGroupRev2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryMIBComplianceRev2 = ciscoLwappMeshBatteryMIBComplianceRev2.setStatus('current')
ciscoLwappMeshBatteryInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 1)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryModelName"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingState"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingLevel"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryRemainingCapacity"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySwVersion"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySerialNumber"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputPower"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInternalVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryTemperature"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryInfoGroup = ciscoLwappMeshBatteryInfoGroup.setStatus('deprecated')
ciscoLwappMeshBatteryNotifsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 2)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshBatteryAlarmEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryNotifsConfigGroup = ciscoLwappMeshBatteryNotifsConfigGroup.setStatus('current')
ciscoLwappMeshBatteryNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 3)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryNotifsGroup = ciscoLwappMeshBatteryNotifsGroup.setStatus('current')
ciscoLwappMeshBatteryInfoGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 4)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryModelName"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingState"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingLevel"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryRemainingCapacity"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySwVersion"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySerialNumber"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputPower"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInternalVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryTemperature"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryCurrentValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryInfoGroupRev1 = ciscoLwappMeshBatteryInfoGroupRev1.setStatus('deprecated')
ciscoLwappMeshBatteryInfoGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 5)).setObjects(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryModelName"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingLevel"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySwVersion"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySerialNumber"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputPower"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInternalVoltage"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryTemperature"), ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryCurrentValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshBatteryInfoGroupRev2 = ciscoLwappMeshBatteryInfoGroupRev2.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-MESH-BATTERY-MIB", clMeshNodeBatteryTemperature=clMeshNodeBatteryTemperature, ciscoLwappMeshBatteryMIBConform=ciscoLwappMeshBatteryMIBConform, clMeshNodeBatteryInputVoltage=clMeshNodeBatteryInputVoltage, clMeshNodeBatteryTable=clMeshNodeBatteryTable, PYSNMP_MODULE_ID=ciscoLwappMeshBatteryMIB, ciscoLwappMeshBatteryMIBGroups=ciscoLwappMeshBatteryMIBGroups, clMeshNodeBatterySerialNumber=clMeshNodeBatterySerialNumber, clMeshNodeBatterySwVersion=clMeshNodeBatterySwVersion, ciscoLwappMeshBatteryMIBObjects=ciscoLwappMeshBatteryMIBObjects, ciscoLwappMeshBatteryInfo=ciscoLwappMeshBatteryInfo, ciscoLwappMeshBatteryInfoGroupRev1=ciscoLwappMeshBatteryInfoGroupRev1, ciscoLwappMeshBatteryMIBCompliance=ciscoLwappMeshBatteryMIBCompliance, ciscoLwappMeshBatteryMIBComplianceRev2=ciscoLwappMeshBatteryMIBComplianceRev2, clMeshNodeBatteryModelName=clMeshNodeBatteryModelName, ciscoLwappMeshBatteryMIBNotifs=ciscoLwappMeshBatteryMIBNotifs, clMeshNodeBatteryStatus=clMeshNodeBatteryStatus, ciscoLwappMeshBatteryMIB=ciscoLwappMeshBatteryMIB, ciscoLwappMeshBatteryInfoGroupRev2=ciscoLwappMeshBatteryInfoGroupRev2, clMeshNodeBatteryOutputVoltage=clMeshNodeBatteryOutputVoltage, ciscoLwappMeshBatteryNotifsGroup=ciscoLwappMeshBatteryNotifsGroup, ciscoLwappMeshBatteryMIBCompliances=ciscoLwappMeshBatteryMIBCompliances, ciscoLwappMeshBatteryNotifsConfigGroup=ciscoLwappMeshBatteryNotifsConfigGroup, clMeshNodeBatteryCurrent=clMeshNodeBatteryCurrent, ciscoLwappMeshBatteryMIBComplianceRev1=ciscoLwappMeshBatteryMIBComplianceRev1, clMeshNodeBatteryInternalVoltage=clMeshNodeBatteryInternalVoltage, ciscoLwappMeshBatteryInfoGroup=ciscoLwappMeshBatteryInfoGroup, ciscoLwappMeshBatteryAlarm=ciscoLwappMeshBatteryAlarm, clMeshBatteryAlarmEnabled=clMeshBatteryAlarmEnabled, clMeshNodeBatteryRemainingCapacity=clMeshNodeBatteryRemainingCapacity, clMeshNodeBatteryChargingLevel=clMeshNodeBatteryChargingLevel, clMeshNodeBatteryCurrentValue=clMeshNodeBatteryCurrentValue, clMeshNodeBatteryOutputPower=clMeshNodeBatteryOutputPower, clMeshNodeBatteryEntry=clMeshNodeBatteryEntry, ciscoLwappMeshBatteryNotifControlConfig=ciscoLwappMeshBatteryNotifControlConfig, clMeshNodeBatteryChargingState=clMeshNodeBatteryChargingState)