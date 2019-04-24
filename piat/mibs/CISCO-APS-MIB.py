#
# PySNMP MIB module CISCO-APS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-APS-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:39:27 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, Counter64, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, IpAddress, transmission, iso, Bits, MibIdentifier, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "IpAddress", "transmission", "iso", "Bits", "MibIdentifier", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
RowStatus, TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TimeStamp")
cApsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 71))
cApsMIB.setRevisions(('2001-12-26 12:00', '2001-04-29 00:00',))
if mibBuilder.loadTexts: cApsMIB.setLastUpdated('200112261200Z')
if mibBuilder.loadTexts: cApsMIB.setOrganization('Cisco Systems, inc')
cApsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 71, 1))
cApsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 71, 2))
cApsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 71, 3))
class CApsK1K2(TextualConvention, OctetString):
    reference = 'Bellcore (Telcordia Technologies) GR-253-CORE, Issue 2,Revision 2 (January 1999), 5.3.5.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class CApsSwitchCommand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noCmd", 1), ("clear", 2), ("lockoutOfProtection", 3), ("forcedSwitchWorkToProtect", 4), ("forcedSwitchProtectToWork", 5), ("manualSwitchWorkToProtect", 6), ("manualSwitchProtectToWork", 7), ("exercise", 8))

class CApsControlCommand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noCmd", 1), ("lockoutWorkingChannel", 2), ("clearLockoutWorkingChannel", 3))

cApsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1))
cApsConfigGroups = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsConfigGroups.setStatus('current')
cApsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2), )
if mibBuilder.loadTexts: cApsConfigTable.setStatus('current')
cApsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1), ).setIndexNames((1, "CISCO-APS-MIB", "cApsConfigName"))
if mibBuilder.loadTexts: cApsConfigEntry.setStatus('current')
cApsConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cApsConfigName.setStatus('current')
cApsConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigRowStatus.setStatus('current')
cApsConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("onePlusOne", 1), ("oneToN", 2), ("onePlusOneCompatible", 3), ("onePlusOneOptimized", 4))).clone('onePlusOne')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMode.setStatus('current')
cApsConfigRevert = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nonrevertive", 1), ("revertive", 2))).clone('nonrevertive')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigRevert.setStatus('current')
cApsConfigDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unidirectional", 1), ("bidirectional", 2))).clone('unidirectional')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigDirection.setStatus('current')
cApsConfigExtraTraffic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigExtraTraffic.setStatus('current')
cApsConfigSdBerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 9)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigSdBerThreshold.setStatus('current')
cApsConfigSfBerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 5)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigSfBerThreshold.setStatus('current')
cApsConfigWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 720)).clone(300)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigWaitToRestore.setStatus('current')
cApsConfigCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsConfigCreationTime.setStatus('current')
cApsStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2), )
if mibBuilder.loadTexts: cApsStatusTable.setStatus('current')
cApsStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1), ).setIndexNames((1, "CISCO-APS-MIB", "cApsConfigName"))
if mibBuilder.loadTexts: cApsStatusEntry.setStatus('current')
cApsStatusK1K2Rcv = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 1), CApsK1K2()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusK1K2Rcv.setStatus('current')
cApsStatusK1K2Trans = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 2), CApsK1K2()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusK1K2Trans.setStatus('current')
cApsStatusCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 3), Bits().clone(namedValues=NamedValues(("modeMismatch", 0), ("channelMismatch", 1), ("psbf", 2), ("feplf", 3), ("extraTraffic", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusCurrent.setStatus('current')
cApsStatusModeMismatches = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusModeMismatches.setStatus('current')
cApsStatusChannelMismatches = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusChannelMismatches.setStatus('current')
cApsStatusPSBFs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusPSBFs.setStatus('current')
cApsStatusFEPLFs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusFEPLFs.setStatus('current')
cApsStatusSwitchedChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusSwitchedChannel.setStatus('current')
cApsMap = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3))
cApsChanLTEs = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanLTEs.setStatus('current')
cApsMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 2), )
if mibBuilder.loadTexts: cApsMapTable.setStatus('current')
cApsMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-APS-MIB", "cApsMapIfIndex"))
if mibBuilder.loadTexts: cApsMapEntry.setStatus('current')
cApsMapIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cApsMapIfIndex.setStatus('current')
cApsMapGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsMapGroupName.setStatus('current')
cApsMapChanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsMapChanNumber.setStatus('current')
cApsChanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4), )
if mibBuilder.loadTexts: cApsChanConfigTable.setStatus('current')
cApsChanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1), ).setIndexNames((0, "CISCO-APS-MIB", "cApsChanConfigGroupName"), (0, "CISCO-APS-MIB", "cApsChanConfigNumber"))
if mibBuilder.loadTexts: cApsChanConfigEntry.setStatus('current')
cApsChanConfigGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cApsChanConfigGroupName.setStatus('current')
cApsChanConfigNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 14)))
if mibBuilder.loadTexts: cApsChanConfigNumber.setStatus('current')
cApsChanConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsChanConfigRowStatus.setStatus('current')
cApsChanConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsChanConfigIfIndex.setStatus('current')
cApsChanConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2))).clone('low')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsChanConfigPriority.setStatus('current')
cApsCommandTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 5), )
if mibBuilder.loadTexts: cApsCommandTable.setStatus('current')
cApsCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 5, 1), ).setIndexNames((0, "CISCO-APS-MIB", "cApsChanConfigGroupName"), (0, "CISCO-APS-MIB", "cApsChanConfigNumber"))
if mibBuilder.loadTexts: cApsCommandEntry.setStatus('current')
cApsCommandSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 5, 1, 1), CApsSwitchCommand()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cApsCommandSwitch.setStatus('current')
cApsCommandControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 5, 1, 2), CApsControlCommand()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cApsCommandControl.setStatus('current')
cApsChanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6), )
if mibBuilder.loadTexts: cApsChanStatusTable.setStatus('current')
cApsChanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1), ).setIndexNames((0, "CISCO-APS-MIB", "cApsChanConfigGroupName"), (0, "CISCO-APS-MIB", "cApsChanConfigNumber"))
if mibBuilder.loadTexts: cApsChanStatusEntry.setStatus('current')
cApsChanStatusCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 1), Bits().clone(namedValues=NamedValues(("lockedOut", 0), ("sd", 1), ("sf", 2), ("switched", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanStatusCurrent.setStatus('current')
cApsChanStatusSignalDegrades = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanStatusSignalDegrades.setStatus('current')
cApsChanStatusSignalFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanStatusSignalFailures.setStatus('current')
cApsChanStatusSwitchovers = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanStatusSwitchovers.setStatus('current')
cApsChanStatusLastSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanStatusLastSwitchover.setStatus('current')
cApsChanStatusSwitchoverSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanStatusSwitchoverSeconds.setStatus('current')
cApsNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0))
cApsEventSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0, 1)).setObjects(("CISCO-APS-MIB", "cApsChanStatusSwitchovers"), ("CISCO-APS-MIB", "cApsChanStatusCurrent"))
if mibBuilder.loadTexts: cApsEventSwitchover.setStatus('current')
cApsEventModeMismatch = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0, 2)).setObjects(("CISCO-APS-MIB", "cApsStatusModeMismatches"), ("CISCO-APS-MIB", "cApsStatusCurrent"))
if mibBuilder.loadTexts: cApsEventModeMismatch.setStatus('current')
cApsEventChannelMismatch = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0, 3)).setObjects(("CISCO-APS-MIB", "cApsStatusChannelMismatches"), ("CISCO-APS-MIB", "cApsStatusCurrent"))
if mibBuilder.loadTexts: cApsEventChannelMismatch.setStatus('current')
cApsEventPSBF = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0, 4)).setObjects(("CISCO-APS-MIB", "cApsStatusPSBFs"), ("CISCO-APS-MIB", "cApsStatusCurrent"))
if mibBuilder.loadTexts: cApsEventPSBF.setStatus('current')
cApsEventFEPLF = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0, 5)).setObjects(("CISCO-APS-MIB", "cApsStatusFEPLFs"), ("CISCO-APS-MIB", "cApsStatusCurrent"))
if mibBuilder.loadTexts: cApsEventFEPLF.setStatus('current')
cApsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1))
cApsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 2))
cApsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 2, 1)).setObjects(("CISCO-APS-MIB", "cApsConfigGeneral"), ("CISCO-APS-MIB", "cApsStatusGeneral"), ("CISCO-APS-MIB", "cApsChanGeneral"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsCompliance = cApsCompliance.setStatus('current')
cApsConfigGeneral = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 1)).setObjects(("CISCO-APS-MIB", "cApsConfigMode"), ("CISCO-APS-MIB", "cApsConfigRevert"), ("CISCO-APS-MIB", "cApsConfigDirection"), ("CISCO-APS-MIB", "cApsConfigExtraTraffic"), ("CISCO-APS-MIB", "cApsConfigSdBerThreshold"), ("CISCO-APS-MIB", "cApsConfigSfBerThreshold"), ("CISCO-APS-MIB", "cApsConfigCreationTime"), ("CISCO-APS-MIB", "cApsConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigGeneral = cApsConfigGeneral.setStatus('current')
cApsConfigWtr = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 2)).setObjects(("CISCO-APS-MIB", "cApsConfigWaitToRestore"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigWtr = cApsConfigWtr.setStatus('current')
cApsCommandOnePlusOne = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 3)).setObjects(("CISCO-APS-MIB", "cApsCommandSwitch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsCommandOnePlusOne = cApsCommandOnePlusOne.setStatus('current')
cApsCommandOneToN = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 4)).setObjects(("CISCO-APS-MIB", "cApsCommandSwitch"), ("CISCO-APS-MIB", "cApsCommandControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsCommandOneToN = cApsCommandOneToN.setStatus('current')
cApsStatusGeneral = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 5)).setObjects(("CISCO-APS-MIB", "cApsStatusK1K2Rcv"), ("CISCO-APS-MIB", "cApsStatusK1K2Trans"), ("CISCO-APS-MIB", "cApsStatusCurrent"), ("CISCO-APS-MIB", "cApsStatusModeMismatches"), ("CISCO-APS-MIB", "cApsStatusChannelMismatches"), ("CISCO-APS-MIB", "cApsStatusPSBFs"), ("CISCO-APS-MIB", "cApsStatusFEPLFs"), ("CISCO-APS-MIB", "cApsStatusSwitchedChannel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsStatusGeneral = cApsStatusGeneral.setStatus('current')
cApsChanGeneral = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 6)).setObjects(("CISCO-APS-MIB", "cApsChanConfigIfIndex"), ("CISCO-APS-MIB", "cApsChanConfigRowStatus"), ("CISCO-APS-MIB", "cApsChanStatusCurrent"), ("CISCO-APS-MIB", "cApsChanStatusSignalDegrades"), ("CISCO-APS-MIB", "cApsChanStatusSignalFailures"), ("CISCO-APS-MIB", "cApsChanStatusSwitchovers"), ("CISCO-APS-MIB", "cApsChanStatusLastSwitchover"), ("CISCO-APS-MIB", "cApsChanStatusSwitchoverSeconds"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsChanGeneral = cApsChanGeneral.setStatus('current')
cApsChanOneToN = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 7)).setObjects(("CISCO-APS-MIB", "cApsChanConfigPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsChanOneToN = cApsChanOneToN.setStatus('current')
cApsTotalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 8)).setObjects(("CISCO-APS-MIB", "cApsConfigGroups"), ("CISCO-APS-MIB", "cApsChanLTEs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsTotalsGroup = cApsTotalsGroup.setStatus('current')
cApsMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 9)).setObjects(("CISCO-APS-MIB", "cApsMapGroupName"), ("CISCO-APS-MIB", "cApsMapChanNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsMapGroup = cApsMapGroup.setStatus('current')
cApsEventOptional = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 10)).setObjects(("CISCO-APS-MIB", "cApsEventSwitchover"), ("CISCO-APS-MIB", "cApsEventModeMismatch"), ("CISCO-APS-MIB", "cApsEventChannelMismatch"), ("CISCO-APS-MIB", "cApsEventPSBF"), ("CISCO-APS-MIB", "cApsEventFEPLF"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsEventOptional = cApsEventOptional.setStatus('current')
mibBuilder.exportSymbols("CISCO-APS-MIB", cApsConfigGroups=cApsConfigGroups, cApsEventFEPLF=cApsEventFEPLF, cApsChanStatusTable=cApsChanStatusTable, cApsChanConfigNumber=cApsChanConfigNumber, cApsChanConfigEntry=cApsChanConfigEntry, cApsChanStatusLastSwitchover=cApsChanStatusLastSwitchover, cApsEventChannelMismatch=cApsEventChannelMismatch, cApsMap=cApsMap, cApsStatusPSBFs=cApsStatusPSBFs, cApsChanStatusCurrent=cApsChanStatusCurrent, cApsMIBNotifications=cApsMIBNotifications, cApsMapChanNumber=cApsMapChanNumber, cApsEventPSBF=cApsEventPSBF, CApsSwitchCommand=CApsSwitchCommand, cApsConfigExtraTraffic=cApsConfigExtraTraffic, cApsConfigWtr=cApsConfigWtr, cApsConfigCreationTime=cApsConfigCreationTime, cApsChanConfigIfIndex=cApsChanConfigIfIndex, cApsMapIfIndex=cApsMapIfIndex, cApsStatusModeMismatches=cApsStatusModeMismatches, cApsCommandControl=cApsCommandControl, cApsChanOneToN=cApsChanOneToN, cApsConfigSdBerThreshold=cApsConfigSdBerThreshold, cApsChanStatusEntry=cApsChanStatusEntry, cApsConfigGeneral=cApsConfigGeneral, cApsConfigMode=cApsConfigMode, cApsConfigDirection=cApsConfigDirection, cApsConfigWaitToRestore=cApsConfigWaitToRestore, CApsControlCommand=CApsControlCommand, cApsStatusChannelMismatches=cApsStatusChannelMismatches, cApsChanStatusSwitchoverSeconds=cApsChanStatusSwitchoverSeconds, cApsGroups=cApsGroups, cApsEventOptional=cApsEventOptional, CApsK1K2=CApsK1K2, cApsConfig=cApsConfig, PYSNMP_MODULE_ID=cApsMIB, cApsStatusTable=cApsStatusTable, cApsStatusFEPLFs=cApsStatusFEPLFs, cApsCommandOneToN=cApsCommandOneToN, cApsNotificationsPrefix=cApsNotificationsPrefix, cApsConfigRowStatus=cApsConfigRowStatus, cApsCompliance=cApsCompliance, cApsMIB=cApsMIB, cApsChanConfigPriority=cApsChanConfigPriority, cApsStatusSwitchedChannel=cApsStatusSwitchedChannel, cApsStatusK1K2Trans=cApsStatusK1K2Trans, cApsMIBObjects=cApsMIBObjects, cApsEventModeMismatch=cApsEventModeMismatch, cApsCommandOnePlusOne=cApsCommandOnePlusOne, cApsChanStatusSwitchovers=cApsChanStatusSwitchovers, cApsConfigSfBerThreshold=cApsConfigSfBerThreshold, cApsChanStatusSignalDegrades=cApsChanStatusSignalDegrades, cApsMIBConformance=cApsMIBConformance, cApsTotalsGroup=cApsTotalsGroup, cApsCommandTable=cApsCommandTable, cApsMapGroupName=cApsMapGroupName, cApsStatusCurrent=cApsStatusCurrent, cApsMapEntry=cApsMapEntry, cApsChanConfigRowStatus=cApsChanConfigRowStatus, cApsStatusGeneral=cApsStatusGeneral, cApsChanConfigGroupName=cApsChanConfigGroupName, cApsMapTable=cApsMapTable, cApsEventSwitchover=cApsEventSwitchover, cApsChanGeneral=cApsChanGeneral, cApsChanLTEs=cApsChanLTEs, cApsCompliances=cApsCompliances, cApsConfigRevert=cApsConfigRevert, cApsChanStatusSignalFailures=cApsChanStatusSignalFailures, cApsMapGroup=cApsMapGroup, cApsConfigEntry=cApsConfigEntry, cApsConfigName=cApsConfigName, cApsStatusEntry=cApsStatusEntry, cApsChanConfigTable=cApsChanConfigTable, cApsCommandEntry=cApsCommandEntry, cApsCommandSwitch=cApsCommandSwitch, cApsStatusK1K2Rcv=cApsStatusK1K2Rcv, cApsConfigTable=cApsConfigTable)