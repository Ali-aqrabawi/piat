#
# PySNMP MIB module CISCO-SCSI-FLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-SCSI-FLOW-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:46:57 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ScsiLUNOrZero, = mibBuilder.importSymbols("CISCO-SCSI-MIB", "ScsiLUNOrZero")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VsanIndex, FcNameId = mibBuilder.importSymbols("CISCO-ST-TC", "VsanIndex", "FcNameId")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Integer32, Unsigned32, TimeTicks, iso, IpAddress, NotificationType, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Integer32", "Unsigned32", "TimeTicks", "iso", "IpAddress", "NotificationType", "Counter64", "Counter32")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
ciscoScsiFlowMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 447))
ciscoScsiFlowMIB.setRevisions(('2005-01-06 00:00',))
if mibBuilder.loadTexts: ciscoScsiFlowMIB.setLastUpdated('200501060000Z')
if mibBuilder.loadTexts: ciscoScsiFlowMIB.setOrganization('Cisco Systems Inc.')
ciscoScsiFlowMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 447, 0))
ciscoScsiFlowMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 447, 1))
ciscoScsiFlowMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 447, 2))
csfConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1))
csfStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2))
csfFeatureStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3))
class CSFlowDeviceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("initiator", 1), ("target", 2))

class CSFlowVerifyReasonCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("success", 1), ("noLicense", 2), ("generalError", 3), ("notInNameServer", 4), ("notInFlogiServer", 5), ("deviceNotOnIlc", 6), ("deviceNotScsi", 7), ("deviceNotInitiator", 8), ("deviceNotTarget", 9), ("deviceNotFibreChannel", 10), ("ipcTimeout", 11), ("cfsError", 12), ("cfsTimeout", 13), ("portsUnprovisioned", 14), ("initTargetZonedOut", 15), ("statusNotChecked", 16), ("initNotInNameServer", 17), ("tgtNotInNameServer", 18), ("tgtNotInFlogiServer", 19))

class CSFlowCfgReasonCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("success", 1), ("ipcError", 2), ("ipcTimeout", 3), ("sfmGenericError", 4), ("sfcGenericError", 5), ("cfsError", 6), ("cfsTimeout", 7), ("deviceNotOnIlc", 8), ("lcIpcError", 9), ("tcamError", 10), ("ilcAsicDrvError", 11), ("dppError", 12), ("statusNotChecked", 13), ("sfcDBError", 14), ("sfcNoSuchFlow", 15), ("sfcFlowExists", 16), ("dppNoBuffers", 17), ("dppNoMemory", 18), ("dppFlowExists", 19))

class CSFlowFeatureCfgReasonCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("success", 1), ("featureCfgFailure", 2), ("flowVerifFailure", 3))

