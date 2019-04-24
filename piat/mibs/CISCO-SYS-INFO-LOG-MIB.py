#
# PySNMP MIB module CISCO-SYS-INFO-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-SYS-INFO-LOG-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:34:20 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, IpAddress, ModuleIdentity, Gauge32, Counter32, Counter64, MibIdentifier, Unsigned32, iso, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Gauge32", "Counter32", "Counter64", "MibIdentifier", "Unsigned32", "iso", "NotificationType", "TimeTicks")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
ciscoSysInfoLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 330))
ciscoSysInfoLogMIB.setRevisions(('2005-08-12 10:00', '2003-01-24 10:00',))
if mibBuilder.loadTexts: ciscoSysInfoLogMIB.setLastUpdated('200508121000Z')
if mibBuilder.loadTexts: ciscoSysInfoLogMIB.setOrganization('Cisco System, Inc.')
ciscoSysInfoLogMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 330, 0))
ciscoSysInfoLogMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 330, 1))
ciscoSysInfoLogMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 330, 2))
csilGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 1))
csilServerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2))
csilCommandConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3))
csilSysInfoLogEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csilSysInfoLogEnabled.setStatus('current')
csilSysInfoLogNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csilSysInfoLogNotifEnabled.setStatus('current')
csilMaxServerAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('servers').setMaxAccess("readwrite")
if mibBuilder.loadTexts: csilMaxServerAllowed.setStatus('current')
csilMaxProfilePerServerAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 2), Unsigned32()).setUnits('profiles').setMaxAccess("readonly")
if mibBuilder.loadTexts: csilMaxProfilePerServerAllowed.setStatus('current')
csilServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3), )
if mibBuilder.loadTexts: csilServerTable.setStatus('current')
csilServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-SYS-INFO-LOG-MIB", "csilServerIndex"))
if mibBuilder.loadTexts: csilServerEntry.setStatus('current')
csilServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: csilServerIndex.setStatus('current')
csilServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilServerAddressType.setStatus('current')
csilServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilServerAddress.setStatus('current')
csilServerProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilServerProfileIndex.setStatus('current')
csilServerProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tftp", 1), ("rcp", 2), ("ftp", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilServerProtocol.setStatus('current')
csilServerRcpUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 6), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilServerRcpUserName.setStatus('current')
csilServerInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 7), Unsigned32().clone(1440)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilServerInterval.setStatus('current')
csilServerLoggingFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 8), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilServerLoggingFileName.setStatus('current')
csilServerLastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("none", 1), ("noLogFile", 2), ("noCommand", 3), ("linkBlock", 4), ("authError", 5), ("addrError", 6), ("copying", 7), ("writeError", 8), ("success", 9), ("ftpError", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csilServerLastStatus.setStatus('current')
csilServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilServerRowStatus.setStatus('current')
csilMaxCommandPerProfile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csilMaxCommandPerProfile.setStatus('current')
csilCommandsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2), )
if mibBuilder.loadTexts: csilCommandsTable.setStatus('current')
csilCommandsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-SYS-INFO-LOG-MIB", "csilCommandProfileIndex"), (0, "CISCO-SYS-INFO-LOG-MIB", "csilCommandIndex"))
if mibBuilder.loadTexts: csilCommandsEntry.setStatus('current')
csilCommandProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: csilCommandProfileIndex.setStatus('current')
csilCommandIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: csilCommandIndex.setStatus('current')
csilCommandString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilCommandString.setStatus('current')
csilCommandExecOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilCommandExecOrder.setStatus('current')
csilCommandStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csilCommandStatus.setStatus('current')
csilLoggingFailNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 330, 0, 1)).setObjects(("CISCO-SYS-INFO-LOG-MIB", "csilServerLastStatus"))
if mibBuilder.loadTexts: csilLoggingFailNotif.setStatus('current')
ciscoSysInfoLogMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 1))
ciscoSysInfoLogMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2))
ciscoSysInfoLogMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 1, 1)).setObjects(("CISCO-SYS-INFO-LOG-MIB", "csilGlobalConfigGroup"), ("CISCO-SYS-INFO-LOG-MIB", "csilServerConfigGroup"), ("CISCO-SYS-INFO-LOG-MIB", "csilCommandConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogMIBCompliance = ciscoSysInfoLogMIBCompliance.setStatus('current')
csilGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2, 1)).setObjects(("CISCO-SYS-INFO-LOG-MIB", "csilSysInfoLogEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csilGlobalConfigGroup = csilGlobalConfigGroup.setStatus('current')
csilServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2, 2)).setObjects(("CISCO-SYS-INFO-LOG-MIB", "csilMaxServerAllowed"), ("CISCO-SYS-INFO-LOG-MIB", "csilMaxProfilePerServerAllowed"), ("CISCO-SYS-INFO-LOG-MIB", "csilServerAddress"), ("CISCO-SYS-INFO-LOG-MIB", "csilServerAddressType"), ("CISCO-SYS-INFO-LOG-MIB", "csilServerProfileIndex"), ("CISCO-SYS-INFO-LOG-MIB", "csilServerProtocol"), ("CISCO-SYS-INFO-LOG-MIB", "csilServerInterval"), ("CISCO-SYS-INFO-LOG-MIB", "csilServerLoggingFileName"), ("CISCO-SYS-INFO-LOG-MIB", "csilServerRcpUserName"), ("CISCO-SYS-INFO-LOG-MIB", "csilServerLastStatus"), ("CISCO-SYS-INFO-LOG-MIB", "csilServerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csilServerConfigGroup = csilServerConfigGroup.setStatus('current')
csilCommandConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2, 3)).setObjects(("CISCO-SYS-INFO-LOG-MIB", "csilMaxCommandPerProfile"), ("CISCO-SYS-INFO-LOG-MIB", "csilCommandString"), ("CISCO-SYS-INFO-LOG-MIB", "csilCommandExecOrder"), ("CISCO-SYS-INFO-LOG-MIB", "csilCommandStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csilCommandConfigGroup = csilCommandConfigGroup.setStatus('current')
csilNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2, 4)).setObjects(("CISCO-SYS-INFO-LOG-MIB", "csilSysInfoLogNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csilNotifControlGroup = csilNotifControlGroup.setStatus('current')
csilLoggingFailNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2, 5)).setObjects(("CISCO-SYS-INFO-LOG-MIB", "csilLoggingFailNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csilLoggingFailNotifGroup = csilLoggingFailNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYS-INFO-LOG-MIB", ciscoSysInfoLogMIBCompliance=ciscoSysInfoLogMIBCompliance, csilServerTable=csilServerTable, csilCommandIndex=csilCommandIndex, csilLoggingFailNotifGroup=csilLoggingFailNotifGroup, csilMaxCommandPerProfile=csilMaxCommandPerProfile, ciscoSysInfoLogMIBGroups=ciscoSysInfoLogMIBGroups, csilServerConfig=csilServerConfig, csilServerProfileIndex=csilServerProfileIndex, ciscoSysInfoLogMIBConform=ciscoSysInfoLogMIBConform, csilGlobalConfigGroup=csilGlobalConfigGroup, csilServerRowStatus=csilServerRowStatus, csilCommandStatus=csilCommandStatus, csilSysInfoLogEnabled=csilSysInfoLogEnabled, csilServerLoggingFileName=csilServerLoggingFileName, PYSNMP_MODULE_ID=ciscoSysInfoLogMIB, csilCommandProfileIndex=csilCommandProfileIndex, ciscoSysInfoLogMIBNotifs=ciscoSysInfoLogMIBNotifs, csilCommandConfig=csilCommandConfig, csilMaxServerAllowed=csilMaxServerAllowed, csilGlobalConfig=csilGlobalConfig, csilServerProtocol=csilServerProtocol, csilServerIndex=csilServerIndex, ciscoSysInfoLogMIBCompliances=ciscoSysInfoLogMIBCompliances, csilMaxProfilePerServerAllowed=csilMaxProfilePerServerAllowed, ciscoSysInfoLogMIB=ciscoSysInfoLogMIB, csilServerEntry=csilServerEntry, csilServerLastStatus=csilServerLastStatus, csilCommandConfigGroup=csilCommandConfigGroup, csilServerConfigGroup=csilServerConfigGroup, csilCommandExecOrder=csilCommandExecOrder, csilCommandString=csilCommandString, csilLoggingFailNotif=csilLoggingFailNotif, csilServerAddress=csilServerAddress, csilSysInfoLogNotifEnabled=csilSysInfoLogNotifEnabled, csilServerAddressType=csilServerAddressType, csilServerInterval=csilServerInterval, csilCommandsTable=csilCommandsTable, csilNotifControlGroup=csilNotifControlGroup, csilCommandsEntry=csilCommandsEntry, csilServerRcpUserName=csilServerRcpUserName, ciscoSysInfoLogMIBObjects=ciscoSysInfoLogMIBObjects)
