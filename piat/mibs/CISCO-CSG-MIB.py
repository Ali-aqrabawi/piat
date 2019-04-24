#
# PySNMP MIB module CISCO-CSG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-CSG-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:37:21 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetPortNumber, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, ObjectIdentity, Counter32, Counter64, iso, MibIdentifier, TimeTicks, Unsigned32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "ObjectIdentity", "Counter32", "Counter64", "iso", "MibIdentifier", "TimeTicks", "Unsigned32", "ModuleIdentity", "NotificationType")
TruthValue, TimeInterval, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeInterval", "DisplayString", "RowStatus", "TextualConvention")
ciscoCsgMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 331))
ciscoCsgMIB.setRevisions(('2003-02-20 00:00',))
if mibBuilder.loadTexts: ciscoCsgMIB.setLastUpdated('200302200000Z')
if mibBuilder.loadTexts: ciscoCsgMIB.setOrganization('Cisco Systems, Inc.')
ciscoCsgMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 0))
ciscoCsgMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 1))
ciscoCsgMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 2))
csgScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 1))
csgUserStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2))
csgUserDataBaseStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3))
csgAgentStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4))
csgQuotaMgrStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5))
csgNotifsEnable = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 6))
class CsgSlotNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class CsgEntityName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 15)

class CsgServerPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1000)

class CsgUserTableUpperBound(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 10000000)

