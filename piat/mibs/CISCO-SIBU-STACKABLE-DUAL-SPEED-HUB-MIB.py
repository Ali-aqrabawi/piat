#
# PySNMP MIB module CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:43:39 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
rptrPortIndex, rptrPortGroupIndex, rptrGroupIndex = mibBuilder.importSymbols("SNMP-REPEATER-MIB", "rptrPortIndex", "rptrPortGroupIndex", "rptrGroupIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, IpAddress, ModuleIdentity, NotificationType, Gauge32, ObjectIdentity, Integer32, Counter32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "ModuleIdentity", "NotificationType", "Gauge32", "ObjectIdentity", "Integer32", "Counter32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
ciscoSibuStackableDualSpeedHubMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 44))
ciscoSibuStackableDualSpeedHubMIB.setRevisions(('1998-10-23 00:00',))
if mibBuilder.loadTexts: ciscoSibuStackableDualSpeedHubMIB.setLastUpdated('9810230000Z')
if mibBuilder.loadTexts: ciscoSibuStackableDualSpeedHubMIB.setOrganization('Cisco Systems Inc.')
ciscoSibuStackableDualSpeedHubMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 44, 1))
cssSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 1))
cssGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2))
cssRepeaterPort = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3))
cssSwitchPort = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4))
class HubNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