ciscoScsiFlowNextIndexAvail = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowNextIndexAvail.setStatus('current')
ciscoScsiFlowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2), )
if mibBuilder.loadTexts: ciscoScsiFlowTable.setStatus('current')
ciscoScsiFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowId"))
if mibBuilder.loadTexts: ciscoScsiFlowEntry.setStatus('current')
ciscoScsiFlowId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ciscoScsiFlowId.setStatus('current')
ciscoScsiFlowIntrWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 2), FcNameId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoScsiFlowIntrWwn.setStatus('current')
ciscoScsiFlowTargetWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 3), FcNameId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoScsiFlowTargetWwn.setStatus('current')
ciscoScsiFlowIntrVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 4), VsanIndex().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoScsiFlowIntrVsan.setStatus('current')
ciscoScsiFlowTargetVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 5), VsanIndex().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoScsiFlowTargetVsan.setStatus('current')
ciscoScsiFlowAllLuns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoScsiFlowAllLuns.setStatus('current')
ciscoScsiFlowWriteAcc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoScsiFlowWriteAcc.setStatus('current')
ciscoScsiFlowBufCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(1024)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoScsiFlowBufCount.setStatus('current')
ciscoScsiFlowStatsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoScsiFlowStatsEnabled.setStatus('current')
ciscoScsiFlowClearStats = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("noop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoScsiFlowClearStats.setStatus('current')
ciscoScsiFlowIntrVrfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 11), CSFlowVerifyReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowIntrVrfStatus.setStatus('current')
ciscoScsiFlowTgtVrfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 12), CSFlowVerifyReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowTgtVrfStatus.setStatus('current')
ciscoScsiFlowIntrLCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 13), CSFlowVerifyReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowIntrLCStatus.setStatus('current')
ciscoScsiFlowTgtLCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 14), CSFlowVerifyReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowTgtLCStatus.setStatus('current')
ciscoScsiFlowRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoScsiFlowRowStatus.setStatus('current')
ciscoScsiFlowNum = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoScsiFlowNum.setStatus('current')
ciscoScsiFlowDeviceType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 4), CSFlowDeviceType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoScsiFlowDeviceType.setStatus('current')
ciscoScsiFlowVerifyReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 5), CSFlowVerifyReasonCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoScsiFlowVerifyReasonCode.setStatus('current')
ciscoScsiFlowCfgReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 6), CSFlowCfgReasonCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoScsiFlowCfgReasonCode.setStatus('current')
ciscoScsiFlowStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1), )
if mibBuilder.loadTexts: ciscoScsiFlowStatsTable.setStatus('current')
ciscoScsiFlowStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowId"), (0, "CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowLunId"))
if mibBuilder.loadTexts: ciscoScsiFlowStatsEntry.setStatus('current')
ciscoScsiFlowLunId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 1), ScsiLUNOrZero())
if mibBuilder.loadTexts: ciscoScsiFlowLunId.setStatus('current')
ciscoScsiFlowRdIos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRdIos.setStatus('current')
ciscoScsiFlowRdFailedIos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRdFailedIos.setStatus('current')
ciscoScsiFlowRdTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRdTimeouts.setStatus('current')
ciscoScsiFlowRdBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRdBlocks.setStatus('current')
ciscoScsiFlowRdMaxBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRdMaxBlocks.setStatus('current')
ciscoScsiFlowRdMinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRdMinTime.setStatus('current')
ciscoScsiFlowRdMaxTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRdMaxTime.setStatus('current')
ciscoScsiFlowRdsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRdsActive.setStatus('current')
ciscoScsiFlowWrIos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrIos.setStatus('current')
ciscoScsiFlowWrFailedIos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrFailedIos.setStatus('current')
ciscoScsiFlowWrTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrTimeouts.setStatus('current')
ciscoScsiFlowWrBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrBlocks.setStatus('current')
ciscoScsiFlowWrMaxBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrMaxBlocks.setStatus('current')
ciscoScsiFlowWrMinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrMinTime.setStatus('current')
ciscoScsiFlowWrMaxTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrMaxTime.setStatus('current')
ciscoScsiFlowWrsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrsActive.setStatus('current')
ciscoScsiFlowTestUnitRdys = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowTestUnitRdys.setStatus('current')
ciscoScsiFlowRepLuns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRepLuns.setStatus('current')
ciscoScsiFlowInquirys = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowInquirys.setStatus('current')
ciscoScsiFlowRdCapacitys = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRdCapacitys.setStatus('current')
ciscoScsiFlowModeSenses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowModeSenses.setStatus('current')
ciscoScsiFlowReqSenses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowReqSenses.setStatus('current')
ciscoScsiFlowRxFc2Frames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRxFc2Frames.setStatus('current')
ciscoScsiFlowTxFc2Frames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowTxFc2Frames.setStatus('current')
ciscoScsiFlowRxFc2Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowRxFc2Octets.setStatus('current')
ciscoScsiFlowTxFc2Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowTxFc2Octets.setStatus('current')
ciscoScsiFlowBusyStatuses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowBusyStatuses.setStatus('current')
ciscoScsiFlowStatusResvConfs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowStatusResvConfs.setStatus('current')
ciscoScsiFlowTskSetFulStatuses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowTskSetFulStatuses.setStatus('current')
ciscoScsiFlowAcaActiveStatuses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowAcaActiveStatuses.setStatus('current')
ciscoScsiFlowSenseKeyNotRdyErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyNotRdyErrs.setStatus('current')
ciscoScsiFlowSenseKeyMedErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyMedErrs.setStatus('current')
ciscoScsiFlowSenseKeyHwErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyHwErrs.setStatus('current')
ciscoScsiFlowSenseKeyIllReqErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyIllReqErrs.setStatus('current')
ciscoScsiFlowSenseKeyUnitAttErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyUnitAttErrs.setStatus('current')
ciscoScsiFlowSenseKeyDatProtErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyDatProtErrs.setStatus('current')
ciscoScsiFlowSenseKeyBlankErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyBlankErrs.setStatus('current')
ciscoScsiFlowSenseKeyCpAbrtErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyCpAbrtErrs.setStatus('current')
ciscoScsiFlowSenseKeyAbrtCmdErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyAbrtCmdErrs.setStatus('current')
ciscoScsiFlowSenseKeyVolFlowErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyVolFlowErrs.setStatus('current')
ciscoScsiFlowSenseKeyMiscmpErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowSenseKeyMiscmpErrs.setStatus('current')
ciscoScsiFlowAbts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowAbts.setStatus('current')
ciscoScsiFlowWrAccStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 1), )
if mibBuilder.loadTexts: ciscoScsiFlowWrAccStatusTable.setStatus('current')
ciscoScsiFlowWrAccStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowId"))
if mibBuilder.loadTexts: ciscoScsiFlowWrAccStatusEntry.setStatus('current')
ciscoScsiFlowWrAccCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 1, 1, 1), CSFlowFeatureCfgReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrAccCfgStatus.setStatus('current')
ciscoScsiFlowWrAccIntrCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 1, 1, 2), CSFlowCfgReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrAccIntrCfgStatus.setStatus('current')
ciscoScsiFlowWrAccTgtCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 1, 1, 3), CSFlowCfgReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowWrAccTgtCfgStatus.setStatus('current')
ciscoScsiFlowStatsStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 2), )
if mibBuilder.loadTexts: ciscoScsiFlowStatsStatusTable.setStatus('current')
ciscoScsiFlowStatsStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowId"))
if mibBuilder.loadTexts: ciscoScsiFlowStatsStatusEntry.setStatus('current')
ciscoScsiFlowStatsCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 2, 1, 1), CSFlowFeatureCfgReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowStatsCfgStatus.setStatus('current')
ciscoScsiFlowStatsIntrCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 2, 1, 2), CSFlowCfgReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowStatsIntrCfgStatus.setStatus('current')
ciscoScsiFlowStatsTgtCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 2, 1, 3), CSFlowCfgReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoScsiFlowStatsTgtCfgStatus.setStatus('current')
ciscoScsiFlowVerifyNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 447, 0, 1)).setObjects(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNum"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowDeviceType"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowVerifyReasonCode"))
if mibBuilder.loadTexts: ciscoScsiFlowVerifyNotify.setStatus('current')
ciscoScsiFlowWrAccNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 447, 0, 2)).setObjects(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNum"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowDeviceType"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowCfgReasonCode"))
if mibBuilder.loadTexts: ciscoScsiFlowWrAccNotify.setStatus('current')
ciscoScsiFlowStatsNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 447, 0, 3)).setObjects(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNum"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowDeviceType"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowCfgReasonCode"))
if mibBuilder.loadTexts: ciscoScsiFlowStatsNotify.setStatus('current')
ciscoScsiFlowMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 1))
ciscoScsiFlowMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2))
ciscoScsiFlowMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 1, 1)).setObjects(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowGroup"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNotifyGroup"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowInfoGroup"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsGroup"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowFeatureStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoScsiFlowMIBCompliance = ciscoScsiFlowMIBCompliance.setStatus('current')
ciscoScsiFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2, 1)).setObjects(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNextIndexAvail"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowIntrWwn"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTargetWwn"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowIntrVsan"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTargetVsan"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowAllLuns"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWriteAcc"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowBufCount"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsEnabled"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRowStatus"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowClearStats"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowIntrVrfStatus"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowIntrLCStatus"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTgtLCStatus"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTgtVrfStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoScsiFlowGroup = ciscoScsiFlowGroup.setStatus('current')
ciscoScsiFlowStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2, 2)).setObjects(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdIos"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdFailedIos"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdTimeouts"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdBlocks"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdMaxBlocks"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdMinTime"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdMaxTime"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdsActive"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrIos"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrFailedIos"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrTimeouts"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrBlocks"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrMaxBlocks"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrMinTime"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrMaxTime"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrsActive"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTestUnitRdys"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRepLuns"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowInquirys"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdCapacitys"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowModeSenses"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowReqSenses"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRxFc2Frames"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTxFc2Frames"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRxFc2Octets"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTxFc2Octets"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowBusyStatuses"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatusResvConfs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTskSetFulStatuses"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowAcaActiveStatuses"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyNotRdyErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyMedErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyHwErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyIllReqErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyUnitAttErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyDatProtErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyBlankErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyCpAbrtErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyAbrtCmdErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyVolFlowErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyMiscmpErrs"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowAbts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoScsiFlowStatsGroup = ciscoScsiFlowStatsGroup.setStatus('current')
ciscoScsiFlowInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2, 3)).setObjects(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNum"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowDeviceType"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowVerifyReasonCode"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowCfgReasonCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoScsiFlowInfoGroup = ciscoScsiFlowInfoGroup.setStatus('current')
ciscoScsiFlowNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2, 4)).setObjects(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowVerifyNotify"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrAccNotify"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoScsiFlowNotifyGroup = ciscoScsiFlowNotifyGroup.setStatus('current')
ciscoScsiFlowFeatureStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2, 5)).setObjects(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrAccCfgStatus"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrAccIntrCfgStatus"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrAccTgtCfgStatus"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsCfgStatus"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsIntrCfgStatus"), ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsTgtCfgStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoScsiFlowFeatureStatusGroup = ciscoScsiFlowFeatureStatusGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SCSI-FLOW-MIB", ciscoScsiFlowIntrLCStatus=ciscoScsiFlowIntrLCStatus, ciscoScsiFlowStatsStatusTable=ciscoScsiFlowStatsStatusTable, ciscoScsiFlowTxFc2Frames=ciscoScsiFlowTxFc2Frames, ciscoScsiFlowSenseKeyIllReqErrs=ciscoScsiFlowSenseKeyIllReqErrs, ciscoScsiFlowRepLuns=ciscoScsiFlowRepLuns, ciscoScsiFlowWrMaxBlocks=ciscoScsiFlowWrMaxBlocks, ciscoScsiFlowModeSenses=ciscoScsiFlowModeSenses, ciscoScsiFlowRxFc2Octets=ciscoScsiFlowRxFc2Octets, csfConfiguration=csfConfiguration, ciscoScsiFlowMIBGroups=ciscoScsiFlowMIBGroups, ciscoScsiFlowMIBCompliances=ciscoScsiFlowMIBCompliances, ciscoScsiFlowStatsEntry=ciscoScsiFlowStatsEntry, ciscoScsiFlowLunId=ciscoScsiFlowLunId, ciscoScsiFlowStatsTgtCfgStatus=ciscoScsiFlowStatsTgtCfgStatus, ciscoScsiFlowInfoGroup=ciscoScsiFlowInfoGroup, ciscoScsiFlowWrFailedIos=ciscoScsiFlowWrFailedIos, ciscoScsiFlowRdCapacitys=ciscoScsiFlowRdCapacitys, CSFlowCfgReasonCode=CSFlowCfgReasonCode, ciscoScsiFlowRdFailedIos=ciscoScsiFlowRdFailedIos, ciscoScsiFlowIntrVsan=ciscoScsiFlowIntrVsan, ciscoScsiFlowBusyStatuses=ciscoScsiFlowBusyStatuses, ciscoScsiFlowAllLuns=ciscoScsiFlowAllLuns, ciscoScsiFlowWrMaxTime=ciscoScsiFlowWrMaxTime, ciscoScsiFlowAcaActiveStatuses=ciscoScsiFlowAcaActiveStatuses, ciscoScsiFlowStatsEnabled=ciscoScsiFlowStatsEnabled, ciscoScsiFlowAbts=ciscoScsiFlowAbts, ciscoScsiFlowSenseKeyNotRdyErrs=ciscoScsiFlowSenseKeyNotRdyErrs, ciscoScsiFlowSenseKeyVolFlowErrs=ciscoScsiFlowSenseKeyVolFlowErrs, ciscoScsiFlowRdMaxTime=ciscoScsiFlowRdMaxTime, ciscoScsiFlowRdIos=ciscoScsiFlowRdIos, ciscoScsiFlowSenseKeyMiscmpErrs=ciscoScsiFlowSenseKeyMiscmpErrs, ciscoScsiFlowSenseKeyAbrtCmdErrs=ciscoScsiFlowSenseKeyAbrtCmdErrs, ciscoScsiFlowCfgReasonCode=ciscoScsiFlowCfgReasonCode, ciscoScsiFlowWrAccNotify=ciscoScsiFlowWrAccNotify, ciscoScsiFlowSenseKeyDatProtErrs=ciscoScsiFlowSenseKeyDatProtErrs, ciscoScsiFlowTgtLCStatus=ciscoScsiFlowTgtLCStatus, ciscoScsiFlowDeviceType=ciscoScsiFlowDeviceType, ciscoScsiFlowId=ciscoScsiFlowId, ciscoScsiFlowSenseKeyMedErrs=ciscoScsiFlowSenseKeyMedErrs, ciscoScsiFlowWrTimeouts=ciscoScsiFlowWrTimeouts, ciscoScsiFlowStatsStatusEntry=ciscoScsiFlowStatsStatusEntry, ciscoScsiFlowRowStatus=ciscoScsiFlowRowStatus, ciscoScsiFlowSenseKeyBlankErrs=ciscoScsiFlowSenseKeyBlankErrs, ciscoScsiFlowRdMaxBlocks=ciscoScsiFlowRdMaxBlocks, ciscoScsiFlowStatsTable=ciscoScsiFlowStatsTable, ciscoScsiFlowEntry=ciscoScsiFlowEntry, ciscoScsiFlowReqSenses=ciscoScsiFlowReqSenses, ciscoScsiFlowTxFc2Octets=ciscoScsiFlowTxFc2Octets, ciscoScsiFlowVerifyNotify=ciscoScsiFlowVerifyNotify, CSFlowDeviceType=CSFlowDeviceType, ciscoScsiFlowStatsCfgStatus=ciscoScsiFlowStatsCfgStatus, CSFlowVerifyReasonCode=CSFlowVerifyReasonCode, ciscoScsiFlowStatsGroup=ciscoScsiFlowStatsGroup, ciscoScsiFlowRdsActive=ciscoScsiFlowRdsActive, ciscoScsiFlowTgtVrfStatus=ciscoScsiFlowTgtVrfStatus, PYSNMP_MODULE_ID=ciscoScsiFlowMIB, ciscoScsiFlowRxFc2Frames=ciscoScsiFlowRxFc2Frames, ciscoScsiFlowTable=ciscoScsiFlowTable, csfStats=csfStats, ciscoScsiFlowMIBCompliance=ciscoScsiFlowMIBCompliance, ciscoScsiFlowRdBlocks=ciscoScsiFlowRdBlocks, ciscoScsiFlowNotifyGroup=ciscoScsiFlowNotifyGroup, ciscoScsiFlowMIBNotifs=ciscoScsiFlowMIBNotifs, ciscoScsiFlowBufCount=ciscoScsiFlowBufCount, ciscoScsiFlowSenseKeyHwErrs=ciscoScsiFlowSenseKeyHwErrs, ciscoScsiFlowIntrVrfStatus=ciscoScsiFlowIntrVrfStatus, ciscoScsiFlowWrBlocks=ciscoScsiFlowWrBlocks, ciscoScsiFlowWrAccTgtCfgStatus=ciscoScsiFlowWrAccTgtCfgStatus, ciscoScsiFlowStatsIntrCfgStatus=ciscoScsiFlowStatsIntrCfgStatus, ciscoScsiFlowStatsNotify=ciscoScsiFlowStatsNotify, ciscoScsiFlowSenseKeyCpAbrtErrs=ciscoScsiFlowSenseKeyCpAbrtErrs, ciscoScsiFlowMIBObjects=ciscoScsiFlowMIBObjects, ciscoScsiFlowTargetWwn=ciscoScsiFlowTargetWwn, ciscoScsiFlowClearStats=ciscoScsiFlowClearStats, ciscoScsiFlowRdMinTime=ciscoScsiFlowRdMinTime, ciscoScsiFlowWrAccCfgStatus=ciscoScsiFlowWrAccCfgStatus, ciscoScsiFlowWrAccIntrCfgStatus=ciscoScsiFlowWrAccIntrCfgStatus, ciscoScsiFlowIntrWwn=ciscoScsiFlowIntrWwn, ciscoScsiFlowGroup=ciscoScsiFlowGroup, ciscoScsiFlowTskSetFulStatuses=ciscoScsiFlowTskSetFulStatuses, CSFlowFeatureCfgReasonCode=CSFlowFeatureCfgReasonCode, ciscoScsiFlowNextIndexAvail=ciscoScsiFlowNextIndexAvail, ciscoScsiFlowWrIos=ciscoScsiFlowWrIos, ciscoScsiFlowWrsActive=ciscoScsiFlowWrsActive, ciscoScsiFlowNum=ciscoScsiFlowNum, ciscoScsiFlowSenseKeyUnitAttErrs=ciscoScsiFlowSenseKeyUnitAttErrs, ciscoScsiFlowTargetVsan=ciscoScsiFlowTargetVsan, ciscoScsiFlowInquirys=ciscoScsiFlowInquirys, ciscoScsiFlowWriteAcc=ciscoScsiFlowWriteAcc, ciscoScsiFlowWrMinTime=ciscoScsiFlowWrMinTime, ciscoScsiFlowMIB=ciscoScsiFlowMIB, ciscoScsiFlowFeatureStatusGroup=ciscoScsiFlowFeatureStatusGroup, csfFeatureStatus=csfFeatureStatus, ciscoScsiFlowVerifyReasonCode=ciscoScsiFlowVerifyReasonCode, ciscoScsiFlowWrAccStatusEntry=ciscoScsiFlowWrAccStatusEntry, ciscoScsiFlowRdTimeouts=ciscoScsiFlowRdTimeouts, ciscoScsiFlowWrAccStatusTable=ciscoScsiFlowWrAccStatusTable, ciscoScsiFlowStatusResvConfs=ciscoScsiFlowStatusResvConfs, ciscoScsiFlowMIBConform=ciscoScsiFlowMIBConform, ciscoScsiFlowTestUnitRdys=ciscoScsiFlowTestUnitRdys)