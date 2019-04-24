#
# PySNMP MIB module CISCO-SERVICE-CONTROL-ATTACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-SERVICE-CONTROL-ATTACK-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:39:54 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, entPhysicalName = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalName")
InetAddress, InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32, MibIdentifier, TimeTicks, Counter64, ModuleIdentity, IpAddress, Counter32, Integer32, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32", "MibIdentifier", "TimeTicks", "Counter64", "ModuleIdentity", "IpAddress", "Counter32", "Integer32", "Unsigned32", "NotificationType")
TimeInterval, TextualConvention, TruthValue, DisplayString, TimeStamp, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "TruthValue", "DisplayString", "TimeStamp", "AutonomousType")
ciscoServiceControlAttackMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 693))
ciscoServiceControlAttackMIB.setRevisions(('2013-08-16 00:00', '2009-05-05 00:00',))
if mibBuilder.loadTexts: ciscoServiceControlAttackMIB.setLastUpdated('201308160000Z')
if mibBuilder.loadTexts: ciscoServiceControlAttackMIB.setOrganization('Cisco Systems, Inc.')
class CscaAttackType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

ciscoServiceControlAttackMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 693, 0))
ciscoServiceControlAttackMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 693, 1))
ciscoServiceControlAttackMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 693, 2))
cscaFilterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1))
cscaTypeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2), )
if mibBuilder.loadTexts: cscaTypeTable.setStatus('current')
cscaTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeIndex"))
if mibBuilder.loadTexts: cscaTypeEntry.setStatus('current')
cscaTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 1), CscaAttackType().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: cscaTypeIndex.setStatus('current')
cscaTypeCurrentNumAttacks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 2), Gauge32()).setUnits('attacks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaTypeCurrentNumAttacks.setStatus('current')
cscaTypeTotalNumAttacks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 3), Counter32()).setUnits('attacks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaTypeTotalNumAttacks.setStatus('current')
cscaTypeTotalNumFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 4), Counter64()).setUnits('IP flows').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaTypeTotalNumFlows.setStatus('current')
cscaTypeTotalNumSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 5), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaTypeTotalNumSeconds.setStatus('current')
cscaTypeOriginatedByNetworkSide = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaTypeOriginatedByNetworkSide.setStatus('current')
cscaTypeProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaTypeProtocol.setStatus('current')
cscaTypeIsPortSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaTypeIsPortSpecific.setStatus('current')
cscaTypeIPsDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaTypeIPsDetected.setStatus('current')
cscaInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3), )
if mibBuilder.loadTexts: cscaInfoTable.setStatus('current')
cscaInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cscaInfoEntry.setStatus('current')
cscaInfoUpStreamAttackFilteringTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3, 1, 1), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaInfoUpStreamAttackFilteringTime.setStatus('current')
cscaInfoUpStreamLastAttackFilteringTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3, 1, 2), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaInfoUpStreamLastAttackFilteringTime.setStatus('current')
cscaInfoDownStreamAttackFilteringTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3, 1, 3), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaInfoDownStreamAttackFilteringTime.setStatus('current')
cscaInfoDownStreamLastAttackFilteringTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 3, 1, 4), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaInfoDownStreamLastAttackFilteringTime.setStatus('current')
cscaType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 1), CscaAttackType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cscaType.setStatus('current')
cscaSourceAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cscaSourceAddressType.setStatus('current')
cscaSourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cscaSourceAddress.setStatus('current')
cscaDestinationAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 4), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cscaDestinationAddressType.setStatus('current')
cscaDestinationAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 5), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cscaDestinationAddress.setStatus('current')
cscaAttackedPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 6), InetPortNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cscaAttackedPort.setStatus('current')
cscaFilterStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("activated", 1), ("deactivated", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cscaFilterStatus.setStatus('current')
cscaNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscaNotifsEnabled.setStatus('current')
cscaLastDiscontinuityTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaLastDiscontinuityTimeStamp.setStatus('current')
cscaGlobalAttackType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("icmpAttack", 1), ("udpAttack", 2), ("udpFragmentAttack", 3), ("tcpSynAttack", 4), ("tcpRstAttack", 5), ("tcpFragmentAttack", 6), ("tcpNonSynAttack", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscaGlobalAttackType.setStatus('current')
cscaGlobalAttackNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 693, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscaGlobalAttackNotifsEnabled.setStatus('current')
cscaFilterChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 693, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaType"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddressType"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddress"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddressType"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddress"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaAttackedPort"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterStatus"))
if mibBuilder.loadTexts: cscaFilterChange.setStatus('current')
cscaGlobalAttackFilterChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 693, 0, 2)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaGlobalAttackType"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterStatus"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeOriginatedByNetworkSide"))
if mibBuilder.loadTexts: cscaGlobalAttackFilterChange.setStatus('current')
cscaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 1))
cscaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2))
cscaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 1, 1)).setObjects(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaMIBAttackTypeObjectGroup"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaMIBNotificationGroup"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaMIBAttackInfoObjectGroup"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterObjectGroup"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaMIBNotifControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscaMIBCompliance = cscaMIBCompliance.setStatus('deprecated')
cscaMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 1, 2)).setObjects(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaMIBAttackTypeObjectGroup"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaMIBNotificationGroupRev1"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaMIBAttackInfoObjectGroup"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterObjectGroupRev1"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaMIBNotifControlGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscaMIBComplianceRev1 = cscaMIBComplianceRev1.setStatus('current')
cscaMIBAttackTypeObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 1)).setObjects(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeCurrentNumAttacks"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeTotalNumAttacks"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeTotalNumFlows"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeTotalNumSeconds"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeOriginatedByNetworkSide"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeProtocol"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeIsPortSpecific"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaTypeIPsDetected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscaMIBAttackTypeObjectGroup = cscaMIBAttackTypeObjectGroup.setStatus('current')
cscaMIBAttackInfoObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 2)).setObjects(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaInfoUpStreamAttackFilteringTime"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaInfoUpStreamLastAttackFilteringTime"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaInfoDownStreamAttackFilteringTime"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaInfoDownStreamLastAttackFilteringTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscaMIBAttackInfoObjectGroup = cscaMIBAttackInfoObjectGroup.setStatus('current')
cscaMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 3)).setObjects(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscaMIBNotificationGroup = cscaMIBNotificationGroup.setStatus('deprecated')
cscaFilterObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 4)).setObjects(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaType"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddressType"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddress"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddressType"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddress"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaAttackedPort"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterStatus"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaLastDiscontinuityTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscaFilterObjectGroup = cscaFilterObjectGroup.setStatus('deprecated')
cscaMIBNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 5)).setObjects(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaNotifsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscaMIBNotifControlGroup = cscaMIBNotifControlGroup.setStatus('deprecated')
cscaMIBNotificationGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 6)).setObjects(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterChange"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaGlobalAttackFilterChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscaMIBNotificationGroupRev1 = cscaMIBNotificationGroupRev1.setStatus('current')
cscaFilterObjectGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 7)).setObjects(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaType"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddressType"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaSourceAddress"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddressType"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaDestinationAddress"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaAttackedPort"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaFilterStatus"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaLastDiscontinuityTimeStamp"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaGlobalAttackType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscaFilterObjectGroupRev1 = cscaFilterObjectGroupRev1.setStatus('current')
cscaMIBNotifControlGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 693, 2, 2, 8)).setObjects(("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaNotifsEnabled"), ("CISCO-SERVICE-CONTROL-ATTACK-MIB", "cscaGlobalAttackNotifsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cscaMIBNotifControlGroupRev1 = cscaMIBNotifControlGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-SERVICE-CONTROL-ATTACK-MIB", cscaFilterObjectGroup=cscaFilterObjectGroup, cscaFilterMIBObjects=cscaFilterMIBObjects, cscaGlobalAttackNotifsEnabled=cscaGlobalAttackNotifsEnabled, cscaMIBNotificationGroup=cscaMIBNotificationGroup, cscaDestinationAddressType=cscaDestinationAddressType, cscaMIBGroups=cscaMIBGroups, cscaTypeEntry=cscaTypeEntry, cscaMIBCompliance=cscaMIBCompliance, cscaGlobalAttackType=cscaGlobalAttackType, ciscoServiceControlAttackMIB=ciscoServiceControlAttackMIB, cscaSourceAddress=cscaSourceAddress, cscaMIBNotifControlGroup=cscaMIBNotifControlGroup, cscaInfoDownStreamAttackFilteringTime=cscaInfoDownStreamAttackFilteringTime, CscaAttackType=CscaAttackType, cscaInfoUpStreamLastAttackFilteringTime=cscaInfoUpStreamLastAttackFilteringTime, cscaTypeProtocol=cscaTypeProtocol, cscaFilterObjectGroupRev1=cscaFilterObjectGroupRev1, cscaType=cscaType, cscaLastDiscontinuityTimeStamp=cscaLastDiscontinuityTimeStamp, cscaMIBAttackInfoObjectGroup=cscaMIBAttackInfoObjectGroup, cscaTypeTotalNumAttacks=cscaTypeTotalNumAttacks, cscaTypeOriginatedByNetworkSide=cscaTypeOriginatedByNetworkSide, cscaInfoDownStreamLastAttackFilteringTime=cscaInfoDownStreamLastAttackFilteringTime, cscaDestinationAddress=cscaDestinationAddress, PYSNMP_MODULE_ID=ciscoServiceControlAttackMIB, cscaTypeTotalNumSeconds=cscaTypeTotalNumSeconds, cscaInfoUpStreamAttackFilteringTime=cscaInfoUpStreamAttackFilteringTime, cscaSourceAddressType=cscaSourceAddressType, cscaFilterStatus=cscaFilterStatus, cscaMIBComplianceRev1=cscaMIBComplianceRev1, cscaTypeCurrentNumAttacks=cscaTypeCurrentNumAttacks, cscaTypeTable=cscaTypeTable, cscaMIBNotificationGroupRev1=cscaMIBNotificationGroupRev1, ciscoServiceControlAttackMIBNotifs=ciscoServiceControlAttackMIBNotifs, cscaAttackedPort=cscaAttackedPort, cscaInfoEntry=cscaInfoEntry, cscaInfoTable=cscaInfoTable, cscaMIBCompliances=cscaMIBCompliances, cscaTypeIPsDetected=cscaTypeIPsDetected, cscaFilterChange=cscaFilterChange, cscaGlobalAttackFilterChange=cscaGlobalAttackFilterChange, cscaMIBNotifControlGroupRev1=cscaMIBNotifControlGroupRev1, cscaTypeTotalNumFlows=cscaTypeTotalNumFlows, ciscoServiceControlAttackMIBConform=ciscoServiceControlAttackMIBConform, cscaTypeIsPortSpecific=cscaTypeIsPortSpecific, cscaMIBAttackTypeObjectGroup=cscaMIBAttackTypeObjectGroup, ciscoServiceControlAttackMIBObjects=ciscoServiceControlAttackMIBObjects, cscaTypeIndex=cscaTypeIndex, cscaNotifsEnabled=cscaNotifsEnabled)
