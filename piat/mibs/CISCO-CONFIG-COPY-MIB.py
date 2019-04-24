#
# PySNMP MIB module CISCO-CONFIG-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-CONFIG-COPY-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:37:09 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameIdOrZero, = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameIdOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, Counter32, NotificationType, IpAddress, Unsigned32, Gauge32, Bits, ModuleIdentity, iso, MibIdentifier, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter32", "NotificationType", "IpAddress", "Unsigned32", "Gauge32", "Bits", "ModuleIdentity", "iso", "MibIdentifier", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TimeStamp, TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
ciscoConfigCopyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 96))
ciscoConfigCopyMIB.setRevisions(('2009-02-27 00:00', '2005-04-06 00:00', '2004-03-17 00:00', '2002-12-17 00:00', '2002-05-30 00:00', '2002-05-07 00:00', '2002-03-28 00:00',))
if mibBuilder.loadTexts: ciscoConfigCopyMIB.setLastUpdated('200902270000Z')
if mibBuilder.loadTexts: ciscoConfigCopyMIB.setOrganization('Cisco Systems, Inc.')
class ConfigCopyProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("tftp", 1), ("ftp", 2), ("rcp", 3), ("scp", 4), ("sftp", 5))

class ConfigCopyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("waiting", 1), ("running", 2), ("successful", 3), ("failed", 4))

class ConfigCopyFailCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 1), ("badFileName", 2), ("timeout", 3), ("noMem", 4), ("noConfig", 5), ("unsupportedProtocol", 6), ("someConfigApplyFailed", 7), ("systemNotReady", 8), ("requestAborted", 9))

class ConfigFileType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("networkFile", 1), ("iosFile", 2), ("startupConfig", 3), ("runningConfig", 4), ("terminal", 5), ("fabricStartupConfig", 6))

ciscoConfigCopyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 1))
ccCopy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1))
ccCopyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1), )
if mibBuilder.loadTexts: ccCopyTable.setStatus('current')
ccCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-CONFIG-COPY-MIB", "ccCopyIndex"))
if mibBuilder.loadTexts: ccCopyEntry.setStatus('current')
ccCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ccCopyIndex.setStatus('current')
ccCopyProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 2), ConfigCopyProtocol().clone('tftp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyProtocol.setStatus('current')
ccCopySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 3), ConfigFileType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopySourceFileType.setStatus('current')
ccCopyDestFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 4), ConfigFileType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyDestFileType.setStatus('current')
ccCopyServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyServerAddress.setStatus('deprecated')
ccCopyFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyFileName.setStatus('current')
ccCopyUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyUserName.setStatus('current')
ccCopyUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyUserPassword.setStatus('current')
ccCopyNotificationOnCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyNotificationOnCompletion.setStatus('current')
ccCopyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 10), ConfigCopyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyState.setStatus('current')
ccCopyTimeStarted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyTimeStarted.setStatus('current')
ccCopyTimeCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyTimeCompleted.setStatus('current')
ccCopyFailCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 13), ConfigCopyFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyFailCause.setStatus('current')
ccCopyEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyEntryRowStatus.setStatus('current')
ccCopyServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 15), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyServerAddressType.setStatus('current')
ccCopyServerAddressRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 16), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyServerAddressRev1.setStatus('current')
ccCopyVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyVrfName.setStatus('current')
ccCopyErrorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2), )
if mibBuilder.loadTexts: ccCopyErrorTable.setStatus('current')
ccCopyErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-CONFIG-COPY-MIB", "ccCopyIndex"), (0, "CISCO-CONFIG-COPY-MIB", "ccCopyErrorIndex"))
if mibBuilder.loadTexts: ccCopyErrorEntry.setStatus('current')
ccCopyErrorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ccCopyErrorIndex.setStatus('current')
ccCopyErrorDeviceIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyErrorDeviceIpAddressType.setStatus('current')
ccCopyErrorDeviceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyErrorDeviceIpAddress.setStatus('current')
ccCopyErrorDeviceWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 4), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyErrorDeviceWWN.setStatus('current')
ccCopyErrorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyErrorDescription.setStatus('current')
ciscoConfigCopyMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 2))
ccCopyMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 2, 1))
ccCopyCompletion = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 96, 2, 1, 1)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddress"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFileName"), ("CISCO-CONFIG-COPY-MIB", "ccCopyState"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeStarted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeCompleted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFailCause"))
if mibBuilder.loadTexts: ccCopyCompletion.setStatus('current')
ciscoConfigCopyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 3))
ccCopyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1))
ccCopyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2))
ccCopyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 1)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyGroup"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyMIBCompliance = ccCopyMIBCompliance.setStatus('deprecated')
ccCopyMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 2)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyGroupRev1"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyMIBComplianceRev1 = ccCopyMIBComplianceRev1.setStatus('deprecated')
ccCopyMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 3)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyGroupRev1"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationsGroup"), ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyMIBComplianceRev2 = ccCopyMIBComplianceRev2.setStatus('deprecated')
ccCopyMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 4)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyGroupRev1"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationsGroup"), ("CISCO-CONFIG-COPY-MIB", "ccCopyGroupVpn"), ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyMIBComplianceRev3 = ccCopyMIBComplianceRev3.setStatus('current')
ccCopyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 1)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyProtocol"), ("CISCO-CONFIG-COPY-MIB", "ccCopySourceFileType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyDestFileType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddress"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFileName"), ("CISCO-CONFIG-COPY-MIB", "ccCopyUserName"), ("CISCO-CONFIG-COPY-MIB", "ccCopyUserPassword"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationOnCompletion"), ("CISCO-CONFIG-COPY-MIB", "ccCopyState"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeStarted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeCompleted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFailCause"), ("CISCO-CONFIG-COPY-MIB", "ccCopyEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyGroup = ccCopyGroup.setStatus('deprecated')
ccCopyNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 2)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyCompletion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyNotificationsGroup = ccCopyNotificationsGroup.setStatus('current')
ccCopyGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 3)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyProtocol"), ("CISCO-CONFIG-COPY-MIB", "ccCopySourceFileType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyDestFileType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddressType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddressRev1"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFileName"), ("CISCO-CONFIG-COPY-MIB", "ccCopyUserName"), ("CISCO-CONFIG-COPY-MIB", "ccCopyUserPassword"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationOnCompletion"), ("CISCO-CONFIG-COPY-MIB", "ccCopyState"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeStarted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeCompleted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFailCause"), ("CISCO-CONFIG-COPY-MIB", "ccCopyEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyGroupRev1 = ccCopyGroupRev1.setStatus('current')
ccCopyErrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 4)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDeviceIpAddressType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDeviceIpAddress"), ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDeviceWWN"), ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyErrorGroup = ccCopyErrorGroup.setStatus('current')
ccCopyGroupVpn = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 5)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyVrfName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyGroupVpn = ccCopyGroupVpn.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONFIG-COPY-MIB", ConfigCopyFailCause=ConfigCopyFailCause, ccCopyErrorGroup=ccCopyErrorGroup, ccCopyEntryRowStatus=ccCopyEntryRowStatus, ccCopyEntry=ccCopyEntry, ccCopyServerAddressRev1=ccCopyServerAddressRev1, ccCopyErrorDeviceIpAddressType=ccCopyErrorDeviceIpAddressType, ccCopyGroupRev1=ccCopyGroupRev1, ciscoConfigCopyMIB=ciscoConfigCopyMIB, ccCopyMIBTraps=ccCopyMIBTraps, ccCopyMIBComplianceRev1=ccCopyMIBComplianceRev1, ccCopyServerAddressType=ccCopyServerAddressType, ConfigCopyProtocol=ConfigCopyProtocol, ccCopyTable=ccCopyTable, ccCopyNotificationOnCompletion=ccCopyNotificationOnCompletion, ccCopyTimeCompleted=ccCopyTimeCompleted, ccCopyFailCause=ccCopyFailCause, ccCopyErrorIndex=ccCopyErrorIndex, ccCopyErrorDeviceIpAddress=ccCopyErrorDeviceIpAddress, ccCopyErrorTable=ccCopyErrorTable, ccCopyMIBCompliance=ccCopyMIBCompliance, ccCopyMIBCompliances=ccCopyMIBCompliances, ccCopyServerAddress=ccCopyServerAddress, ccCopyUserName=ccCopyUserName, ccCopyDestFileType=ccCopyDestFileType, ccCopyMIBComplianceRev3=ccCopyMIBComplianceRev3, ccCopyMIBComplianceRev2=ccCopyMIBComplianceRev2, ccCopyUserPassword=ccCopyUserPassword, ccCopyIndex=ccCopyIndex, ccCopyErrorDescription=ccCopyErrorDescription, ccCopyState=ccCopyState, ccCopyMIBGroups=ccCopyMIBGroups, ConfigCopyState=ConfigCopyState, ciscoConfigCopyMIBConformance=ciscoConfigCopyMIBConformance, ccCopyCompletion=ccCopyCompletion, ccCopyGroup=ccCopyGroup, ccCopyVrfName=ccCopyVrfName, ccCopySourceFileType=ccCopySourceFileType, ciscoConfigCopyMIBTrapPrefix=ciscoConfigCopyMIBTrapPrefix, ciscoConfigCopyMIBObjects=ciscoConfigCopyMIBObjects, ccCopyGroupVpn=ccCopyGroupVpn, ccCopyProtocol=ccCopyProtocol, ccCopyNotificationsGroup=ccCopyNotificationsGroup, ConfigFileType=ConfigFileType, ccCopyFileName=ccCopyFileName, ccCopyTimeStarted=ccCopyTimeStarted, ccCopy=ccCopy, ccCopyErrorEntry=ccCopyErrorEntry, ccCopyErrorDeviceWWN=ccCopyErrorDeviceWWN, PYSNMP_MODULE_ID=ciscoConfigCopyMIB)
