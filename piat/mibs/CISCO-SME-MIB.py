#
# PySNMP MIB module CISCO-SME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-SME-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:25:25 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameId, = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameId")
ifDescr, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, ModuleIdentity, iso, Integer32, Counter32, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "ModuleIdentity", "iso", "Integer32", "Counter32", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Counter64")
TimeStamp, RowStatus, TextualConvention, DisplayString, TruthValue, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "RowStatus", "TextualConvention", "DisplayString", "TruthValue", "StorageType")
ciscoSmeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 632))
ciscoSmeMIB.setRevisions(('2008-03-28 00:00',))
if mibBuilder.loadTexts: ciscoSmeMIB.setLastUpdated('200803280000Z')
if mibBuilder.loadTexts: ciscoSmeMIB.setOrganization('Cisco Systems Inc. ')
ciscoSmeMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 632, 0))
ciscoSmeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 632, 1))
ciscoSmeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 632, 2))
cSmeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1))
class CiscoSmeInterfaceStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("initializing", 2), ("offline", 3), ("online", 4))

class CiscoSmeClusterStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("inactive", 2), ("degraded", 3), ("recovery", 4), ("active", 5))

class CiscoSmeClusterIndex(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

cSmeClusterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1), )
if mibBuilder.loadTexts: cSmeClusterTable.setStatus('current')
cSmeClusterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-SME-MIB", "cSmeClusterId"))
if mibBuilder.loadTexts: cSmeClusterEntry.setStatus('current')
cSmeClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 1), CiscoSmeClusterIndex())
if mibBuilder.loadTexts: cSmeClusterId.setStatus('current')
cSmeClusterName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeClusterName.setStatus('current')
cSmeClusterState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 3), CiscoSmeClusterStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSmeClusterState.setStatus('current')
cSmeClusterMasterInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSmeClusterMasterInetAddrType.setStatus('current')
cSmeClusterMasterInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSmeClusterMasterInetAddr.setStatus('current')
cSmeClusterStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeClusterStorageType.setStatus('current')
cSmeClusterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeClusterRowStatus.setStatus('current')
cSmeClusterMembersTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2), )
if mibBuilder.loadTexts: cSmeClusterMembersTable.setStatus('current')
cSmeClusterMembersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-SME-MIB", "cSmeClusterId"), (0, "CISCO-SME-MIB", "cSmeMemberInetAddrType"), (0, "CISCO-SME-MIB", "cSmeMemberInetAddr"))
if mibBuilder.loadTexts: cSmeClusterMembersEntry.setStatus('current')
cSmeMemberInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cSmeMemberInetAddrType.setStatus('current')
cSmeMemberInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: cSmeMemberInetAddr.setStatus('current')
cSmeFabric = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeFabric.setStatus('current')
cSmeIsMemberLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSmeIsMemberLocal.setStatus('current')
cSmeMemberIsMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSmeMemberIsMaster.setStatus('current')
cSmeClusterMemberStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeClusterMemberStorageType.setStatus('current')
cSmeClusterMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeClusterMemberRowStatus.setStatus('current')
cSmeClusterMemberIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 3), )
if mibBuilder.loadTexts: cSmeClusterMemberIfTable.setStatus('current')
cSmeClusterMemberIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-SME-MIB", "cSmeClusterId"), (0, "CISCO-SME-MIB", "cSmeMemberInetAddrType"), (0, "CISCO-SME-MIB", "cSmeMemberInetAddr"), (0, "CISCO-SME-MIB", "cSmeClusterInterfaceIndex"))
if mibBuilder.loadTexts: cSmeClusterMemberIfEntry.setStatus('current')
cSmeClusterInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cSmeClusterInterfaceIndex.setStatus('current')
cSmeClusterInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 3, 1, 2), CiscoSmeInterfaceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSmeClusterInterfaceState.setStatus('current')
cSmeInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4), )
if mibBuilder.loadTexts: cSmeInterfaceTable.setStatus('current')
cSmeInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-SME-MIB", "cSmeInterfaceIndex"))
if mibBuilder.loadTexts: cSmeInterfaceEntry.setStatus('current')
cSmeInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cSmeInterfaceIndex.setStatus('current')
cSmeInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1, 2), CiscoSmeInterfaceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSmeInterfaceState.setStatus('current')
cSmeInterfaceClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1, 3), CiscoSmeClusterIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeInterfaceClusterId.setStatus('current')
cSmeInterfaceStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1, 4), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeInterfaceStorageType.setStatus('current')
cSmeInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeInterfaceRowStatus.setStatus('current')
cSmeHostPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5), )
if mibBuilder.loadTexts: cSmeHostPortTable.setStatus('current')
cSmeHostPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-SME-MIB", "cSmeHostPortName"))
if mibBuilder.loadTexts: cSmeHostPortEntry.setStatus('current')
cSmeHostPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5, 1, 1), FcNameId())
if mibBuilder.loadTexts: cSmeHostPortName.setStatus('current')
cSmeHostPortClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5, 1, 2), CiscoSmeClusterIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeHostPortClusterId.setStatus('current')
cSmeHostPortStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5, 1, 3), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeHostPortStorageType.setStatus('current')
cSmeHostPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSmeHostPortRowStatus.setStatus('current')
cSmeConfigTableLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSmeConfigTableLastChanged.setStatus('current')
cSmeHostPortTableLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSmeHostPortTableLastChanged.setStatus('current')
cSmeNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cSmeNotifyEnable.setStatus('current')
ciscoSmeInterfaceCreate = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 632, 0, 1)).setObjects(("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: ciscoSmeInterfaceCreate.setStatus('current')
ciscoSmeInterfaceDelete = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 632, 0, 2)).setObjects(("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: ciscoSmeInterfaceDelete.setStatus('current')
ciscoSmeClusterNewMaster = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 632, 0, 3)).setObjects(("CISCO-SME-MIB", "cSmeClusterName"), ("CISCO-SME-MIB", "cSmeClusterMasterInetAddrType"), ("CISCO-SME-MIB", "cSmeClusterMasterInetAddr"))
if mibBuilder.loadTexts: ciscoSmeClusterNewMaster.setStatus('current')
ciscoSmeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 1))
ciscoSmeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 2))
ciscoSmeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 1, 1)).setObjects(("CISCO-SME-MIB", "ciscoSmeConfigGroup"), ("CISCO-SME-MIB", "ciscoSmeNotifControlGroup"), ("CISCO-SME-MIB", "ciscoSmeNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSmeMIBCompliance = ciscoSmeMIBCompliance.setStatus('current')
ciscoSmeConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 2, 1)).setObjects(("CISCO-SME-MIB", "cSmeClusterState"), ("CISCO-SME-MIB", "cSmeClusterMasterInetAddrType"), ("CISCO-SME-MIB", "cSmeClusterMasterInetAddr"), ("CISCO-SME-MIB", "cSmeIsMemberLocal"), ("CISCO-SME-MIB", "cSmeClusterInterfaceState"), ("CISCO-SME-MIB", "cSmeInterfaceState"), ("CISCO-SME-MIB", "cSmeInterfaceClusterId"), ("CISCO-SME-MIB", "cSmeHostPortClusterId"), ("CISCO-SME-MIB", "cSmeConfigTableLastChanged"), ("CISCO-SME-MIB", "cSmeHostPortTableLastChanged"), ("CISCO-SME-MIB", "cSmeFabric"), ("CISCO-SME-MIB", "cSmeClusterName"), ("CISCO-SME-MIB", "cSmeInterfaceRowStatus"), ("CISCO-SME-MIB", "cSmeClusterRowStatus"), ("CISCO-SME-MIB", "cSmeMemberIsMaster"), ("CISCO-SME-MIB", "cSmeClusterMemberRowStatus"), ("CISCO-SME-MIB", "cSmeClusterStorageType"), ("CISCO-SME-MIB", "cSmeClusterMemberStorageType"), ("CISCO-SME-MIB", "cSmeInterfaceStorageType"), ("CISCO-SME-MIB", "cSmeHostPortStorageType"), ("CISCO-SME-MIB", "cSmeHostPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSmeConfigGroup = ciscoSmeConfigGroup.setStatus('current')
ciscoSmeNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 2, 2)).setObjects(("CISCO-SME-MIB", "cSmeNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSmeNotifControlGroup = ciscoSmeNotifControlGroup.setStatus('current')
ciscoSmeNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 2, 3)).setObjects(("CISCO-SME-MIB", "ciscoSmeInterfaceCreate"), ("CISCO-SME-MIB", "ciscoSmeInterfaceDelete"), ("CISCO-SME-MIB", "ciscoSmeClusterNewMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSmeNotifsGroup = ciscoSmeNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SME-MIB", cSmeFabric=cSmeFabric, cSmeClusterId=cSmeClusterId, cSmeInterfaceStorageType=cSmeInterfaceStorageType, cSmeClusterMemberStorageType=cSmeClusterMemberStorageType, CiscoSmeClusterIndex=CiscoSmeClusterIndex, cSmeInterfaceState=cSmeInterfaceState, cSmeClusterTable=cSmeClusterTable, ciscoSmeMIBGroups=ciscoSmeMIBGroups, cSmeClusterEntry=cSmeClusterEntry, cSmeClusterStorageType=cSmeClusterStorageType, cSmeInterfaceRowStatus=cSmeInterfaceRowStatus, ciscoSmeInterfaceCreate=ciscoSmeInterfaceCreate, cSmeMemberInetAddrType=cSmeMemberInetAddrType, cSmeInterfaceClusterId=cSmeInterfaceClusterId, ciscoSmeMIBCompliances=ciscoSmeMIBCompliances, cSmeClusterInterfaceState=cSmeClusterInterfaceState, ciscoSmeMIBConform=ciscoSmeMIBConform, cSmeClusterMembersTable=cSmeClusterMembersTable, ciscoSmeMIBCompliance=ciscoSmeMIBCompliance, cSmeHostPortTableLastChanged=cSmeHostPortTableLastChanged, cSmeClusterState=cSmeClusterState, ciscoSmeNotifsGroup=ciscoSmeNotifsGroup, CiscoSmeClusterStatus=CiscoSmeClusterStatus, cSmeClusterMembersEntry=cSmeClusterMembersEntry, cSmeClusterMasterInetAddr=cSmeClusterMasterInetAddr, cSmeHostPortName=cSmeHostPortName, cSmeHostPortClusterId=cSmeHostPortClusterId, cSmeClusterMasterInetAddrType=cSmeClusterMasterInetAddrType, CiscoSmeInterfaceStatus=CiscoSmeInterfaceStatus, cSmeClusterMemberIfEntry=cSmeClusterMemberIfEntry, cSmeInterfaceEntry=cSmeInterfaceEntry, ciscoSmeClusterNewMaster=ciscoSmeClusterNewMaster, cSmeHostPortRowStatus=cSmeHostPortRowStatus, cSmeConfig=cSmeConfig, cSmeMemberIsMaster=cSmeMemberIsMaster, cSmeClusterMemberIfTable=cSmeClusterMemberIfTable, ciscoSmeMIBNotifs=ciscoSmeMIBNotifs, cSmeIsMemberLocal=cSmeIsMemberLocal, cSmeInterfaceIndex=cSmeInterfaceIndex, cSmeClusterRowStatus=cSmeClusterRowStatus, cSmeMemberInetAddr=cSmeMemberInetAddr, cSmeClusterName=cSmeClusterName, cSmeHostPortEntry=cSmeHostPortEntry, PYSNMP_MODULE_ID=ciscoSmeMIB, ciscoSmeMIBObjects=ciscoSmeMIBObjects, cSmeInterfaceTable=cSmeInterfaceTable, ciscoSmeNotifControlGroup=ciscoSmeNotifControlGroup, ciscoSmeConfigGroup=ciscoSmeConfigGroup, ciscoSmeMIB=ciscoSmeMIB, cSmeClusterInterfaceIndex=cSmeClusterInterfaceIndex, cSmeClusterMemberRowStatus=cSmeClusterMemberRowStatus, cSmeHostPortTable=cSmeHostPortTable, cSmeConfigTableLastChanged=cSmeConfigTableLastChanged, cSmeHostPortStorageType=cSmeHostPortStorageType, cSmeNotifyEnable=cSmeNotifyEnable, ciscoSmeInterfaceDelete=ciscoSmeInterfaceDelete)