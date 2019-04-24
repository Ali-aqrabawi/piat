#
# PySNMP MIB module CISCO-FSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-FSPF-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:29:30 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
DomainIdOrZero, DomainId = mibBuilder.importSymbols("CISCO-ST-TC", "DomainIdOrZero", "DomainId")
CiscoMilliSeconds, TimeIntervalSec, TimeIntervalMin = mibBuilder.importSymbols("CISCO-TC", "CiscoMilliSeconds", "TimeIntervalSec", "TimeIntervalMin")
notifyVsanIndex, vsanIndex = mibBuilder.importSymbols("CISCO-VSAN-MIB", "notifyVsanIndex", "vsanIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, IpAddress, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, iso, ModuleIdentity, Counter32, TimeTicks, MibIdentifier, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "iso", "ModuleIdentity", "Counter32", "TimeTicks", "MibIdentifier", "Gauge32", "NotificationType")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
ciscoFspfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 287))
ciscoFspfMIB.setRevisions(('2003-10-08 00:00', '2003-04-13 00:00', '2003-02-21 00:00', '2002-11-21 00:00', '2002-11-01 00:00', '2002-10-04 00:00',))
if mibBuilder.loadTexts: ciscoFspfMIB.setLastUpdated('200310080000Z')
if mibBuilder.loadTexts: ciscoFspfMIB.setOrganization('Cisco Systems Inc. ')
fspfConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 287, 1))
fspfDatabase = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 287, 2))
fspfNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 287, 3))
fspfNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 287, 3, 0))
fspfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 287, 4))
class FspfRegionId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class FspfLsrType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class FspfLinkType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class FspfInterfaceState(TextualConvention, Integer32):
    reference = 'FC-SW2, Switch Fabric-2, Rev 5.4, June 26, 2001, section 8.7 .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("down", 1), ("init", 2), ("dbExchange", 3), ("dbAckwait", 4), ("dbWait", 5), ("full", 6))

class LastCreationTime(TextualConvention, TimeTicks):
    status = 'current'

fspfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1), )
if mibBuilder.loadTexts: fspfTable.setStatus('current')
fspfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: fspfEntry.setStatus('current')
fspfRegionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 1), FspfRegionId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfRegionId.setStatus('current')
fspfDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 2), DomainId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfDomainId.setStatus('current')
fspfSpfDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 3), TimeIntervalSec()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfSpfDelay.setStatus('current')
fspfSpfHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 4), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('MilliSeconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfSpfHoldTime.setStatus('current')
fspfMinLsArrival = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 5), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1000)).setUnits('MilliSeconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfMinLsArrival.setStatus('current')
fspfMinLsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 6), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(5000)).setUnits('MilliSeconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfMinLsInterval.setStatus('current')
fspfLsRefreshTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 7), TimeIntervalMin()).setUnits('Minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsRefreshTime.setStatus('current')
fspfMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 8), TimeIntervalMin()).setUnits('Minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfMaxAge.setStatus('current')
fspfMaxAgeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfMaxAgeCount.setStatus('current')
fspfSpfComputations = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfSpfComputations.setStatus('current')
fspfChecksumErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfChecksumErrors.setStatus('current')
fspfLsuRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsuRxPkts.setStatus('current')
fspfLsaRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsaRxPkts.setStatus('current')
fspfLsuTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsuTxPkts.setStatus('current')
fspfLsaTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsaTxPkts.setStatus('current')
fspfHelloTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfHelloTxPkts.setStatus('current')
fspfHelloRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfHelloRxPkts.setStatus('current')
fspfRetransmittedLsuTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfRetransmittedLsuTxPkts.setStatus('current')
fspfErrorRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfErrorRxPkts.setStatus('current')
fspfLsrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsrs.setStatus('current')
fspfCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 21), LastCreationTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfCreateTime.setStatus('current')
fspfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfAdminStatus.setStatus('current')
fspfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfOperStatus.setStatus('current')
fspfSetToDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("noOp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfSetToDefault.setStatus('current')
fspfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfRowStatus.setStatus('current')
fspfTotalCheckSum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 26), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfTotalCheckSum.setStatus('current')
fspfIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2), )
if mibBuilder.loadTexts: fspfIfTable.setStatus('current')
fspfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fspfIfEntry.setStatus('current')
fspfIfCost = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfIfCost.setStatus('current')
fspfIfHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 2), TimeIntervalSec().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(20)).setUnits('Seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfIfHelloInterval.setStatus('current')
fspfIfDeadInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 3), TimeIntervalSec().subtype(subtypeSpec=ValueRangeConstraint(2, 65535)).clone(80)).setUnits('Seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfIfDeadInterval.setStatus('current')
fspfIfRetransmitInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 4), TimeIntervalSec().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(5)).setUnits('Seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfIfRetransmitInterval.setStatus('current')
fspfIfLsuRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfLsuRxPkts.setStatus('current')
fspfIfLsaRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfLsaRxPkts.setStatus('current')
fspfIfLsuTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfLsuTxPkts.setStatus('current')
fspfIfLsaTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfLsaTxPkts.setStatus('current')
fspfIfHelloTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfHelloTxPkts.setStatus('current')
fspfIfHelloRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfHelloRxPkts.setStatus('current')
fspfIfRetransmittedLsuTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfRetransmittedLsuTxPkts.setStatus('current')
fspfIfErrorRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfErrorRxPkts.setStatus('current')
fspfIfInactivityExpirations = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfInactivityExpirations.setStatus('current')
fspfIfNbrState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 14), FspfInterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfNbrState.setStatus('current')
fspfIfNbrDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 15), DomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfNbrDomainId.setStatus('current')
fspfIfNbrPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfNbrPortIndex.setStatus('current')
fspfIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfIfAdminStatus.setStatus('current')
fspfIfCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 18), LastCreationTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfIfCreateTime.setStatus('current')
fspfIfSetToDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("noOp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfIfSetToDefault.setStatus('current')
fspfIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fspfIfRowStatus.setStatus('current')
fspfLsrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1), )
if mibBuilder.loadTexts: fspfLsrTable.setStatus('current')
fspfLsrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FSPF-MIB", "fspfLsrDomainId"), (0, "CISCO-FSPF-MIB", "fspfLsrType"))
if mibBuilder.loadTexts: fspfLsrEntry.setStatus('current')
fspfLsrDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 1), DomainId())
if mibBuilder.loadTexts: fspfLsrDomainId.setStatus('current')
fspfLsrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 2), FspfLsrType())
if mibBuilder.loadTexts: fspfLsrType.setStatus('current')
fspfLsrAdvDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 3), DomainId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsrAdvDomainId.setStatus('current')
fspfLsrAge = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 4), TimeIntervalSec().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsrAge.setStatus('current')
fspfLsrIncarnationNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsrIncarnationNumber.setStatus('current')
fspfLsrCheckSum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsrCheckSum.setStatus('current')
fspfLsrLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65355))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsrLinks.setStatus('current')
fspfLsrExternal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsrExternal.setStatus('current')
fspfLinkTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2), )
if mibBuilder.loadTexts: fspfLinkTable.setStatus('current')
fspfLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FSPF-MIB", "fspfLsrDomainId"), (0, "CISCO-FSPF-MIB", "fspfLsrType"), (0, "CISCO-FSPF-MIB", "fspfLinkIndex"))
if mibBuilder.loadTexts: fspfLinkEntry.setStatus('current')
fspfLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: fspfLinkIndex.setStatus('current')
fspfLinkNbrDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 2), DomainId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLinkNbrDomainId.setStatus('current')
fspfLinkPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLinkPortIndex.setStatus('current')
fspfLinkNbrPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLinkNbrPortIndex.setStatus('current')
fspfLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 5), FspfLinkType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLinkType.setStatus('current')
fspfLinkCost = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLinkCost.setStatus('current')
fspfLsrNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLsrNumber.setStatus('current')
fspfLinkNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fspfLinkNumber.setStatus('current')
fspfNbrStateChangeNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fspfNbrStateChangeNotifyEnable.setStatus('current')
fspfIfPrevNbrState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 4), FspfInterfaceState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fspfIfPrevNbrState.setStatus('current')
fspfNbrStateChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 287, 3, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-FSPF-MIB", "fspfDomainId"), ("CISCO-FSPF-MIB", "fspfIfNbrDomainId"), ("CISCO-FSPF-MIB", "fspfIfNbrState"), ("CISCO-FSPF-MIB", "fspfIfPrevNbrState"))
if mibBuilder.loadTexts: fspfNbrStateChangeNotify.setStatus('current')
fspfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 1))
fspfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2))
fspfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 1, 1)).setObjects(("CISCO-FSPF-MIB", "fspfGenericGroup"), ("CISCO-FSPF-MIB", "fspfIfGroup"), ("CISCO-FSPF-MIB", "fspfDatabaseGroup"), ("CISCO-FSPF-MIB", "fspfNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfMIBCompliance = fspfMIBCompliance.setStatus('deprecated')
fspfMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 1, 2)).setObjects(("CISCO-FSPF-MIB", "fspfGenericGroupRev1"), ("CISCO-FSPF-MIB", "fspfIfGroup"), ("CISCO-FSPF-MIB", "fspfDatabaseGroup"), ("CISCO-FSPF-MIB", "fspfNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfMIBCompliance1 = fspfMIBCompliance1.setStatus('deprecated')
fspfMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 1, 3)).setObjects(("CISCO-FSPF-MIB", "fspfGenericGroupRev1"), ("CISCO-FSPF-MIB", "fspfIfGroup"), ("CISCO-FSPF-MIB", "fspfDatabaseGroupRev1"), ("CISCO-FSPF-MIB", "fspfNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfMIBCompliance2 = fspfMIBCompliance2.setStatus('deprecated')
fspfMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 1, 4)).setObjects(("CISCO-FSPF-MIB", "fspfGenericGroupRev1"), ("CISCO-FSPF-MIB", "fspfIfGroup"), ("CISCO-FSPF-MIB", "fspfDatabaseGroupRev2"), ("CISCO-FSPF-MIB", "fspfNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfMIBCompliance3 = fspfMIBCompliance3.setStatus('current')
fspfGenericGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 1)).setObjects(("CISCO-FSPF-MIB", "fspfRegionId"), ("CISCO-FSPF-MIB", "fspfDomainId"), ("CISCO-FSPF-MIB", "fspfSpfDelay"), ("CISCO-FSPF-MIB", "fspfSpfHoldTime"), ("CISCO-FSPF-MIB", "fspfMinLsArrival"), ("CISCO-FSPF-MIB", "fspfMinLsInterval"), ("CISCO-FSPF-MIB", "fspfLsRefreshTime"), ("CISCO-FSPF-MIB", "fspfMaxAge"), ("CISCO-FSPF-MIB", "fspfMaxAgeCount"), ("CISCO-FSPF-MIB", "fspfSpfComputations"), ("CISCO-FSPF-MIB", "fspfChecksumErrors"), ("CISCO-FSPF-MIB", "fspfLsuRxPkts"), ("CISCO-FSPF-MIB", "fspfLsaRxPkts"), ("CISCO-FSPF-MIB", "fspfLsuTxPkts"), ("CISCO-FSPF-MIB", "fspfLsaTxPkts"), ("CISCO-FSPF-MIB", "fspfHelloTxPkts"), ("CISCO-FSPF-MIB", "fspfHelloRxPkts"), ("CISCO-FSPF-MIB", "fspfRetransmittedLsuTxPkts"), ("CISCO-FSPF-MIB", "fspfErrorRxPkts"), ("CISCO-FSPF-MIB", "fspfLsrs"), ("CISCO-FSPF-MIB", "fspfCreateTime"), ("CISCO-FSPF-MIB", "fspfAdminStatus"), ("CISCO-FSPF-MIB", "fspfOperStatus"), ("CISCO-FSPF-MIB", "fspfSetToDefault"), ("CISCO-FSPF-MIB", "fspfRowStatus"), ("CISCO-FSPF-MIB", "fspfNbrStateChangeNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfGenericGroup = fspfGenericGroup.setStatus('deprecated')
fspfIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 3)).setObjects(("CISCO-FSPF-MIB", "fspfIfCost"), ("CISCO-FSPF-MIB", "fspfIfHelloInterval"), ("CISCO-FSPF-MIB", "fspfIfDeadInterval"), ("CISCO-FSPF-MIB", "fspfIfRetransmitInterval"), ("CISCO-FSPF-MIB", "fspfIfLsuRxPkts"), ("CISCO-FSPF-MIB", "fspfIfLsaRxPkts"), ("CISCO-FSPF-MIB", "fspfIfLsuTxPkts"), ("CISCO-FSPF-MIB", "fspfIfLsaTxPkts"), ("CISCO-FSPF-MIB", "fspfIfHelloTxPkts"), ("CISCO-FSPF-MIB", "fspfIfHelloRxPkts"), ("CISCO-FSPF-MIB", "fspfIfRetransmittedLsuTxPkts"), ("CISCO-FSPF-MIB", "fspfIfErrorRxPkts"), ("CISCO-FSPF-MIB", "fspfIfInactivityExpirations"), ("CISCO-FSPF-MIB", "fspfIfNbrState"), ("CISCO-FSPF-MIB", "fspfIfNbrDomainId"), ("CISCO-FSPF-MIB", "fspfIfNbrPortIndex"), ("CISCO-FSPF-MIB", "fspfIfAdminStatus"), ("CISCO-FSPF-MIB", "fspfIfCreateTime"), ("CISCO-FSPF-MIB", "fspfIfSetToDefault"), ("CISCO-FSPF-MIB", "fspfIfRowStatus"), ("CISCO-FSPF-MIB", "fspfIfPrevNbrState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfIfGroup = fspfIfGroup.setStatus('current')
fspfDatabaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 4)).setObjects(("CISCO-FSPF-MIB", "fspfLsrAdvDomainId"), ("CISCO-FSPF-MIB", "fspfLsrAge"), ("CISCO-FSPF-MIB", "fspfLsrIncarnationNumber"), ("CISCO-FSPF-MIB", "fspfLsrCheckSum"), ("CISCO-FSPF-MIB", "fspfLsrLinks"), ("CISCO-FSPF-MIB", "fspfLinkNbrDomainId"), ("CISCO-FSPF-MIB", "fspfLinkPortIndex"), ("CISCO-FSPF-MIB", "fspfLinkNbrPortIndex"), ("CISCO-FSPF-MIB", "fspfLinkType"), ("CISCO-FSPF-MIB", "fspfLinkCost"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfDatabaseGroup = fspfDatabaseGroup.setStatus('deprecated')
fspfNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 5)).setObjects(("CISCO-FSPF-MIB", "fspfNbrStateChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfNotificationGroup = fspfNotificationGroup.setStatus('current')
fspfGenericGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 6)).setObjects(("CISCO-FSPF-MIB", "fspfRegionId"), ("CISCO-FSPF-MIB", "fspfDomainId"), ("CISCO-FSPF-MIB", "fspfSpfDelay"), ("CISCO-FSPF-MIB", "fspfSpfHoldTime"), ("CISCO-FSPF-MIB", "fspfMinLsArrival"), ("CISCO-FSPF-MIB", "fspfMinLsInterval"), ("CISCO-FSPF-MIB", "fspfLsRefreshTime"), ("CISCO-FSPF-MIB", "fspfMaxAge"), ("CISCO-FSPF-MIB", "fspfMaxAgeCount"), ("CISCO-FSPF-MIB", "fspfSpfComputations"), ("CISCO-FSPF-MIB", "fspfChecksumErrors"), ("CISCO-FSPF-MIB", "fspfLsuRxPkts"), ("CISCO-FSPF-MIB", "fspfLsaRxPkts"), ("CISCO-FSPF-MIB", "fspfLsuTxPkts"), ("CISCO-FSPF-MIB", "fspfLsaTxPkts"), ("CISCO-FSPF-MIB", "fspfHelloTxPkts"), ("CISCO-FSPF-MIB", "fspfHelloRxPkts"), ("CISCO-FSPF-MIB", "fspfRetransmittedLsuTxPkts"), ("CISCO-FSPF-MIB", "fspfErrorRxPkts"), ("CISCO-FSPF-MIB", "fspfLsrs"), ("CISCO-FSPF-MIB", "fspfCreateTime"), ("CISCO-FSPF-MIB", "fspfAdminStatus"), ("CISCO-FSPF-MIB", "fspfOperStatus"), ("CISCO-FSPF-MIB", "fspfSetToDefault"), ("CISCO-FSPF-MIB", "fspfRowStatus"), ("CISCO-FSPF-MIB", "fspfTotalCheckSum"), ("CISCO-FSPF-MIB", "fspfNbrStateChangeNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfGenericGroupRev1 = fspfGenericGroupRev1.setStatus('current')
fspfDatabaseGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 7)).setObjects(("CISCO-FSPF-MIB", "fspfLsrAdvDomainId"), ("CISCO-FSPF-MIB", "fspfLsrAge"), ("CISCO-FSPF-MIB", "fspfLsrIncarnationNumber"), ("CISCO-FSPF-MIB", "fspfLsrCheckSum"), ("CISCO-FSPF-MIB", "fspfLsrLinks"), ("CISCO-FSPF-MIB", "fspfLinkNbrDomainId"), ("CISCO-FSPF-MIB", "fspfLinkPortIndex"), ("CISCO-FSPF-MIB", "fspfLinkNbrPortIndex"), ("CISCO-FSPF-MIB", "fspfLinkType"), ("CISCO-FSPF-MIB", "fspfLinkCost"), ("CISCO-FSPF-MIB", "fspfLsrNumber"), ("CISCO-FSPF-MIB", "fspfLinkNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfDatabaseGroupRev1 = fspfDatabaseGroupRev1.setStatus('deprecated')
fspfDatabaseGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 8)).setObjects(("CISCO-FSPF-MIB", "fspfLsrAdvDomainId"), ("CISCO-FSPF-MIB", "fspfLsrAge"), ("CISCO-FSPF-MIB", "fspfLsrIncarnationNumber"), ("CISCO-FSPF-MIB", "fspfLsrCheckSum"), ("CISCO-FSPF-MIB", "fspfLsrLinks"), ("CISCO-FSPF-MIB", "fspfLinkNbrDomainId"), ("CISCO-FSPF-MIB", "fspfLinkPortIndex"), ("CISCO-FSPF-MIB", "fspfLinkNbrPortIndex"), ("CISCO-FSPF-MIB", "fspfLinkType"), ("CISCO-FSPF-MIB", "fspfLinkCost"), ("CISCO-FSPF-MIB", "fspfLsrNumber"), ("CISCO-FSPF-MIB", "fspfLinkNumber"), ("CISCO-FSPF-MIB", "fspfLsrExternal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspfDatabaseGroupRev2 = fspfDatabaseGroupRev2.setStatus('current')
mibBuilder.exportSymbols("CISCO-FSPF-MIB", fspfLinkCost=fspfLinkCost, fspfCreateTime=fspfCreateTime, fspfLsrIncarnationNumber=fspfLsrIncarnationNumber, FspfRegionId=FspfRegionId, fspfLsrs=fspfLsrs, fspfHelloRxPkts=fspfHelloRxPkts, fspfDatabaseGroupRev2=fspfDatabaseGroupRev2, fspfLsrAdvDomainId=fspfLsrAdvDomainId, fspfIfEntry=fspfIfEntry, fspfIfHelloTxPkts=fspfIfHelloTxPkts, fspfIfNbrDomainId=fspfIfNbrDomainId, fspfLinkNumber=fspfLinkNumber, fspfGenericGroupRev1=fspfGenericGroupRev1, fspfIfLsuRxPkts=fspfIfLsuRxPkts, fspfSpfHoldTime=fspfSpfHoldTime, fspfSpfComputations=fspfSpfComputations, fspfChecksumErrors=fspfChecksumErrors, fspfIfGroup=fspfIfGroup, fspfNbrStateChangeNotifyEnable=fspfNbrStateChangeNotifyEnable, fspfNbrStateChangeNotify=fspfNbrStateChangeNotify, fspfLinkTable=fspfLinkTable, fspfIfLsuTxPkts=fspfIfLsuTxPkts, fspfIfErrorRxPkts=fspfIfErrorRxPkts, fspfIfSetToDefault=fspfIfSetToDefault, fspfDatabase=fspfDatabase, fspfIfLsaRxPkts=fspfIfLsaRxPkts, fspfIfTable=fspfIfTable, fspfLinkEntry=fspfLinkEntry, fspfDatabaseGroup=fspfDatabaseGroup, fspfIfPrevNbrState=fspfIfPrevNbrState, fspfLsuTxPkts=fspfLsuTxPkts, fspfRowStatus=fspfRowStatus, fspfLsrAge=fspfLsrAge, fspfLsrDomainId=fspfLsrDomainId, fspfDomainId=fspfDomainId, fspfLinkPortIndex=fspfLinkPortIndex, fspfNotification=fspfNotification, fspfIfCost=fspfIfCost, fspfLinkNbrPortIndex=fspfLinkNbrPortIndex, LastCreationTime=LastCreationTime, fspfAdminStatus=fspfAdminStatus, fspfLsrExternal=fspfLsrExternal, fspfNotificationPrefix=fspfNotificationPrefix, fspfLinkType=fspfLinkType, fspfIfAdminStatus=fspfIfAdminStatus, fspfMinLsArrival=fspfMinLsArrival, fspfDatabaseGroupRev1=fspfDatabaseGroupRev1, fspfIfRowStatus=fspfIfRowStatus, fspfLsaTxPkts=fspfLsaTxPkts, fspfLsRefreshTime=fspfLsRefreshTime, fspfMIBCompliances=fspfMIBCompliances, fspfMIBCompliance1=fspfMIBCompliance1, fspfRegionId=fspfRegionId, fspfLsrTable=fspfLsrTable, fspfLinkNbrDomainId=fspfLinkNbrDomainId, FspfLsrType=FspfLsrType, fspfLsrEntry=fspfLsrEntry, fspfLsrCheckSum=fspfLsrCheckSum, fspfIfLsaTxPkts=fspfIfLsaTxPkts, FspfInterfaceState=FspfInterfaceState, fspfSpfDelay=fspfSpfDelay, fspfMaxAge=fspfMaxAge, fspfMaxAgeCount=fspfMaxAgeCount, fspfIfNbrState=fspfIfNbrState, fspfSetToDefault=fspfSetToDefault, fspfMIBCompliance=fspfMIBCompliance, fspfHelloTxPkts=fspfHelloTxPkts, fspfRetransmittedLsuTxPkts=fspfRetransmittedLsuTxPkts, fspfIfInactivityExpirations=fspfIfInactivityExpirations, fspfNotificationGroup=fspfNotificationGroup, fspfIfDeadInterval=fspfIfDeadInterval, fspfLsuRxPkts=fspfLsuRxPkts, fspfLsrLinks=fspfLsrLinks, fspfMIBCompliance3=fspfMIBCompliance3, fspfErrorRxPkts=fspfErrorRxPkts, fspfIfHelloInterval=fspfIfHelloInterval, PYSNMP_MODULE_ID=ciscoFspfMIB, fspfTable=fspfTable, fspfConfiguration=fspfConfiguration, fspfLsrNumber=fspfLsrNumber, fspfLsrType=fspfLsrType, fspfIfNbrPortIndex=fspfIfNbrPortIndex, fspfLinkIndex=fspfLinkIndex, fspfMIBGroups=fspfMIBGroups, fspfEntry=fspfEntry, fspfMinLsInterval=fspfMinLsInterval, ciscoFspfMIB=ciscoFspfMIB, fspfOperStatus=fspfOperStatus, fspfIfCreateTime=fspfIfCreateTime, fspfTotalCheckSum=fspfTotalCheckSum, fspfLsaRxPkts=fspfLsaRxPkts, fspfIfRetransmitInterval=fspfIfRetransmitInterval, fspfMIBCompliance2=fspfMIBCompliance2, fspfIfRetransmittedLsuTxPkts=fspfIfRetransmittedLsuTxPkts, fspfMIBConformance=fspfMIBConformance, fspfIfHelloRxPkts=fspfIfHelloRxPkts, FspfLinkType=FspfLinkType, fspfGenericGroup=fspfGenericGroup)
