#
# PySNMP MIB module CISCO-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:32:28 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, NotificationType, Gauge32, ObjectIdentity, Counter64, TimeTicks, IpAddress, ModuleIdentity, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "NotificationType", "Gauge32", "ObjectIdentity", "Counter64", "TimeTicks", "IpAddress", "ModuleIdentity", "Integer32", "Bits")
RowStatus, TimeStamp, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp", "TextualConvention", "DisplayString", "TruthValue")
ciscoSyslogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 41))
ciscoSyslogMIB.setRevisions(('2005-12-03 00:00', '2005-08-11 00:00', '2005-06-01 00:00', '1995-08-07 00:00',))
if mibBuilder.loadTexts: ciscoSyslogMIB.setLastUpdated('200512030000Z')
if mibBuilder.loadTexts: ciscoSyslogMIB.setOrganization('Cisco Systems, Inc.')
ciscoSyslogMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 41, 1))
clogBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1))
clogHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2))
clogServer = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3))
class SyslogSeverity(TextualConvention, Integer32):
    reference = 'RFC 3164, Section 4.1 - syslog Message Parts'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))

clogNotificationsSent = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 1), Counter32()).setUnits('notifications').setMaxAccess("readonly")
if mibBuilder.loadTexts: clogNotificationsSent.setStatus('current')
clogNotificationsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clogNotificationsEnabled.setStatus('current')
clogMaxSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 3), SyslogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clogMaxSeverity.setStatus('current')
clogMsgIgnores = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 4), Counter32()).setUnits('messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: clogMsgIgnores.setStatus('current')
clogMsgDrops = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 5), Counter32()).setUnits('messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: clogMsgDrops.setStatus('current')
clogOriginIDType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("other", 2), ("hostName", 3), ("ipv4Address", 4), ("contextName", 5), ("userDefined", 6))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clogOriginIDType.setStatus('current')
clogOriginID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 7), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clogOriginID.setStatus('current')
clogHistTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 500)).clone(1)).setUnits('entries').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clogHistTableMaxLength.setStatus('current')
clogHistMsgsFlushed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 2), Counter32()).setUnits('messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: clogHistMsgsFlushed.setStatus('current')
clogHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3), )
if mibBuilder.loadTexts: clogHistoryTable.setStatus('current')
clogHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-SYSLOG-MIB", "clogHistIndex"))
if mibBuilder.loadTexts: clogHistoryEntry.setStatus('current')
clogHistIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: clogHistIndex.setStatus('current')
clogHistFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clogHistFacility.setStatus('current')
clogHistSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 3), SyslogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clogHistSeverity.setStatus('current')
clogHistMsgName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clogHistMsgName.setStatus('current')
clogHistMsgText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clogHistMsgText.setStatus('current')
clogHistTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clogHistTimestamp.setStatus('current')
clogMaxServers = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clogMaxServers.setStatus('current')
clogServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 2), )
if mibBuilder.loadTexts: clogServerConfigTable.setStatus('current')
clogServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-SYSLOG-MIB", "clogServerAddrType"), (0, "CISCO-SYSLOG-MIB", "clogServerAddr"))
if mibBuilder.loadTexts: clogServerConfigEntry.setStatus('current')
clogServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: clogServerAddrType.setStatus('current')
clogServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 2, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: clogServerAddr.setStatus('current')
clogServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clogServerStatus.setStatus('current')
ciscoSyslogMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 41, 2))
ciscoSyslogMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 41, 2, 0))
clogMessageGenerated = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 41, 2, 0, 1)).setObjects(("CISCO-SYSLOG-MIB", "clogHistFacility"), ("CISCO-SYSLOG-MIB", "clogHistSeverity"), ("CISCO-SYSLOG-MIB", "clogHistMsgName"), ("CISCO-SYSLOG-MIB", "clogHistMsgText"), ("CISCO-SYSLOG-MIB", "clogHistTimestamp"))
if mibBuilder.loadTexts: clogMessageGenerated.setStatus('current')
ciscoSyslogMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 41, 3))
ciscoSyslogMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 1))
ciscoSyslogMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 2))
ciscoSyslogMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 1, 1)).setObjects(("CISCO-SYSLOG-MIB", "ciscoSyslogMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogMIBCompliance = ciscoSyslogMIBCompliance.setStatus('deprecated')
ciscoSyslogMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 1, 2)).setObjects(("CISCO-SYSLOG-MIB", "ciscoSyslogMIBGroup"), ("CISCO-SYSLOG-MIB", "clogServerGroup"), ("CISCO-SYSLOG-MIB", "clogOriginIDGroup"), ("CISCO-SYSLOG-MIB", "clogNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogMIBComplianceRev1 = ciscoSyslogMIBComplianceRev1.setStatus('current')
ciscoSyslogMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 2, 1)).setObjects(("CISCO-SYSLOG-MIB", "clogNotificationsSent"), ("CISCO-SYSLOG-MIB", "clogNotificationsEnabled"), ("CISCO-SYSLOG-MIB", "clogMaxSeverity"), ("CISCO-SYSLOG-MIB", "clogMsgIgnores"), ("CISCO-SYSLOG-MIB", "clogMsgDrops"), ("CISCO-SYSLOG-MIB", "clogHistTableMaxLength"), ("CISCO-SYSLOG-MIB", "clogHistMsgsFlushed"), ("CISCO-SYSLOG-MIB", "clogHistFacility"), ("CISCO-SYSLOG-MIB", "clogHistSeverity"), ("CISCO-SYSLOG-MIB", "clogHistMsgName"), ("CISCO-SYSLOG-MIB", "clogHistMsgText"), ("CISCO-SYSLOG-MIB", "clogHistTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogMIBGroup = ciscoSyslogMIBGroup.setStatus('current')
clogNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 2, 2)).setObjects(("CISCO-SYSLOG-MIB", "clogMessageGenerated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clogNotificationsGroup = clogNotificationsGroup.setStatus('current')
clogServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 2, 3)).setObjects(("CISCO-SYSLOG-MIB", "clogMaxServers"), ("CISCO-SYSLOG-MIB", "clogServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clogServerGroup = clogServerGroup.setStatus('current')
clogOriginIDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 2, 4)).setObjects(("CISCO-SYSLOG-MIB", "clogOriginIDType"), ("CISCO-SYSLOG-MIB", "clogOriginID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clogOriginIDGroup = clogOriginIDGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSLOG-MIB", clogNotificationsGroup=clogNotificationsGroup, clogMsgIgnores=clogMsgIgnores, ciscoSyslogMIBConformance=ciscoSyslogMIBConformance, clogMessageGenerated=clogMessageGenerated, clogBasic=clogBasic, clogHistory=clogHistory, clogHistSeverity=clogHistSeverity, clogMsgDrops=clogMsgDrops, ciscoSyslogMIB=ciscoSyslogMIB, clogHistFacility=clogHistFacility, clogMaxServers=clogMaxServers, ciscoSyslogMIBComplianceRev1=ciscoSyslogMIBComplianceRev1, clogHistTableMaxLength=clogHistTableMaxLength, ciscoSyslogMIBGroup=ciscoSyslogMIBGroup, clogServerGroup=clogServerGroup, clogNotificationsSent=clogNotificationsSent, ciscoSyslogMIBObjects=ciscoSyslogMIBObjects, clogServer=clogServer, clogServerAddrType=clogServerAddrType, clogHistMsgName=clogHistMsgName, clogHistMsgText=clogHistMsgText, ciscoSyslogMIBNotificationPrefix=ciscoSyslogMIBNotificationPrefix, clogHistTimestamp=clogHistTimestamp, clogMaxSeverity=clogMaxSeverity, clogServerStatus=clogServerStatus, clogOriginID=clogOriginID, clogHistoryEntry=clogHistoryEntry, clogNotificationsEnabled=clogNotificationsEnabled, clogHistIndex=clogHistIndex, clogHistoryTable=clogHistoryTable, clogServerConfigTable=clogServerConfigTable, clogServerAddr=clogServerAddr, SyslogSeverity=SyslogSeverity, clogServerConfigEntry=clogServerConfigEntry, ciscoSyslogMIBCompliances=ciscoSyslogMIBCompliances, ciscoSyslogMIBCompliance=ciscoSyslogMIBCompliance, clogOriginIDType=clogOriginIDType, ciscoSyslogMIBNotifications=ciscoSyslogMIBNotifications, clogHistMsgsFlushed=clogHistMsgsFlushed, clogOriginIDGroup=clogOriginIDGroup, ciscoSyslogMIBGroups=ciscoSyslogMIBGroups, PYSNMP_MODULE_ID=ciscoSyslogMIB)