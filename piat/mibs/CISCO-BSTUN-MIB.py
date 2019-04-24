#
# PySNMP MIB module CISCO-BSTUN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-BSTUN-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:39:49 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, Integer32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, NotificationType, MibIdentifier, Gauge32, Unsigned32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Integer32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "NotificationType", "MibIdentifier", "Gauge32", "Unsigned32", "IpAddress", "TimeTicks")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoBstunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 35))
ciscoBstunMIB.setRevisions(('2003-02-10 00:00', '2001-06-19 00:00', '1997-01-22 00:00', '1995-08-21 00:00',))
if mibBuilder.loadTexts: ciscoBstunMIB.setLastUpdated('200302100000Z')
if mibBuilder.loadTexts: ciscoBstunMIB.setOrganization('Cisco Systems, Inc.')
bstunObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 35, 1))
bstunGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 1))
bstunGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2))
bstunPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3))
bstunRoutes = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4))
bstunIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunIPAddr.setStatus('current')
bstunLisnSap = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunLisnSap.setStatus('current')
bstunPeerKeepaliveInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300))).setUnits('deciseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunPeerKeepaliveInterval.setStatus('current')
bstunPeerKeepaliveLimit = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunPeerKeepaliveLimit.setStatus('current')
bstunGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1), )
if mibBuilder.loadTexts: bstunGroupTable.setStatus('current')
bstunGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-BSTUN-MIB", "bstunGroupIndex"))
if mibBuilder.loadTexts: bstunGroupEntry.setStatus('current')
bstunGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: bstunGroupIndex.setStatus('current')
bstunProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("bsc", 1), ("adtVariPoll", 2), ("adtPollSelect", 3), ("adplex", 4), ("diebold", 5), ("asyncGeneric", 6), ("mdi", 7), ("mosec", 8), ("gddb", 9), ("apos", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunProtocolType.setStatus('current')
bstunLocalAck = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunLocalAck.setStatus('current')
bstunGroupUnroutableTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunGroupUnroutableTransmit.setStatus('current')
bstunGroupUnroutableReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunGroupUnroutableReceive.setStatus('current')
bstunPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1), )
if mibBuilder.loadTexts: bstunPortTable.setStatus('current')
bstunPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: bstunPortEntry.setStatus('current')
bstunPortGroupNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunPortGroupNumber.setStatus('current')
bstunPortDefaultPeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("ip", 2), ("serial", 3), ("serialDirect", 4), ("serialFrameRelay", 5), ("serialLLC2", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunPortDefaultPeerType.setStatus('current')
bstunPortDefaultPeerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunPortDefaultPeerIP.setStatus('current')
bstunPortDefaultPeerSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 3, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunPortDefaultPeerSerial.setStatus('current')
bstunRouteTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1), )
if mibBuilder.loadTexts: bstunRouteTable.setStatus('current')
bstunRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-BSTUN-MIB", "bstunRouteGroupIndex"), (0, "CISCO-BSTUN-MIB", "bstunRouteStationAddress"))
if mibBuilder.loadTexts: bstunRouteEntry.setStatus('current')
bstunRouteGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: bstunRouteGroupIndex.setStatus('current')
bstunRouteStationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: bstunRouteStationAddress.setStatus('current')
bstunRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 1), ("ip", 2), ("serial", 3), ("serialDirect", 4), ("serialFrameRelay", 5), ("serialLLC2", 6), ("bip", 7), ("apip", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteType.setStatus('current')
bstunRouteIP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteIP.setStatus('current')
bstunRouteSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteSerial.setStatus('current')
bstunRoutePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("low", 1), ("normal", 2), ("medium", 3), ("high", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRoutePriority.setStatus('current')
bstunRoutePeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("dead", 1), ("closed", 2), ("opening", 3), ("openWait", 4), ("connected", 5), ("direct", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRoutePeerState.setStatus('current')
bstunRouteRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteRxPackets.setStatus('current')
bstunRouteTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteTxPackets.setStatus('current')
bstunRouteRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteRxBytes.setStatus('current')
bstunRouteTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteTxBytes.setStatus('current')
bstunRouteDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1007))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteDLCI.setStatus('current')
bstunRouteRSAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteRSAP.setStatus('current')
bstunLLC2Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunLLC2Priority.setStatus('current')
bstunRouteBIPPassive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 15), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteBIPPassive.setStatus('current')
bstunRouteBIPLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1025, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteBIPLocalPort.setStatus('current')
bstunRouteBIPForeignPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1025, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteBIPForeignPort.setStatus('current')
bstunRouteBIPDeviceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 18), Bits().clone(namedValues=NamedValues(("operationcheck", 0), ("reservedBit1", 1), ("datacheck", 2), ("equipmentcheck", 3), ("interventionrequired", 4), ("commandreject", 5), ("deviceinactive", 6), ("deviceactive", 7), ("reservedBit8", 8), ("deviceend", 9), ("unitspecify", 10), ("devicebusy", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteBIPDeviceStatus.setStatus('current')
bstunRouteAPIPHeaderVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 35, 1, 4, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("v0", 1), ("v1", 2), ("v2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bstunRouteAPIPHeaderVersion.setStatus('current')
bstunNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 35, 2))
bstunNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 35, 2, 0))
bstunPeerStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 35, 2, 0, 1)).setObjects(("CISCO-BSTUN-MIB", "bstunRoutePeerState"))
if mibBuilder.loadTexts: bstunPeerStateChangeNotification.setStatus('deprecated')
bstunPeerStateChangeNotification2 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 35, 2, 0, 2)).setObjects(("CISCO-BSTUN-MIB", "bstunRoutePeerState"), ("CISCO-BSTUN-MIB", "bstunRouteType"), ("CISCO-BSTUN-MIB", "bstunRouteRxPackets"), ("CISCO-BSTUN-MIB", "bstunRouteTxPackets"))
if mibBuilder.loadTexts: bstunPeerStateChangeNotification2.setStatus('current')
bstunCUStatusChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 35, 2, 0, 3)).setObjects(("CISCO-BSTUN-MIB", "bstunRouteIP"), ("CISCO-BSTUN-MIB", "bstunRouteBIPForeignPort"), ("CISCO-BSTUN-MIB", "bstunRouteBIPLocalPort"), ("CISCO-BSTUN-MIB", "bstunRouteBIPDeviceStatus"))
if mibBuilder.loadTexts: bstunCUStatusChangeNotification.setStatus('current')
bstunMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 35, 3))
bstunMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 1))
bstunMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2))
bstunMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 1, 1)).setObjects(("CISCO-BSTUN-MIB", "bstunGlobalGroup"), ("CISCO-BSTUN-MIB", "bstunGroupGroup"), ("CISCO-BSTUN-MIB", "bstunPortGroup"), ("CISCO-BSTUN-MIB", "bstunRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunMibCompliance = bstunMibCompliance.setStatus('obsolete')
bstunMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 1, 2)).setObjects(("CISCO-BSTUN-MIB", "bstunGlobalGroupRev1"), ("CISCO-BSTUN-MIB", "bstunGroupGroup"), ("CISCO-BSTUN-MIB", "bstunPortGroup"), ("CISCO-BSTUN-MIB", "bstunRouteGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunMibComplianceRev1 = bstunMibComplianceRev1.setStatus('obsolete')
bstunMibComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 1, 3)).setObjects(("CISCO-BSTUN-MIB", "bstunGlobalGroupRev1"), ("CISCO-BSTUN-MIB", "bstunGroupGroup"), ("CISCO-BSTUN-MIB", "bstunPortGroup"), ("CISCO-BSTUN-MIB", "bstunRouteGroupRev2"), ("CISCO-BSTUN-MIB", "bstunNotificationGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunMibComplianceRev2 = bstunMibComplianceRev2.setStatus('deprecated')
bstunMibComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 1, 4)).setObjects(("CISCO-BSTUN-MIB", "bstunGlobalGroupRev1"), ("CISCO-BSTUN-MIB", "bstunGroupGroup"), ("CISCO-BSTUN-MIB", "bstunPortGroup"), ("CISCO-BSTUN-MIB", "bstunRouteGroupRev1"), ("CISCO-BSTUN-MIB", "bstunNotificationGroupRev1"), ("CISCO-BSTUN-MIB", "bstunRouteBipGroup"), ("CISCO-BSTUN-MIB", "bstunRoutePortsGroup"), ("CISCO-BSTUN-MIB", "bstunRouteApipGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunMibComplianceRev3 = bstunMibComplianceRev3.setStatus('current')
bstunGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 1)).setObjects(("CISCO-BSTUN-MIB", "bstunIPAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunGlobalGroup = bstunGlobalGroup.setStatus('obsolete')
bstunGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 2)).setObjects(("CISCO-BSTUN-MIB", "bstunProtocolType"), ("CISCO-BSTUN-MIB", "bstunLocalAck"), ("CISCO-BSTUN-MIB", "bstunGroupUnroutableTransmit"), ("CISCO-BSTUN-MIB", "bstunGroupUnroutableReceive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunGroupGroup = bstunGroupGroup.setStatus('current')
bstunPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 3)).setObjects(("CISCO-BSTUN-MIB", "bstunPortGroupNumber"), ("CISCO-BSTUN-MIB", "bstunPortDefaultPeerType"), ("CISCO-BSTUN-MIB", "bstunPortDefaultPeerIP"), ("CISCO-BSTUN-MIB", "bstunPortDefaultPeerSerial"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunPortGroup = bstunPortGroup.setStatus('current')
bstunRouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 4)).setObjects(("CISCO-BSTUN-MIB", "bstunRouteType"), ("CISCO-BSTUN-MIB", "bstunRouteIP"), ("CISCO-BSTUN-MIB", "bstunRouteSerial"), ("CISCO-BSTUN-MIB", "bstunRoutePriority"), ("CISCO-BSTUN-MIB", "bstunRoutePeerState"), ("CISCO-BSTUN-MIB", "bstunRouteRxPackets"), ("CISCO-BSTUN-MIB", "bstunRouteTxPackets"), ("CISCO-BSTUN-MIB", "bstunRouteRxBytes"), ("CISCO-BSTUN-MIB", "bstunRouteTxBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunRouteGroup = bstunRouteGroup.setStatus('obsolete')
bstunGlobalGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 5)).setObjects(("CISCO-BSTUN-MIB", "bstunIPAddr"), ("CISCO-BSTUN-MIB", "bstunLisnSap"), ("CISCO-BSTUN-MIB", "bstunPeerKeepaliveInterval"), ("CISCO-BSTUN-MIB", "bstunPeerKeepaliveLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunGlobalGroupRev1 = bstunGlobalGroupRev1.setStatus('current')
bstunRouteGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 6)).setObjects(("CISCO-BSTUN-MIB", "bstunRouteType"), ("CISCO-BSTUN-MIB", "bstunRouteIP"), ("CISCO-BSTUN-MIB", "bstunRouteSerial"), ("CISCO-BSTUN-MIB", "bstunRoutePriority"), ("CISCO-BSTUN-MIB", "bstunRoutePeerState"), ("CISCO-BSTUN-MIB", "bstunRouteRxPackets"), ("CISCO-BSTUN-MIB", "bstunRouteTxPackets"), ("CISCO-BSTUN-MIB", "bstunRouteRxBytes"), ("CISCO-BSTUN-MIB", "bstunRouteTxBytes"), ("CISCO-BSTUN-MIB", "bstunRouteDLCI"), ("CISCO-BSTUN-MIB", "bstunRouteRSAP"), ("CISCO-BSTUN-MIB", "bstunLLC2Priority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunRouteGroupRev1 = bstunRouteGroupRev1.setStatus('current')
bstunRouteGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 7)).setObjects(("CISCO-BSTUN-MIB", "bstunRouteType"), ("CISCO-BSTUN-MIB", "bstunRouteIP"), ("CISCO-BSTUN-MIB", "bstunRouteSerial"), ("CISCO-BSTUN-MIB", "bstunRoutePriority"), ("CISCO-BSTUN-MIB", "bstunRoutePeerState"), ("CISCO-BSTUN-MIB", "bstunRouteRxPackets"), ("CISCO-BSTUN-MIB", "bstunRouteTxPackets"), ("CISCO-BSTUN-MIB", "bstunRouteRxBytes"), ("CISCO-BSTUN-MIB", "bstunRouteTxBytes"), ("CISCO-BSTUN-MIB", "bstunRouteDLCI"), ("CISCO-BSTUN-MIB", "bstunRouteRSAP"), ("CISCO-BSTUN-MIB", "bstunLLC2Priority"), ("CISCO-BSTUN-MIB", "bstunRouteBIPPassive"), ("CISCO-BSTUN-MIB", "bstunRouteBIPLocalPort"), ("CISCO-BSTUN-MIB", "bstunRouteBIPForeignPort"), ("CISCO-BSTUN-MIB", "bstunRouteBIPDeviceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunRouteGroupRev2 = bstunRouteGroupRev2.setStatus('deprecated')
bstunNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 8)).setObjects(("CISCO-BSTUN-MIB", "bstunPeerStateChangeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunNotificationGroup = bstunNotificationGroup.setStatus('deprecated')
bstunNotificationGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 9)).setObjects(("CISCO-BSTUN-MIB", "bstunPeerStateChangeNotification2"), ("CISCO-BSTUN-MIB", "bstunCUStatusChangeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunNotificationGroupRev1 = bstunNotificationGroupRev1.setStatus('current')
bstunRouteBipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 10)).setObjects(("CISCO-BSTUN-MIB", "bstunRouteBIPPassive"), ("CISCO-BSTUN-MIB", "bstunRouteBIPDeviceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunRouteBipGroup = bstunRouteBipGroup.setStatus('current')
bstunRoutePortsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 11)).setObjects(("CISCO-BSTUN-MIB", "bstunRouteBIPLocalPort"), ("CISCO-BSTUN-MIB", "bstunRouteBIPForeignPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunRoutePortsGroup = bstunRoutePortsGroup.setStatus('current')
bstunRouteApipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 35, 3, 2, 12)).setObjects(("CISCO-BSTUN-MIB", "bstunRouteAPIPHeaderVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bstunRouteApipGroup = bstunRouteApipGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-BSTUN-MIB", bstunRoutePortsGroup=bstunRoutePortsGroup, bstunRouteEntry=bstunRouteEntry, bstunRouteTxBytes=bstunRouteTxBytes, bstunRouteGroupIndex=bstunRouteGroupIndex, bstunGlobal=bstunGlobal, bstunLocalAck=bstunLocalAck, bstunRouteIP=bstunRouteIP, bstunPeerKeepaliveLimit=bstunPeerKeepaliveLimit, bstunGroupTable=bstunGroupTable, bstunRouteBIPPassive=bstunRouteBIPPassive, ciscoBstunMIB=ciscoBstunMIB, bstunPeerKeepaliveInterval=bstunPeerKeepaliveInterval, bstunRouteBIPForeignPort=bstunRouteBIPForeignPort, bstunGroupUnroutableTransmit=bstunGroupUnroutableTransmit, bstunRoutePriority=bstunRoutePriority, bstunPortEntry=bstunPortEntry, bstunRouteRxPackets=bstunRouteRxPackets, bstunRouteType=bstunRouteType, bstunIPAddr=bstunIPAddr, bstunRouteBIPLocalPort=bstunRouteBIPLocalPort, bstunCUStatusChangeNotification=bstunCUStatusChangeNotification, bstunMibConformance=bstunMibConformance, bstunRouteGroup=bstunRouteGroup, bstunPorts=bstunPorts, bstunLisnSap=bstunLisnSap, bstunMibComplianceRev3=bstunMibComplianceRev3, bstunGroupEntry=bstunGroupEntry, bstunRouteDLCI=bstunRouteDLCI, bstunMibComplianceRev1=bstunMibComplianceRev1, bstunRouteBipGroup=bstunRouteBipGroup, bstunGroupGroup=bstunGroupGroup, bstunRoutes=bstunRoutes, bstunObjects=bstunObjects, bstunNotificationPrefix=bstunNotificationPrefix, bstunMibComplianceRev2=bstunMibComplianceRev2, bstunPortDefaultPeerType=bstunPortDefaultPeerType, bstunRouteStationAddress=bstunRouteStationAddress, bstunLLC2Priority=bstunLLC2Priority, bstunRouteTxPackets=bstunRouteTxPackets, bstunRouteRSAP=bstunRouteRSAP, bstunMibCompliance=bstunMibCompliance, bstunNotificationGroupRev1=bstunNotificationGroupRev1, bstunRouteApipGroup=bstunRouteApipGroup, bstunPeerStateChangeNotification=bstunPeerStateChangeNotification, bstunRouteGroupRev1=bstunRouteGroupRev1, bstunGroupIndex=bstunGroupIndex, bstunPortGroup=bstunPortGroup, bstunGroupUnroutableReceive=bstunGroupUnroutableReceive, bstunNotificationGroup=bstunNotificationGroup, bstunProtocolType=bstunProtocolType, bstunPortGroupNumber=bstunPortGroupNumber, bstunRouteRxBytes=bstunRouteRxBytes, bstunMibCompliances=bstunMibCompliances, bstunRouteGroupRev2=bstunRouteGroupRev2, bstunRouteAPIPHeaderVersion=bstunRouteAPIPHeaderVersion, bstunGlobalGroup=bstunGlobalGroup, bstunRouteBIPDeviceStatus=bstunRouteBIPDeviceStatus, bstunPortTable=bstunPortTable, bstunRoutePeerState=bstunRoutePeerState, bstunRouteSerial=bstunRouteSerial, bstunNotifications=bstunNotifications, bstunMibGroups=bstunMibGroups, bstunPortDefaultPeerIP=bstunPortDefaultPeerIP, bstunGlobalGroupRev1=bstunGlobalGroupRev1, bstunPortDefaultPeerSerial=bstunPortDefaultPeerSerial, PYSNMP_MODULE_ID=ciscoBstunMIB, bstunGroups=bstunGroups, bstunRouteTable=bstunRouteTable, bstunPeerStateChangeNotification2=bstunPeerStateChangeNotification2)
