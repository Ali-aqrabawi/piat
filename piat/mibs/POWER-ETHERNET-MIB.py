#
# PySNMP MIB module POWER-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/ietf/POWER-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:30:14 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, iso, IpAddress, Gauge32, Unsigned32, Integer32, mib_2, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "iso", "IpAddress", "Gauge32", "Unsigned32", "Integer32", "mib-2", "Bits", "Counter64")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
powerEthernetMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 105))
powerEthernetMIB.setRevisions(('2003-11-24 00:00',))
if mibBuilder.loadTexts: powerEthernetMIB.setLastUpdated('200311240000Z')
if mibBuilder.loadTexts: powerEthernetMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
pethNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 0))
pethObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1))
pethConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2))
pethPsePortTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 1), )
if mibBuilder.loadTexts: pethPsePortTable.setStatus('current')
pethPsePortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 1, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"), (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"))
if mibBuilder.loadTexts: pethPsePortEntry.setStatus('current')
pethPsePortGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethPsePortGroupIndex.setStatus('current')
pethPsePortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethPsePortIndex.setStatus('current')
pethPsePortAdminEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortAdminEnable.setStatus('current')
pethPsePortPowerPairsControlAbility = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerPairsControlAbility.setStatus('current')
pethPsePortPowerPairs = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("signal", 1), ("spare", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPairs.setStatus('current')
pethPsePortDetectionStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("searching", 2), ("deliveringPower", 3), ("fault", 4), ("test", 5), ("otherFault", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortDetectionStatus.setStatus('current')
pethPsePortPowerPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPriority.setStatus('current')
pethPsePortMPSAbsentCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortMPSAbsentCounter.setStatus('current')
pethPsePortType = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortType.setStatus('current')
pethPsePortPowerClassifications = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("class0", 1), ("class1", 2), ("class2", 3), ("class3", 4), ("class4", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerClassifications.setStatus('current')
pethPsePortInvalidSignatureCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortInvalidSignatureCounter.setStatus('current')
pethPsePortPowerDeniedCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerDeniedCounter.setStatus('current')
pethPsePortOverLoadCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortOverLoadCounter.setStatus('current')
pethPsePortShortCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortShortCounter.setStatus('current')
pethMainPseObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1, 3))
pethMainPseTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 3, 1), )
if mibBuilder.loadTexts: pethMainPseTable.setStatus('current')
pethMainPseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"))
if mibBuilder.loadTexts: pethMainPseEntry.setStatus('current')
pethMainPseGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethMainPseGroupIndex.setStatus('current')
pethMainPsePower = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPsePower.setStatus('current')
pethMainPseOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("faulty", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseOperStatus.setStatus('current')
pethMainPseConsumptionPower = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 4), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseConsumptionPower.setStatus('current')
pethMainPseUsageThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethMainPseUsageThreshold.setStatus('current')
pethNotificationControl = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1, 4))
pethNotificationControlTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 4, 1), )
if mibBuilder.loadTexts: pethNotificationControlTable.setStatus('current')
pethNotificationControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethNotificationControlGroupIndex"))
if mibBuilder.loadTexts: pethNotificationControlEntry.setStatus('current')
pethNotificationControlGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethNotificationControlGroupIndex.setStatus('current')
pethNotificationControlEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethNotificationControlEnable.setStatus('current')
pethPsePortOnOffNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 1)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"))
if mibBuilder.loadTexts: pethPsePortOnOffNotification.setStatus('current')
pethMainPowerUsageOnNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 2)).setObjects(("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"))
if mibBuilder.loadTexts: pethMainPowerUsageOnNotification.setStatus('current')
pethMainPowerUsageOffNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 3)).setObjects(("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"))
if mibBuilder.loadTexts: pethMainPowerUsageOffNotification.setStatus('current')
pethCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2, 1))
pethGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2, 2))
pethCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 105, 2, 1, 1)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortGroup"), ("POWER-ETHERNET-MIB", "pethPsePortNotificationGroup"), ("POWER-ETHERNET-MIB", "pethNotificationControlGroup"), ("POWER-ETHERNET-MIB", "pethMainPseGroup"), ("POWER-ETHERNET-MIB", "pethMainPowerNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethCompliance = pethCompliance.setStatus('current')
pethPsePortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 1)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortAdminEnable"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPairsControlAbility"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPairs"), ("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPriority"), ("POWER-ETHERNET-MIB", "pethPsePortMPSAbsentCounter"), ("POWER-ETHERNET-MIB", "pethPsePortInvalidSignatureCounter"), ("POWER-ETHERNET-MIB", "pethPsePortPowerDeniedCounter"), ("POWER-ETHERNET-MIB", "pethPsePortOverLoadCounter"), ("POWER-ETHERNET-MIB", "pethPsePortShortCounter"), ("POWER-ETHERNET-MIB", "pethPsePortType"), ("POWER-ETHERNET-MIB", "pethPsePortPowerClassifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPsePortGroup = pethPsePortGroup.setStatus('current')
pethMainPseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 2)).setObjects(("POWER-ETHERNET-MIB", "pethMainPsePower"), ("POWER-ETHERNET-MIB", "pethMainPseOperStatus"), ("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"), ("POWER-ETHERNET-MIB", "pethMainPseUsageThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethMainPseGroup = pethMainPseGroup.setStatus('current')
pethNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 3)).setObjects(("POWER-ETHERNET-MIB", "pethNotificationControlEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethNotificationControlGroup = pethNotificationControlGroup.setStatus('current')
pethPsePortNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 4)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortOnOffNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPsePortNotificationGroup = pethPsePortNotificationGroup.setStatus('current')
pethMainPowerNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 5)).setObjects(("POWER-ETHERNET-MIB", "pethMainPowerUsageOnNotification"), ("POWER-ETHERNET-MIB", "pethMainPowerUsageOffNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethMainPowerNotificationGroup = pethMainPowerNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", pethNotificationControlEntry=pethNotificationControlEntry, pethPsePortOverLoadCounter=pethPsePortOverLoadCounter, pethMainPseConsumptionPower=pethMainPseConsumptionPower, pethNotificationControlEnable=pethNotificationControlEnable, pethPsePortGroupIndex=pethPsePortGroupIndex, pethMainPseUsageThreshold=pethMainPseUsageThreshold, pethNotificationControlTable=pethNotificationControlTable, pethCompliances=pethCompliances, pethNotificationControlGroup=pethNotificationControlGroup, pethPsePortShortCounter=pethPsePortShortCounter, PYSNMP_MODULE_ID=powerEthernetMIB, pethPsePortEntry=pethPsePortEntry, pethPsePortPowerClassifications=pethPsePortPowerClassifications, pethObjects=pethObjects, pethMainPseEntry=pethMainPseEntry, pethGroups=pethGroups, pethPsePortNotificationGroup=pethPsePortNotificationGroup, pethPsePortPowerPairsControlAbility=pethPsePortPowerPairsControlAbility, pethCompliance=pethCompliance, pethMainPowerNotificationGroup=pethMainPowerNotificationGroup, pethPsePortOnOffNotification=pethPsePortOnOffNotification, pethConformance=pethConformance, pethMainPseOperStatus=pethMainPseOperStatus, pethMainPseObjects=pethMainPseObjects, pethNotifications=pethNotifications, pethMainPseTable=pethMainPseTable, pethPsePortInvalidSignatureCounter=pethPsePortInvalidSignatureCounter, pethPsePortPowerPriority=pethPsePortPowerPriority, pethPsePortMPSAbsentCounter=pethPsePortMPSAbsentCounter, pethPsePortPowerPairs=pethPsePortPowerPairs, pethPsePortGroup=pethPsePortGroup, pethPsePortPowerDeniedCounter=pethPsePortPowerDeniedCounter, powerEthernetMIB=powerEthernetMIB, pethNotificationControlGroupIndex=pethNotificationControlGroupIndex, pethPsePortTable=pethPsePortTable, pethPsePortIndex=pethPsePortIndex, pethPsePortAdminEnable=pethPsePortAdminEnable, pethMainPowerUsageOffNotification=pethMainPowerUsageOffNotification, pethMainPseGroup=pethMainPseGroup, pethMainPsePower=pethMainPsePower, pethPsePortDetectionStatus=pethPsePortDetectionStatus, pethMainPowerUsageOnNotification=pethMainPowerUsageOnNotification, pethNotificationControl=pethNotificationControl, pethPsePortType=pethPsePortType, pethMainPseGroupIndex=pethMainPseGroupIndex)