csgAgentLostRecordTimer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 1, 1), TimeInterval().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csgAgentLostRecordTimer.setStatus('current')
csgQuotaMgrLostRecordTimer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 1, 2), TimeInterval().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csgQuotaMgrLostRecordTimer.setStatus('current')
csgUserTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1), )
if mibBuilder.loadTexts: csgUserTable.setStatus('current')
csgUserTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-CSG-MIB", "csgUserCardId"), (0, "CISCO-CSG-MIB", "csgUserGroupName"))
if mibBuilder.loadTexts: csgUserTableEntry.setStatus('current')
csgUserCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 1), CsgSlotNumber())
if mibBuilder.loadTexts: csgUserCardId.setStatus('current')
csgUserGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 2), CsgEntityName())
if mibBuilder.loadTexts: csgUserGroupName.setStatus('current')
csgUserMaxEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 3), CsgUserTableUpperBound()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgUserMaxEntries.setStatus('current')
csgUserCurrEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgUserCurrEntries.setStatus('current')
csgUserHighWater = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 5), CsgUserTableUpperBound()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgUserHighWater.setStatus('current')
csgUserLRUSteals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgUserLRUSteals.setStatus('current')
csgUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgUserRowStatus.setStatus('current')
csgUserDbTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1), )
if mibBuilder.loadTexts: csgUserDbTable.setStatus('current')
csgUserDbTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-CSG-MIB", "csgUserCardId"), (0, "CISCO-CSG-MIB", "csgUserGroupName"), (0, "CISCO-CSG-MIB", "csgUserDbIpAddrType"), (0, "CISCO-CSG-MIB", "csgUserDbIpAddr"), (0, "CISCO-CSG-MIB", "csgUserDbPort"))
if mibBuilder.loadTexts: csgUserDbTableEntry.setStatus('current')
csgUserDbIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: csgUserDbIpAddrType.setStatus('current')
csgUserDbIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: csgUserDbIpAddr.setStatus('current')
csgUserDbPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: csgUserDbPort.setStatus('current')
csgUserDbState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("reset", 1), ("active", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgUserDbState.setStatus('current')
csgUserDbRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgUserDbRequests.setStatus('current')
csgUserDbUidsReturned = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgUserDbUidsReturned.setStatus('current')
csgUserDbReqResent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgUserDbReqResent.setStatus('current')
csgUserDbReqTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgUserDbReqTimeouts.setStatus('current')
csgUserDbReqErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgUserDbReqErrors.setStatus('current')
csgUserDbRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 3, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgUserDbRowStatus.setStatus('current')
csgAgentTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1), )
if mibBuilder.loadTexts: csgAgentTable.setStatus('current')
csgAgentTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-CSG-MIB", "csgUserCardId"), (0, "CISCO-CSG-MIB", "csgAgentIpAddrType"), (0, "CISCO-CSG-MIB", "csgAgentIpAddr"), (0, "CISCO-CSG-MIB", "csgAgentPort"))
if mibBuilder.loadTexts: csgAgentTableEntry.setStatus('current')
csgAgentIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: csgAgentIpAddrType.setStatus('current')
csgAgentIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: csgAgentIpAddr.setStatus('current')
csgAgentPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: csgAgentPort.setStatus('current')
csgAgentAcctName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 4), CsgEntityName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgAgentAcctName.setStatus('current')
csgAgentPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 5), CsgServerPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgAgentPriority.setStatus('current')
csgAgentState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("standby", 1), ("failed", 2), ("active", 3), ("echowait", 4), ("nawait", 5), ("suspended", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgAgentState.setStatus('current')
csgAgentLostRecords = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgAgentLostRecords.setStatus('current')
csgAgentTotalSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgAgentTotalSent.setStatus('current')
csgAgentFailAck = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgAgentFailAck.setStatus('current')
csgAgentOutstanding = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgAgentOutstanding.setStatus('current')
csgAgentHighWater = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgAgentHighWater.setStatus('current')
csgAgentBadRecord = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgAgentBadRecord.setStatus('current')
csgAgentRetransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgAgentRetransmit.setStatus('current')
csgAgentRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 4, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgAgentRowStatus.setStatus('current')
csgQuotaMgrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1), )
if mibBuilder.loadTexts: csgQuotaMgrTable.setStatus('current')
csgQuotaMgrTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1), ).setIndexNames((0, "CISCO-CSG-MIB", "csgUserCardId"), (0, "CISCO-CSG-MIB", "csgQuotaMgrIpAddrType"), (0, "CISCO-CSG-MIB", "csgQuotaMgrIpAddr"), (0, "CISCO-CSG-MIB", "csgQuotaMgrPort"))
if mibBuilder.loadTexts: csgQuotaMgrTableEntry.setStatus('current')
csgQuotaMgrIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: csgQuotaMgrIpAddrType.setStatus('current')
csgQuotaMgrIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: csgQuotaMgrIpAddr.setStatus('current')
csgQuotaMgrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: csgQuotaMgrPort.setStatus('current')
csgQuotaMgrUserGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 4), CsgEntityName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgQuotaMgrUserGroupName.setStatus('current')
csgQuotaMgrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 5), CsgServerPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgQuotaMgrPriority.setStatus('current')
csgQuotaMgrState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("standby", 1), ("failed", 2), ("active", 3), ("echowait", 4), ("nawait", 5), ("suspended", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgQuotaMgrState.setStatus('current')
csgQuotaMgrLostRecords = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgQuotaMgrLostRecords.setStatus('current')
csgQuotaMgrTotalSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgQuotaMgrTotalSent.setStatus('current')
csgQuotaMgrFailAck = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgQuotaMgrFailAck.setStatus('current')
csgQuotaMgrOutstanding = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgQuotaMgrOutstanding.setStatus('current')
csgQuotaMgrHighWater = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgQuotaMgrHighWater.setStatus('current')
csgQuotaMgrBadRecord = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgQuotaMgrBadRecord.setStatus('current')
csgQuotaMgrRetransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csgQuotaMgrRetransmit.setStatus('current')
csgQuotaMgrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 5, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csgQuotaMgrRowStatus.setStatus('current')
csgAgentNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 6, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csgAgentNotifsEnabled.setStatus('current')
csgQuotaNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 6, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csgQuotaNotifsEnabled.setStatus('current')
csgDatabaseNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 331, 1, 6, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csgDatabaseNotifsEnabled.setStatus('current')
ciscoCsgAgentStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 331, 0, 1)).setObjects(("CISCO-CSG-MIB", "csgAgentState"), ("CISCO-CSG-MIB", "csgAgentLostRecords"), ("CISCO-CSG-MIB", "csgAgentTotalSent"), ("CISCO-CSG-MIB", "csgAgentFailAck"), ("CISCO-CSG-MIB", "csgAgentOutstanding"), ("CISCO-CSG-MIB", "csgAgentHighWater"), ("CISCO-CSG-MIB", "csgAgentBadRecord"), ("CISCO-CSG-MIB", "csgAgentRetransmit"))
if mibBuilder.loadTexts: ciscoCsgAgentStateChange.setStatus('current')
ciscoCsgQuotaMgrStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 331, 0, 2)).setObjects(("CISCO-CSG-MIB", "csgQuotaMgrState"), ("CISCO-CSG-MIB", "csgQuotaMgrLostRecords"), ("CISCO-CSG-MIB", "csgQuotaMgrTotalSent"), ("CISCO-CSG-MIB", "csgQuotaMgrFailAck"), ("CISCO-CSG-MIB", "csgQuotaMgrOutstanding"), ("CISCO-CSG-MIB", "csgQuotaMgrHighWater"), ("CISCO-CSG-MIB", "csgQuotaMgrBadRecord"), ("CISCO-CSG-MIB", "csgQuotaMgrRetransmit"))
if mibBuilder.loadTexts: ciscoCsgQuotaMgrStateChange.setStatus('current')
ciscoCsgUserDbStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 331, 0, 3)).setObjects(("CISCO-CSG-MIB", "csgUserDbState"), ("CISCO-CSG-MIB", "csgUserDbRequests"), ("CISCO-CSG-MIB", "csgUserDbUidsReturned"), ("CISCO-CSG-MIB", "csgUserDbReqResent"), ("CISCO-CSG-MIB", "csgUserDbReqTimeouts"), ("CISCO-CSG-MIB", "csgUserDbReqErrors"))
if mibBuilder.loadTexts: ciscoCsgUserDbStateChange.setStatus('current')
ciscoCsgAgentLostRecordEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 331, 0, 4)).setObjects(("CISCO-CSG-MIB", "csgAgentState"), ("CISCO-CSG-MIB", "csgAgentLostRecords"), ("CISCO-CSG-MIB", "csgAgentTotalSent"), ("CISCO-CSG-MIB", "csgAgentFailAck"), ("CISCO-CSG-MIB", "csgAgentOutstanding"), ("CISCO-CSG-MIB", "csgAgentHighWater"), ("CISCO-CSG-MIB", "csgAgentBadRecord"), ("CISCO-CSG-MIB", "csgAgentRetransmit"))
if mibBuilder.loadTexts: ciscoCsgAgentLostRecordEvent.setStatus('current')
ciscoCsgQuotaMgrLostRecordEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 331, 0, 5)).setObjects(("CISCO-CSG-MIB", "csgQuotaMgrState"), ("CISCO-CSG-MIB", "csgQuotaMgrLostRecords"), ("CISCO-CSG-MIB", "csgQuotaMgrTotalSent"), ("CISCO-CSG-MIB", "csgQuotaMgrFailAck"), ("CISCO-CSG-MIB", "csgQuotaMgrOutstanding"), ("CISCO-CSG-MIB", "csgQuotaMgrHighWater"), ("CISCO-CSG-MIB", "csgQuotaMgrBadRecord"), ("CISCO-CSG-MIB", "csgQuotaMgrRetransmit"))
if mibBuilder.loadTexts: ciscoCsgQuotaMgrLostRecordEvent.setStatus('current')
ciscoCsgMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 1))
ciscoCsgMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2))
ciscoCsgMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 1, 1)).setObjects(("CISCO-CSG-MIB", "ciscoUserGroup"), ("CISCO-CSG-MIB", "ciscoAgentGroup"), ("CISCO-CSG-MIB", "ciscoQuotaMgrGroup"), ("CISCO-CSG-MIB", "ciscoUserDbGroup"), ("CISCO-CSG-MIB", "ciscoCsgNotifEnableGroup"), ("CISCO-CSG-MIB", "ciscoCsgNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCsgMIBCompliance = ciscoCsgMIBCompliance.setStatus('current')
ciscoUserGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 1)).setObjects(("CISCO-CSG-MIB", "csgUserMaxEntries"), ("CISCO-CSG-MIB", "csgUserCurrEntries"), ("CISCO-CSG-MIB", "csgUserHighWater"), ("CISCO-CSG-MIB", "csgUserLRUSteals"), ("CISCO-CSG-MIB", "csgUserRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUserGroup = ciscoUserGroup.setStatus('current')
ciscoUserDbGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 2)).setObjects(("CISCO-CSG-MIB", "csgUserDbState"), ("CISCO-CSG-MIB", "csgUserDbRequests"), ("CISCO-CSG-MIB", "csgUserDbUidsReturned"), ("CISCO-CSG-MIB", "csgUserDbReqResent"), ("CISCO-CSG-MIB", "csgUserDbReqTimeouts"), ("CISCO-CSG-MIB", "csgUserDbReqErrors"), ("CISCO-CSG-MIB", "csgUserDbRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUserDbGroup = ciscoUserDbGroup.setStatus('current')
ciscoAgentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 3)).setObjects(("CISCO-CSG-MIB", "csgAgentAcctName"), ("CISCO-CSG-MIB", "csgAgentPriority"), ("CISCO-CSG-MIB", "csgAgentState"), ("CISCO-CSG-MIB", "csgAgentLostRecords"), ("CISCO-CSG-MIB", "csgAgentTotalSent"), ("CISCO-CSG-MIB", "csgAgentFailAck"), ("CISCO-CSG-MIB", "csgAgentOutstanding"), ("CISCO-CSG-MIB", "csgAgentHighWater"), ("CISCO-CSG-MIB", "csgAgentBadRecord"), ("CISCO-CSG-MIB", "csgAgentRetransmit"), ("CISCO-CSG-MIB", "csgAgentLostRecordTimer"), ("CISCO-CSG-MIB", "csgAgentRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAgentGroup = ciscoAgentGroup.setStatus('current')
ciscoQuotaMgrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 4)).setObjects(("CISCO-CSG-MIB", "csgQuotaMgrUserGroupName"), ("CISCO-CSG-MIB", "csgQuotaMgrPriority"), ("CISCO-CSG-MIB", "csgQuotaMgrState"), ("CISCO-CSG-MIB", "csgQuotaMgrLostRecords"), ("CISCO-CSG-MIB", "csgQuotaMgrTotalSent"), ("CISCO-CSG-MIB", "csgQuotaMgrFailAck"), ("CISCO-CSG-MIB", "csgQuotaMgrOutstanding"), ("CISCO-CSG-MIB", "csgQuotaMgrHighWater"), ("CISCO-CSG-MIB", "csgQuotaMgrBadRecord"), ("CISCO-CSG-MIB", "csgQuotaMgrRetransmit"), ("CISCO-CSG-MIB", "csgQuotaMgrLostRecordTimer"), ("CISCO-CSG-MIB", "csgQuotaMgrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQuotaMgrGroup = ciscoQuotaMgrGroup.setStatus('current')
ciscoCsgNotifEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 5)).setObjects(("CISCO-CSG-MIB", "csgAgentNotifsEnabled"), ("CISCO-CSG-MIB", "csgQuotaNotifsEnabled"), ("CISCO-CSG-MIB", "csgDatabaseNotifsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCsgNotifEnableGroup = ciscoCsgNotifEnableGroup.setStatus('current')
ciscoCsgNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 331, 2, 2, 6)).setObjects(("CISCO-CSG-MIB", "ciscoCsgAgentStateChange"), ("CISCO-CSG-MIB", "ciscoCsgQuotaMgrStateChange"), ("CISCO-CSG-MIB", "ciscoCsgUserDbStateChange"), ("CISCO-CSG-MIB", "ciscoCsgAgentLostRecordEvent"), ("CISCO-CSG-MIB", "ciscoCsgQuotaMgrLostRecordEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCsgNotifGroup = ciscoCsgNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CSG-MIB", csgUserCurrEntries=csgUserCurrEntries, csgUserDbUidsReturned=csgUserDbUidsReturned, csgQuotaMgrTable=csgQuotaMgrTable, csgQuotaMgrLostRecordTimer=csgQuotaMgrLostRecordTimer, csgUserCardId=csgUserCardId, csgAgentIpAddr=csgAgentIpAddr, csgUserGroupName=csgUserGroupName, ciscoUserDbGroup=ciscoUserDbGroup, ciscoCsgMIBConform=ciscoCsgMIBConform, csgUserDbPort=csgUserDbPort, ciscoCsgQuotaMgrLostRecordEvent=ciscoCsgQuotaMgrLostRecordEvent, ciscoUserGroup=ciscoUserGroup, csgAgentLostRecordTimer=csgAgentLostRecordTimer, csgQuotaMgrTotalSent=csgQuotaMgrTotalSent, csgQuotaMgrPriority=csgQuotaMgrPriority, csgUserTable=csgUserTable, csgUserTableEntry=csgUserTableEntry, csgQuotaMgrLostRecords=csgQuotaMgrLostRecords, csgQuotaMgrRowStatus=csgQuotaMgrRowStatus, ciscoAgentGroup=ciscoAgentGroup, csgUserDbReqErrors=csgUserDbReqErrors, csgScalars=csgScalars, csgQuotaMgrUserGroupName=csgQuotaMgrUserGroupName, ciscoCsgMIBNotifs=ciscoCsgMIBNotifs, csgAgentPriority=csgAgentPriority, csgAgentHighWater=csgAgentHighWater, csgQuotaMgrRetransmit=csgQuotaMgrRetransmit, csgQuotaMgrOutstanding=csgQuotaMgrOutstanding, csgQuotaMgrHighWater=csgQuotaMgrHighWater, csgAgentTableEntry=csgAgentTableEntry, csgUserDbReqTimeouts=csgUserDbReqTimeouts, csgQuotaMgrBadRecord=csgQuotaMgrBadRecord, csgUserMaxEntries=csgUserMaxEntries, csgAgentPort=csgAgentPort, csgUserHighWater=csgUserHighWater, csgQuotaMgrPort=csgQuotaMgrPort, CsgUserTableUpperBound=CsgUserTableUpperBound, ciscoCsgUserDbStateChange=ciscoCsgUserDbStateChange, ciscoCsgNotifGroup=ciscoCsgNotifGroup, csgQuotaMgrState=csgQuotaMgrState, ciscoCsgMIBObjects=ciscoCsgMIBObjects, csgUserDataBaseStats=csgUserDataBaseStats, csgUserDbRequests=csgUserDbRequests, csgAgentAcctName=csgAgentAcctName, ciscoCsgMIBCompliances=ciscoCsgMIBCompliances, csgAgentState=csgAgentState, csgNotifsEnable=csgNotifsEnable, csgUserDbState=csgUserDbState, ciscoCsgAgentLostRecordEvent=ciscoCsgAgentLostRecordEvent, csgUserStats=csgUserStats, csgUserLRUSteals=csgUserLRUSteals, ciscoCsgMIBCompliance=ciscoCsgMIBCompliance, CsgServerPriority=CsgServerPriority, ciscoCsgAgentStateChange=ciscoCsgAgentStateChange, csgAgentBadRecord=csgAgentBadRecord, ciscoCsgQuotaMgrStateChange=ciscoCsgQuotaMgrStateChange, csgUserDbTableEntry=csgUserDbTableEntry, csgQuotaNotifsEnabled=csgQuotaNotifsEnabled, csgUserDbIpAddrType=csgUserDbIpAddrType, csgAgentStats=csgAgentStats, csgAgentNotifsEnabled=csgAgentNotifsEnabled, csgQuotaMgrFailAck=csgQuotaMgrFailAck, csgAgentTotalSent=csgAgentTotalSent, CsgSlotNumber=CsgSlotNumber, ciscoCsgMIBGroups=ciscoCsgMIBGroups, csgUserDbTable=csgUserDbTable, ciscoQuotaMgrGroup=ciscoQuotaMgrGroup, ciscoCsgMIB=ciscoCsgMIB, CsgEntityName=CsgEntityName, csgDatabaseNotifsEnabled=csgDatabaseNotifsEnabled, csgAgentLostRecords=csgAgentLostRecords, csgAgentIpAddrType=csgAgentIpAddrType, csgAgentFailAck=csgAgentFailAck, csgAgentRetransmit=csgAgentRetransmit, csgQuotaMgrIpAddr=csgQuotaMgrIpAddr, csgAgentTable=csgAgentTable, csgQuotaMgrTableEntry=csgQuotaMgrTableEntry, csgUserRowStatus=csgUserRowStatus, csgQuotaMgrIpAddrType=csgQuotaMgrIpAddrType, csgUserDbRowStatus=csgUserDbRowStatus, PYSNMP_MODULE_ID=ciscoCsgMIB, csgUserDbIpAddr=csgUserDbIpAddr, ciscoCsgNotifEnableGroup=ciscoCsgNotifEnableGroup, csgAgentOutstanding=csgAgentOutstanding, csgUserDbReqResent=csgUserDbReqResent, csgQuotaMgrStats=csgQuotaMgrStats, csgAgentRowStatus=csgAgentRowStatus)