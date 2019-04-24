#
# PySNMP MIB module CISCO-MEETINGPLACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-MEETINGPLACE-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:45:40 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, Bits, iso, MibIdentifier, Integer32, ObjectIdentity, Counter32, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "iso", "MibIdentifier", "Integer32", "ObjectIdentity", "Counter32", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "NotificationType", "IpAddress")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoMeetingPlaceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 733))
ciscoMeetingPlaceMIB.setRevisions(('2010-05-06 00:00',))
if mibBuilder.loadTexts: ciscoMeetingPlaceMIB.setLastUpdated('201005060000Z')
if mibBuilder.loadTexts: ciscoMeetingPlaceMIB.setOrganization('Cisco Systems, Inc.')
ciscoMeetingPlaceMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 733, 0))
ciscoMeetingPlaceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 733, 1))
ciscoMeetingPlaceMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 733, 2))
cmpAlarmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1))
cmpConferenceInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 2))
cmpLicenseInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 3))
cmpUsageInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4))
cmpNodeInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 5))
cmpNotificationStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmpNotificationStatus.setStatus('current')
cmpExceptionCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmpExceptionCode.setStatus('current')
cmpSysUnit = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmpSysUnit.setStatus('current')
cmpHwDev = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))).clone(namedValues=NamedValues(("mpTemperature", 1), ("mpPowerSupply", 2), ("mpSerialPort", 3), ("mpTapeDrive", 4), ("mpHardDrive", 5), ("mpDisketteDrive", 6), ("mpEthernet", 7), ("mpModem", 8), ("mpSystemMisc", 9), ("mpDSPMSC", 10), ("mpDSPPRC", 11), ("mpT1Blade", 12), ("mpAnalogBlade", 13), ("mpT1Network", 14), ("mpSystemIntegrityCard", 15), ("mpMainMemory", 16), ("mpE1Blade", 17), ("mpE1Network", 18), ("mpVoIPBlade", 19)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmpHwDev.setStatus('current')
cmpHwUnit = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmpHwUnit.setStatus('current')
cmpHwSlot = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 5), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmpHwSlot.setStatus('current')
cmpHwPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 6), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmpHwPort.setStatus('current')
cmpAlarmDesc = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 7), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmpAlarmDesc.setStatus('current')
cmpPeakMeeting = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpPeakMeeting.setStatus('current')
cmpPeakHour = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpPeakHour.setStatus('current')
cmpMeetingCurrent = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpMeetingCurrent.setStatus('current')
cmpAudioLicense = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpAudioLicense.setStatus('current')
cmpMaxAudioLicense = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpMaxAudioLicense.setStatus('current')
cmpVideoLicense = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 3, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpVideoLicense.setStatus('current')
cmpMaxVideoLicense = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 3, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpMaxVideoLicense.setStatus('current')
cmpVideoPortsUsage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpVideoPortsUsage.setStatus('current')
cmpMaxVideoPortsAvailable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpMaxVideoPortsAvailable.setStatus('current')
cmpAudioPortsUsage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpAudioPortsUsage.setStatus('current')
cmpMaxAudioPortsAvailable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpMaxAudioPortsAvailable.setStatus('current')
cmpMaxAudioPortsUsage24Hours = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpMaxAudioPortsUsage24Hours.setStatus('current')
cmpMaxVideoPortsUsage24Hours = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpMaxVideoPortsUsage24Hours.setStatus('current')
cmpNodeDeployType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 5, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpNodeDeployType.setStatus('current')
cmpNodeRole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 5, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpNodeRole.setStatus('current')
cmpRegionInfo = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 5, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpRegionInfo.setStatus('current')
cmpSiteInfo = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 5, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmpSiteInfo.setStatus('current')
cmpT1Down = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 1))
if mibBuilder.loadTexts: cmpT1Down.setStatus('current')
cmpGWSimAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 2))
if mibBuilder.loadTexts: cmpGWSimAlarm.setStatus('current')
cmpMajHwAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 3)).setObjects(("CISCO-MEETINGPLACE-MIB", "cmpExceptionCode"), ("CISCO-MEETINGPLACE-MIB", "cmpSysUnit"), ("CISCO-MEETINGPLACE-MIB", "cmpHwDev"), ("CISCO-MEETINGPLACE-MIB", "cmpHwUnit"), ("CISCO-MEETINGPLACE-MIB", "cmpHwSlot"), ("CISCO-MEETINGPLACE-MIB", "cmpHwPort"))
if mibBuilder.loadTexts: cmpMajHwAlarm.setStatus('current')
cmpMinHwAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 4)).setObjects(("CISCO-MEETINGPLACE-MIB", "cmpExceptionCode"), ("CISCO-MEETINGPLACE-MIB", "cmpSysUnit"), ("CISCO-MEETINGPLACE-MIB", "cmpHwDev"), ("CISCO-MEETINGPLACE-MIB", "cmpHwUnit"), ("CISCO-MEETINGPLACE-MIB", "cmpHwSlot"), ("CISCO-MEETINGPLACE-MIB", "cmpHwPort"))
if mibBuilder.loadTexts: cmpMinHwAlarm.setStatus('current')
cmpMajSwAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 5)).setObjects(("CISCO-MEETINGPLACE-MIB", "cmpExceptionCode"), ("CISCO-MEETINGPLACE-MIB", "cmpSysUnit"), ("CISCO-MEETINGPLACE-MIB", "cmpAlarmDesc"))
if mibBuilder.loadTexts: cmpMajSwAlarm.setStatus('current')
cmpMinSwAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 6)).setObjects(("CISCO-MEETINGPLACE-MIB", "cmpExceptionCode"), ("CISCO-MEETINGPLACE-MIB", "cmpSysUnit"), ("CISCO-MEETINGPLACE-MIB", "cmpAlarmDesc"))
if mibBuilder.loadTexts: cmpMinSwAlarm.setStatus('current')
cmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 1))
cmpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 1, 1)).setObjects(("CISCO-MEETINGPLACE-MIB", "cmpAlarmGroup"), ("CISCO-MEETINGPLACE-MIB", "cmpNotifsGroup"), ("CISCO-MEETINGPLACE-MIB", "cmpInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpMIBCompliance = cmpMIBCompliance.setStatus('current')
cmpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 2))
cmpAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 2, 1)).setObjects(("CISCO-MEETINGPLACE-MIB", "cmpExceptionCode"), ("CISCO-MEETINGPLACE-MIB", "cmpSysUnit"), ("CISCO-MEETINGPLACE-MIB", "cmpHwDev"), ("CISCO-MEETINGPLACE-MIB", "cmpHwUnit"), ("CISCO-MEETINGPLACE-MIB", "cmpHwSlot"), ("CISCO-MEETINGPLACE-MIB", "cmpHwPort"), ("CISCO-MEETINGPLACE-MIB", "cmpAlarmDesc"), ("CISCO-MEETINGPLACE-MIB", "cmpNotificationStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpAlarmGroup = cmpAlarmGroup.setStatus('current')
cmpNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 2, 2)).setObjects(("CISCO-MEETINGPLACE-MIB", "cmpT1Down"), ("CISCO-MEETINGPLACE-MIB", "cmpGWSimAlarm"), ("CISCO-MEETINGPLACE-MIB", "cmpMajHwAlarm"), ("CISCO-MEETINGPLACE-MIB", "cmpMinHwAlarm"), ("CISCO-MEETINGPLACE-MIB", "cmpMajSwAlarm"), ("CISCO-MEETINGPLACE-MIB", "cmpMinSwAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpNotifsGroup = cmpNotifsGroup.setStatus('current')
cmpInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 2, 3)).setObjects(("CISCO-MEETINGPLACE-MIB", "cmpPeakMeeting"), ("CISCO-MEETINGPLACE-MIB", "cmpPeakHour"), ("CISCO-MEETINGPLACE-MIB", "cmpMaxAudioPortsUsage24Hours"), ("CISCO-MEETINGPLACE-MIB", "cmpAudioLicense"), ("CISCO-MEETINGPLACE-MIB", "cmpMaxAudioLicense"), ("CISCO-MEETINGPLACE-MIB", "cmpVideoLicense"), ("CISCO-MEETINGPLACE-MIB", "cmpMaxVideoLicense"), ("CISCO-MEETINGPLACE-MIB", "cmpVideoPortsUsage"), ("CISCO-MEETINGPLACE-MIB", "cmpMaxVideoPortsAvailable"), ("CISCO-MEETINGPLACE-MIB", "cmpAudioPortsUsage"), ("CISCO-MEETINGPLACE-MIB", "cmpMaxAudioPortsAvailable"), ("CISCO-MEETINGPLACE-MIB", "cmpMeetingCurrent"), ("CISCO-MEETINGPLACE-MIB", "cmpMaxVideoPortsUsage24Hours"), ("CISCO-MEETINGPLACE-MIB", "cmpNodeDeployType"), ("CISCO-MEETINGPLACE-MIB", "cmpNodeRole"), ("CISCO-MEETINGPLACE-MIB", "cmpRegionInfo"), ("CISCO-MEETINGPLACE-MIB", "cmpSiteInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpInfoGroup = cmpInfoGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEETINGPLACE-MIB", cmpMIBCompliance=cmpMIBCompliance, cmpRegionInfo=cmpRegionInfo, ciscoMeetingPlaceMIBConform=ciscoMeetingPlaceMIBConform, cmpMeetingCurrent=cmpMeetingCurrent, cmpMaxVideoPortsAvailable=cmpMaxVideoPortsAvailable, cmpAudioPortsUsage=cmpAudioPortsUsage, cmpMaxAudioLicense=cmpMaxAudioLicense, cmpGWSimAlarm=cmpGWSimAlarm, cmpMajHwAlarm=cmpMajHwAlarm, cmpMIBCompliances=cmpMIBCompliances, PYSNMP_MODULE_ID=ciscoMeetingPlaceMIB, cmpMIBGroups=cmpMIBGroups, cmpInfoGroup=cmpInfoGroup, cmpVideoPortsUsage=cmpVideoPortsUsage, cmpUsageInfo=cmpUsageInfo, cmpMaxAudioPortsUsage24Hours=cmpMaxAudioPortsUsage24Hours, cmpHwDev=cmpHwDev, cmpSysUnit=cmpSysUnit, cmpPeakHour=cmpPeakHour, cmpNodeDeployType=cmpNodeDeployType, cmpNodeInfo=cmpNodeInfo, cmpAudioLicense=cmpAudioLicense, cmpMaxVideoLicense=cmpMaxVideoLicense, cmpAlarmObjects=cmpAlarmObjects, cmpConferenceInfo=cmpConferenceInfo, ciscoMeetingPlaceMIBObjects=ciscoMeetingPlaceMIBObjects, cmpNotificationStatus=cmpNotificationStatus, cmpVideoLicense=cmpVideoLicense, ciscoMeetingPlaceMIB=ciscoMeetingPlaceMIB, cmpExceptionCode=cmpExceptionCode, cmpNodeRole=cmpNodeRole, cmpMinSwAlarm=cmpMinSwAlarm, cmpMajSwAlarm=cmpMajSwAlarm, cmpHwPort=cmpHwPort, cmpNotifsGroup=cmpNotifsGroup, cmpT1Down=cmpT1Down, cmpPeakMeeting=cmpPeakMeeting, cmpSiteInfo=cmpSiteInfo, cmpMinHwAlarm=cmpMinHwAlarm, cmpHwSlot=cmpHwSlot, cmpHwUnit=cmpHwUnit, ciscoMeetingPlaceMIBNotifs=ciscoMeetingPlaceMIBNotifs, cmpMaxVideoPortsUsage24Hours=cmpMaxVideoPortsUsage24Hours, cmpAlarmGroup=cmpAlarmGroup, cmpMaxAudioPortsAvailable=cmpMaxAudioPortsAvailable, cmpAlarmDesc=cmpAlarmDesc, cmpLicenseInfo=cmpLicenseInfo)
