#
# PySNMP MIB module CISCO-DDP-IAPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-DDP-IAPP-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:46:44 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPort, = mibBuilder.importSymbols("CISCO-TC", "CiscoPort")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, Gauge32, IpAddress, Integer32, Bits, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Gauge32", "IpAddress", "Integer32", "Bits", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "NotificationType", "Counter32")
MacAddress, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "TruthValue")
ciscoDdpIappMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 277))
ciscoDdpIappMIB.setRevisions(('2002-07-31 00:00', '2002-07-17 00:00', '2002-03-19 00:00', '2002-03-07 00:00', '2001-09-28 00:00',))
if mibBuilder.loadTexts: ciscoDdpIappMIB.setLastUpdated('200207310000Z')
if mibBuilder.loadTexts: ciscoDdpIappMIB.setOrganization('Cisco System Inc.')
ciscoDdpIappMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 0))
ciscoDdpIappMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1))
ciscoDdpIappMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2))
cDdpIappGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1))
cDdpIappRogueApInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 2))
cDdpIappMcastIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappMcastIpAddrType.setStatus('current')
cDdpIappMcastIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 2), InetAddress().clone(hexValue="e0000128")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappMcastIpAddr.setStatus('current')
cDdpIappPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 3), CiscoPort().clone(2887)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDdpIappPort.setStatus('current')
cDdpIappRogueApNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappRogueApNotifEnabled.setStatus('current')
cDdpIappLastRogueApMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 2, 1), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDdpIappLastRogueApMacAddr.setStatus('current')
cDdpIappLastRogueApNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 277, 0, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApMacAddr"))
if mibBuilder.loadTexts: cDdpIappLastRogueApNotif.setStatus('current')
ciscoDdpIappMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 1))
ciscoDdpIappMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2))
ciscoDdpIappCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 1, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "ciscoDdpIappConfigGroup"), ("CISCO-DDP-IAPP-MIB", "ciscoDdpIappRogueApInfoGroup"), ("CISCO-DDP-IAPP-MIB", "ciscoDdpIappNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappCompliance = ciscoDdpIappCompliance.setStatus('current')
ciscoDdpIappConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappMcastIpAddrType"), ("CISCO-DDP-IAPP-MIB", "cDdpIappMcastIpAddr"), ("CISCO-DDP-IAPP-MIB", "cDdpIappPort"), ("CISCO-DDP-IAPP-MIB", "cDdpIappRogueApNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappConfigGroup = ciscoDdpIappConfigGroup.setStatus('current')
ciscoDdpIappRogueApInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 2)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApMacAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappRogueApInfoGroup = ciscoDdpIappRogueApInfoGroup.setStatus('current')
ciscoDdpIappNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 3)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappNotificationGroup = ciscoDdpIappNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DDP-IAPP-MIB", cDdpIappLastRogueApNotif=cDdpIappLastRogueApNotif, cDdpIappRogueApNotifEnabled=cDdpIappRogueApNotifEnabled, cDdpIappRogueApInfo=cDdpIappRogueApInfo, ciscoDdpIappMIBObjects=ciscoDdpIappMIBObjects, cDdpIappMcastIpAddr=cDdpIappMcastIpAddr, ciscoDdpIappNotificationGroup=ciscoDdpIappNotificationGroup, ciscoDdpIappMIBConformance=ciscoDdpIappMIBConformance, PYSNMP_MODULE_ID=ciscoDdpIappMIB, ciscoDdpIappCompliance=ciscoDdpIappCompliance, ciscoDdpIappMIBNotifications=ciscoDdpIappMIBNotifications, cDdpIappGlobalConfig=cDdpIappGlobalConfig, ciscoDdpIappMIBCompliances=ciscoDdpIappMIBCompliances, ciscoDdpIappRogueApInfoGroup=ciscoDdpIappRogueApInfoGroup, cDdpIappMcastIpAddrType=cDdpIappMcastIpAddrType, cDdpIappPort=cDdpIappPort, ciscoDdpIappMIB=ciscoDdpIappMIB, ciscoDdpIappMIBGroups=ciscoDdpIappMIBGroups, cDdpIappLastRogueApMacAddr=cDdpIappLastRogueApMacAddr, ciscoDdpIappConfigGroup=ciscoDdpIappConfigGroup)
