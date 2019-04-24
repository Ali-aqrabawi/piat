#
# PySNMP MIB module CISCO-IETF-SCTP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-IETF-SCTP-EXT-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:48:13 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
cSctpAssocEntry, cSctpAssocRemAddressEntry, cSctpAssocRemAddressStatus = mibBuilder.importSymbols("CISCO-IETF-SCTP-MIB", "cSctpAssocEntry", "cSctpAssocRemAddressEntry", "cSctpAssocRemAddressStatus")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, MibIdentifier, Counter32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Counter64, NotificationType, IpAddress, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "MibIdentifier", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Counter64", "NotificationType", "IpAddress", "iso", "TimeTicks")
TruthValue, DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeStamp", "TextualConvention")
cSctpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 76))
cSctpExtMIB.setRevisions(('2001-11-09 00:00', '2001-08-27 00:00',))
if mibBuilder.loadTexts: cSctpExtMIB.setLastUpdated('200111090000Z')
if mibBuilder.loadTexts: cSctpExtMIB.setOrganization(' ')
cSctpExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 76, 0))
cSctpExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 76, 1))
cSctpScalarsExt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1))
cSctpExtTables = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2))
cSctpStatRtxChucks = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 1), Counter32()).setUnits('chunks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpStatRtxChucks.setStatus('current')
cSctpStatRtxChucksFast = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 2), Counter32()).setUnits('chunks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpStatRtxChucksFast.setStatus('current')
cSctpStatDestAddressFailures = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpStatDestAddressFailures.setStatus('current')
cSctpCtrlPurgeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3600, 3000000)).clone(86400)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cSctpCtrlPurgeTimeout.setStatus('current')
cSctpCtrlMaxHeld = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 10000)).clone(100)).setUnits('association TCBs').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cSctpCtrlMaxHeld.setStatus('current')
cSctpAddressStateNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cSctpAddressStateNotifEnabled.setStatus('current')
cSctpAssocExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1), )
if mibBuilder.loadTexts: cSctpAssocExtTable.setStatus('current')
cSctpAssocExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1), )
cSctpAssocEntry.registerAugmentions(("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtEntry"))
cSctpAssocExtEntry.setIndexNames(*cSctpAssocEntry.getIndexNames())
if mibBuilder.loadTexts: cSctpAssocExtEntry.setStatus('current')
cSctpAssocExtRtoMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 1), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtRtoMin.setStatus('current')
cSctpAssocExtRtoMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 2), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtRtoMax.setStatus('current')
cSctpAssocExtRtoInitial = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 3), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtRtoInitial.setStatus('current')
cSctpAssocExtValCookieLife = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 4), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtValCookieLife.setStatus('current')
cSctpAssocExtMaxInitRetr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtMaxInitRetr.setStatus('current')
cSctpAssocExtMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(37, 65535))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtMTU.setStatus('current')
cSctpAssocExtLocRecWnd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtLocRecWnd.setStatus('current')
cSctpAssocExtLocRecWndLowMark = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtLocRecWndLowMark.setStatus('current')
cSctpAssocExtLocRecWndZeroCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtLocRecWndZeroCnt.setStatus('current')
cSctpAssocExtRemRecWnd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtRemRecWnd.setStatus('current')
cSctpAssocExtRemRecWndLowMark = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtRemRecWndLowMark.setStatus('current')
cSctpAssocExtRemRecWndZeroCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtRemRecWndZeroCnt.setStatus('current')
cSctpAssocExtUlpQueued = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('datagrams').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtUlpQueued.setStatus('current')
cSctpAssocExtUlpQueuedHW = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('datagrams').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cSctpAssocExtUlpQueuedHW.setStatus('current')
cSctpAssocExtUlpQueuedRT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 15), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtUlpQueuedRT.setStatus('current')
cSctpAssocExtChunksRecControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 16), Counter32()).setUnits('chunks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtChunksRecControl.setStatus('current')
cSctpAssocExtChunksRecOrdered = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 17), Counter32()).setUnits('chunks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtChunksRecOrdered.setStatus('current')
cSctpAssocExtChunksRecUnOrdered = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 18), Counter32()).setUnits('chunks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtChunksRecUnOrdered.setStatus('current')
cSctpAssocExtChunksSentControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 19), Counter32()).setUnits('chunks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtChunksSentControl.setStatus('current')
cSctpAssocExtChunksSentOrdered = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 20), Counter32()).setUnits('chunks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtChunksSentOrdered.setStatus('current')
cSctpAssocExtChunksSentUnOrdered = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 21), Counter32()).setUnits('chunks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtChunksSentUnOrdered.setStatus('current')
cSctpAssocExtDatagramsRec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 22), Counter32()).setUnits('datagrams').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtDatagramsRec.setStatus('current')
cSctpAssocExtDatagramsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 23), Counter32()).setUnits('datagrams').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtDatagramsSent.setStatus('current')
cSctpAssocExtEffectiveAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 24), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtEffectiveAddrType.setStatus('current')
cSctpAssocExtEffectiveAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 25), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtEffectiveAddress.setStatus('current')
cSctpAssocExtRtxChunksFast = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 26), Counter32()).setUnits('chunks').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtRtxChunksFast.setStatus('current')
cSctpAssocExtBundleFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 27), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtBundleFlag.setStatus('current')
cSctpAssocExtBundleTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 28), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocExtBundleTimeout.setStatus('current')
cSctpAssocRemAddressExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 2), )
if mibBuilder.loadTexts: cSctpAssocRemAddressExtTable.setStatus('current')
cSctpAssocRemAddressExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 2, 1), )
cSctpAssocRemAddressEntry.registerAugmentions(("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocRemAddressExtEntry"))
cSctpAssocRemAddressExtEntry.setIndexNames(*cSctpAssocRemAddressEntry.getIndexNames())
if mibBuilder.loadTexts: cSctpAssocRemAddressExtEntry.setStatus('current')
cSctpAssocRemAddressFailedCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocRemAddressFailedCnt.setStatus('current')
cSctpAssocRemAddressSRTT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cSctpAssocRemAddressSRTT.setStatus('current')
cSctpExtDestAddressStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 76, 0, 1)).setObjects(("CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressStatus"))
if mibBuilder.loadTexts: cSctpExtDestAddressStateChange.setStatus('current')
cSctpExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 76, 3))
cSctpExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 1))
cSctpExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2))
cSctpExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 1, 1)).setObjects(("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtStatGroup"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtCtrlGroup"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtAssocCtrlGroup"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtAssocStatGroup"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtAssocRemAddrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSctpExtCompliance = cSctpExtCompliance.setStatus('deprecated')
cSctpExtComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 1, 2)).setObjects(("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtStatGroup"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtAssocCtrlGroup"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtAssocRemAddrGroup"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtAssocNotificationsGroup"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtCtrlGroupRev1"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtAssocStatGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSctpExtComplianceRev1 = cSctpExtComplianceRev1.setStatus('current')
cSctpExtStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 1)).setObjects(("CISCO-IETF-SCTP-EXT-MIB", "cSctpStatRtxChucks"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpStatRtxChucksFast"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpStatDestAddressFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSctpExtStatGroup = cSctpExtStatGroup.setStatus('current')
cSctpExtCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 2)).setObjects(("CISCO-IETF-SCTP-EXT-MIB", "cSctpCtrlPurgeTimeout"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpCtrlMaxHeld"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSctpExtCtrlGroup = cSctpExtCtrlGroup.setStatus('deprecated')
cSctpExtAssocCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 3)).setObjects(("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRtoMin"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRtoMax"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRtoInitial"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtValCookieLife"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtMaxInitRetr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSctpExtAssocCtrlGroup = cSctpExtAssocCtrlGroup.setStatus('current')
cSctpExtAssocStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 4)).setObjects(("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtMTU"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWnd"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWndLowMark"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWndZeroCnt"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWnd"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWndLowMark"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWndZeroCnt"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueued"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueuedHW"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueuedRT"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecControl"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecOrdered"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecUnOrdered"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentControl"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentOrdered"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentUnOrdered"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtDatagramsRec"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtDatagramsSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSctpExtAssocStatGroup = cSctpExtAssocStatGroup.setStatus('deprecated')
cSctpExtAssocRemAddrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 5)).setObjects(("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocRemAddressFailedCnt"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocRemAddressSRTT"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSctpExtAssocRemAddrGroup = cSctpExtAssocRemAddrGroup.setStatus('current')
cSctpExtAssocNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 6)).setObjects(("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtDestAddressStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSctpExtAssocNotificationsGroup = cSctpExtAssocNotificationsGroup.setStatus('current')
cSctpExtCtrlGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 7)).setObjects(("CISCO-IETF-SCTP-EXT-MIB", "cSctpCtrlPurgeTimeout"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpCtrlMaxHeld"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAddressStateNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSctpExtCtrlGroupRev1 = cSctpExtCtrlGroupRev1.setStatus('current')
cSctpExtAssocStatGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 8)).setObjects(("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtMTU"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWnd"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWndLowMark"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWndZeroCnt"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWnd"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWndLowMark"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWndZeroCnt"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueued"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueuedHW"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueuedRT"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecControl"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecOrdered"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecUnOrdered"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentControl"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentOrdered"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentUnOrdered"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtDatagramsRec"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtDatagramsSent"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtEffectiveAddrType"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtEffectiveAddress"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRtxChunksFast"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtBundleTimeout"), ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtBundleFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSctpExtAssocStatGroupRev1 = cSctpExtAssocStatGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-SCTP-EXT-MIB", cSctpAssocRemAddressSRTT=cSctpAssocRemAddressSRTT, cSctpAssocExtRemRecWndZeroCnt=cSctpAssocExtRemRecWndZeroCnt, cSctpAssocRemAddressExtEntry=cSctpAssocRemAddressExtEntry, cSctpExtAssocCtrlGroup=cSctpExtAssocCtrlGroup, cSctpAssocExtRtoInitial=cSctpAssocExtRtoInitial, cSctpExtAssocNotificationsGroup=cSctpExtAssocNotificationsGroup, cSctpAssocExtEntry=cSctpAssocExtEntry, cSctpExtAssocRemAddrGroup=cSctpExtAssocRemAddrGroup, cSctpExtNotifications=cSctpExtNotifications, cSctpAssocExtUlpQueued=cSctpAssocExtUlpQueued, cSctpAssocExtRemRecWnd=cSctpAssocExtRemRecWnd, cSctpAssocExtChunksRecUnOrdered=cSctpAssocExtChunksRecUnOrdered, cSctpAssocExtChunksSentOrdered=cSctpAssocExtChunksSentOrdered, PYSNMP_MODULE_ID=cSctpExtMIB, cSctpAssocExtEffectiveAddrType=cSctpAssocExtEffectiveAddrType, cSctpAssocRemAddressExtTable=cSctpAssocRemAddressExtTable, cSctpStatDestAddressFailures=cSctpStatDestAddressFailures, cSctpAssocExtChunksSentControl=cSctpAssocExtChunksSentControl, cSctpAssocExtDatagramsRec=cSctpAssocExtDatagramsRec, cSctpExtDestAddressStateChange=cSctpExtDestAddressStateChange, cSctpAssocExtMTU=cSctpAssocExtMTU, cSctpAssocExtChunksRecControl=cSctpAssocExtChunksRecControl, cSctpAssocExtLocRecWndZeroCnt=cSctpAssocExtLocRecWndZeroCnt, cSctpCtrlMaxHeld=cSctpCtrlMaxHeld, cSctpExtTables=cSctpExtTables, cSctpAssocExtTable=cSctpAssocExtTable, cSctpAssocExtRemRecWndLowMark=cSctpAssocExtRemRecWndLowMark, cSctpAssocExtChunksRecOrdered=cSctpAssocExtChunksRecOrdered, cSctpAssocExtBundleFlag=cSctpAssocExtBundleFlag, cSctpExtGroups=cSctpExtGroups, cSctpAssocExtRtoMin=cSctpAssocExtRtoMin, cSctpAssocExtEffectiveAddress=cSctpAssocExtEffectiveAddress, cSctpAssocExtLocRecWnd=cSctpAssocExtLocRecWnd, cSctpExtCompliances=cSctpExtCompliances, cSctpCtrlPurgeTimeout=cSctpCtrlPurgeTimeout, cSctpAssocExtMaxInitRetr=cSctpAssocExtMaxInitRetr, cSctpAssocRemAddressFailedCnt=cSctpAssocRemAddressFailedCnt, cSctpExtCtrlGroup=cSctpExtCtrlGroup, cSctpStatRtxChucks=cSctpStatRtxChucks, cSctpAssocExtRtxChunksFast=cSctpAssocExtRtxChunksFast, cSctpExtMIB=cSctpExtMIB, cSctpAssocExtLocRecWndLowMark=cSctpAssocExtLocRecWndLowMark, cSctpExtObjects=cSctpExtObjects, cSctpExtAssocStatGroup=cSctpExtAssocStatGroup, cSctpAssocExtBundleTimeout=cSctpAssocExtBundleTimeout, cSctpScalarsExt=cSctpScalarsExt, cSctpAssocExtValCookieLife=cSctpAssocExtValCookieLife, cSctpAssocExtDatagramsSent=cSctpAssocExtDatagramsSent, cSctpAssocExtChunksSentUnOrdered=cSctpAssocExtChunksSentUnOrdered, cSctpExtCtrlGroupRev1=cSctpExtCtrlGroupRev1, cSctpExtConformance=cSctpExtConformance, cSctpExtComplianceRev1=cSctpExtComplianceRev1, cSctpExtCompliance=cSctpExtCompliance, cSctpExtStatGroup=cSctpExtStatGroup, cSctpAddressStateNotifEnabled=cSctpAddressStateNotifEnabled, cSctpStatRtxChucksFast=cSctpStatRtxChucksFast, cSctpExtAssocStatGroupRev1=cSctpExtAssocStatGroupRev1, cSctpAssocExtUlpQueuedHW=cSctpAssocExtUlpQueuedHW, cSctpAssocExtRtoMax=cSctpAssocExtRtoMax, cSctpAssocExtUlpQueuedRT=cSctpAssocExtUlpQueuedRT)
