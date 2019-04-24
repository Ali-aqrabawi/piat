#
# PySNMP MIB module CISCO-IMAGE-UPGRADE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-IMAGE-UPGRADE-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:25:39 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, iso, Unsigned32, MibIdentifier, Integer32, Counter64, Gauge32, Counter32, ObjectIdentity, Bits, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "iso", "Unsigned32", "MibIdentifier", "Integer32", "Counter64", "Gauge32", "Counter32", "ObjectIdentity", "Bits", "NotificationType", "IpAddress")
DisplayString, TextualConvention, TruthValue, TimeStamp, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "TimeStamp", "RowStatus")
ciscoImageUpgradeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 360))
ciscoImageUpgradeMIB.setRevisions(('2011-03-28 00:00', '2008-03-18 00:00', '2007-07-18 00:00', '2006-12-21 00:00', '2004-01-20 00:00', '2003-11-04 00:00', '2003-10-28 00:00', '2003-07-11 00:00', '2003-07-08 00:00', '2003-06-01 00:00',))
if mibBuilder.loadTexts: ciscoImageUpgradeMIB.setLastUpdated('201103280000Z')
if mibBuilder.loadTexts: ciscoImageUpgradeMIB.setOrganization('Cisco Systems Inc.')
ciscoImageUpgradeMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 360, 0))
ciscoImageUpgradeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 360, 1))
ciscoImageUpgradeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 360, 2))
ciscoImageUpgradeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1))
ciscoImageUpgradeOp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4))
ciscoImageUpgradeMisc = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 10))
class CiuImageVariableTypeName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

