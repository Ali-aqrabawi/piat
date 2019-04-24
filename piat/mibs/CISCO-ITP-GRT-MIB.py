#
# PySNMP MIB module CISCO-ITP-GRT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-ITP-GRT-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:34:27 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
cgspCLLICode, cgspInstNetwork, cgspInstDisplayName, cgspEventSequenceNumber = mibBuilder.importSymbols("CISCO-ITP-GSP-MIB", "cgspCLLICode", "cgspInstNetwork", "cgspInstDisplayName", "cgspEventSequenceNumber")
CItpTcServiceIndicator, CItpTcQos, CItpTcRouteTableName, CItpTcLinksetId, CItpTcPointCode, CItpTcTableLoadStatus, CItpTcDisplayPC, CItpTcURL = mibBuilder.importSymbols("CISCO-ITP-TC-MIB", "CItpTcServiceIndicator", "CItpTcQos", "CItpTcRouteTableName", "CItpTcLinksetId", "CItpTcPointCode", "CItpTcTableLoadStatus", "CItpTcDisplayPC", "CItpTcURL")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, ModuleIdentity, Counter64, Unsigned32, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, IpAddress, Integer32, Counter32, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Counter64", "Unsigned32", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "IpAddress", "Integer32", "Counter32", "iso", "Gauge32")
TextualConvention, TimeStamp, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString", "RowStatus", "TruthValue")
ciscoGrtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 334))
ciscoGrtMIB.setRevisions(('2008-05-01 00:00', '2003-03-03 00:00',))
if mibBuilder.loadTexts: ciscoGrtMIB.setLastUpdated('200805010000Z')
if mibBuilder.loadTexts: ciscoGrtMIB.setOrganization('Cisco Systems, Inc.')
ciscoGrtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 334, 0))
ciscoGrtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 334, 1))
ciscoGrtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 334, 2))
cgrtScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1))
cgrtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2))
class CgrtDisplayPCSI(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

cgrtRouteMaxDynamic = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtRouteMaxDynamic.setStatus('current')
cgrtDestNotifDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtDestNotifDelayTime.setStatus('deprecated')
cgrtDestNotifWindowTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 900))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtDestNotifWindowTime.setStatus('deprecated')
cgrtDestNotifMaxPerWindow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 9000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtDestNotifMaxPerWindow.setStatus('deprecated')
cgrtDestNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtDestNotifEnabled.setStatus('deprecated')
cgrtMgmtNotifDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtMgmtNotifDelayTime.setStatus('deprecated')
cgrtMgmtNotifWindowTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 900))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtMgmtNotifWindowTime.setStatus('deprecated')
cgrtMgmtNotifMaxPerWindow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 9000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtMgmtNotifMaxPerWindow.setStatus('deprecated')
cgrtMgmtNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 19), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtMgmtNotifEnabled.setStatus('deprecated')
cgrtRouteTableLoadNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 20), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtRouteTableLoadNotifEnabled.setStatus('current')
cgrtDynamicRoutes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDynamicRoutes.setStatus('current')
cgrtDynamicRoutesDropped = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDynamicRoutesDropped.setStatus('current')
cgrtDestNotifWindowTimeRev1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 86400), )).clone(900)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtDestNotifWindowTimeRev1.setStatus('current')
cgrtDestNotifMaxPerWindowRev1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 9000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtDestNotifMaxPerWindowRev1.setStatus('current')
cgrtDestNotifEnabledRev1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 25), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtDestNotifEnabledRev1.setStatus('current')
cgrtMgmtNotifWindowTimeRev1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 86400), )).clone(900)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtMgmtNotifWindowTimeRev1.setStatus('current')
cgrtMgmtNotifMaxPerWindowRev1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 9000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtMgmtNotifMaxPerWindowRev1.setStatus('current')
cgrtMgmtNotifEnabledRev1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 28), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtMgmtNotifEnabledRev1.setStatus('current')
cgrtOrigTableEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 29), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtOrigTableEnabled.setStatus('current')
cgrtPCStatsInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 30), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(900, 3600), )).clone(900)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtPCStatsInterval.setStatus('current')
cgrtNoRouteMSUsNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 31), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtNoRouteMSUsNotifEnabled.setStatus('current')
cgrtNoRouteMSUsNotifWindowTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 86400)).clone(900)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgrtNoRouteMSUsNotifWindowTime.setStatus('current')
cgrtInstTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1), )
if mibBuilder.loadTexts: cgrtInstTable.setStatus('current')
cgrtInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"))
if mibBuilder.loadTexts: cgrtInstEntry.setStatus('current')
cgrtInstLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtInstLastChanged.setStatus('current')
cgrtInstLastLoadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtInstLastLoadTime.setStatus('current')
cgrtInstLoadStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 3), CItpTcTableLoadStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtInstLoadStatus.setStatus('current')
cgrtInstTableName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 4), CItpTcRouteTableName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtInstTableName.setStatus('current')
cgrtInstLastURL = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 5), CItpTcURL()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtInstLastURL.setStatus('current')
cgrtInstNumberDestinations = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 6), Gauge32()).setUnits('entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtInstNumberDestinations.setStatus('current')
cgrtInstNumberRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 7), Gauge32()).setUnits('entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtInstNumberRoutes.setStatus('current')
cgrtInstUnknownOrigPCs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 8), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtInstUnknownOrigPCs.setStatus('current')
cgrtInstNoRouteDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 9), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtInstNoRouteDrops.setStatus('current')
cgrtDestTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2), )
if mibBuilder.loadTexts: cgrtDestTable.setStatus('current')
cgrtDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GRT-MIB", "cgrtRouteDpc"), (0, "CISCO-ITP-GRT-MIB", "cgrtRouteMask"))
if mibBuilder.loadTexts: cgrtDestEntry.setStatus('current')
cgrtDestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("accessible", 2), ("inaccessible", 3), ("restricted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestStatus.setStatus('current')
cgrtDestCongestion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestCongestion.setStatus('current')
cgrtDestAccessibleSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 3), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestAccessibleSeconds.setStatus('current')
cgrtDestInaccessibleSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 4), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestInaccessibleSeconds.setStatus('current')
cgrtDestRestrictedSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 5), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestRestrictedSeconds.setStatus('current')
cgrtDestMSUsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 6), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestMSUsOut.setStatus('current')
cgrtDestOctetsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 7), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestOctetsOut.setStatus('current')
cgrtDestMSUsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 8), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestMSUsIn.setStatus('current')
cgrtDestOctetsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 9), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestOctetsIn.setStatus('current')
cgrtDestInaccessibleDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 10), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestInaccessibleDrops.setStatus('current')
cgrtDestRestrictedMSUs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 11), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestRestrictedMSUs.setStatus('current')
cgrtDestCongestionDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 12), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestCongestionDrops.setStatus('current')
cgrtDestDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 13), CItpTcDisplayPC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestDisplay.setStatus('current')
cgrtRouteTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3), )
if mibBuilder.loadTexts: cgrtRouteTable.setStatus('current')
cgrtRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GRT-MIB", "cgrtRouteDpc"), (0, "CISCO-ITP-GRT-MIB", "cgrtRouteMask"), (0, "CISCO-ITP-GRT-MIB", "cgrtRouteDestLsCost"), (0, "CISCO-ITP-GRT-MIB", "cgrtRouteDestLinkset"))
if mibBuilder.loadTexts: cgrtRouteEntry.setStatus('current')
cgrtRouteDpc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 1), CItpTcPointCode())
if mibBuilder.loadTexts: cgrtRouteDpc.setStatus('current')
cgrtRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215)))
if mibBuilder.loadTexts: cgrtRouteMask.setStatus('current')
cgrtRouteDestLsCost = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)))
if mibBuilder.loadTexts: cgrtRouteDestLsCost.setStatus('current')
cgrtRouteDestLinkset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 4), CItpTcLinksetId())
if mibBuilder.loadTexts: cgrtRouteDestLinkset.setStatus('current')
cgrtRouteQos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 5), CItpTcQos()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgrtRouteQos.setStatus('current')
cgrtRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("available", 2), ("restricted", 3), ("unavailable", 4), ("deleted", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgrtRouteStatus.setStatus('current')
cgrtRouteMgmtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("allowed", 2), ("restricted", 3), ("prohibited", 4), ("deleted", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgrtRouteMgmtStatus.setStatus('current')
cgrtRouteDynamic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtRouteDynamic.setStatus('current')
cgrtRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("static", 1), ("cluster", 2), ("summary", 3), ("xlist", 4), ("shadow", 5), ("management", 6), ("alias", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtRouteType.setStatus('current')
cgrtRouteAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("unknown", 1), ("available", 2), ("restricted", 3), ("unavailable", 4), ("deleted", 5))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgrtRouteAdminStatus.setStatus('current')
cgrtRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgrtRouteRowStatus.setStatus('current')
cgrtRouteAllowedSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 12), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtRouteAllowedSeconds.setStatus('current')
cgrtRouteRestrictedSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 13), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtRouteRestrictedSeconds.setStatus('current')
cgrtRouteProhibitedSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 14), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtRouteProhibitedSeconds.setStatus('current')
cgrtRouteDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 15), CItpTcDisplayPC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtRouteDisplay.setStatus('current')
cgrtOrigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5), )
if mibBuilder.loadTexts: cgrtOrigTable.setStatus('current')
cgrtOrigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GRT-MIB", "cgrtOrigPC"), (0, "CISCO-ITP-GRT-MIB", "cgrtRouteMask"))
if mibBuilder.loadTexts: cgrtOrigEntry.setStatus('current')
cgrtOrigPC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5, 1, 1), CItpTcPointCode())
if mibBuilder.loadTexts: cgrtOrigPC.setStatus('current')
cgrtOrigMSUs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5, 1, 2), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtOrigMSUs.setStatus('current')
cgrtOrigOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5, 1, 3), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtOrigOctets.setStatus('current')
cgrtOrigDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5, 1, 4), CItpTcDisplayPC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtOrigDisplay.setStatus('current')
cgrtDestSITable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6), )
if mibBuilder.loadTexts: cgrtDestSITable.setStatus('current')
cgrtDestSIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GRT-MIB", "cgrtRouteDpc"), (0, "CISCO-ITP-GRT-MIB", "cgrtRouteMask"), (0, "CISCO-ITP-GRT-MIB", "cgrtMtp3SI"))
if mibBuilder.loadTexts: cgrtDestSIEntry.setStatus('current')
cgrtMtp3SI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 1), CItpTcServiceIndicator())
if mibBuilder.loadTexts: cgrtMtp3SI.setStatus('current')
cgrtDestSIMSUsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 2), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestSIMSUsOut.setStatus('current')
cgrtDestSIOctetsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 3), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestSIOctetsOut.setStatus('current')
cgrtDestSIMSUsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 4), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestSIMSUsIn.setStatus('current')
cgrtDestSIOctetsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 5), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestSIOctetsIn.setStatus('current')
cgrtDestSIDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 6), CgrtDisplayPCSI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtDestSIDisplay.setStatus('current')
cgrtOrigSITable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 7), )
if mibBuilder.loadTexts: cgrtOrigSITable.setStatus('current')
cgrtOrigSIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 7, 1), ).setIndexNames((0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"), (0, "CISCO-ITP-GRT-MIB", "cgrtOrigPC"), (0, "CISCO-ITP-GRT-MIB", "cgrtRouteMask"), (0, "CISCO-ITP-GRT-MIB", "cgrtMtp3SI"))
if mibBuilder.loadTexts: cgrtOrigSIEntry.setStatus('current')
cgrtOrigSIMSUs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 7, 1, 1), Counter32()).setUnits('MSUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtOrigSIMSUs.setStatus('current')
cgrtOrigSIOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 7, 1, 2), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtOrigSIOctets.setStatus('current')
cgrtOrigSIDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 7, 1, 3), CgrtDisplayPCSI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgrtOrigSIDisplay.setStatus('current')
cgrtNotificationsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4))
cgrtDestNotifSupFlag = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 1), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cgrtDestNotifSupFlag.setStatus('deprecated')
cgrtDestNotifChanges = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cgrtDestNotifChanges.setStatus('deprecated')
cgrtMgmtNotifSupFlag = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 3), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cgrtMgmtNotifSupFlag.setStatus('deprecated')
cgrtMgmtNotifChanges = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cgrtMgmtNotifChanges.setStatus('deprecated')
cgrtDestNotifSuppressed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 5), Counter32()).setUnits('occurrences').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cgrtDestNotifSuppressed.setStatus('current')
cgrtRouteNotifSuppressed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 6), Counter32()).setUnits('occurrences').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cgrtRouteNotifSuppressed.setStatus('current')
cgrtNoRouteMSUsInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 7), Unsigned32()).setUnits('seconds').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cgrtNoRouteMSUsInterval.setStatus('current')
cgrtIntervalNoRouteMSUs = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 8), Unsigned32()).setUnits('MSUs').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cgrtIntervalNoRouteMSUs.setStatus('current')
ciscoGrtDestStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 1)).setObjects(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"), ("CISCO-ITP-GSP-MIB", "cgspCLLICode"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifSupFlag"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifChanges"))
if mibBuilder.loadTexts: ciscoGrtDestStateChange.setStatus('deprecated')
ciscoGrtMgmtStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 2)).setObjects(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"), ("CISCO-ITP-GSP-MIB", "cgspCLLICode"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifSupFlag"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifChanges"))
if mibBuilder.loadTexts: ciscoGrtMgmtStateChange.setStatus('deprecated')
ciscoGrtRouteTableLoad = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 3)).setObjects(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"), ("CISCO-ITP-GSP-MIB", "cgspCLLICode"), ("CISCO-ITP-GRT-MIB", "cgrtInstLoadStatus"), ("CISCO-ITP-GRT-MIB", "cgrtInstTableName"), ("CISCO-ITP-GRT-MIB", "cgrtInstLastURL"))
if mibBuilder.loadTexts: ciscoGrtRouteTableLoad.setStatus('current')
ciscoGrtDestStateChangeRev1 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 4)).setObjects(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"), ("CISCO-ITP-GSP-MIB", "cgspCLLICode"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifSuppressed"), ("CISCO-ITP-GRT-MIB", "cgrtDestDisplay"), ("CISCO-ITP-GRT-MIB", "cgrtDestStatus"), ("CISCO-ITP-GRT-MIB", "cgrtDestCongestion"))
if mibBuilder.loadTexts: ciscoGrtDestStateChangeRev1.setStatus('current')
ciscoGrtMgmtStateChangeRev1 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 5)).setObjects(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"), ("CISCO-ITP-GSP-MIB", "cgspCLLICode"), ("CISCO-ITP-GRT-MIB", "cgrtRouteStatus"), ("CISCO-ITP-GRT-MIB", "cgrtRouteMgmtStatus"), ("CISCO-ITP-GRT-MIB", "cgrtRouteDynamic"), ("CISCO-ITP-GRT-MIB", "cgrtRouteAdminStatus"), ("CISCO-ITP-GRT-MIB", "cgrtRouteNotifSuppressed"), ("CISCO-ITP-GRT-MIB", "cgrtRouteDisplay"))
if mibBuilder.loadTexts: ciscoGrtMgmtStateChangeRev1.setStatus('current')
ciscoGrtNoRouteMSUDiscards = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 6)).setObjects(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"), ("CISCO-ITP-GSP-MIB", "cgspCLLICode"), ("CISCO-ITP-GSP-MIB", "cgspInstDisplayName"), ("CISCO-ITP-GRT-MIB", "cgrtNoRouteMSUsInterval"), ("CISCO-ITP-GRT-MIB", "cgrtIntervalNoRouteMSUs"))
if mibBuilder.loadTexts: ciscoGrtNoRouteMSUDiscards.setStatus('current')
ciscoGrtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 1))
ciscoGrtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2))
ciscoGrtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 1, 1)).setObjects(("CISCO-ITP-GRT-MIB", "ciscoGrtInstGroup"), ("CISCO-ITP-GRT-MIB", "ciscoGrtDestGroup"), ("CISCO-ITP-GRT-MIB", "ciscoGrtRouteGroup"), ("CISCO-ITP-GRT-MIB", "ciscoGrtNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtMIBCompliance = ciscoGrtMIBCompliance.setStatus('deprecated')
ciscoGrtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 1, 2)).setObjects(("CISCO-ITP-GRT-MIB", "ciscoGrtInstGroup"), ("CISCO-ITP-GRT-MIB", "ciscoGrtScalarsGroup"), ("CISCO-ITP-GRT-MIB", "ciscoGrtDestGroupRev1"), ("CISCO-ITP-GRT-MIB", "ciscoGrtRouteGroupRev1"), ("CISCO-ITP-GRT-MIB", "ciscoGrtOrigGroup"), ("CISCO-ITP-GRT-MIB", "ciscoGrtDestSIGroup"), ("CISCO-ITP-GRT-MIB", "ciscoGrtOrigSIGroup"), ("CISCO-ITP-GRT-MIB", "ciscoGrtNotificationsGroupRev1"), ("CISCO-ITP-GRT-MIB", "ciscoGrtInstGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtMIBComplianceRev1 = ciscoGrtMIBComplianceRev1.setStatus('current')
ciscoGrtInstGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 1)).setObjects(("CISCO-ITP-GRT-MIB", "cgrtInstLastChanged"), ("CISCO-ITP-GRT-MIB", "cgrtInstLastLoadTime"), ("CISCO-ITP-GRT-MIB", "cgrtInstLoadStatus"), ("CISCO-ITP-GRT-MIB", "cgrtInstTableName"), ("CISCO-ITP-GRT-MIB", "cgrtInstLastURL"), ("CISCO-ITP-GRT-MIB", "cgrtInstNumberDestinations"), ("CISCO-ITP-GRT-MIB", "cgrtInstNumberRoutes"), ("CISCO-ITP-GRT-MIB", "cgrtRouteTableLoadNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtInstGroup = ciscoGrtInstGroup.setStatus('current')
ciscoGrtDestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 2)).setObjects(("CISCO-ITP-GRT-MIB", "cgrtDestNotifDelayTime"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifWindowTime"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifMaxPerWindow"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifEnabled"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifSupFlag"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifChanges"), ("CISCO-ITP-GRT-MIB", "cgrtDestStatus"), ("CISCO-ITP-GRT-MIB", "cgrtDestCongestion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtDestGroup = ciscoGrtDestGroup.setStatus('deprecated')
ciscoGrtRouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 3)).setObjects(("CISCO-ITP-GRT-MIB", "cgrtRouteMaxDynamic"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifDelayTime"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifWindowTime"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifMaxPerWindow"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifEnabled"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifSupFlag"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifChanges"), ("CISCO-ITP-GRT-MIB", "cgrtDynamicRoutes"), ("CISCO-ITP-GRT-MIB", "cgrtDynamicRoutesDropped"), ("CISCO-ITP-GRT-MIB", "cgrtRouteQos"), ("CISCO-ITP-GRT-MIB", "cgrtRouteStatus"), ("CISCO-ITP-GRT-MIB", "cgrtRouteMgmtStatus"), ("CISCO-ITP-GRT-MIB", "cgrtRouteDynamic"), ("CISCO-ITP-GRT-MIB", "cgrtRouteType"), ("CISCO-ITP-GRT-MIB", "cgrtRouteAdminStatus"), ("CISCO-ITP-GRT-MIB", "cgrtRouteRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtRouteGroup = ciscoGrtRouteGroup.setStatus('deprecated')
ciscoGrtNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 4)).setObjects(("CISCO-ITP-GRT-MIB", "ciscoGrtDestStateChange"), ("CISCO-ITP-GRT-MIB", "ciscoGrtMgmtStateChange"), ("CISCO-ITP-GRT-MIB", "ciscoGrtRouteTableLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtNotificationsGroup = ciscoGrtNotificationsGroup.setStatus('deprecated')
ciscoGrtScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 5)).setObjects(("CISCO-ITP-GRT-MIB", "cgrtPCStatsInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtScalarsGroup = ciscoGrtScalarsGroup.setStatus('current')
ciscoGrtDestGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 6)).setObjects(("CISCO-ITP-GRT-MIB", "cgrtDestNotifWindowTimeRev1"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifMaxPerWindowRev1"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifEnabledRev1"), ("CISCO-ITP-GRT-MIB", "cgrtDestNotifSuppressed"), ("CISCO-ITP-GRT-MIB", "cgrtDestStatus"), ("CISCO-ITP-GRT-MIB", "cgrtDestCongestion"), ("CISCO-ITP-GRT-MIB", "cgrtDestAccessibleSeconds"), ("CISCO-ITP-GRT-MIB", "cgrtDestInaccessibleSeconds"), ("CISCO-ITP-GRT-MIB", "cgrtDestRestrictedSeconds"), ("CISCO-ITP-GRT-MIB", "cgrtDestMSUsOut"), ("CISCO-ITP-GRT-MIB", "cgrtDestOctetsOut"), ("CISCO-ITP-GRT-MIB", "cgrtDestMSUsIn"), ("CISCO-ITP-GRT-MIB", "cgrtDestOctetsIn"), ("CISCO-ITP-GRT-MIB", "cgrtDestRestrictedMSUs"), ("CISCO-ITP-GRT-MIB", "cgrtDestInaccessibleDrops"), ("CISCO-ITP-GRT-MIB", "cgrtDestCongestionDrops"), ("CISCO-ITP-GRT-MIB", "cgrtDestDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtDestGroupRev1 = ciscoGrtDestGroupRev1.setStatus('current')
ciscoGrtRouteGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 7)).setObjects(("CISCO-ITP-GRT-MIB", "cgrtRouteMaxDynamic"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifWindowTimeRev1"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifMaxPerWindowRev1"), ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifEnabledRev1"), ("CISCO-ITP-GRT-MIB", "cgrtRouteNotifSuppressed"), ("CISCO-ITP-GRT-MIB", "cgrtDynamicRoutes"), ("CISCO-ITP-GRT-MIB", "cgrtDynamicRoutesDropped"), ("CISCO-ITP-GRT-MIB", "cgrtRouteQos"), ("CISCO-ITP-GRT-MIB", "cgrtRouteStatus"), ("CISCO-ITP-GRT-MIB", "cgrtRouteMgmtStatus"), ("CISCO-ITP-GRT-MIB", "cgrtRouteDynamic"), ("CISCO-ITP-GRT-MIB", "cgrtRouteType"), ("CISCO-ITP-GRT-MIB", "cgrtRouteAdminStatus"), ("CISCO-ITP-GRT-MIB", "cgrtRouteRowStatus"), ("CISCO-ITP-GRT-MIB", "cgrtRouteAllowedSeconds"), ("CISCO-ITP-GRT-MIB", "cgrtRouteRestrictedSeconds"), ("CISCO-ITP-GRT-MIB", "cgrtRouteProhibitedSeconds"), ("CISCO-ITP-GRT-MIB", "cgrtRouteDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtRouteGroupRev1 = ciscoGrtRouteGroupRev1.setStatus('current')
ciscoGrtOrigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 8)).setObjects(("CISCO-ITP-GRT-MIB", "cgrtOrigTableEnabled"), ("CISCO-ITP-GRT-MIB", "cgrtOrigMSUs"), ("CISCO-ITP-GRT-MIB", "cgrtOrigOctets"), ("CISCO-ITP-GRT-MIB", "cgrtOrigDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtOrigGroup = ciscoGrtOrigGroup.setStatus('current')
ciscoGrtDestSIGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 9)).setObjects(("CISCO-ITP-GRT-MIB", "cgrtDestSIMSUsOut"), ("CISCO-ITP-GRT-MIB", "cgrtDestSIOctetsOut"), ("CISCO-ITP-GRT-MIB", "cgrtDestSIMSUsIn"), ("CISCO-ITP-GRT-MIB", "cgrtDestSIOctetsIn"), ("CISCO-ITP-GRT-MIB", "cgrtDestSIDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtDestSIGroup = ciscoGrtDestSIGroup.setStatus('current')
ciscoGrtOrigSIGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 10)).setObjects(("CISCO-ITP-GRT-MIB", "cgrtOrigSIMSUs"), ("CISCO-ITP-GRT-MIB", "cgrtOrigSIOctets"), ("CISCO-ITP-GRT-MIB", "cgrtOrigSIDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtOrigSIGroup = ciscoGrtOrigSIGroup.setStatus('current')
ciscoGrtNotificationsGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 11)).setObjects(("CISCO-ITP-GRT-MIB", "ciscoGrtRouteTableLoad"), ("CISCO-ITP-GRT-MIB", "ciscoGrtDestStateChangeRev1"), ("CISCO-ITP-GRT-MIB", "ciscoGrtMgmtStateChangeRev1"), ("CISCO-ITP-GRT-MIB", "ciscoGrtNoRouteMSUDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtNotificationsGroupRev1 = ciscoGrtNotificationsGroupRev1.setStatus('current')
ciscoGrtInstGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 12)).setObjects(("CISCO-ITP-GRT-MIB", "cgrtNoRouteMSUsNotifEnabled"), ("CISCO-ITP-GRT-MIB", "cgrtNoRouteMSUsNotifWindowTime"), ("CISCO-ITP-GRT-MIB", "cgrtInstUnknownOrigPCs"), ("CISCO-ITP-GRT-MIB", "cgrtInstNoRouteDrops"), ("CISCO-ITP-GRT-MIB", "cgrtNoRouteMSUsInterval"), ("CISCO-ITP-GRT-MIB", "cgrtIntervalNoRouteMSUs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtInstGroupSup1 = ciscoGrtInstGroupSup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-GRT-MIB", cgrtRouteNotifSuppressed=cgrtRouteNotifSuppressed, cgrtRouteTable=cgrtRouteTable, cgrtDynamicRoutesDropped=cgrtDynamicRoutesDropped, cgrtRouteMaxDynamic=cgrtRouteMaxDynamic, cgrtDestOctetsOut=cgrtDestOctetsOut, cgrtRouteRowStatus=cgrtRouteRowStatus, CgrtDisplayPCSI=CgrtDisplayPCSI, cgrtOrigTableEnabled=cgrtOrigTableEnabled, cgrtInstLastChanged=cgrtInstLastChanged, cgrtRouteQos=cgrtRouteQos, cgrtRouteRestrictedSeconds=cgrtRouteRestrictedSeconds, cgrtDestStatus=cgrtDestStatus, cgrtOrigSIEntry=cgrtOrigSIEntry, ciscoGrtMIBObjects=ciscoGrtMIBObjects, cgrtMgmtNotifEnabledRev1=cgrtMgmtNotifEnabledRev1, cgrtDestCongestionDrops=cgrtDestCongestionDrops, cgrtDestNotifDelayTime=cgrtDestNotifDelayTime, ciscoGrtNoRouteMSUDiscards=ciscoGrtNoRouteMSUDiscards, cgrtDestNotifWindowTimeRev1=cgrtDestNotifWindowTimeRev1, cgrtInstLoadStatus=cgrtInstLoadStatus, ciscoGrtNotificationsGroupRev1=ciscoGrtNotificationsGroupRev1, cgrtDestInaccessibleDrops=cgrtDestInaccessibleDrops, cgrtDynamicRoutes=cgrtDynamicRoutes, cgrtDestMSUsOut=cgrtDestMSUsOut, cgrtDestNotifWindowTime=cgrtDestNotifWindowTime, cgrtDestSIEntry=cgrtDestSIEntry, ciscoGrtMIBCompliances=ciscoGrtMIBCompliances, cgrtNotificationsInfo=cgrtNotificationsInfo, ciscoGrtMIBCompliance=ciscoGrtMIBCompliance, cgrtOrigTable=cgrtOrigTable, cgrtOrigMSUs=cgrtOrigMSUs, cgrtDestSIOctetsIn=cgrtDestSIOctetsIn, cgrtInstNoRouteDrops=cgrtInstNoRouteDrops, cgrtDestNotifSupFlag=cgrtDestNotifSupFlag, cgrtOrigDisplay=cgrtOrigDisplay, cgrtDestTable=cgrtDestTable, cgrtNoRouteMSUsNotifEnabled=cgrtNoRouteMSUsNotifEnabled, cgrtRouteDisplay=cgrtRouteDisplay, cgrtRouteDestLinkset=cgrtRouteDestLinkset, ciscoGrtMgmtStateChange=ciscoGrtMgmtStateChange, cgrtMgmtNotifMaxPerWindowRev1=cgrtMgmtNotifMaxPerWindowRev1, ciscoGrtMIBComplianceRev1=ciscoGrtMIBComplianceRev1, ciscoGrtDestStateChangeRev1=ciscoGrtDestStateChangeRev1, cgrtMgmtNotifDelayTime=cgrtMgmtNotifDelayTime, cgrtRouteMask=cgrtRouteMask, cgrtNoRouteMSUsInterval=cgrtNoRouteMSUsInterval, PYSNMP_MODULE_ID=ciscoGrtMIB, cgrtRouteStatus=cgrtRouteStatus, cgrtInstUnknownOrigPCs=cgrtInstUnknownOrigPCs, ciscoGrtMIBConform=ciscoGrtMIBConform, ciscoGrtNotifications=ciscoGrtNotifications, cgrtMgmtNotifMaxPerWindow=cgrtMgmtNotifMaxPerWindow, ciscoGrtRouteGroup=ciscoGrtRouteGroup, cgrtRouteMgmtStatus=cgrtRouteMgmtStatus, cgrtDestInaccessibleSeconds=cgrtDestInaccessibleSeconds, cgrtInstTable=cgrtInstTable, cgrtInstTableName=cgrtInstTableName, cgrtOrigPC=cgrtOrigPC, cgrtInstNumberDestinations=cgrtInstNumberDestinations, cgrtDestSIMSUsIn=cgrtDestSIMSUsIn, cgrtDestNotifMaxPerWindow=cgrtDestNotifMaxPerWindow, cgrtMgmtNotifChanges=cgrtMgmtNotifChanges, cgrtDestRestrictedSeconds=cgrtDestRestrictedSeconds, ciscoGrtDestGroupRev1=ciscoGrtDestGroupRev1, cgrtDestNotifMaxPerWindowRev1=cgrtDestNotifMaxPerWindowRev1, cgrtInstLastLoadTime=cgrtInstLastLoadTime, cgrtDestSIOctetsOut=cgrtDestSIOctetsOut, cgrtDestMSUsIn=cgrtDestMSUsIn, ciscoGrtOrigSIGroup=ciscoGrtOrigSIGroup, cgrtOrigSIDisplay=cgrtOrigSIDisplay, ciscoGrtRouteTableLoad=ciscoGrtRouteTableLoad, cgrtRouteEntry=cgrtRouteEntry, cgrtDestSIDisplay=cgrtDestSIDisplay, cgrtOrigSIOctets=cgrtOrigSIOctets, cgrtRouteType=cgrtRouteType, ciscoGrtMIBGroups=ciscoGrtMIBGroups, ciscoGrtMIB=ciscoGrtMIB, cgrtObjects=cgrtObjects, cgrtOrigSIMSUs=cgrtOrigSIMSUs, ciscoGrtInstGroup=ciscoGrtInstGroup, cgrtPCStatsInterval=cgrtPCStatsInterval, cgrtNoRouteMSUsNotifWindowTime=cgrtNoRouteMSUsNotifWindowTime, cgrtIntervalNoRouteMSUs=cgrtIntervalNoRouteMSUs, cgrtOrigEntry=cgrtOrigEntry, cgrtDestOctetsIn=cgrtDestOctetsIn, cgrtInstNumberRoutes=cgrtInstNumberRoutes, cgrtMgmtNotifEnabled=cgrtMgmtNotifEnabled, cgrtDestCongestion=cgrtDestCongestion, cgrtDestDisplay=cgrtDestDisplay, ciscoGrtRouteGroupRev1=ciscoGrtRouteGroupRev1, cgrtDestEntry=cgrtDestEntry, cgrtMtp3SI=cgrtMtp3SI, cgrtInstLastURL=cgrtInstLastURL, cgrtRouteDestLsCost=cgrtRouteDestLsCost, cgrtRouteAdminStatus=cgrtRouteAdminStatus, cgrtMgmtNotifWindowTimeRev1=cgrtMgmtNotifWindowTimeRev1, ciscoGrtOrigGroup=ciscoGrtOrigGroup, cgrtRouteProhibitedSeconds=cgrtRouteProhibitedSeconds, cgrtOrigOctets=cgrtOrigOctets, cgrtOrigSITable=cgrtOrigSITable, ciscoGrtDestStateChange=ciscoGrtDestStateChange, cgrtRouteTableLoadNotifEnabled=cgrtRouteTableLoadNotifEnabled, cgrtDestNotifEnabled=cgrtDestNotifEnabled, cgrtRouteDpc=cgrtRouteDpc, cgrtDestNotifEnabledRev1=cgrtDestNotifEnabledRev1, cgrtDestRestrictedMSUs=cgrtDestRestrictedMSUs, cgrtInstEntry=cgrtInstEntry, cgrtDestSIMSUsOut=cgrtDestSIMSUsOut, cgrtMgmtNotifSupFlag=cgrtMgmtNotifSupFlag, ciscoGrtMgmtStateChangeRev1=ciscoGrtMgmtStateChangeRev1, cgrtRouteDynamic=cgrtRouteDynamic, cgrtDestAccessibleSeconds=cgrtDestAccessibleSeconds, ciscoGrtInstGroupSup1=ciscoGrtInstGroupSup1, cgrtMgmtNotifWindowTime=cgrtMgmtNotifWindowTime, cgrtDestNotifChanges=cgrtDestNotifChanges, ciscoGrtScalarsGroup=ciscoGrtScalarsGroup, ciscoGrtDestSIGroup=ciscoGrtDestSIGroup, ciscoGrtDestGroup=ciscoGrtDestGroup, ciscoGrtNotificationsGroup=ciscoGrtNotificationsGroup, cgrtDestSITable=cgrtDestSITable, cgrtRouteAllowedSeconds=cgrtRouteAllowedSeconds, cgrtScalars=cgrtScalars, cgrtDestNotifSuppressed=cgrtDestNotifSuppressed)