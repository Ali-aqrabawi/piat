#
# PySNMP MIB module CISCO-FLEX-LINKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-FLEX-LINKS-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:41:27 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Cisco2KVlanList, = mibBuilder.importSymbols("CISCO-TC", "Cisco2KVlanList")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
VlanIdOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, TimeTicks, MibIdentifier, iso, Counter64, Gauge32, Bits, Counter32, IpAddress, ModuleIdentity, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "TimeTicks", "MibIdentifier", "iso", "Counter64", "Gauge32", "Bits", "Counter32", "IpAddress", "ModuleIdentity", "ObjectIdentity", "NotificationType")
RowStatus, TruthValue, TextualConvention, DisplayString, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString", "StorageType")
ciscoFlexLinksMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 471))
ciscoFlexLinksMIB.setRevisions(('2010-02-04 00:00', '2005-04-25 00:00',))
if mibBuilder.loadTexts: ciscoFlexLinksMIB.setLastUpdated('201002040000Z')
if mibBuilder.loadTexts: ciscoFlexLinksMIB.setOrganization('Cisco Systems, Inc.')
ciscoFlexLinksMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 471, 0))
ciscoFlexLinksMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 471, 1))
ciscoFlexLinksMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 471, 2))
cflConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1))
cflStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 2))
cflIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1), )
if mibBuilder.loadTexts: cflIfConfigTable.setStatus('current')
cflIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-FLEX-LINKS-MIB", "cflIfConfigPrimary"))
if mibBuilder.loadTexts: cflIfConfigEntry.setStatus('current')
cflIfConfigPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cflIfConfigPrimary.setStatus('current')
cflIfConfigBackUp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cflIfConfigBackUp.setStatus('current')
cflIfConfigStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cflIfConfigStorageType.setStatus('current')
cflIfConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cflIfConfigStatus.setStatus('current')
cflEnableStatusChangeNotif = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cflEnableStatusChangeNotif.setStatus('current')
cflIfConfigExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3), )
if mibBuilder.loadTexts: cflIfConfigExtTable.setStatus('current')
cflIfConfigExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-FLEX-LINKS-MIB", "cflIfConfigPrimary"))
if mibBuilder.loadTexts: cflIfConfigExtEntry.setStatus('current')
cflIfConfigMmuPrimaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1, 1), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cflIfConfigMmuPrimaryVlan.setStatus('current')
cflIfConfigPreemptionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("forced", 2), ("bandwidth", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cflIfConfigPreemptionMode.setStatus('current')
cflIfConfigPreemptionDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1, 3), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cflIfConfigPreemptionDelay.setStatus('current')
cflIfConfigPrefer2kVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1, 4), Cisco2KVlanList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cflIfConfigPrefer2kVlan.setStatus('current')
cflIfConfigPrefer4kVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1, 5), Cisco2KVlanList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cflIfConfigPrefer4kVlan.setStatus('current')
cflIfStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 2, 1), )
if mibBuilder.loadTexts: cflIfStatusTable.setStatus('current')
cflIfStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-FLEX-LINKS-MIB", "cflIfIndex"))
if mibBuilder.loadTexts: cflIfStatusEntry.setStatus('current')
cflIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cflIfIndex.setStatus('current')
cflIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("forwarding", 1), ("blocking", 2), ("down", 3), ("waitingToSync", 4), ("waitingForPeerStrate", 5), ("unknown", 6), ("vlbAll", 7), ("vlbConfig", 8), ("vlbPreempt", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cflIfStatus.setStatus('current')
cflIfStatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 471, 0, 1)).setObjects(("CISCO-FLEX-LINKS-MIB", "cflIfStatus"))
if mibBuilder.loadTexts: cflIfStatusChangeNotif.setStatus('current')
ciscoFlexLinksMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 1))
ciscoFlexLinksMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2))
ciscoFlexLinksMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 1, 1)).setObjects(("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksIfConfigGroup"), ("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksIfStatusGroup"), ("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksEnableNotifGroup"), ("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksMIBCompliance = ciscoFlexLinksMIBCompliance.setStatus('deprecated')
ciscoFlexLinksMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 1, 2)).setObjects(("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksIfConfigGroup"), ("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksIfStatusGroup"), ("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksEnableNotifGroup"), ("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksNotifGroup"), ("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksMmuPrimaryVlanGroup"), ("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksPreemptionGroup"), ("CISCO-FLEX-LINKS-MIB", "ciscoFlexLinksPreferVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksMIBCompliance2 = ciscoFlexLinksMIBCompliance2.setStatus('current')
ciscoFlexLinksIfConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 1)).setObjects(("CISCO-FLEX-LINKS-MIB", "cflIfConfigBackUp"), ("CISCO-FLEX-LINKS-MIB", "cflIfConfigStorageType"), ("CISCO-FLEX-LINKS-MIB", "cflIfConfigStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksIfConfigGroup = ciscoFlexLinksIfConfigGroup.setStatus('current')
ciscoFlexLinksIfStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 2)).setObjects(("CISCO-FLEX-LINKS-MIB", "cflIfStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksIfStatusGroup = ciscoFlexLinksIfStatusGroup.setStatus('current')
ciscoFlexLinksEnableNotifGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 3)).setObjects(("CISCO-FLEX-LINKS-MIB", "cflEnableStatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksEnableNotifGroup = ciscoFlexLinksEnableNotifGroup.setStatus('current')
ciscoFlexLinksNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 4)).setObjects(("CISCO-FLEX-LINKS-MIB", "cflIfStatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksNotifGroup = ciscoFlexLinksNotifGroup.setStatus('current')
ciscoFlexLinksMmuPrimaryVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 5)).setObjects(("CISCO-FLEX-LINKS-MIB", "cflIfConfigMmuPrimaryVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksMmuPrimaryVlanGroup = ciscoFlexLinksMmuPrimaryVlanGroup.setStatus('current')
ciscoFlexLinksPreemptionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 6)).setObjects(("CISCO-FLEX-LINKS-MIB", "cflIfConfigPreemptionMode"), ("CISCO-FLEX-LINKS-MIB", "cflIfConfigPreemptionDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksPreemptionGroup = ciscoFlexLinksPreemptionGroup.setStatus('current')
ciscoFlexLinksPreferVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 7)).setObjects(("CISCO-FLEX-LINKS-MIB", "cflIfConfigPrefer2kVlan"), ("CISCO-FLEX-LINKS-MIB", "cflIfConfigPrefer4kVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksPreferVlanGroup = ciscoFlexLinksPreferVlanGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FLEX-LINKS-MIB", PYSNMP_MODULE_ID=ciscoFlexLinksMIB, cflIfConfigTable=cflIfConfigTable, cflIfStatusTable=cflIfStatusTable, ciscoFlexLinksIfStatusGroup=ciscoFlexLinksIfStatusGroup, cflIfConfigBackUp=cflIfConfigBackUp, ciscoFlexLinksNotifGroup=ciscoFlexLinksNotifGroup, cflEnableStatusChangeNotif=cflEnableStatusChangeNotif, cflIfConfigStatus=cflIfConfigStatus, ciscoFlexLinksMIBCompliance2=ciscoFlexLinksMIBCompliance2, cflIfStatusChangeNotif=cflIfStatusChangeNotif, cflIfConfigPreemptionMode=cflIfConfigPreemptionMode, ciscoFlexLinksMmuPrimaryVlanGroup=ciscoFlexLinksMmuPrimaryVlanGroup, ciscoFlexLinksMIBGroups=ciscoFlexLinksMIBGroups, ciscoFlexLinksEnableNotifGroup=ciscoFlexLinksEnableNotifGroup, ciscoFlexLinksIfConfigGroup=ciscoFlexLinksIfConfigGroup, cflIfConfigPrimary=cflIfConfigPrimary, cflIfStatusEntry=cflIfStatusEntry, cflIfConfigExtEntry=cflIfConfigExtEntry, cflIfConfigPreemptionDelay=cflIfConfigPreemptionDelay, ciscoFlexLinksMIBObjects=ciscoFlexLinksMIBObjects, cflIfConfigStorageType=cflIfConfigStorageType, cflIfConfigPrefer2kVlan=cflIfConfigPrefer2kVlan, cflIfConfigExtTable=cflIfConfigExtTable, cflIfIndex=cflIfIndex, cflIfConfigMmuPrimaryVlan=cflIfConfigMmuPrimaryVlan, ciscoFlexLinksMIBCompliance=ciscoFlexLinksMIBCompliance, cflIfStatus=cflIfStatus, ciscoFlexLinksMIBConformance=ciscoFlexLinksMIBConformance, cflStatus=cflStatus, cflConfig=cflConfig, ciscoFlexLinksPreferVlanGroup=ciscoFlexLinksPreferVlanGroup, ciscoFlexLinksMIBCompliances=ciscoFlexLinksMIBCompliances, cflIfConfigEntry=cflIfConfigEntry, cflIfConfigPrefer4kVlan=cflIfConfigPrefer4kVlan, ciscoFlexLinksMIB=ciscoFlexLinksMIB, ciscoFlexLinksPreemptionGroup=ciscoFlexLinksPreemptionGroup, ciscoFlexLinksMIBNotifs=ciscoFlexLinksMIBNotifs)
