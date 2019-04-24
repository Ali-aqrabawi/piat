#
# PySNMP MIB module CISCO-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-PING-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:26:13 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoNetworkAddress, CiscoNetworkProtocol = mibBuilder.importSymbols("CISCO-TC", "CiscoNetworkAddress", "CiscoNetworkProtocol")
OwnerString, = mibBuilder.importSymbols("IF-MIB", "OwnerString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, Unsigned32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Integer32, ModuleIdentity, ObjectIdentity, TimeTicks, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Integer32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "iso", "Counter32")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
ciscoPingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 16))
ciscoPingMIB.setRevisions(('2001-08-28 00:00', '2001-05-14 00:00', '1999-10-08 00:00', '1994-11-11 00:00', '1994-07-22 00:00',))
if mibBuilder.loadTexts: ciscoPingMIB.setLastUpdated('200108280000Z')
if mibBuilder.loadTexts: ciscoPingMIB.setOrganization('Cisco Systems, Inc.')
ciscoPingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 16, 1))
ciscoPingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1), )
if mibBuilder.loadTexts: ciscoPingTable.setStatus('current')
ciscoPingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1), ).setIndexNames((0, "CISCO-PING-MIB", "ciscoPingSerialNumber"))
if mibBuilder.loadTexts: ciscoPingEntry.setStatus('current')
ciscoPingSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ciscoPingSerialNumber.setStatus('current')
ciscoPingProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 2), CiscoNetworkProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPingProtocol.setStatus('current')
ciscoPingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 3), CiscoNetworkAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPingAddress.setStatus('current')
ciscoPingPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPingPacketCount.setStatus('current')
ciscoPingPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 5), Integer32().clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPingPacketSize.setStatus('current')
ciscoPingPacketTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600000)).clone(2000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPingPacketTimeout.setStatus('current')
ciscoPingDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600000))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPingDelay.setStatus('current')
ciscoPingTrapOnCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPingTrapOnCompletion.setStatus('current')
ciscoPingSentPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPingSentPackets.setStatus('current')
ciscoPingReceivedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPingReceivedPackets.setStatus('current')
ciscoPingMinRtt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 11), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPingMinRtt.setStatus('current')
ciscoPingAvgRtt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 12), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPingAvgRtt.setStatus('current')
ciscoPingMaxRtt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 13), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPingMaxRtt.setStatus('current')
ciscoPingCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPingCompleted.setStatus('current')
ciscoPingEntryOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 15), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPingEntryOwner.setStatus('current')
ciscoPingEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPingEntryStatus.setStatus('current')
ciscoPingVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoPingVrfName.setStatus('current')
ciscoPingMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 16, 2))
ciscoPingMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 16, 2, 0))
ciscoPingCompletion = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 16, 2, 0, 1)).setObjects(("CISCO-PING-MIB", "ciscoPingCompleted"), ("CISCO-PING-MIB", "ciscoPingSentPackets"), ("CISCO-PING-MIB", "ciscoPingReceivedPackets"))
if mibBuilder.loadTexts: ciscoPingCompletion.setStatus('current')
ciscoPingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 16, 3))
ciscoPingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 1))
ciscoPingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 2))
ciscoPingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 1, 1)).setObjects(("CISCO-PING-MIB", "ciscoPingMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingMIBCompliance = ciscoPingMIBCompliance.setStatus('obsolete')
ciscoPingMIBComplianceVpn = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 1, 2)).setObjects(("CISCO-PING-MIB", "ciscoPingMIBGroupVpn"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingMIBComplianceVpn = ciscoPingMIBComplianceVpn.setStatus('current')
ciscoPingMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 2, 1)).setObjects(("CISCO-PING-MIB", "ciscoPingProtocol"), ("CISCO-PING-MIB", "ciscoPingAddress"), ("CISCO-PING-MIB", "ciscoPingPacketCount"), ("CISCO-PING-MIB", "ciscoPingPacketSize"), ("CISCO-PING-MIB", "ciscoPingPacketTimeout"), ("CISCO-PING-MIB", "ciscoPingDelay"), ("CISCO-PING-MIB", "ciscoPingTrapOnCompletion"), ("CISCO-PING-MIB", "ciscoPingSentPackets"), ("CISCO-PING-MIB", "ciscoPingReceivedPackets"), ("CISCO-PING-MIB", "ciscoPingMinRtt"), ("CISCO-PING-MIB", "ciscoPingAvgRtt"), ("CISCO-PING-MIB", "ciscoPingMaxRtt"), ("CISCO-PING-MIB", "ciscoPingCompleted"), ("CISCO-PING-MIB", "ciscoPingEntryOwner"), ("CISCO-PING-MIB", "ciscoPingEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingMIBGroup = ciscoPingMIBGroup.setStatus('obsolete')
ciscoPingMIBGroupVpn = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 2, 2)).setObjects(("CISCO-PING-MIB", "ciscoPingProtocol"), ("CISCO-PING-MIB", "ciscoPingAddress"), ("CISCO-PING-MIB", "ciscoPingPacketCount"), ("CISCO-PING-MIB", "ciscoPingPacketSize"), ("CISCO-PING-MIB", "ciscoPingPacketTimeout"), ("CISCO-PING-MIB", "ciscoPingDelay"), ("CISCO-PING-MIB", "ciscoPingTrapOnCompletion"), ("CISCO-PING-MIB", "ciscoPingSentPackets"), ("CISCO-PING-MIB", "ciscoPingReceivedPackets"), ("CISCO-PING-MIB", "ciscoPingMinRtt"), ("CISCO-PING-MIB", "ciscoPingAvgRtt"), ("CISCO-PING-MIB", "ciscoPingMaxRtt"), ("CISCO-PING-MIB", "ciscoPingCompleted"), ("CISCO-PING-MIB", "ciscoPingEntryOwner"), ("CISCO-PING-MIB", "ciscoPingEntryStatus"), ("CISCO-PING-MIB", "ciscoPingVrfName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingMIBGroupVpn = ciscoPingMIBGroupVpn.setStatus('current')
ciscoPingMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 2, 3)).setObjects(("CISCO-PING-MIB", "ciscoPingCompletion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingMIBNotificationGroup = ciscoPingMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PING-MIB", ciscoPingMIBNotificationGroup=ciscoPingMIBNotificationGroup, ciscoPingSerialNumber=ciscoPingSerialNumber, ciscoPingMIBCompliances=ciscoPingMIBCompliances, ciscoPingAddress=ciscoPingAddress, ciscoPingMIBConformance=ciscoPingMIBConformance, ciscoPingTable=ciscoPingTable, ciscoPingMIBGroupVpn=ciscoPingMIBGroupVpn, ciscoPingMIBTraps=ciscoPingMIBTraps, ciscoPingMIBCompliance=ciscoPingMIBCompliance, ciscoPingPacketSize=ciscoPingPacketSize, ciscoPingSentPackets=ciscoPingSentPackets, ciscoPingMIBObjects=ciscoPingMIBObjects, ciscoPingReceivedPackets=ciscoPingReceivedPackets, ciscoPingCompletion=ciscoPingCompletion, ciscoPingPacketCount=ciscoPingPacketCount, ciscoPingCompleted=ciscoPingCompleted, ciscoPingProtocol=ciscoPingProtocol, ciscoPingMIBTrapPrefix=ciscoPingMIBTrapPrefix, ciscoPingEntryStatus=ciscoPingEntryStatus, ciscoPingMIB=ciscoPingMIB, ciscoPingVrfName=ciscoPingVrfName, ciscoPingMIBGroups=ciscoPingMIBGroups, ciscoPingTrapOnCompletion=ciscoPingTrapOnCompletion, ciscoPingDelay=ciscoPingDelay, ciscoPingEntry=ciscoPingEntry, ciscoPingMaxRtt=ciscoPingMaxRtt, ciscoPingAvgRtt=ciscoPingAvgRtt, PYSNMP_MODULE_ID=ciscoPingMIB, ciscoPingMIBGroup=ciscoPingMIBGroup, ciscoPingPacketTimeout=ciscoPingPacketTimeout, ciscoPingEntryOwner=ciscoPingEntryOwner, ciscoPingMIBComplianceVpn=ciscoPingMIBComplianceVpn, ciscoPingMinRtt=ciscoPingMinRtt)
