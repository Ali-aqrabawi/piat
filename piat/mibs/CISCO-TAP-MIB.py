#
# PySNMP MIB module CISCO-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-TAP-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:35:52 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetPortNumber, InetAddressType, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType", "InetAddressPrefixLength")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Integer32, Counter32, iso, Bits, IpAddress, Unsigned32, Counter64, Gauge32, enterprises, ModuleIdentity, MibIdentifier, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter32", "iso", "Bits", "IpAddress", "Unsigned32", "Counter64", "Gauge32", "enterprises", "ModuleIdentity", "MibIdentifier", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
MacAddress, DateAndTime, TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DateAndTime", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
cTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 252))
cTapMIB.setRevisions(('2005-10-12 00:00', '2002-07-25 00:00',))
if mibBuilder.loadTexts: cTapMIB.setLastUpdated('200510120000Z')
if mibBuilder.loadTexts: cTapMIB.setOrganization('Cisco Systems, Inc.')
cTapMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 252, 0))
cTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 252, 1))
cTapMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 252, 2))
cTapMediationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1))
cTapStreamGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2))
cTapDebugGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 3))
class Dscp(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

cTapMediationNewIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cTapMediationNewIndex.setStatus('current')
cTapMediationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2), )
if mibBuilder.loadTexts: cTapMediationTable.setStatus('current')
cTapMediationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-TAP-MIB", "cTapMediationContentId"))
if mibBuilder.loadTexts: cTapMediationEntry.setStatus('current')
cTapMediationContentId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cTapMediationContentId.setStatus('current')
cTapMediationDestAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationDestAddressType.setStatus('current')
cTapMediationDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationDestAddress.setStatus('current')
cTapMediationDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 4), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationDestPort.setStatus('current')
cTapMediationSrcInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationSrcInterface.setStatus('current')
cTapMediationRtcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 6), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cTapMediationRtcpPort.setStatus('current')
cTapMediationDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 7), Dscp().clone(34)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationDscp.setStatus('current')
cTapMediationDataType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationDataType.setStatus('current')
cTapMediationRetransmitType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationRetransmitType.setStatus('current')
cTapMediationTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 10), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationTimeout.setStatus('current')
cTapMediationTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("udp", 1), ("rtpNack", 2), ("tcp", 3), ("sctp", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationTransport.setStatus('current')
cTapMediationNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 12), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationNotificationEnable.setStatus('current')
cTapMediationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapMediationStatus.setStatus('current')
cTapMediationCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 3), Bits().clone(namedValues=NamedValues(("ipV4SrcInterface", 0), ("ipV6SrcInterface", 1), ("udp", 2), ("rtpNack", 3), ("tcp", 4), ("sctp", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cTapMediationCapabilities.setStatus('current')
cTapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("interface", 1), ("ipV4", 2), ("ipV6", 3), ("l4Port", 4), ("dscp", 5), ("dstMacAddr", 6), ("srcMacAddr", 7), ("ethernetPid", 8), ("dstLlcSap", 9), ("srcLlcSap", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cTapStreamCapabilities.setStatus('current')
cTapStreamIpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2), )
if mibBuilder.loadTexts: cTapStreamIpTable.setStatus('current')
cTapStreamIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-TAP-MIB", "cTapMediationContentId"), (0, "CISCO-TAP-MIB", "cTapStreamIpIndex"))
if mibBuilder.loadTexts: cTapStreamIpEntry.setStatus('current')
cTapStreamIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cTapStreamIpIndex.setStatus('current')
cTapStreamIpInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpInterface.setStatus('current')
cTapStreamIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpAddrType.setStatus('current')
cTapStreamIpDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 4), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpDestinationAddress.setStatus('current')
cTapStreamIpDestinationLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 5), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpDestinationLength.setStatus('current')
cTapStreamIpSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 6), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpSourceAddress.setStatus('current')
cTapStreamIpSourceLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 7), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpSourceLength.setStatus('current')
cTapStreamIpTosByte = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpTosByte.setStatus('current')
cTapStreamIpTosByteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpTosByteMask.setStatus('current')
cTapStreamIpFlowId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048575), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpFlowId.setStatus('current')
cTapStreamIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpProtocol.setStatus('current')
cTapStreamIpDestL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 12), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpDestL4PortMin.setStatus('current')
cTapStreamIpDestL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 13), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpDestL4PortMax.setStatus('current')
cTapStreamIpSourceL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 14), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpSourceL4PortMin.setStatus('current')
cTapStreamIpSourceL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 15), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpSourceL4PortMax.setStatus('current')
cTapStreamIpInterceptEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 16), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpInterceptEnable.setStatus('current')
cTapStreamIpInterceptedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cTapStreamIpInterceptedPackets.setStatus('current')
cTapStreamIpInterceptDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cTapStreamIpInterceptDrops.setStatus('current')
cTapStreamIpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStreamIpStatus.setStatus('current')
cTapStream802Table = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3), )
if mibBuilder.loadTexts: cTapStream802Table.setStatus('current')
cTapStream802Entry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-TAP-MIB", "cTapMediationContentId"), (0, "CISCO-TAP-MIB", "cTapStream802Index"))
if mibBuilder.loadTexts: cTapStream802Entry.setStatus('current')
cTapStream802Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cTapStream802Index.setStatus('current')
cTapStream802Fields = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 2), Bits().clone(namedValues=NamedValues(("interface", 0), ("dstMacAddress", 1), ("srcMacAddress", 2), ("ethernetPid", 3), ("dstLlcSap", 4), ("srcLlcSap", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStream802Fields.setStatus('current')
cTapStream802Interface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStream802Interface.setStatus('current')
cTapStream802DestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStream802DestinationAddress.setStatus('current')
cTapStream802SourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStream802SourceAddress.setStatus('current')
cTapStream802EthernetPid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStream802EthernetPid.setStatus('current')
cTapStream802DestinationLlcSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStream802DestinationLlcSap.setStatus('current')
cTapStream802SourceLlcSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStream802SourceLlcSap.setStatus('current')
cTapStream802InterceptEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 9), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStream802InterceptEnable.setStatus('current')
cTapStream802InterceptedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cTapStream802InterceptedPackets.setStatus('current')
cTapStream802InterceptDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cTapStream802InterceptDrops.setStatus('current')
cTapStream802Status = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cTapStream802Status.setStatus('current')
cTapDebugTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 3, 1), )
if mibBuilder.loadTexts: cTapDebugTable.setStatus('current')
cTapDebugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-TAP-MIB", "cTapDebugIndex"))
if mibBuilder.loadTexts: cTapDebugEntry.setStatus('current')
cTapDebugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cTapDebugIndex.setStatus('current')
cTapDebugMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 3, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cTapDebugMessage.setStatus('current')
cTapMIBActive = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 252, 0, 1)).setObjects(("CISCO-TAP-MIB", "cTapStream802Status"))
if mibBuilder.loadTexts: cTapMIBActive.setStatus('current')
cTapMediationTimedOut = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 252, 0, 2)).setObjects(("CISCO-TAP-MIB", "cTapMediationStatus"))
if mibBuilder.loadTexts: cTapMediationTimedOut.setStatus('current')
cTapMediationDebug = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 252, 0, 3)).setObjects(("CISCO-TAP-MIB", "cTapMediationContentId"), ("CISCO-TAP-MIB", "cTapDebugIndex"))
if mibBuilder.loadTexts: cTapMediationDebug.setStatus('current')
cTapStreamIpDebug = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 252, 0, 4)).setObjects(("CISCO-TAP-MIB", "cTapMediationContentId"), ("CISCO-TAP-MIB", "cTapStreamIpIndex"), ("CISCO-TAP-MIB", "cTapDebugIndex"))
if mibBuilder.loadTexts: cTapStreamIpDebug.setStatus('current')
cTapStream802Debug = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 252, 0, 5)).setObjects(("CISCO-TAP-MIB", "cTapMediationContentId"), ("CISCO-TAP-MIB", "cTapStream802Index"), ("CISCO-TAP-MIB", "cTapDebugIndex"))
if mibBuilder.loadTexts: cTapStream802Debug.setStatus('current')
cTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 1))
cTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2))
cTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 1, 1)).setObjects(("CISCO-TAP-MIB", "cTapMediationComplianceGroup"), ("CISCO-TAP-MIB", "cTapStreamComplianceGroup"), ("CISCO-TAP-MIB", "cTapMediationCpbComplianceGroup"), ("CISCO-TAP-MIB", "cTapNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTapMIBCompliance = cTapMIBCompliance.setStatus('current')
cTapMediationComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 1)).setObjects(("CISCO-TAP-MIB", "cTapMediationNewIndex"), ("CISCO-TAP-MIB", "cTapMediationDestAddressType"), ("CISCO-TAP-MIB", "cTapMediationDestAddress"), ("CISCO-TAP-MIB", "cTapMediationDestPort"), ("CISCO-TAP-MIB", "cTapMediationSrcInterface"), ("CISCO-TAP-MIB", "cTapMediationRtcpPort"), ("CISCO-TAP-MIB", "cTapMediationDscp"), ("CISCO-TAP-MIB", "cTapMediationDataType"), ("CISCO-TAP-MIB", "cTapMediationRetransmitType"), ("CISCO-TAP-MIB", "cTapMediationTimeout"), ("CISCO-TAP-MIB", "cTapMediationTransport"), ("CISCO-TAP-MIB", "cTapMediationNotificationEnable"), ("CISCO-TAP-MIB", "cTapMediationStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTapMediationComplianceGroup = cTapMediationComplianceGroup.setStatus('current')
cTapStreamComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 2)).setObjects(("CISCO-TAP-MIB", "cTapStreamCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTapStreamComplianceGroup = cTapStreamComplianceGroup.setStatus('current')
cTapStreamIpComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 3)).setObjects(("CISCO-TAP-MIB", "cTapStreamIpInterface"), ("CISCO-TAP-MIB", "cTapStreamIpAddrType"), ("CISCO-TAP-MIB", "cTapStreamIpDestinationAddress"), ("CISCO-TAP-MIB", "cTapStreamIpDestinationLength"), ("CISCO-TAP-MIB", "cTapStreamIpSourceAddress"), ("CISCO-TAP-MIB", "cTapStreamIpSourceLength"), ("CISCO-TAP-MIB", "cTapStreamIpTosByte"), ("CISCO-TAP-MIB", "cTapStreamIpTosByteMask"), ("CISCO-TAP-MIB", "cTapStreamIpFlowId"), ("CISCO-TAP-MIB", "cTapStreamIpProtocol"), ("CISCO-TAP-MIB", "cTapStreamIpDestL4PortMin"), ("CISCO-TAP-MIB", "cTapStreamIpDestL4PortMax"), ("CISCO-TAP-MIB", "cTapStreamIpSourceL4PortMin"), ("CISCO-TAP-MIB", "cTapStreamIpSourceL4PortMax"), ("CISCO-TAP-MIB", "cTapStreamIpInterceptEnable"), ("CISCO-TAP-MIB", "cTapStreamIpInterceptedPackets"), ("CISCO-TAP-MIB", "cTapStreamIpInterceptDrops"), ("CISCO-TAP-MIB", "cTapStreamIpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTapStreamIpComplianceGroup = cTapStreamIpComplianceGroup.setStatus('current')
cTapStream802ComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 4)).setObjects(("CISCO-TAP-MIB", "cTapStream802Fields"), ("CISCO-TAP-MIB", "cTapStream802Interface"), ("CISCO-TAP-MIB", "cTapStream802DestinationAddress"), ("CISCO-TAP-MIB", "cTapStream802SourceAddress"), ("CISCO-TAP-MIB", "cTapStream802EthernetPid"), ("CISCO-TAP-MIB", "cTapStream802SourceLlcSap"), ("CISCO-TAP-MIB", "cTapStream802DestinationLlcSap"), ("CISCO-TAP-MIB", "cTapStream802InterceptEnable"), ("CISCO-TAP-MIB", "cTapStream802InterceptedPackets"), ("CISCO-TAP-MIB", "cTapStream802InterceptDrops"), ("CISCO-TAP-MIB", "cTapStream802Status"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTapStream802ComplianceGroup = cTapStream802ComplianceGroup.setStatus('current')
cTapNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 5)).setObjects(("CISCO-TAP-MIB", "cTapMIBActive"), ("CISCO-TAP-MIB", "cTapMediationTimedOut"), ("CISCO-TAP-MIB", "cTapMediationDebug"), ("CISCO-TAP-MIB", "cTapStreamIpDebug"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTapNotificationGroup = cTapNotificationGroup.setStatus('current')
cTapMediationCpbComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 6)).setObjects(("CISCO-TAP-MIB", "cTapMediationCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTapMediationCpbComplianceGroup = cTapMediationCpbComplianceGroup.setStatus('current')
cTapDebugComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 7)).setObjects(("CISCO-TAP-MIB", "cTapDebugMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTapDebugComplianceGroup = cTapDebugComplianceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-TAP-MIB", cTapMediationDataType=cTapMediationDataType, cTapMediationContentId=cTapMediationContentId, cTapMIBActive=cTapMIBActive, cTapStreamIpSourceL4PortMax=cTapStreamIpSourceL4PortMax, cTapMediationTimeout=cTapMediationTimeout, cTapStreamIpTable=cTapStreamIpTable, cTapStream802Entry=cTapStream802Entry, cTapStreamIpFlowId=cTapStreamIpFlowId, cTapStream802SourceAddress=cTapStream802SourceAddress, cTapDebugIndex=cTapDebugIndex, cTapStreamIpProtocol=cTapStreamIpProtocol, Dscp=Dscp, cTapStreamIpAddrType=cTapStreamIpAddrType, cTapStream802Interface=cTapStream802Interface, cTapMediationDebug=cTapMediationDebug, cTapMIBCompliances=cTapMIBCompliances, cTapMIBGroups=cTapMIBGroups, cTapMediationSrcInterface=cTapMediationSrcInterface, cTapMediationCapabilities=cTapMediationCapabilities, cTapDebugTable=cTapDebugTable, cTapStreamIpComplianceGroup=cTapStreamIpComplianceGroup, cTapStreamIpTosByteMask=cTapStreamIpTosByteMask, cTapMIBObjects=cTapMIBObjects, cTapMediationComplianceGroup=cTapMediationComplianceGroup, cTapNotificationGroup=cTapNotificationGroup, cTapDebugComplianceGroup=cTapDebugComplianceGroup, cTapDebugEntry=cTapDebugEntry, cTapStream802Fields=cTapStream802Fields, cTapStreamComplianceGroup=cTapStreamComplianceGroup, cTapMIB=cTapMIB, cTapStreamIpStatus=cTapStreamIpStatus, cTapStream802Table=cTapStream802Table, cTapMediationNewIndex=cTapMediationNewIndex, cTapStreamIpSourceLength=cTapStreamIpSourceLength, PYSNMP_MODULE_ID=cTapMIB, cTapStream802SourceLlcSap=cTapStream802SourceLlcSap, cTapStreamIpTosByte=cTapStreamIpTosByte, cTapStreamIpDebug=cTapStreamIpDebug, cTapMIBCompliance=cTapMIBCompliance, cTapMediationCpbComplianceGroup=cTapMediationCpbComplianceGroup, cTapMediationRetransmitType=cTapMediationRetransmitType, cTapStreamCapabilities=cTapStreamCapabilities, cTapStreamIpDestL4PortMax=cTapStreamIpDestL4PortMax, cTapMediationRtcpPort=cTapMediationRtcpPort, cTapDebugGroup=cTapDebugGroup, cTapStreamIpInterceptedPackets=cTapStreamIpInterceptedPackets, cTapMIBNotifications=cTapMIBNotifications, cTapMediationNotificationEnable=cTapMediationNotificationEnable, cTapMediationDestAddress=cTapMediationDestAddress, cTapMediationEntry=cTapMediationEntry, cTapMediationDscp=cTapMediationDscp, cTapStreamGroup=cTapStreamGroup, cTapStreamIpInterceptEnable=cTapStreamIpInterceptEnable, cTapStreamIpDestinationLength=cTapStreamIpDestinationLength, cTapStream802InterceptedPackets=cTapStream802InterceptedPackets, cTapMediationGroup=cTapMediationGroup, cTapStreamIpInterceptDrops=cTapStreamIpInterceptDrops, cTapStream802InterceptDrops=cTapStream802InterceptDrops, cTapStreamIpIndex=cTapStreamIpIndex, cTapStream802Status=cTapStream802Status, cTapStream802Index=cTapStream802Index, cTapStream802ComplianceGroup=cTapStream802ComplianceGroup, cTapMediationTable=cTapMediationTable, cTapStreamIpSourceAddress=cTapStreamIpSourceAddress, cTapMIBConformance=cTapMIBConformance, cTapMediationStatus=cTapMediationStatus, cTapStream802DestinationLlcSap=cTapStream802DestinationLlcSap, cTapDebugMessage=cTapDebugMessage, cTapStreamIpDestinationAddress=cTapStreamIpDestinationAddress, cTapMediationTimedOut=cTapMediationTimedOut, cTapMediationDestPort=cTapMediationDestPort, cTapStream802Debug=cTapStream802Debug, cTapStreamIpEntry=cTapStreamIpEntry, cTapStream802EthernetPid=cTapStream802EthernetPid, cTapStream802InterceptEnable=cTapStream802InterceptEnable, cTapStreamIpInterface=cTapStreamIpInterface, cTapStream802DestinationAddress=cTapStream802DestinationAddress, cTapMediationDestAddressType=cTapMediationDestAddressType, cTapStreamIpDestL4PortMin=cTapStreamIpDestL4PortMin, cTapMediationTransport=cTapMediationTransport, cTapStreamIpSourceL4PortMin=cTapStreamIpSourceL4PortMin)
