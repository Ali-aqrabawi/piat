#
# PySNMP MIB module CISCO-FDMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-FDMI-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:44:29 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameId, = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameId")
notifyVsanIndex, vsanIndex = mibBuilder.importSymbols("CISCO-VSAN-MIB", "notifyVsanIndex", "vsanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, NotificationType, Bits, Unsigned32, Integer32, Counter64, TimeTicks, MibIdentifier, ModuleIdentity, Counter32, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "NotificationType", "Bits", "Unsigned32", "Integer32", "Counter64", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Counter32", "IpAddress", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoFdmiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 373))
ciscoFdmiMIB.setRevisions(('2003-11-07 00:00', '2003-08-24 00:00',))
if mibBuilder.loadTexts: ciscoFdmiMIB.setLastUpdated('200311070000Z')
if mibBuilder.loadTexts: ciscoFdmiMIB.setOrganization('Cisco Systems Inc. ')
ciscoFdmiMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 373, 0))
ciscoFdmiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 373, 1))
ciscoFdmiMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 373, 2))
cfdmiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 1))
cfdmiInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2))
cfdmiStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 3))
class CFdmiRejectReasonCode(TextualConvention, Integer32):
    reference = 'Fibre Channel Generic Services-4 Section 6.7.4.6 : Reason Code Explanation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("invalidCommandCode", 1), ("unableToPerformCmdReq", 2), ("invalidSize", 3))

class CFdmiRejectReasonCodeExpl(TextualConvention, Integer32):
    reference = 'Fibre Channel Generic Services-4 Section 6.7.4.6 : Reason Code Explanation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("noAdditionalExpl", 1), ("hbaAlreadyRegistered", 2), ("attrForSpecifiedHbaNotReg", 3), ("hbaAttrMultiAttribSameType", 4), ("invalidHbaAttrBlockLen", 5), ("reqdHbaAttrNotPresent", 6), ("origPortNotInRegPortList", 7), ("hbaIdNotInRegPortList", 8), ("portAttrNotRegistered", 9), ("portNotRegistered", 10), ("portAttrMultiAttrSameType", 11), ("invalidPortAttrBlockLen", 12), ("none", 13))

cfdmiRejectRegNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfdmiRejectRegNotifyEnable.setStatus('current')
cfdmiHbaInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1), )
if mibBuilder.loadTexts: cfdmiHbaInfoTable.setStatus('current')
cfdmiHbaInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FDMI-MIB", "cfdmiHbaInfoId"))
if mibBuilder.loadTexts: cfdmiHbaInfoEntry.setStatus('current')
cfdmiHbaInfoId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 1), FcNameId())
if mibBuilder.loadTexts: cfdmiHbaInfoId.setStatus('current')
cfdmiHbaInfoNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 2), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoNodeName.setStatus('current')
cfdmiHbaInfoMfg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoMfg.setStatus('current')
cfdmiHbaInfoSn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoSn.setStatus('current')
cfdmiHbaInfoModel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoModel.setStatus('current')
cfdmiHbaInfoModelDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoModelDescr.setStatus('current')
cfdmiHbaInfoHwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoHwVer.setStatus('current')
cfdmiHbaInfoDriverVer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoDriverVer.setStatus('current')
cfdmiHbaInfoOptROMVer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoOptROMVer.setStatus('current')
cfdmiHbaInfoFwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoFwVer.setStatus('current')
cfdmiHbaInfoOSInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoOSInfo.setStatus('current')
cfdmiHbaInfoMaxCTPayload = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 12), Unsigned32()).setUnits('32-bit words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaInfoMaxCTPayload.setStatus('current')
cfdmiHbaPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2), )
if mibBuilder.loadTexts: cfdmiHbaPortTable.setStatus('current')
cfdmiHbaPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FDMI-MIB", "cfdmiHbaInfoId"), (0, "CISCO-FDMI-MIB", "cfdmiHbaPortId"))
if mibBuilder.loadTexts: cfdmiHbaPortEntry.setStatus('current')
cfdmiHbaPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 1), FcNameId())
if mibBuilder.loadTexts: cfdmiHbaPortId.setStatus('current')
cfdmiHbaPortSupportedFC4Type = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaPortSupportedFC4Type.setStatus('current')
cfdmiHbaPortSupportedSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaPortSupportedSpeed.setStatus('current')
cfdmiHbaPortCurrentSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaPortCurrentSpeed.setStatus('current')
cfdmiHbaPortMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaPortMaxFrameSize.setStatus('current')
cfdmiHbaPortOsDevName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaPortOsDevName.setStatus('current')
cfdmiHbaPortHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfdmiHbaPortHostName.setStatus('current')
cfdmiRejectReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 3), CFdmiRejectReasonCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cfdmiRejectReasonCode.setStatus('current')
cfdmiRejectReasonCodeExpl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 4), CFdmiRejectReasonCodeExpl()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cfdmiRejectReasonCodeExpl.setStatus('current')
cfdmiNotifyRegOperType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("regHBA", 1), ("regHAT", 2), ("regPRT", 3), ("regPA", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cfdmiNotifyRegOperType.setStatus('current')
cfdmiNotifyHBAPortId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 6), FcNameId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cfdmiNotifyHBAPortId.setStatus('current')
cfdmiRejectRegNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 373, 0, 1)).setObjects(("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-FDMI-MIB", "cfdmiNotifyRegOperType"), ("CISCO-FDMI-MIB", "cfdmiNotifyHBAPortId"), ("CISCO-FDMI-MIB", "cfdmiRejectReasonCode"), ("CISCO-FDMI-MIB", "cfdmiRejectReasonCodeExpl"))
if mibBuilder.loadTexts: cfdmiRejectRegNotify.setStatus('current')
ciscoFdmiMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 1))
ciscoFdmiMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 2))
ciscoFdmiMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 1, 1)).setObjects(("CISCO-FDMI-MIB", "cfdmiConfigGroup"), ("CISCO-FDMI-MIB", "cfdmiHbaInformationGroup"), ("CISCO-FDMI-MIB", "cfdmiHbaPortInformationGroup"), ("CISCO-FDMI-MIB", "cfdmiNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFdmiMIBCompliance = ciscoFdmiMIBCompliance.setStatus('current')
cfdmiConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 2, 1)).setObjects(("CISCO-FDMI-MIB", "cfdmiRejectRegNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfdmiConfigGroup = cfdmiConfigGroup.setStatus('current')
cfdmiHbaInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 2, 2)).setObjects(("CISCO-FDMI-MIB", "cfdmiHbaInfoNodeName"), ("CISCO-FDMI-MIB", "cfdmiHbaInfoMfg"), ("CISCO-FDMI-MIB", "cfdmiHbaInfoSn"), ("CISCO-FDMI-MIB", "cfdmiHbaInfoModel"), ("CISCO-FDMI-MIB", "cfdmiHbaInfoModelDescr"), ("CISCO-FDMI-MIB", "cfdmiHbaInfoHwVer"), ("CISCO-FDMI-MIB", "cfdmiHbaInfoDriverVer"), ("CISCO-FDMI-MIB", "cfdmiHbaInfoOptROMVer"), ("CISCO-FDMI-MIB", "cfdmiHbaInfoFwVer"), ("CISCO-FDMI-MIB", "cfdmiHbaInfoOSInfo"), ("CISCO-FDMI-MIB", "cfdmiHbaInfoMaxCTPayload"), ("CISCO-FDMI-MIB", "cfdmiRejectReasonCode"), ("CISCO-FDMI-MIB", "cfdmiRejectReasonCodeExpl"), ("CISCO-FDMI-MIB", "cfdmiNotifyRegOperType"), ("CISCO-FDMI-MIB", "cfdmiNotifyHBAPortId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfdmiHbaInformationGroup = cfdmiHbaInformationGroup.setStatus('current')
cfdmiHbaPortInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 2, 3)).setObjects(("CISCO-FDMI-MIB", "cfdmiHbaPortSupportedFC4Type"), ("CISCO-FDMI-MIB", "cfdmiHbaPortSupportedSpeed"), ("CISCO-FDMI-MIB", "cfdmiHbaPortCurrentSpeed"), ("CISCO-FDMI-MIB", "cfdmiHbaPortMaxFrameSize"), ("CISCO-FDMI-MIB", "cfdmiHbaPortOsDevName"), ("CISCO-FDMI-MIB", "cfdmiHbaPortHostName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfdmiHbaPortInformationGroup = cfdmiHbaPortInformationGroup.setStatus('current')
cfdmiNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 2, 4)).setObjects(("CISCO-FDMI-MIB", "cfdmiRejectRegNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfdmiNotificationGroup = cfdmiNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FDMI-MIB", CFdmiRejectReasonCode=CFdmiRejectReasonCode, cfdmiHbaInfoOSInfo=cfdmiHbaInfoOSInfo, cfdmiHbaInformationGroup=cfdmiHbaInformationGroup, cfdmiNotifyHBAPortId=cfdmiNotifyHBAPortId, ciscoFdmiMIBGroups=ciscoFdmiMIBGroups, cfdmiHbaPortInformationGroup=cfdmiHbaPortInformationGroup, ciscoFdmiMIBCompliance=ciscoFdmiMIBCompliance, cfdmiNotificationGroup=cfdmiNotificationGroup, cfdmiNotifyRegOperType=cfdmiNotifyRegOperType, cfdmiRejectRegNotify=cfdmiRejectRegNotify, cfdmiHbaInfoDriverVer=cfdmiHbaInfoDriverVer, cfdmiHbaInfoMfg=cfdmiHbaInfoMfg, cfdmiHbaInfoHwVer=cfdmiHbaInfoHwVer, cfdmiHbaPortMaxFrameSize=cfdmiHbaPortMaxFrameSize, cfdmiHbaInfoEntry=cfdmiHbaInfoEntry, cfdmiHbaPortSupportedSpeed=cfdmiHbaPortSupportedSpeed, ciscoFdmiMIB=ciscoFdmiMIB, cfdmiConfig=cfdmiConfig, cfdmiConfigGroup=cfdmiConfigGroup, cfdmiRejectRegNotifyEnable=cfdmiRejectRegNotifyEnable, PYSNMP_MODULE_ID=ciscoFdmiMIB, cfdmiInfo=cfdmiInfo, ciscoFdmiMIBConformance=ciscoFdmiMIBConformance, cfdmiHbaInfoMaxCTPayload=cfdmiHbaInfoMaxCTPayload, cfdmiHbaInfoSn=cfdmiHbaInfoSn, cfdmiHbaPortTable=cfdmiHbaPortTable, cfdmiRejectReasonCode=cfdmiRejectReasonCode, cfdmiHbaInfoModel=cfdmiHbaInfoModel, cfdmiHbaInfoOptROMVer=cfdmiHbaInfoOptROMVer, cfdmiHbaPortCurrentSpeed=cfdmiHbaPortCurrentSpeed, cfdmiRejectReasonCodeExpl=cfdmiRejectReasonCodeExpl, cfdmiHbaPortSupportedFC4Type=cfdmiHbaPortSupportedFC4Type, cfdmiHbaInfoTable=cfdmiHbaInfoTable, cfdmiHbaInfoModelDescr=cfdmiHbaInfoModelDescr, cfdmiHbaInfoNodeName=cfdmiHbaInfoNodeName, cfdmiHbaInfoFwVer=cfdmiHbaInfoFwVer, cfdmiHbaPortHostName=cfdmiHbaPortHostName, CFdmiRejectReasonCodeExpl=CFdmiRejectReasonCodeExpl, ciscoFdmiMIBObjects=ciscoFdmiMIBObjects, cfdmiStatistics=cfdmiStatistics, cfdmiHbaInfoId=cfdmiHbaInfoId, ciscoFdmiMIBNotifications=ciscoFdmiMIBNotifications, cfdmiHbaPortEntry=cfdmiHbaPortEntry, cfdmiHbaPortOsDevName=cfdmiHbaPortOsDevName, cfdmiHbaPortId=cfdmiHbaPortId, ciscoFdmiMIBCompliances=ciscoFdmiMIBCompliances)
