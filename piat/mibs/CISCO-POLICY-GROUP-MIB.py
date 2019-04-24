#
# PySNMP MIB module CISCO-POLICY-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-POLICY-GROUP-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:32:38 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Integer32, NotificationType, MibIdentifier, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ModuleIdentity, iso, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "NotificationType", "MibIdentifier", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ModuleIdentity", "iso", "Gauge32", "IpAddress")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ciscoPolicyGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 507))
ciscoPolicyGroupMIB.setRevisions(('2006-01-13 16:00',))
if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setLastUpdated('200601131600Z')
if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setOrganization('Cisco Systems, Inc.')
class CpgPolicyName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CpgPolicyNameOrEmpty(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CpgGroupName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

ciscoPolicyGroupMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 0))
ciscoPolicyGroupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 1))
ciscoPolicyGroupMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 2))
cpgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1))
cpgPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2))
cpgGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1), )
if mibBuilder.loadTexts: cpgGroupTable.setStatus('current')
cpgGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1), ).setIndexNames((1, "CISCO-POLICY-GROUP-MIB", "cpgGroupName"))
if mibBuilder.loadTexts: cpgGroupEntry.setStatus('current')
cpgGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 1), CpgGroupName())
if mibBuilder.loadTexts: cpgGroupName.setStatus('current')
cpgGroupSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("accessList", 2), ("configured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgGroupSourceType.setStatus('current')
cpgGroupIpAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgGroupIpAddrCount.setStatus('current')
cpgGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgGroupRowStatus.setStatus('current')
cpgGroupIpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2), )
if mibBuilder.loadTexts: cpgGroupIpTable.setStatus('current')
cpgGroupIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpGroupName"), (0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddrType"), (0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddress"))
if mibBuilder.loadTexts: cpgGroupIpEntry.setStatus('current')
cpgGroupIpGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 1), CpgGroupName())
if mibBuilder.loadTexts: cpgGroupIpGroupName.setStatus('current')
cpgGroupIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: cpgGroupIpAddrType.setStatus('current')
cpgGroupIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 3), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cpgGroupIpAddress.setStatus('current')
cpgGroupIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 4), InetAddress().clone(hexValue="FFFFFFFF")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgGroupIpMask.setStatus('current')
cpgGroupIpSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("configured", 2), ("dot1x", 3), ("nac", 4), ("webAuth", 5), ("macAuth", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgGroupIpSourceType.setStatus('current')
cpgGroupIpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgGroupIpRowStatus.setStatus('current')
cpgPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1), )
if mibBuilder.loadTexts: cpgPolicyTable.setStatus('current')
cpgPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1), ).setIndexNames((1, "CISCO-POLICY-GROUP-MIB", "cpgPolicyName"))
if mibBuilder.loadTexts: cpgPolicyEntry.setStatus('current')
cpgPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1, 1), CpgPolicyName())
if mibBuilder.loadTexts: cpgPolicyName.setStatus('current')
cpgPolicyGroupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgPolicyGroupCount.setStatus('current')
cpgPolicyGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2), )
if mibBuilder.loadTexts: cpgPolicyGroupTable.setStatus('current')
cpgPolicyGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupPolicyName"), (1, "CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupGroupName"))
if mibBuilder.loadTexts: cpgPolicyGroupEntry.setStatus('current')
cpgPolicyGroupPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 1), CpgPolicyName())
if mibBuilder.loadTexts: cpgPolicyGroupPolicyName.setStatus('current')
cpgPolicyGroupGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 2), CpgGroupName())
if mibBuilder.loadTexts: cpgPolicyGroupGroupName.setStatus('current')
cpgPolicyGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgPolicyGroupRowStatus.setStatus('current')
ciscoPolicyGroupMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 1))
ciscoPolicyGroupMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2))
ciscoPolicyGroupMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 1, 1)).setObjects(("CISCO-POLICY-GROUP-MIB", "ciscoCpgPolicyInfoGroup"), ("CISCO-POLICY-GROUP-MIB", "ciscoCpgGroupInfoGroup"), ("CISCO-POLICY-GROUP-MIB", "ciscoCpgGroupIpInfoGroup"), ("CISCO-POLICY-GROUP-MIB", "ciscoCpgPolicyGroupInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupMIBCompliance = ciscoPolicyGroupMIBCompliance.setStatus('current')
ciscoCpgGroupInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 1)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgGroupSourceType"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddrCount"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgGroupInfoGroup = ciscoCpgGroupInfoGroup.setStatus('current')
ciscoCpgGroupIpInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 2)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgGroupIpMask"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpSourceType"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgGroupIpInfoGroup = ciscoCpgGroupIpInfoGroup.setStatus('current')
ciscoCpgPolicyInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 3)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgPolicyInfoGroup = ciscoCpgPolicyInfoGroup.setStatus('current')
ciscoCpgPolicyGroupInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 4)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgPolicyGroupInfoGroup = ciscoCpgPolicyGroupInfoGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-POLICY-GROUP-MIB", CpgPolicyNameOrEmpty=CpgPolicyNameOrEmpty, cpgPolicyGroupRowStatus=cpgPolicyGroupRowStatus, cpgPolicyEntry=cpgPolicyEntry, cpgGroupIpAddrCount=cpgGroupIpAddrCount, cpgGroupRowStatus=cpgGroupRowStatus, cpgGroupSourceType=cpgGroupSourceType, ciscoPolicyGroupMIBCompliance=ciscoPolicyGroupMIBCompliance, ciscoPolicyGroupMIBCompliances=ciscoPolicyGroupMIBCompliances, cpgPolicy=cpgPolicy, cpgGroup=cpgGroup, cpgGroupIpSourceType=cpgGroupIpSourceType, cpgPolicyGroupGroupName=cpgPolicyGroupGroupName, ciscoCpgGroupIpInfoGroup=ciscoCpgGroupIpInfoGroup, cpgPolicyGroupPolicyName=cpgPolicyGroupPolicyName, PYSNMP_MODULE_ID=ciscoPolicyGroupMIB, cpgPolicyGroupCount=cpgPolicyGroupCount, ciscoPolicyGroupMIBNotifs=ciscoPolicyGroupMIBNotifs, cpgGroupIpGroupName=cpgGroupIpGroupName, CpgGroupName=CpgGroupName, CpgPolicyName=CpgPolicyName, cpgGroupIpAddress=cpgGroupIpAddress, cpgPolicyGroupTable=cpgPolicyGroupTable, cpgGroupTable=cpgGroupTable, cpgGroupIpTable=cpgGroupIpTable, ciscoPolicyGroupMIBObjects=ciscoPolicyGroupMIBObjects, cpgGroupIpAddrType=cpgGroupIpAddrType, cpgPolicyTable=cpgPolicyTable, ciscoPolicyGroupMIB=ciscoPolicyGroupMIB, cpgPolicyName=cpgPolicyName, cpgGroupName=cpgGroupName, cpgGroupEntry=cpgGroupEntry, cpgGroupIpMask=cpgGroupIpMask, ciscoPolicyGroupMIBGroups=ciscoPolicyGroupMIBGroups, ciscoCpgGroupInfoGroup=ciscoCpgGroupInfoGroup, cpgPolicyGroupEntry=cpgPolicyGroupEntry, cpgGroupIpEntry=cpgGroupIpEntry, ciscoPolicyGroupMIBConformance=ciscoPolicyGroupMIBConformance, ciscoCpgPolicyGroupInfoGroup=ciscoCpgPolicyGroupInfoGroup, cpgGroupIpRowStatus=cpgGroupIpRowStatus, ciscoCpgPolicyInfoGroup=ciscoCpgPolicyInfoGroup)