ciuTotalImageVariables = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuTotalImageVariables.setStatus('current')
ciuImageVariableTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 2), )
if mibBuilder.loadTexts: ciuImageVariableTable.setStatus('current')
ciuImageVariableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableName"))
if mibBuilder.loadTexts: ciuImageVariableEntry.setStatus('current')
ciuImageVariableName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 2, 1, 1), CiuImageVariableTypeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuImageVariableName.setStatus('current')
ciuImageURITable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 3), )
if mibBuilder.loadTexts: ciuImageURITable.setStatus('current')
ciuImageURIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableName"))
if mibBuilder.loadTexts: ciuImageURIEntry.setStatus('current')
ciuImageURI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 3, 1, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciuImageURI.setStatus('current')
ciuUpgradeOpCommand = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("done", 2), ("install", 3), ("check", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciuUpgradeOpCommand.setStatus('current')
ciuUpgradeOpStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("none", 1), ("invalidOperation", 2), ("failure", 3), ("inProgress", 4), ("success", 5), ("abortInProgress", 6), ("abortSuccess", 7), ("abortFailed", 8), ("successReset", 9), ("fsUpgReset", 10))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpStatus.setStatus('current')
ciuUpgradeOpNotifyOnCompletion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciuUpgradeOpNotifyOnCompletion.setStatus('current')
ciuUpgradeOpTimeStarted = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpTimeStarted.setStatus('current')
ciuUpgradeOpTimeCompleted = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpTimeCompleted.setStatus('current')
ciuUpgradeOpAbort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciuUpgradeOpAbort.setStatus('current')
ciuUpgradeOpStatusReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpStatusReason.setStatus('current')
ciuUpgradeOpLastCommand = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("done", 2), ("install", 3), ("check", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpLastCommand.setStatus('current')
ciuUpgradeOpLastStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("none", 1), ("invalidOperation", 2), ("failure", 3), ("inProgress", 4), ("success", 5), ("abortInProgress", 6), ("abortSuccess", 7), ("abortFailed", 8), ("successReset", 9), ("fsUpgReset", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpLastStatus.setStatus('current')
ciuUpgradeOpLastStatusReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpLastStatusReason.setStatus('current')
ciuUpgradeJobStatusNotifyOnCompletion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciuUpgradeJobStatusNotifyOnCompletion.setStatus('current')
ciuUpgradeTargetTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 5), )
if mibBuilder.loadTexts: ciuUpgradeTargetTable.setStatus('current')
ciuUpgradeTargetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ciuUpgradeTargetEntry.setStatus('current')
ciuUpgradeTargetAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("image", 1), ("bios", 2), ("loader", 3), ("bootrom", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciuUpgradeTargetAction.setStatus('current')
ciuUpgradeTargetEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciuUpgradeTargetEntryStatus.setStatus('current')
ciuImageLocInputTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 6), )
if mibBuilder.loadTexts: ciuImageLocInputTable.setStatus('current')
ciuImageLocInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableName"))
if mibBuilder.loadTexts: ciuImageLocInputEntry.setStatus('current')
ciuImageLocInputURI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 6, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciuImageLocInputURI.setStatus('current')
ciuImageLocInputEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciuImageLocInputEntryStatus.setStatus('current')
ciuVersionCompChkTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7), )
if mibBuilder.loadTexts: ciuVersionCompChkTable.setStatus('current')
ciuVersionCompChkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ciuVersionCompChkEntry.setStatus('current')
ciuVersionCompImageSame = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuVersionCompImageSame.setStatus('current')
ciuVersionCompUpgradable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuVersionCompUpgradable.setStatus('current')
ciuVersionCompUpgradeAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 1), ("other", 2), ("rollingUpgrade", 3), ("switchOverReset", 4), ("reset", 5), ("copy", 6), ("notApplicable", 7), ("plugin", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuVersionCompUpgradeAction.setStatus('current')
ciuVersionCompUpgradeBios = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuVersionCompUpgradeBios.setStatus('current')
ciuVersionCompUpgradeBootrom = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuVersionCompUpgradeBootrom.setStatus('current')
ciuVersionCompUpgradeLoader = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuVersionCompUpgradeLoader.setStatus('current')
ciuVersionCompUpgradeImpact = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("nonDisruptive", 2), ("disruptive", 3), ("notApplicable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuVersionCompUpgradeImpact.setStatus('current')
ciuVersionCompUpgradeReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuVersionCompUpgradeReason.setStatus('current')
ciuUpgradeImageVersionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8), )
if mibBuilder.loadTexts: ciuUpgradeImageVersionTable.setStatus('current')
ciuUpgradeImageVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionIndex"))
if mibBuilder.loadTexts: ciuUpgradeImageVersionEntry.setStatus('current')
ciuUpgradeImageVersionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ciuUpgradeImageVersionIndex.setStatus('current')
ciuUpgradeImageVersionVarName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1, 2), CiuImageVariableTypeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeImageVersionVarName.setStatus('current')
ciuUpgradeImageVersionRunning = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeImageVersionRunning.setStatus('current')
ciuUpgradeImageVersionNew = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeImageVersionNew.setStatus('current')
ciuUpgradeImageVersionUpgReqd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeImageVersionUpgReqd.setStatus('current')
ciuUpgradeOpStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9), )
if mibBuilder.loadTexts: ciuUpgradeOpStatusTable.setStatus('current')
ciuUpgradeOpStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1), ).setIndexNames((0, "CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusOperIndex"))
if mibBuilder.loadTexts: ciuUpgradeOpStatusEntry.setStatus('current')
ciuUpgradeOpStatusOperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ciuUpgradeOpStatusOperIndex.setStatus('current')
ciuUpgradeOpStatusOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("copy", 3), ("verify", 4), ("versionExtraction", 5), ("imageSync", 6), ("configSync", 7), ("preUpgrade", 8), ("forceDownload", 9), ("moduleOnline", 10), ("hitlessLCUpgrade", 11), ("hitfulLCUpgrade", 12), ("unusedBootvar", 13), ("convertStartUp", 14), ("looseIncompatibility", 15), ("haSeqNumMismatch", 16), ("unknownModuleOnline", 17), ("recommendedAction", 18), ("recoveryAction", 19), ("remainingAction", 20), ("additionalInfo", 21), ("settingBootvars", 22), ("informLcmFsUpg", 23), ("sysmgrSaveRuntimeStateAndSuccessReset", 24), ("kexecLoadUpgImages", 25), ("fsUpgCleanup", 26), ("saveMtsState", 27), ("fsUpgBegin", 28), ("lcWarmBootStatus", 29), ("waitStateVerificationStatus", 30), ("informLcmFsUpgExternalLc", 31), ("externalLcWarmBootStatus", 32), ("total", 33), ("compactFlashTcamSanity", 34), ("systemPreupgradeBegin", 35)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpStatusOperation.setStatus('current')
ciuUpgradeOpStatusModule = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 3), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpStatusModule.setStatus('current')
ciuUpgradeOpStatusSrcImageLoc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpStatusSrcImageLoc.setStatus('current')
ciuUpgradeOpStatusDestImageLoc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpStatusDestImageLoc.setStatus('current')
ciuUpgradeOpStatusJobStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("failed", 3), ("inProgress", 4), ("success", 5), ("planned", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpStatusJobStatus.setStatus('current')
ciuUpgradeOpStatusPercentCompl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpStatusPercentCompl.setStatus('current')
ciuUpgradeOpStatusJobStatusReas = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeOpStatusJobStatusReas.setStatus('current')
ciuUpgradeMiscAutoCopy = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 10, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciuUpgradeMiscAutoCopy.setStatus('current')
ciuUpgradeMiscInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 11), )
if mibBuilder.loadTexts: ciuUpgradeMiscInfoTable.setStatus('current')
ciuUpgradeMiscInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 11, 1), ).setIndexNames((0, "CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscInfoIndex"))
if mibBuilder.loadTexts: ciuUpgradeMiscInfoEntry.setStatus('current')
ciuUpgradeMiscInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 11, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ciuUpgradeMiscInfoIndex.setStatus('current')
ciuUpgradeMiscInfoModule = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 11, 1, 2), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeMiscInfoModule.setStatus('current')
ciuUpgradeMiscInfoDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 11, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciuUpgradeMiscInfoDescr.setStatus('current')
ciuUpgradeOpCompletionNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 360, 0, 1)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpCommand"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatus"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpTimeCompleted"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpLastCommand"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpLastStatus"))
if mibBuilder.loadTexts: ciuUpgradeOpCompletionNotify.setStatus('current')
ciuUpgradeJobStatusNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 360, 0, 2)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusOperation"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusModule"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusSrcImageLoc"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusDestImageLoc"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusJobStatus"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusPercentCompl"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusJobStatusReas"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatus"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusReason"))
if mibBuilder.loadTexts: ciuUpgradeJobStatusNotify.setStatus('current')
ciuImageUpgradeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1))
ciuImageUpgradeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2))
ciuImageUpgradeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1, 1)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuImageUpgradeGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageURIGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageLocInputGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompChkGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuImageUpgradeCompliance = ciuImageUpgradeCompliance.setStatus('deprecated')
ciuImageUpgradeComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1, 2)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuImageUpgradeGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageURIGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageLocInputGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompChkGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeNotificationGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuImageUpgradeComplianceRev1 = ciuImageUpgradeComplianceRev1.setStatus('deprecated')
ciuImageUpgradeComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1, 3)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuImageUpgradeGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageURIGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageLocInputGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompChkGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeNotificationGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuImageUpgradeComplianceRev2 = ciuImageUpgradeComplianceRev2.setStatus('deprecated')
ciuImageUpgradeComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1, 4)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuImageUpgradeGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageURIGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageLocInputGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompChkGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeNotificationGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeNotificationGroupSup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuImageUpgradeComplianceRev3 = ciuImageUpgradeComplianceRev3.setStatus('deprecated')
ciuImageUpgradeComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1, 5)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuImageUpgradeGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageURIGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageLocInputGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompChkGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeNotificationGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeNotificationGroupSup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscInfoGroup"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpNewGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuImageUpgradeComplianceRev4 = ciuImageUpgradeComplianceRev4.setStatus('current')
ciuImageUpgradeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 1)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuTotalImageVariables"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuImageUpgradeGroup = ciuImageUpgradeGroup.setStatus('current')
ciuImageVariableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 2)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuImageVariableGroup = ciuImageVariableGroup.setStatus('current')
ciuImageURIGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 3)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuImageURI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuImageURIGroup = ciuImageURIGroup.setStatus('current')
ciuUpgradeOpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 4)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpCommand"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatus"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpNotifyOnCompletion"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpTimeStarted"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpTimeCompleted"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpAbort"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuUpgradeOpGroup = ciuUpgradeOpGroup.setStatus('current')
ciuUpgradeTargetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 5)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeTargetAction"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeTargetEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuUpgradeTargetGroup = ciuUpgradeTargetGroup.setStatus('current')
ciuImageLocInputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 6)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuImageLocInputURI"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageLocInputEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuImageLocInputGroup = ciuImageLocInputGroup.setStatus('current')
ciuVersionCompChkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 7)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompImageSame"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradable"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeAction"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeBios"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeBootrom"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeLoader"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeImpact"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuVersionCompChkGroup = ciuVersionCompChkGroup.setStatus('current')
ciuUpgradeImageVersionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 8)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionVarName"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionRunning"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionNew"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionUpgReqd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuUpgradeImageVersionGroup = ciuUpgradeImageVersionGroup.setStatus('current')
ciuUpgradeOpStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 9)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusOperation"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusModule"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusSrcImageLoc"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusDestImageLoc"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusJobStatus"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusPercentCompl"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusJobStatusReas"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuUpgradeOpStatusGroup = ciuUpgradeOpStatusGroup.setStatus('current')
ciuUpgradeNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 10)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpCompletionNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuUpgradeNotificationGroup = ciuUpgradeNotificationGroup.setStatus('current')
ciuUpgradeMiscGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 11)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscAutoCopy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuUpgradeMiscGroup = ciuUpgradeMiscGroup.setStatus('current')
ciuUpgradeMiscInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 12)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscInfoModule"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscInfoDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuUpgradeMiscInfoGroup = ciuUpgradeMiscInfoGroup.setStatus('current')
ciuUpgradeNotificationGroupSup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 13)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeJobStatusNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuUpgradeNotificationGroupSup = ciuUpgradeNotificationGroupSup.setStatus('current')
ciuUpgradeOpNewGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 14)).setObjects(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeJobStatusNotifyOnCompletion"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpLastCommand"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpLastStatus"), ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpLastStatusReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciuUpgradeOpNewGroup = ciuUpgradeOpNewGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMAGE-UPGRADE-MIB", ciuImageURIEntry=ciuImageURIEntry, ciscoImageUpgradeMIBObjects=ciscoImageUpgradeMIBObjects, ciuVersionCompUpgradeAction=ciuVersionCompUpgradeAction, ciuUpgradeTargetEntryStatus=ciuUpgradeTargetEntryStatus, ciuUpgradeOpLastCommand=ciuUpgradeOpLastCommand, ciuUpgradeOpStatusReason=ciuUpgradeOpStatusReason, ciuVersionCompUpgradeLoader=ciuVersionCompUpgradeLoader, ciuVersionCompUpgradable=ciuVersionCompUpgradable, ciuUpgradeOpLastStatusReason=ciuUpgradeOpLastStatusReason, ciuUpgradeTargetTable=ciuUpgradeTargetTable, ciuUpgradeOpNewGroup=ciuUpgradeOpNewGroup, ciuVersionCompChkEntry=ciuVersionCompChkEntry, ciuUpgradeOpGroup=ciuUpgradeOpGroup, ciuUpgradeOpCompletionNotify=ciuUpgradeOpCompletionNotify, ciuUpgradeImageVersionTable=ciuUpgradeImageVersionTable, ciscoImageUpgradeOp=ciscoImageUpgradeOp, ciscoImageUpgradeMisc=ciscoImageUpgradeMisc, ciuUpgradeOpStatusEntry=ciuUpgradeOpStatusEntry, ciuUpgradeMiscInfoModule=ciuUpgradeMiscInfoModule, ciuUpgradeTargetAction=ciuUpgradeTargetAction, ciuVersionCompImageSame=ciuVersionCompImageSame, ciuUpgradeOpStatusJobStatusReas=ciuUpgradeOpStatusJobStatusReas, ciuVersionCompChkGroup=ciuVersionCompChkGroup, ciuImageVariableTable=ciuImageVariableTable, ciuUpgradeOpStatusGroup=ciuUpgradeOpStatusGroup, ciuVersionCompUpgradeBios=ciuVersionCompUpgradeBios, ciuVersionCompUpgradeReason=ciuVersionCompUpgradeReason, ciuUpgradeOpTimeStarted=ciuUpgradeOpTimeStarted, ciuUpgradeJobStatusNotify=ciuUpgradeJobStatusNotify, ciuUpgradeMiscInfoDescr=ciuUpgradeMiscInfoDescr, ciuVersionCompUpgradeBootrom=ciuVersionCompUpgradeBootrom, ciscoImageUpgradeMIB=ciscoImageUpgradeMIB, ciuUpgradeImageVersionGroup=ciuUpgradeImageVersionGroup, ciuUpgradeOpAbort=ciuUpgradeOpAbort, ciuUpgradeNotificationGroup=ciuUpgradeNotificationGroup, ciuUpgradeOpNotifyOnCompletion=ciuUpgradeOpNotifyOnCompletion, ciuImageLocInputGroup=ciuImageLocInputGroup, ciuUpgradeImageVersionIndex=ciuUpgradeImageVersionIndex, ciuUpgradeMiscInfoEntry=ciuUpgradeMiscInfoEntry, ciuUpgradeMiscInfoIndex=ciuUpgradeMiscInfoIndex, ciuUpgradeOpStatus=ciuUpgradeOpStatus, ciuUpgradeOpStatusDestImageLoc=ciuUpgradeOpStatusDestImageLoc, ciuVersionCompChkTable=ciuVersionCompChkTable, ciuUpgradeImageVersionNew=ciuUpgradeImageVersionNew, ciuImageUpgradeComplianceRev3=ciuImageUpgradeComplianceRev3, ciuImageUpgradeCompliance=ciuImageUpgradeCompliance, ciuImageUpgradeComplianceRev1=ciuImageUpgradeComplianceRev1, ciuImageLocInputEntryStatus=ciuImageLocInputEntryStatus, ciuImageUpgradeGroup=ciuImageUpgradeGroup, ciuImageUpgradeComplianceRev4=ciuImageUpgradeComplianceRev4, ciuUpgradeOpStatusOperation=ciuUpgradeOpStatusOperation, ciuUpgradeOpCommand=ciuUpgradeOpCommand, ciuImageUpgradeComplianceRev2=ciuImageUpgradeComplianceRev2, ciuUpgradeOpStatusPercentCompl=ciuUpgradeOpStatusPercentCompl, ciuUpgradeMiscInfoGroup=ciuUpgradeMiscInfoGroup, ciscoImageUpgradeConfig=ciscoImageUpgradeConfig, ciuUpgradeTargetEntry=ciuUpgradeTargetEntry, ciuUpgradeOpStatusJobStatus=ciuUpgradeOpStatusJobStatus, ciuImageLocInputTable=ciuImageLocInputTable, ciscoImageUpgradeMIBNotifs=ciscoImageUpgradeMIBNotifs, ciuUpgradeOpTimeCompleted=ciuUpgradeOpTimeCompleted, ciuUpgradeOpStatusTable=ciuUpgradeOpStatusTable, ciuImageURITable=ciuImageURITable, ciuImageURI=ciuImageURI, ciuTotalImageVariables=ciuTotalImageVariables, ciuUpgradeMiscAutoCopy=ciuUpgradeMiscAutoCopy, ciscoImageUpgradeMIBConform=ciscoImageUpgradeMIBConform, ciuImageLocInputEntry=ciuImageLocInputEntry, ciuUpgradeOpStatusSrcImageLoc=ciuUpgradeOpStatusSrcImageLoc, ciuImageUpgradeCompliances=ciuImageUpgradeCompliances, ciuImageLocInputURI=ciuImageLocInputURI, ciuUpgradeTargetGroup=ciuUpgradeTargetGroup, ciuUpgradeImageVersionVarName=ciuUpgradeImageVersionVarName, PYSNMP_MODULE_ID=ciscoImageUpgradeMIB, CiuImageVariableTypeName=CiuImageVariableTypeName, ciuUpgradeMiscInfoTable=ciuUpgradeMiscInfoTable, ciuImageVariableName=ciuImageVariableName, ciuUpgradeImageVersionEntry=ciuUpgradeImageVersionEntry, ciuImageVariableGroup=ciuImageVariableGroup, ciuUpgradeOpLastStatus=ciuUpgradeOpLastStatus, ciuUpgradeJobStatusNotifyOnCompletion=ciuUpgradeJobStatusNotifyOnCompletion, ciuImageVariableEntry=ciuImageVariableEntry, ciuImageUpgradeGroups=ciuImageUpgradeGroups, ciuUpgradeImageVersionRunning=ciuUpgradeImageVersionRunning, ciuUpgradeOpStatusModule=ciuUpgradeOpStatusModule, ciuUpgradeNotificationGroupSup=ciuUpgradeNotificationGroupSup, ciuUpgradeImageVersionUpgReqd=ciuUpgradeImageVersionUpgReqd, ciuUpgradeMiscGroup=ciuUpgradeMiscGroup, ciuVersionCompUpgradeImpact=ciuVersionCompUpgradeImpact, ciuUpgradeOpStatusOperIndex=ciuUpgradeOpStatusOperIndex, ciuImageURIGroup=ciuImageURIGroup)