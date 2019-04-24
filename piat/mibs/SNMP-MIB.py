#
# PySNMP MIB module SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/SNMP-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:21:39 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ntEnterpriseDataTasmanMgmt, = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Counter64, ObjectIdentity, Gauge32, Bits, NotificationType, IpAddress, ModuleIdentity, TimeTicks, MibIdentifier, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Counter64", "ObjectIdentity", "Gauge32", "Bits", "NotificationType", "IpAddress", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nnsnmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5))
nnsnmpMib.setRevisions(('1999-04-23 00:00',))
if mibBuilder.loadTexts: nnsnmpMib.setLastUpdated('9904230000Z')
if mibBuilder.loadTexts: nnsnmpMib.setOrganization('Nortel Networks')
nnsnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1))
nnsnmpAgentType = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("snmpV1", 2), ("snmpV2V1", 3), ("snmpV2cV1", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnsnmpAgentType.setStatus('current')
nnsnmpRmonSupported = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("not-supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnsnmpRmonSupported.setStatus('current')
nnsnmpSourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nnsnmpSourceAddress.setStatus('current')
nnsnmpTrapRcvrTable = MibTable((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4), )
if mibBuilder.loadTexts: nnsnmpTrapRcvrTable.setStatus('current')
nnsnmpTrapRcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4, 1), ).setIndexNames((0, "SNMP-MIB", "nnsnmpTrapRcvrIndex"))
if mibBuilder.loadTexts: nnsnmpTrapRcvrEntry.setStatus('current')
nnsnmpTrapRcvrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnsnmpTrapRcvrIndex.setStatus('current')
nnsnmpTrapRcvrEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nnsnmpTrapRcvrEntryStatus.setStatus('current')
nnsnmpTrapRcvrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nnsnmpTrapRcvrAddress.setStatus('current')
nnsnmpTrapRcvrCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nnsnmpTrapRcvrCommunity.setStatus('current')
mibBuilder.exportSymbols("SNMP-MIB", nnsnmpSourceAddress=nnsnmpSourceAddress, nnsnmpAgentType=nnsnmpAgentType, nnsnmpTrapRcvrTable=nnsnmpTrapRcvrTable, nnsnmpMib=nnsnmpMib, nnsnmpTrapRcvrEntry=nnsnmpTrapRcvrEntry, nnsnmpTrapRcvrAddress=nnsnmpTrapRcvrAddress, nnsnmpObjects=nnsnmpObjects, nnsnmpTrapRcvrEntryStatus=nnsnmpTrapRcvrEntryStatus, nnsnmpTrapRcvrIndex=nnsnmpTrapRcvrIndex, nnsnmpTrapRcvrCommunity=nnsnmpTrapRcvrCommunity, PYSNMP_MODULE_ID=nnsnmpMib, nnsnmpRmonSupported=nnsnmpRmonSupported)
