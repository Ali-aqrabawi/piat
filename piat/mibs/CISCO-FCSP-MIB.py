#
# PySNMP MIB module CISCO-FCSP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-FCSP-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:37:41 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameId, = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameId")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, Gauge32, TimeTicks, MibIdentifier, NotificationType, Counter32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Gauge32", "TimeTicks", "MibIdentifier", "NotificationType", "Counter32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ciscoFcspMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 391))
ciscoFcspMIB.setRevisions(('2004-07-02 00:00',))
if mibBuilder.loadTexts: ciscoFcspMIB.setLastUpdated('200407020000Z')
if mibBuilder.loadTexts: ciscoFcspMIB.setOrganization('Cisco Systems Inc. ')
ciscoFcspMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 391, 0))
ciscoFcspMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 391, 1))
ciscoFcspMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 391, 2))
cfcspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1))
cfcspInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 2))
cfcspStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3))
cfcspNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 4))
cfcspIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 1), )
if mibBuilder.loadTexts: cfcspIfTable.setStatus('current')
cfcspIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cfcspIfEntry.setStatus('current')
cfcspMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("autoPassive", 2), ("autoActive", 3), ("on", 4))).clone('autoPassive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcspMode.setStatus('current')
cfcspReauthInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcspReauthInterval.setStatus('current')
cfcspReauthenticate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("noOp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcspReauthenticate.setStatus('current')
cfcspAuthProtocols = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("dhChap", 0), ("fcCap", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcspAuthProtocols.setStatus('current')
cfcspTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(20, 1000)).clone(20)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcspTimeout.setStatus('current')
cfcspDhChapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 4))
cfcspDhChapHashList = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 4, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcspDhChapHashList.setStatus('current')
cfcspDhChapGroupList = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcspDhChapGroupList.setStatus('current')
cfcspDhChapGenericPasswd = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 4, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcspDhChapGenericPasswd.setStatus('current')
cfcspLocalPasswdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 5), )
if mibBuilder.loadTexts: cfcspLocalPasswdTable.setStatus('current')
cfcspLocalPasswdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-FCSP-MIB", "cfcspSwitchWwn"))
if mibBuilder.loadTexts: cfcspLocalPasswdEntry.setStatus('current')
cfcspSwitchWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 5, 1, 1), FcNameId())
if mibBuilder.loadTexts: cfcspSwitchWwn.setStatus('current')
cfcspLocalPasswd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 5, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcspLocalPasswd.setStatus('current')
cfcspLocalPassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcspLocalPassRowStatus.setStatus('current')
cfcspRemotePasswdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 6), )
if mibBuilder.loadTexts: cfcspRemotePasswdTable.setStatus('current')
cfcspRemotePasswdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-FCSP-MIB", "cfcspRemoteSwitchWwn"))
if mibBuilder.loadTexts: cfcspRemotePasswdEntry.setStatus('current')
cfcspRemoteSwitchWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 6, 1, 1), FcNameId())
if mibBuilder.loadTexts: cfcspRemoteSwitchWwn.setStatus('current')
cfcspRemotePasswd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 6, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcspRemotePasswd.setStatus('current')
cfcspRemotePassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 1, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcspRemotePassRowStatus.setStatus('current')
cfcspIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3, 1), )
if mibBuilder.loadTexts: cfcspIfStatsTable.setStatus('current')
cfcspIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cfcspIfStatsEntry.setStatus('current')
cfcspIfAuthSucceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcspIfAuthSucceeded.setStatus('current')
cfcspIfAuthFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcspIfAuthFailed.setStatus('current')
cfcspIfAuthByPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 391, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcspIfAuthByPassed.setStatus('current')
cfcspAuthFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 391, 0, 1)).setObjects(("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: cfcspAuthFailNotification.setStatus('current')
ciscoFcspMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 1))
ciscoFcspMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 2))
ciscoFcspMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 1, 1)).setObjects(("CISCO-FCSP-MIB", "cfcspConfigGroup"), ("CISCO-FCSP-MIB", "cfcspLocalPasswdGroup"), ("CISCO-FCSP-MIB", "cfcspIfStatsGroup"), ("CISCO-FCSP-MIB", "cfcspNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcspMIBCompliance = ciscoFcspMIBCompliance.setStatus('current')
cfcspConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 2, 1)).setObjects(("CISCO-FCSP-MIB", "cfcspMode"), ("CISCO-FCSP-MIB", "cfcspReauthInterval"), ("CISCO-FCSP-MIB", "cfcspReauthenticate"), ("CISCO-FCSP-MIB", "cfcspAuthProtocols"), ("CISCO-FCSP-MIB", "cfcspTimeout"), ("CISCO-FCSP-MIB", "cfcspDhChapHashList"), ("CISCO-FCSP-MIB", "cfcspDhChapGroupList"), ("CISCO-FCSP-MIB", "cfcspDhChapGenericPasswd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcspConfigGroup = cfcspConfigGroup.setStatus('current')
cfcspLocalPasswdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 2, 2)).setObjects(("CISCO-FCSP-MIB", "cfcspLocalPasswd"), ("CISCO-FCSP-MIB", "cfcspLocalPassRowStatus"), ("CISCO-FCSP-MIB", "cfcspRemotePasswd"), ("CISCO-FCSP-MIB", "cfcspRemotePassRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcspLocalPasswdGroup = cfcspLocalPasswdGroup.setStatus('current')
cfcspIfStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 2, 3)).setObjects(("CISCO-FCSP-MIB", "cfcspIfAuthSucceeded"), ("CISCO-FCSP-MIB", "cfcspIfAuthFailed"), ("CISCO-FCSP-MIB", "cfcspIfAuthByPassed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcspIfStatsGroup = cfcspIfStatsGroup.setStatus('current')
cfcspNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 391, 2, 2, 4)).setObjects(("CISCO-FCSP-MIB", "cfcspAuthFailNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcspNotificationGroup = cfcspNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FCSP-MIB", cfcspIfTable=cfcspIfTable, cfcspDhChapGroupList=cfcspDhChapGroupList, ciscoFcspMIBNotifications=ciscoFcspMIBNotifications, cfcspMode=cfcspMode, cfcspLocalPasswdEntry=cfcspLocalPasswdEntry, cfcspRemotePassRowStatus=cfcspRemotePassRowStatus, cfcspInfo=cfcspInfo, cfcspSwitchWwn=cfcspSwitchWwn, cfcspStatistics=cfcspStatistics, cfcspReauthInterval=cfcspReauthInterval, cfcspIfEntry=cfcspIfEntry, cfcspIfStatsTable=cfcspIfStatsTable, cfcspConfigGroup=cfcspConfigGroup, cfcspIfAuthByPassed=cfcspIfAuthByPassed, cfcspConfig=cfcspConfig, cfcspDhChapObjects=cfcspDhChapObjects, cfcspIfAuthFailed=cfcspIfAuthFailed, cfcspRemotePasswd=cfcspRemotePasswd, PYSNMP_MODULE_ID=ciscoFcspMIB, ciscoFcspMIBCompliance=ciscoFcspMIBCompliance, cfcspTimeout=cfcspTimeout, cfcspRemotePasswdTable=cfcspRemotePasswdTable, ciscoFcspMIBConformance=ciscoFcspMIBConformance, ciscoFcspMIBCompliances=ciscoFcspMIBCompliances, ciscoFcspMIBObjects=ciscoFcspMIBObjects, cfcspLocalPassRowStatus=cfcspLocalPassRowStatus, cfcspNotificationGroup=cfcspNotificationGroup, cfcspIfStatsEntry=cfcspIfStatsEntry, ciscoFcspMIB=ciscoFcspMIB, cfcspDhChapGenericPasswd=cfcspDhChapGenericPasswd, cfcspLocalPasswdTable=cfcspLocalPasswdTable, cfcspRemoteSwitchWwn=cfcspRemoteSwitchWwn, cfcspIfStatsGroup=cfcspIfStatsGroup, ciscoFcspMIBGroups=ciscoFcspMIBGroups, cfcspNotificationObjects=cfcspNotificationObjects, cfcspDhChapHashList=cfcspDhChapHashList, cfcspRemotePasswdEntry=cfcspRemotePasswdEntry, cfcspAuthFailNotification=cfcspAuthFailNotification, cfcspAuthProtocols=cfcspAuthProtocols, cfcspReauthenticate=cfcspReauthenticate, cfcspLocalPasswd=cfcspLocalPasswd, cfcspLocalPasswdGroup=cfcspLocalPasswdGroup, cfcspIfAuthSucceeded=cfcspIfAuthSucceeded)