#
# PySNMP MIB module CISCO-CONTENT-NETWORK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-CONTENT-NETWORK-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:25:51 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ZeroBasedCounter32, = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, ModuleIdentity, iso, ObjectIdentity, Counter32, TimeTicks, Counter64, Unsigned32, NotificationType, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "ModuleIdentity", "iso", "ObjectIdentity", "Counter32", "TimeTicks", "Counter64", "Unsigned32", "NotificationType", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoContentNetworkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 216))
ciscoContentNetworkMIB.setRevisions(('2001-10-11 18:25', '2001-05-23 21:34',))
if mibBuilder.loadTexts: ciscoContentNetworkMIB.setLastUpdated('200110111825Z')
if mibBuilder.loadTexts: ciscoContentNetworkMIB.setOrganization('Cisco Systems, Inc.')
ciscoContentNetworkMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 216, 1))
ccnReport = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1))
ccnReportDns = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 1))
ccnReportAcct = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 2))
ccnReportDnsRequestRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 1, 1), Gauge32()).setUnits('requests-per-second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccnReportDnsRequestRate.setStatus('current')
ccnReportDnsClientCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 1, 2), ZeroBasedCounter32()).setUnits('clients').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccnReportDnsClientCount.setStatus('current')
ccnReportDnsRequests = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 1, 3), ZeroBasedCounter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccnReportDnsRequests.setStatus('current')
ccnReportAcctBytesServed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 2, 1), ZeroBasedCounter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccnReportAcctBytesServed.setStatus('current')
ccnReportAcctObjectsCached = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 2, 2), Gauge32()).setUnits('objects').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccnReportAcctObjectsCached.setStatus('current')
ccnReportAcctCacheHitRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 2, 3), Gauge32()).setUnits('objects-per-minute').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccnReportAcctCacheHitRate.setStatus('current')
ccnReportAcctCacheMissRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 2, 4), Gauge32()).setUnits('objects-per-minute').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccnReportAcctCacheMissRate.setStatus('current')
ciscoContentNetworkMIBNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 216, 2))
ccnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0))
ccnNotifServerStart = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 1))
if mibBuilder.loadTexts: ccnNotifServerStart.setStatus('deprecated')
ccnNotifServerStop = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 2))
if mibBuilder.loadTexts: ccnNotifServerStop.setStatus('deprecated')
ccnNotifOffline = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 3))
if mibBuilder.loadTexts: ccnNotifOffline.setStatus('current')
ccnNotifNeedsAttention = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 4))
if mibBuilder.loadTexts: ccnNotifNeedsAttention.setStatus('current')
ccnNotifWaitingForCdm = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 5))
if mibBuilder.loadTexts: ccnNotifWaitingForCdm.setStatus('current')
ccnNotifOnline = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 6))
if mibBuilder.loadTexts: ccnNotifOnline.setStatus('current')
ccnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 216, 3))
ccnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 1))
ccnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 2))
ccnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 1, 1)).setObjects(("CISCO-CONTENT-NETWORK-MIB", "ccnReportingGroup"), ("CISCO-CONTENT-NETWORK-MIB", "ccnNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccnMIBCompliance = ccnMIBCompliance.setStatus('deprecated')
ccnMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 1, 2)).setObjects(("CISCO-CONTENT-NETWORK-MIB", "ccnReportingGroup"), ("CISCO-CONTENT-NETWORK-MIB", "ccnNotifGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccnMIBComplianceRev1 = ccnMIBComplianceRev1.setStatus('current')
ccnReportingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 2, 1)).setObjects(("CISCO-CONTENT-NETWORK-MIB", "ccnReportDnsRequestRate"), ("CISCO-CONTENT-NETWORK-MIB", "ccnReportDnsClientCount"), ("CISCO-CONTENT-NETWORK-MIB", "ccnReportDnsRequests"), ("CISCO-CONTENT-NETWORK-MIB", "ccnReportAcctBytesServed"), ("CISCO-CONTENT-NETWORK-MIB", "ccnReportAcctObjectsCached"), ("CISCO-CONTENT-NETWORK-MIB", "ccnReportAcctCacheHitRate"), ("CISCO-CONTENT-NETWORK-MIB", "ccnReportAcctCacheMissRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccnReportingGroup = ccnReportingGroup.setStatus('current')
ccnNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 2, 2)).setObjects(("CISCO-CONTENT-NETWORK-MIB", "ccnNotifServerStart"), ("CISCO-CONTENT-NETWORK-MIB", "ccnNotifServerStop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccnNotifGroup = ccnNotifGroup.setStatus('deprecated')
ccnNotifGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 2, 3)).setObjects(("CISCO-CONTENT-NETWORK-MIB", "ccnNotifOffline"), ("CISCO-CONTENT-NETWORK-MIB", "ccnNotifNeedsAttention"), ("CISCO-CONTENT-NETWORK-MIB", "ccnNotifWaitingForCdm"), ("CISCO-CONTENT-NETWORK-MIB", "ccnNotifOnline"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccnNotifGroupRev1 = ccnNotifGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONTENT-NETWORK-MIB", ccnReportAcctCacheMissRate=ccnReportAcctCacheMissRate, ccnReportDnsRequests=ccnReportDnsRequests, ccnNotifNeedsAttention=ccnNotifNeedsAttention, ccnReportAcctObjectsCached=ccnReportAcctObjectsCached, ccnNotifOffline=ccnNotifOffline, ccnReportDnsClientCount=ccnReportDnsClientCount, ciscoContentNetworkMIBObjects=ciscoContentNetworkMIBObjects, ccnMIBComplianceRev1=ccnMIBComplianceRev1, PYSNMP_MODULE_ID=ciscoContentNetworkMIB, ccnReport=ccnReport, ccnNotifServerStop=ccnNotifServerStop, ccnNotifGroupRev1=ccnNotifGroupRev1, ccnReportAcctBytesServed=ccnReportAcctBytesServed, ciscoContentNetworkMIBNotif=ciscoContentNetworkMIBNotif, ciscoContentNetworkMIB=ciscoContentNetworkMIB, ccnReportAcct=ccnReportAcct, ccnMIBGroups=ccnMIBGroups, ccnReportDnsRequestRate=ccnReportDnsRequestRate, ccnMIBConformance=ccnMIBConformance, ccnMIBCompliance=ccnMIBCompliance, ccnNotifServerStart=ccnNotifServerStart, ccnNotifOnline=ccnNotifOnline, ccnReportAcctCacheHitRate=ccnReportAcctCacheHitRate, ccnNotifGroup=ccnNotifGroup, ccnNotifWaitingForCdm=ccnNotifWaitingForCdm, ccnMIBCompliances=ccnMIBCompliances, ccnNotifications=ccnNotifications, ccnReportingGroup=ccnReportingGroup, ccnReportDns=ccnReportDns)