cssSystemLinkTraps = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssSystemLinkTraps.setStatus('current')
cssGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1), )
if mibBuilder.loadTexts: cssGroupTable.setStatus('current')
cssGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1), ).setIndexNames((0, "SNMP-REPEATER-MIB", "rptrGroupIndex"))
if mibBuilder.loadTexts: cssGroupEntry.setStatus('current')
cssGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 1), HubNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssGroupID.setStatus('current')
cssGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cisco1538MDS", 1), ("cisco1538UDS", 2), ("wsC412M", 3), ("wsC412", 4), ("wsC424M", 5), ("wsC424", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssGroupType.setStatus('current')
cssGroupSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssGroupSerialNo.setStatus('current')
cssGroupBoardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssGroupBoardRevision.setStatus('current')
cssGroupAgentBootVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssGroupAgentBootVersion.setStatus('current')
cssGroupAgentFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssGroupAgentFirmwareVersion.setStatus('current')
cssGroupAgentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notPresent", 1), ("primary", 2), ("backup", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssGroupAgentStatus.setStatus('current')
cssGroupAgentPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 9), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssGroupAgentPhysAddress.setStatus('current')
cssGroupInternalPowerState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssGroupInternalPowerState.setStatus('current')
cssGroupRedundantPowerState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("healthy", 2), ("faulty", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssGroupRedundantPowerState.setStatus('current')
cssGroupReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2))).clone('noReset')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssGroupReset.setStatus('current')
cssGroupConfigDefaultReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2))).clone('noReset')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssGroupConfigDefaultReset.setStatus('current')
cssGroupIsolatedState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("isolated", 1), ("attached", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssGroupIsolatedState.setStatus('current')
cssRepeaterPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1), )
if mibBuilder.loadTexts: cssRepeaterPortTable.setStatus('current')
cssRepeaterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1), ).setIndexNames((0, "SNMP-REPEATER-MIB", "rptrPortGroupIndex"), (0, "SNMP-REPEATER-MIB", "rptrPortIndex"))
if mibBuilder.loadTexts: cssRepeaterPortEntry.setStatus('current')
cssRepeaterPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssRepeaterPortName.setStatus('current')
cssRepeaterPortControllerRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssRepeaterPortControllerRevision.setStatus('current')
cssRepeaterPortSpeedAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tenMbps", 1), ("oneHundredMbps", 2), ("autoNegotiate", 3))).clone('autoNegotiate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssRepeaterPortSpeedAdmin.setStatus('current')
cssRepeaterPortSpeedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tenMbps", 1), ("oneHundredMbps", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssRepeaterPortSpeedStatus.setStatus('current')
cssRepeaterPortLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link", 1), ("noLink", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssRepeaterPortLinkStatus.setStatus('current')
cssSwitchPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1), )
if mibBuilder.loadTexts: cssSwitchPortTable.setStatus('current')
cssSwitchPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1), ).setIndexNames((0, "SNMP-REPEATER-MIB", "rptrGroupIndex"), (0, "CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortModuleID"), (0, "CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortPortID"))
if mibBuilder.loadTexts: cssSwitchPortEntry.setStatus('current')
cssSwitchPortModuleID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSwitchPortModuleID.setStatus('current')
cssSwitchPortPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSwitchPortPortID.setStatus('current')
cssSwitchPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssSwitchPortName.setStatus('current')
cssSwitchPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wsX4001", 1), ("wsX4002", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSwitchPortType.setStatus('current')
cssSwitchPortControllerRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSwitchPortControllerRevision.setStatus('current')
cssSwitchPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssSwitchPortState.setStatus('current')
cssSwitchPortDuplexAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fullDuplex", 1), ("halfDuplex", 2), ("autoNegotiate", 3))).clone('autoNegotiate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssSwitchPortDuplexAdmin.setStatus('current')
cssSwitchPortDuplexStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fullDuplex", 1), ("halfDuplex", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSwitchPortDuplexStatus.setStatus('current')
cssSwitchPortSpeedAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tenMbps", 1), ("oneHundredMbps", 2), ("autoNegotiate", 3))).clone('autoNegotiate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssSwitchPortSpeedAdmin.setStatus('current')
cssSwitchPortSpeedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tenMbps", 1), ("oneHundredMbps", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSwitchPortSpeedStatus.setStatus('current')
cssSwitchPortLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 44, 1, 4, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link", 1), ("noLink", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSwitchPortLinkStatus.setStatus('current')
ciscoSibuStackableDualSpeedHubNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 44, 2))
ciscoSibuStackableDualSpeedHubNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 44, 2, 0))
ciscoSibuStackableDualSpeedHubRptrPortLinkChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 44, 2, 0, 1)).setObjects(("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortLinkStatus"))
if mibBuilder.loadTexts: ciscoSibuStackableDualSpeedHubRptrPortLinkChange.setStatus('current')
ciscoSibuStackableDualSpeedHubSwitchPortLinkChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 44, 2, 0, 2)).setObjects(("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortLinkStatus"))
if mibBuilder.loadTexts: ciscoSibuStackableDualSpeedHubSwitchPortLinkChange.setStatus('current')
ciscoSibuStackableDualSpeedHubMIBComformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 44, 3))
ciscoSibuStackableDualSpeedHubMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 1))
ciscoSibuStackableDualSpeedHubMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 2))
ciscoSibuStackableDualSpeedHubCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 1, 1)).setObjects(("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "ciscoSibuStackableDualSpeedHubGroup"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "ciscoSibuStackableDualSpeedHubRepeaterPortGroup"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "ciscoSibuStackableDualSpeedHubSwitchPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSibuStackableDualSpeedHubCompliance = ciscoSibuStackableDualSpeedHubCompliance.setStatus('current')
ciscoSibuStackableDualSpeedHubGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 2, 1)).setObjects(("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSystemLinkTraps"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupID"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupType"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupSerialNo"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupBoardRevision"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupAgentBootVersion"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupAgentFirmwareVersion"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupAgentStatus"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupAgentPhysAddress"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupInternalPowerState"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupRedundantPowerState"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupReset"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupConfigDefaultReset"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssGroupIsolatedState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSibuStackableDualSpeedHubGroup = ciscoSibuStackableDualSpeedHubGroup.setStatus('current')
ciscoSibuStackableDualSpeedHubRepeaterPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 2, 2)).setObjects(("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortName"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortControllerRevision"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortSpeedAdmin"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortSpeedStatus"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssRepeaterPortLinkStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSibuStackableDualSpeedHubRepeaterPortGroup = ciscoSibuStackableDualSpeedHubRepeaterPortGroup.setStatus('current')
ciscoSibuStackableDualSpeedHubSwitchPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 44, 3, 2, 3)).setObjects(("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortModuleID"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortPortID"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortName"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortType"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortControllerRevision"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortState"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortDuplexAdmin"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortDuplexStatus"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortSpeedAdmin"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortSpeedStatus"), ("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", "cssSwitchPortLinkStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSibuStackableDualSpeedHubSwitchPortGroup = ciscoSibuStackableDualSpeedHubSwitchPortGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SIBU-STACKABLE-DUAL-SPEED-HUB-MIB", cssGroupAgentBootVersion=cssGroupAgentBootVersion, cssGroupAgentPhysAddress=cssGroupAgentPhysAddress, cssSwitchPortModuleID=cssSwitchPortModuleID, cssGroupAgentFirmwareVersion=cssGroupAgentFirmwareVersion, cssGroupIsolatedState=cssGroupIsolatedState, cssGroupConfigDefaultReset=cssGroupConfigDefaultReset, ciscoSibuStackableDualSpeedHubNotifications=ciscoSibuStackableDualSpeedHubNotifications, cssRepeaterPortLinkStatus=cssRepeaterPortLinkStatus, cssSystemLinkTraps=cssSystemLinkTraps, cssGroupSerialNo=cssGroupSerialNo, ciscoSibuStackableDualSpeedHubSwitchPortGroup=ciscoSibuStackableDualSpeedHubSwitchPortGroup, cssGroupEntry=cssGroupEntry, cssSwitchPortDuplexAdmin=cssSwitchPortDuplexAdmin, ciscoSibuStackableDualSpeedHubSwitchPortLinkChange=ciscoSibuStackableDualSpeedHubSwitchPortLinkChange, cssSwitchPortSpeedAdmin=cssSwitchPortSpeedAdmin, cssGroup=cssGroup, cssGroupBoardRevision=cssGroupBoardRevision, cssRepeaterPortSpeedAdmin=cssRepeaterPortSpeedAdmin, ciscoSibuStackableDualSpeedHubRptrPortLinkChange=ciscoSibuStackableDualSpeedHubRptrPortLinkChange, cssRepeaterPortControllerRevision=cssRepeaterPortControllerRevision, ciscoSibuStackableDualSpeedHubMIBComformance=ciscoSibuStackableDualSpeedHubMIBComformance, ciscoSibuStackableDualSpeedHubMIBCompliances=ciscoSibuStackableDualSpeedHubMIBCompliances, cssGroupAgentStatus=cssGroupAgentStatus, cssSwitchPortDuplexStatus=cssSwitchPortDuplexStatus, cssRepeaterPort=cssRepeaterPort, cssGroupRedundantPowerState=cssGroupRedundantPowerState, cssSwitchPortPortID=cssSwitchPortPortID, cssSystem=cssSystem, cssRepeaterPortName=cssRepeaterPortName, ciscoSibuStackableDualSpeedHubNotificationsPrefix=ciscoSibuStackableDualSpeedHubNotificationsPrefix, ciscoSibuStackableDualSpeedHubRepeaterPortGroup=ciscoSibuStackableDualSpeedHubRepeaterPortGroup, ciscoSibuStackableDualSpeedHubGroup=ciscoSibuStackableDualSpeedHubGroup, cssSwitchPortName=cssSwitchPortName, cssRepeaterPortSpeedStatus=cssRepeaterPortSpeedStatus, cssSwitchPortLinkStatus=cssSwitchPortLinkStatus, cssSwitchPort=cssSwitchPort, HubNumber=HubNumber, ciscoSibuStackableDualSpeedHubMIB=ciscoSibuStackableDualSpeedHubMIB, cssGroupID=cssGroupID, cssSwitchPortEntry=cssSwitchPortEntry, cssGroupType=cssGroupType, cssSwitchPortType=cssSwitchPortType, cssSwitchPortSpeedStatus=cssSwitchPortSpeedStatus, cssRepeaterPortTable=cssRepeaterPortTable, ciscoSibuStackableDualSpeedHubMIBGroups=ciscoSibuStackableDualSpeedHubMIBGroups, cssSwitchPortTable=cssSwitchPortTable, cssGroupReset=cssGroupReset, cssSwitchPortState=cssSwitchPortState, PYSNMP_MODULE_ID=ciscoSibuStackableDualSpeedHubMIB, ciscoSibuStackableDualSpeedHubCompliance=ciscoSibuStackableDualSpeedHubCompliance, cssGroupTable=cssGroupTable, ciscoSibuStackableDualSpeedHubMIBObjects=ciscoSibuStackableDualSpeedHubMIBObjects, cssGroupInternalPowerState=cssGroupInternalPowerState, cssSwitchPortControllerRevision=cssSwitchPortControllerRevision, cssRepeaterPortEntry=cssRepeaterPortEntry)
