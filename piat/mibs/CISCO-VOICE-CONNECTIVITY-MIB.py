#
# PySNMP MIB module CISCO-VOICE-CONNECTIVITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-VOICE-CONNECTIVITY-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:26:55 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, MibIdentifier, ModuleIdentity, Integer32, IpAddress, NotificationType, iso, Gauge32, ObjectIdentity, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "ModuleIdentity", "Integer32", "IpAddress", "NotificationType", "iso", "Gauge32", "ObjectIdentity", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32")
RowPointer, DisplayString, TextualConvention, MacAddress, AutonomousType, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DisplayString", "TextualConvention", "MacAddress", "AutonomousType", "TruthValue", "DateAndTime")
ciscoVoiceConnectivityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 393))
ciscoVoiceConnectivityMIB.setRevisions(('2005-09-13 00:00',))
if mibBuilder.loadTexts: ciscoVoiceConnectivityMIB.setLastUpdated('200509130000Z')
if mibBuilder.loadTexts: ciscoVoiceConnectivityMIB.setOrganization('Cisco Systems, Inc.')
ciscoVoiceConnectivityMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 0))
ciscoVoiceConnectivityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 1))
ciscoVoiceConnectivityMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 2))
cvcCallAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1))
cvcPort = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2))
cvcCallAgentConnection = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3))
cvcNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 4))
cvcCallAgentTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1), )
if mibBuilder.loadTexts: cvcCallAgentTable.setStatus('current')
cvcCallAgentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentIndex"))
if mibBuilder.loadTexts: cvcCallAgentEntry.setStatus('current')
cvcCallAgentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cvcCallAgentIndex.setStatus('current')
cvcCallAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcCallAgentName.setStatus('current')
cvcCallAgentInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcCallAgentInetAddressType.setStatus('current')
cvcCallAgentInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcCallAgentInetAddress.setStatus('current')
cvcCallAgentType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 1, 1, 1, 5), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcCallAgentType.setStatus('current')
cvcPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1), )
if mibBuilder.loadTexts: cvcPortTable.setStatus('current')
cvcPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortIndex"))
if mibBuilder.loadTexts: cvcPortEntry.setStatus('current')
cvcPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cvcPortIndex.setStatus('current')
cvcPortAssociation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortAssociation.setStatus('current')
cvcPortDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortDeviceName.setStatus('current')
cvcPortInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortInetAddressType.setStatus('current')
cvcPortInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortInetAddress.setStatus('current')
cvcPortMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortMACAddress.setStatus('current')
cvcPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 7), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcPortType.setStatus('current')
cvcProductCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("phone", 1), ("gateway", 2), ("h323Device", 3), ("ctiDevice", 4), ("voiceMailDevice", 5), ("mediaResourceDevice", 6), ("huntListDevice", 7), ("sipDevice", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcProductCategory.setStatus('current')
cvcProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("sccp", 1), ("sgcp", 2), ("mgcp", 3), ("h323", 4), ("sip", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcProtocol.setStatus('current')
cvcVirtualInterfaceDN = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 2, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcVirtualInterfaceDN.setStatus('current')
cvcCallAgentConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1), )
if mibBuilder.loadTexts: cvcCallAgentConnectionTable.setStatus('current')
cvcCallAgentConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortIndex"), (0, "CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentIndex"))
if mibBuilder.loadTexts: cvcCallAgentConnectionEntry.setStatus('current')
cvcCallAgentPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcCallAgentPriority.setStatus('current')
cvcRegistrationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("notapplicable", 2), ("registered", 3), ("unregistered", 4), ("rejected", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcRegistrationStatus.setStatus('current')
cvcStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noError", 1), ("unknown", 2), ("configurationError", 3), ("deviceNameUnresolveable", 4), ("maxDevRegReached", 5), ("connectivityError", 6), ("initializationError", 7), ("deviceReset", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcStatusReason.setStatus('current')
cvcLastStatusChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcLastStatusChangeTime.setStatus('current')
cvcLastRegisteredTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 3, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcLastRegisteredTime.setStatus('current')
cvcNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 393, 1, 4, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvcNotifEnable.setStatus('current')
cvcPortRegistrationStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 393, 0, 1)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortDeviceName"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentInetAddress"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentPriority"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcRegistrationStatus"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcStatusReason"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastStatusChangeTime"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastRegisteredTime"))
if mibBuilder.loadTexts: cvcPortRegistrationStatusChange.setStatus('current')
cvcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 1))
cvcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2))
cvcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 1, 1)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentGroup"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortGroup"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentConnectionGroup"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcNotifGroup"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcMIBCompliance = cvcMIBCompliance.setStatus('current')
cvcCallAgentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 1)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentName"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentInetAddressType"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentInetAddress"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcCallAgentGroup = cvcCallAgentGroup.setStatus('current')
cvcPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 2)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortAssociation"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortDeviceName"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortInetAddressType"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortInetAddress"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortMACAddress"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortType"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcProductCategory"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcProtocol"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcVirtualInterfaceDN"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcPortGroup = cvcPortGroup.setStatus('current')
cvcCallAgentConnectionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 3)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcCallAgentPriority"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcRegistrationStatus"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcStatusReason"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastStatusChangeTime"), ("CISCO-VOICE-CONNECTIVITY-MIB", "cvcLastRegisteredTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcCallAgentConnectionGroup = cvcCallAgentConnectionGroup.setStatus('current')
cvcNotifGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 4)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcNotifGroup = cvcNotifGroup.setStatus('current')
cvcNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 393, 2, 2, 5)).setObjects(("CISCO-VOICE-CONNECTIVITY-MIB", "cvcPortRegistrationStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcNotificationsGroup = cvcNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-CONNECTIVITY-MIB", cvcPortInetAddress=cvcPortInetAddress, cvcCallAgentInetAddressType=cvcCallAgentInetAddressType, cvcNotificationsGroup=cvcNotificationsGroup, cvcStatusReason=cvcStatusReason, cvcRegistrationStatus=cvcRegistrationStatus, ciscoVoiceConnectivityMIBObjects=ciscoVoiceConnectivityMIBObjects, cvcNotifGroup=cvcNotifGroup, cvcPortDeviceName=cvcPortDeviceName, cvcPortMACAddress=cvcPortMACAddress, cvcPortAssociation=cvcPortAssociation, cvcNotif=cvcNotif, cvcPortType=cvcPortType, cvcCallAgentConnectionEntry=cvcCallAgentConnectionEntry, cvcCallAgentInetAddress=cvcCallAgentInetAddress, cvcProductCategory=cvcProductCategory, cvcCallAgentPriority=cvcCallAgentPriority, cvcPortRegistrationStatusChange=cvcPortRegistrationStatusChange, PYSNMP_MODULE_ID=ciscoVoiceConnectivityMIB, cvcPortTable=cvcPortTable, cvcLastRegisteredTime=cvcLastRegisteredTime, cvcCallAgentConnection=cvcCallAgentConnection, ciscoVoiceConnectivityMIB=ciscoVoiceConnectivityMIB, ciscoVoiceConnectivityMIBConform=ciscoVoiceConnectivityMIBConform, cvcMIBCompliances=cvcMIBCompliances, cvcPort=cvcPort, cvcVirtualInterfaceDN=cvcVirtualInterfaceDN, cvcMIBGroups=cvcMIBGroups, ciscoVoiceConnectivityMIBNotifs=ciscoVoiceConnectivityMIBNotifs, cvcCallAgentConnectionGroup=cvcCallAgentConnectionGroup, cvcPortEntry=cvcPortEntry, cvcCallAgentIndex=cvcCallAgentIndex, cvcMIBCompliance=cvcMIBCompliance, cvcPortInetAddressType=cvcPortInetAddressType, cvcPortGroup=cvcPortGroup, cvcCallAgentEntry=cvcCallAgentEntry, cvcCallAgentType=cvcCallAgentType, cvcCallAgentName=cvcCallAgentName, cvcCallAgentTable=cvcCallAgentTable, cvcCallAgentConnectionTable=cvcCallAgentConnectionTable, cvcCallAgentGroup=cvcCallAgentGroup, cvcCallAgent=cvcCallAgent, cvcPortIndex=cvcPortIndex, cvcLastStatusChangeTime=cvcLastStatusChangeTime, cvcProtocol=cvcProtocol, cvcNotifEnable=cvcNotifEnable)