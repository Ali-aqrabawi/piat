#
# PySNMP MIB module CISCO-IETF-VDSL-LINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-IETF-VDSL-LINE-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:27:42 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, Counter32, iso, TimeTicks, Counter64, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Unsigned32, IpAddress, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "iso", "TimeTicks", "Counter64", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Unsigned32", "IpAddress", "Integer32", "ObjectIdentity")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
ciscoIetfVdslMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 87))
ciscoIetfVdslMIB.setRevisions(('2002-04-18 00:00',))
if mibBuilder.loadTexts: ciscoIetfVdslMIB.setLastUpdated('200204180000Z')
if mibBuilder.loadTexts: ciscoIetfVdslMIB.setOrganization('Cisco Systems')
cvdslLineMib = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 87, 1))
cvdslMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1))
class CVdslLineCodingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("mcm", 2), ("scm", 3))

class CVdslLineEntity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("vtuc", 1), ("vtur", 2))

cvdslLineTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1), )
if mibBuilder.loadTexts: cvdslLineTable.setStatus('current')
cvdslLineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cvdslLineEntry.setStatus('current')
cvdslLineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1, 1, 1), CVdslLineCodingType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslLineCoding.setStatus('current')
cvdslLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noChannel", 1), ("fastOnly", 2), ("slowOnly", 3), ("either", 4), ("both", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslLineType.setStatus('current')
cvdslLineConfProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvdslLineConfProfile.setStatus('current')
cvdslLineAlarmConfProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvdslLineAlarmConfProfile.setStatus('current')
cvdslPhysTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2), )
if mibBuilder.loadTexts: cvdslPhysTable.setStatus('current')
cvdslPhysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"))
if mibBuilder.loadTexts: cvdslPhysEntry.setStatus('current')
cvdslPhysSide = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 1), CVdslLineEntity())
if mibBuilder.loadTexts: cvdslPhysSide.setStatus('current')
cvdslInvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslInvSerialNumber.setStatus('current')
cvdslInvVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslInvVendorID.setStatus('current')
cvdslInvVersionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslInvVersionNumber.setStatus('current')
cvdslCurrSnrMgn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-640, 640))).setUnits('tenth dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslCurrSnrMgn.setStatus('current')
cvdslCurrAtn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 630))).setUnits('tenth dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslCurrAtn.setStatus('current')
cvdslCurrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 7), Bits().clone(namedValues=NamedValues(("noDefect", 0), ("lossOfFraming", 1), ("lossOfSignal", 2), ("lossOfPower", 3), ("lossOfSignalQuality", 4), ("lossOfLink", 5), ("dataInitFailure", 6), ("configInitFailure", 7), ("protocolInitFailure", 8), ("noPeerVtuPresent", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslCurrStatus.setStatus('current')
cvdslCurrOutputPwr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-310, 310))).setUnits('tenth dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslCurrOutputPwr.setStatus('current')
cvdslCurrAttainableRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 2, 1, 9), Gauge32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslCurrAttainableRate.setStatus('current')
cvdslChanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 3), )
if mibBuilder.loadTexts: cvdslChanTable.setStatus('current')
cvdslChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"))
if mibBuilder.loadTexts: cvdslChanEntry.setStatus('current')
cvdslChanInterleaveDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 3, 1, 1), Gauge32()).setUnits('milli-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslChanInterleaveDelay.setStatus('current')
cvdslChanCrcBlockLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 3, 1, 2), Gauge32()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvdslChanCrcBlockLength.setStatus('current')
cvdslLineConfProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8), )
if mibBuilder.loadTexts: cvdslLineConfProfileTable.setStatus('current')
cvdslLineConfProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1), ).setIndexNames((0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"))
if mibBuilder.loadTexts: cvdslLineConfProfileEntry.setStatus('current')
cvdslLineConfProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvdslLineConfProfileIndex.setStatus('current')
cvdslLineConfProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslLineConfProfileName.setStatus('current')
cvdslLineConfTargetSnrMgn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 310))).setUnits('tenth dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslLineConfTargetSnrMgn.setStatus('current')
cvdslLineConfTxSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslLineConfTxSpeed.setStatus('current')
cvdslLineConfRxSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslLineConfRxSpeed.setStatus('current')
cvdslLineConfProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 8, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslLineConfProfileRowStatus.setStatus('current')
cvdslLineMCMConfProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 9), )
if mibBuilder.loadTexts: cvdslLineMCMConfProfileTable.setStatus('current')
cvdslLineMCMConfProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 9, 1), ).setIndexNames((0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"))
if mibBuilder.loadTexts: cvdslLineMCMConfProfileEntry.setStatus('current')
cvdslMCMConfProfileTxWindowLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setUnits('samples').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileTxWindowLength.setStatus('current')
cvdslMCMConfProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 9, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileRowStatus.setStatus('current')
cvdslLineMCMConfProfileTxBandTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10), )
if mibBuilder.loadTexts: cvdslLineMCMConfProfileTxBandTable.setStatus('current')
cvdslLineMCMConfProfileTxBandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10, 1), ).setIndexNames((0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxBandNumber"))
if mibBuilder.loadTexts: cvdslLineMCMConfProfileTxBandEntry.setStatus('current')
cvdslMCMConfProfileTxBandNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvdslMCMConfProfileTxBandNumber.setStatus('current')
cvdslMCMConfProfileTxBandStart = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileTxBandStart.setStatus('current')
cvdslMCMConfProfileTxBandStop = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileTxBandStop.setStatus('current')
cvdslMCMConfProfileTxBandRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 10, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileTxBandRowStatus.setStatus('current')
cvdslLineMCMConfProfileRxBandTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11), )
if mibBuilder.loadTexts: cvdslLineMCMConfProfileRxBandTable.setStatus('current')
cvdslLineMCMConfProfileRxBandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11, 1), ).setIndexNames((0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileRxBandNumber"))
if mibBuilder.loadTexts: cvdslLineMCMConfProfileRxBandEntry.setStatus('current')
cvdslMCMConfProfileRxBandNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvdslMCMConfProfileRxBandNumber.setStatus('current')
cvdslMCMConfProfileRxBandStart = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileRxBandStart.setStatus('current')
cvdslMCMConfProfileRxBandStop = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileRxBandStop.setStatus('current')
cvdslMCMConfProfileRxBandRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 11, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileRxBandRowStatus.setStatus('current')
cvdslLineMCMConfProfileTxPSDTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12), )
if mibBuilder.loadTexts: cvdslLineMCMConfProfileTxPSDTable.setStatus('current')
cvdslLineMCMConfProfileTxPSDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12, 1), ).setIndexNames((0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxPSDNumber"))
if mibBuilder.loadTexts: cvdslLineMCMConfProfileTxPSDEntry.setStatus('current')
cvdslMCMConfProfileTxPSDNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvdslMCMConfProfileTxPSDNumber.setStatus('current')
cvdslMCMConfProfileTxPSDTone = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileTxPSDTone.setStatus('current')
cvdslMCMConfProfileTxPSDPSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('0.5dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileTxPSDPSD.setStatus('current')
cvdslMCMConfProfileTxPSDRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 12, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileTxPSDRowStatus.setStatus('current')
cvdslLineMCMConfProfileMaxTxPSDTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13), )
if mibBuilder.loadTexts: cvdslLineMCMConfProfileMaxTxPSDTable.setStatus('current')
cvdslLineMCMConfProfileMaxTxPSDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13, 1), ).setIndexNames((0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxTxPSDNumber"))
if mibBuilder.loadTexts: cvdslLineMCMConfProfileMaxTxPSDEntry.setStatus('current')
cvdslMCMConfProfileMaxTxPSDNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvdslMCMConfProfileMaxTxPSDNumber.setStatus('current')
cvdslMCMConfProfileMaxTxPSDTone = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileMaxTxPSDTone.setStatus('current')
cvdslMCMConfProfileMaxTxPSDPSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('0.5dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileMaxTxPSDPSD.setStatus('current')
cvdslMCMConfProfileMaxTxPSDRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 13, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileMaxTxPSDRowStatus.setStatus('current')
cvdslLineMCMConfProfileMaxRxPSDTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14), )
if mibBuilder.loadTexts: cvdslLineMCMConfProfileMaxRxPSDTable.setStatus('current')
cvdslLineMCMConfProfileMaxRxPSDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14, 1), ).setIndexNames((0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxRxPSDNumber"))
if mibBuilder.loadTexts: cvdslLineMCMConfProfileMaxRxPSDEntry.setStatus('current')
cvdslMCMConfProfileMaxRxPSDNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvdslMCMConfProfileMaxRxPSDNumber.setStatus('current')
cvdslMCMConfProfileMaxRxPSDTone = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileMaxRxPSDTone.setStatus('current')
cvdslMCMConfProfileMaxRxPSDPSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('0.5dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileMaxRxPSDPSD.setStatus('current')
cvdslMCMConfProfileMaxRxPSDRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 14, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslMCMConfProfileMaxRxPSDRowStatus.setStatus('current')
cvdslLineSCMConfProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15), )
if mibBuilder.loadTexts: cvdslLineSCMConfProfileTable.setStatus('current')
cvdslLineSCMConfProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1), ).setIndexNames((0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileIndex"))
if mibBuilder.loadTexts: cvdslLineSCMConfProfileEntry.setStatus('current')
cvdslSCMConfProfileInterleaveDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslSCMConfProfileInterleaveDepth.setStatus('current')
cvdslSCMConfProfileFastCodewordSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 180))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslSCMConfProfileFastCodewordSize.setStatus('current')
cvdslSCMConfProfileTransmitPSDMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 3), Bits().clone(namedValues=NamedValues(("vendorNotch1", 0), ("vendorNotch2", 1), ("amateurBand30m", 2), ("amateurBand40m", 3), ("amateurBand80m", 4), ("amateurBand160m", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslSCMConfProfileTransmitPSDMask.setStatus('current')
cvdslSCMConfProfileTransmitPSDLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('dBm/Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslSCMConfProfileTransmitPSDLevel.setStatus('current')
cvdslSCMConfProfileSymbolRateProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('kbaud').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslSCMConfProfileSymbolRateProfile.setStatus('current')
cvdslSCMConfProfileConstellationSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setUnits('log2').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslSCMConfProfileConstellationSize.setStatus('current')
cvdslSCMConfProfileCenterFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 511))).setUnits('kHz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslSCMConfProfileCenterFrequency.setStatus('current')
cvdslSCMConfProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 15, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslSCMConfProfileRowStatus.setStatus('current')
cvdslLineAlarmConfProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16), )
if mibBuilder.loadTexts: cvdslLineAlarmConfProfileTable.setStatus('current')
cvdslLineAlarmConfProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16, 1), ).setIndexNames((0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslPhysSide"), (0, "CISCO-IETF-VDSL-LINE-MIB", "cvdslLineAlarmConfProfileIndex"))
if mibBuilder.loadTexts: cvdslLineAlarmConfProfileEntry.setStatus('current')
cvdslLineAlarmConfProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvdslLineAlarmConfProfileIndex.setStatus('current')
cvdslLineAlarmConfProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslLineAlarmConfProfileName.setStatus('current')
cvdslInitFailureNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslInitFailureNotificationEnable.setStatus('current')
cvdslLineAlarmConfProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 1, 16, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvdslLineAlarmConfProfileRowStatus.setStatus('current')
cvdslNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 0))
cvdslInitFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 0, 1)).setObjects(("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrStatus"))
if mibBuilder.loadTexts: cvdslInitFailureNotification.setStatus('current')
cvdslConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3))
cvdslGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 1))
cvdslCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 2))
cvdslLineMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 2, 1)).setObjects(("CISCO-IETF-VDSL-LINE-MIB", "cvdslGroup"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMGroup"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvdslLineMibCompliance = cvdslLineMibCompliance.setStatus('current')
cvdslGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 1, 1)).setObjects(("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineCoding"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineType"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfile"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineAlarmConfProfile"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslInvSerialNumber"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslInvVendorID"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslInvVersionNumber"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrSnrMgn"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrAtn"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrStatus"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrOutputPwr"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslCurrAttainableRate"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslChanInterleaveDelay"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslChanCrcBlockLength"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileName"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfTargetSnrMgn"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfTxSpeed"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfRxSpeed"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineConfProfileRowStatus"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineAlarmConfProfileName"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslInitFailureNotificationEnable"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslLineAlarmConfProfileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvdslGroup = cvdslGroup.setStatus('current')
cvdslMCMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 1, 2)).setObjects(("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxWindowLength"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileRowStatus"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxBandStart"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxBandStop"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxBandRowStatus"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileRxBandStart"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileRxBandStop"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileRxBandRowStatus"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxPSDTone"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxPSDPSD"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileTxPSDRowStatus"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxTxPSDTone"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxTxPSDPSD"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxTxPSDRowStatus"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxRxPSDTone"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxRxPSDPSD"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslMCMConfProfileMaxRxPSDRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvdslMCMGroup = cvdslMCMGroup.setStatus('current')
cvdslSCMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 1, 3)).setObjects(("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileInterleaveDepth"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileFastCodewordSize"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileTransmitPSDMask"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileTransmitPSDLevel"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileSymbolRateProfile"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileConstellationSize"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileCenterFrequency"), ("CISCO-IETF-VDSL-LINE-MIB", "cvdslSCMConfProfileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvdslSCMGroup = cvdslSCMGroup.setStatus('current')
cvdslNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 87, 1, 3, 1, 4)).setObjects(("CISCO-IETF-VDSL-LINE-MIB", "cvdslInitFailureNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvdslNotificationGroup = cvdslNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-VDSL-LINE-MIB", cvdslSCMConfProfileConstellationSize=cvdslSCMConfProfileConstellationSize, cvdslLineMCMConfProfileMaxTxPSDTable=cvdslLineMCMConfProfileMaxTxPSDTable, cvdslLineMCMConfProfileTxBandTable=cvdslLineMCMConfProfileTxBandTable, cvdslCompliances=cvdslCompliances, cvdslLineMCMConfProfileTxPSDTable=cvdslLineMCMConfProfileTxPSDTable, cvdslSCMConfProfileInterleaveDepth=cvdslSCMConfProfileInterleaveDepth, cvdslMCMGroup=cvdslMCMGroup, cvdslMCMConfProfileMaxTxPSDNumber=cvdslMCMConfProfileMaxTxPSDNumber, cvdslLineMibCompliance=cvdslLineMibCompliance, cvdslLineSCMConfProfileEntry=cvdslLineSCMConfProfileEntry, cvdslGroups=cvdslGroups, cvdslNotificationGroup=cvdslNotificationGroup, ciscoIetfVdslMIB=ciscoIetfVdslMIB, cvdslChanEntry=cvdslChanEntry, cvdslPhysEntry=cvdslPhysEntry, cvdslLineCoding=cvdslLineCoding, cvdslLineConfProfile=cvdslLineConfProfile, cvdslLineTable=cvdslLineTable, cvdslMCMConfProfileTxPSDPSD=cvdslMCMConfProfileTxPSDPSD, cvdslLineSCMConfProfileTable=cvdslLineSCMConfProfileTable, cvdslChanTable=cvdslChanTable, cvdslCurrAttainableRate=cvdslCurrAttainableRate, cvdslMCMConfProfileMaxTxPSDPSD=cvdslMCMConfProfileMaxTxPSDPSD, cvdslLineConfProfileName=cvdslLineConfProfileName, cvdslSCMConfProfileFastCodewordSize=cvdslSCMConfProfileFastCodewordSize, cvdslMCMConfProfileRxBandStop=cvdslMCMConfProfileRxBandStop, cvdslLineType=cvdslLineType, cvdslLineMib=cvdslLineMib, cvdslMCMConfProfileTxBandRowStatus=cvdslMCMConfProfileTxBandRowStatus, cvdslMCMConfProfileMaxTxPSDTone=cvdslMCMConfProfileMaxTxPSDTone, cvdslInvVendorID=cvdslInvVendorID, CVdslLineEntity=CVdslLineEntity, cvdslLineConfTxSpeed=cvdslLineConfTxSpeed, cvdslLineConfProfileIndex=cvdslLineConfProfileIndex, cvdslLineAlarmConfProfileEntry=cvdslLineAlarmConfProfileEntry, cvdslNotifications=cvdslNotifications, cvdslMCMConfProfileTxBandStart=cvdslMCMConfProfileTxBandStart, cvdslGroup=cvdslGroup, cvdslSCMGroup=cvdslSCMGroup, cvdslMCMConfProfileTxPSDTone=cvdslMCMConfProfileTxPSDTone, PYSNMP_MODULE_ID=ciscoIetfVdslMIB, cvdslLineAlarmConfProfileName=cvdslLineAlarmConfProfileName, cvdslMCMConfProfileRxBandNumber=cvdslMCMConfProfileRxBandNumber, cvdslLineMCMConfProfileTxPSDEntry=cvdslLineMCMConfProfileTxPSDEntry, cvdslSCMConfProfileSymbolRateProfile=cvdslSCMConfProfileSymbolRateProfile, cvdslMCMConfProfileRxBandRowStatus=cvdslMCMConfProfileRxBandRowStatus, cvdslMCMConfProfileMaxRxPSDPSD=cvdslMCMConfProfileMaxRxPSDPSD, cvdslInitFailureNotificationEnable=cvdslInitFailureNotificationEnable, cvdslPhysSide=cvdslPhysSide, cvdslLineAlarmConfProfileTable=cvdslLineAlarmConfProfileTable, cvdslLineMCMConfProfileRxBandTable=cvdslLineMCMConfProfileRxBandTable, cvdslLineMCMConfProfileTable=cvdslLineMCMConfProfileTable, cvdslMCMConfProfileMaxTxPSDRowStatus=cvdslMCMConfProfileMaxTxPSDRowStatus, cvdslLineConfRxSpeed=cvdslLineConfRxSpeed, cvdslLineMCMConfProfileEntry=cvdslLineMCMConfProfileEntry, cvdslInvVersionNumber=cvdslInvVersionNumber, cvdslLineConfProfileTable=cvdslLineConfProfileTable, cvdslMCMConfProfileTxPSDNumber=cvdslMCMConfProfileTxPSDNumber, cvdslConformance=cvdslConformance, cvdslLineEntry=cvdslLineEntry, cvdslLineMCMConfProfileMaxRxPSDEntry=cvdslLineMCMConfProfileMaxRxPSDEntry, cvdslMCMConfProfileTxBandStop=cvdslMCMConfProfileTxBandStop, cvdslSCMConfProfileTransmitPSDLevel=cvdslSCMConfProfileTransmitPSDLevel, cvdslMCMConfProfileMaxRxPSDRowStatus=cvdslMCMConfProfileMaxRxPSDRowStatus, cvdslInvSerialNumber=cvdslInvSerialNumber, cvdslMibObjects=cvdslMibObjects, CVdslLineCodingType=CVdslLineCodingType, cvdslMCMConfProfileMaxRxPSDTone=cvdslMCMConfProfileMaxRxPSDTone, cvdslMCMConfProfileTxWindowLength=cvdslMCMConfProfileTxWindowLength, cvdslMCMConfProfileRxBandStart=cvdslMCMConfProfileRxBandStart, cvdslCurrOutputPwr=cvdslCurrOutputPwr, cvdslLineAlarmConfProfileRowStatus=cvdslLineAlarmConfProfileRowStatus, cvdslLineAlarmConfProfileIndex=cvdslLineAlarmConfProfileIndex, cvdslSCMConfProfileRowStatus=cvdslSCMConfProfileRowStatus, cvdslChanInterleaveDelay=cvdslChanInterleaveDelay, cvdslSCMConfProfileTransmitPSDMask=cvdslSCMConfProfileTransmitPSDMask, cvdslSCMConfProfileCenterFrequency=cvdslSCMConfProfileCenterFrequency, cvdslCurrAtn=cvdslCurrAtn, cvdslChanCrcBlockLength=cvdslChanCrcBlockLength, cvdslLineConfProfileRowStatus=cvdslLineConfProfileRowStatus, cvdslMCMConfProfileTxBandNumber=cvdslMCMConfProfileTxBandNumber, cvdslPhysTable=cvdslPhysTable, cvdslMCMConfProfileRowStatus=cvdslMCMConfProfileRowStatus, cvdslMCMConfProfileMaxRxPSDNumber=cvdslMCMConfProfileMaxRxPSDNumber, cvdslInitFailureNotification=cvdslInitFailureNotification, cvdslCurrSnrMgn=cvdslCurrSnrMgn, cvdslMCMConfProfileTxPSDRowStatus=cvdslMCMConfProfileTxPSDRowStatus, cvdslLineMCMConfProfileRxBandEntry=cvdslLineMCMConfProfileRxBandEntry, cvdslLineMCMConfProfileMaxTxPSDEntry=cvdslLineMCMConfProfileMaxTxPSDEntry, cvdslLineAlarmConfProfile=cvdslLineAlarmConfProfile, cvdslCurrStatus=cvdslCurrStatus, cvdslLineMCMConfProfileTxBandEntry=cvdslLineMCMConfProfileTxBandEntry, cvdslLineMCMConfProfileMaxRxPSDTable=cvdslLineMCMConfProfileMaxRxPSDTable, cvdslLineConfTargetSnrMgn=cvdslLineConfTargetSnrMgn, cvdslLineConfProfileEntry=cvdslLineConfProfileEntry)
