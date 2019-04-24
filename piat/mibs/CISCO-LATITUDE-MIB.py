#
# PySNMP MIB module CISCO-LATITUDE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-LATITUDE-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:48:44 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Integer32, enterprises, Bits, Counter64, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Integer32", "enterprises", "Bits", "Counter64", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
latitudeComm = ModuleIdentity((1, 3, 6, 1, 4, 1, 7185))
latitudeComm.setRevisions(('2004-08-16 00:00',))
if mibBuilder.loadTexts: latitudeComm.setLastUpdated('200408160000Z')
if mibBuilder.loadTexts: latitudeComm.setOrganization('Cisco Systems, Inc.')
latitudeReg = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 1))
latitudeModules = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 1, 1))
latitudeGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 2))
latitudeProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 3))
meetingplace = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 3, 1))
meetingplaceConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 3, 1, 1))
meetingplaceObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 3, 1, 2))
meetingplaceEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3))
meetingplaceEventsV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0))
mpExCode = MibScalar((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpExCode.setStatus('current')
mpSysUnit = MibScalar((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpSysUnit.setStatus('current')
mpHwDev = MibScalar((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))).clone(namedValues=NamedValues(("mpTemperature", 1), ("mpPowerSupply", 2), ("mpSerialPort", 3), ("mpTapeDrive", 4), ("mpHardDrive", 5), ("mpDisketteDrive", 6), ("mpEthernet", 7), ("mpModem", 8), ("mpSystemMisc", 9), ("mpDSPMSC", 10), ("mpDSPPRC", 11), ("mpT1Blade", 12), ("mpAnalogBlade", 13), ("mpT1Network", 14), ("mpSystemIntegrityCard", 15), ("mpMainMemory", 16), ("mpE1Blade", 17), ("mpE1Network", 18), ("mpVoIPBlade", 19)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpHwDev.setStatus('current')
mpHwUnit = MibScalar((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpHwUnit.setStatus('current')
mpHwSlot = MibScalar((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpHwSlot.setStatus('current')
mpHwPort = MibScalar((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpHwPort.setStatus('current')
mpAlarmDesc = MibScalar((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpAlarmDesc.setStatus('current')
mpT1Down = NotificationType((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 1))
if mibBuilder.loadTexts: mpT1Down.setStatus('current')
mpGWSimAlarm = NotificationType((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 2))
if mibBuilder.loadTexts: mpGWSimAlarm.setStatus('current')
mpMajHwAlarm = NotificationType((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 3)).setObjects(("CISCO-LATITUDE-MIB", "mpExCode"), ("CISCO-LATITUDE-MIB", "mpSysUnit"), ("CISCO-LATITUDE-MIB", "mpHwDev"), ("CISCO-LATITUDE-MIB", "mpHwUnit"), ("CISCO-LATITUDE-MIB", "mpHwSlot"), ("CISCO-LATITUDE-MIB", "mpHwPort"))
if mibBuilder.loadTexts: mpMajHwAlarm.setStatus('current')
mpMinHwAlarm = NotificationType((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 4)).setObjects(("CISCO-LATITUDE-MIB", "mpExCode"), ("CISCO-LATITUDE-MIB", "mpSysUnit"), ("CISCO-LATITUDE-MIB", "mpHwDev"), ("CISCO-LATITUDE-MIB", "mpHwUnit"), ("CISCO-LATITUDE-MIB", "mpHwSlot"), ("CISCO-LATITUDE-MIB", "mpHwPort"))
if mibBuilder.loadTexts: mpMinHwAlarm.setStatus('current')
mpMajSwAlarm = NotificationType((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 5)).setObjects(("CISCO-LATITUDE-MIB", "mpExCode"), ("CISCO-LATITUDE-MIB", "mpSysUnit"), ("CISCO-LATITUDE-MIB", "mpAlarmDesc"))
if mibBuilder.loadTexts: mpMajSwAlarm.setStatus('current')
mpMinSwAlarm = NotificationType((1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 6)).setObjects(("CISCO-LATITUDE-MIB", "mpExCode"), ("CISCO-LATITUDE-MIB", "mpSysUnit"), ("CISCO-LATITUDE-MIB", "mpAlarmDesc"))
if mibBuilder.loadTexts: mpMinSwAlarm.setStatus('current')
ciscoLatitudeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 3, 1, 1, 1))
ciscoLatitudeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7185, 3, 1, 1, 2))
ciscoLatitudeMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 7185, 3, 1, 1, 1, 1)).setObjects(("CISCO-LATITUDE-MIB", "ciscoLatitudeAlarmGroupRev1"), ("CISCO-LATITUDE-MIB", "ciscoLatitudeNotifsGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLatitudeMIBComplianceRev1 = ciscoLatitudeMIBComplianceRev1.setStatus('current')
ciscoLatitudeAlarmGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 7185, 3, 1, 1, 2, 1)).setObjects(("CISCO-LATITUDE-MIB", "mpExCode"), ("CISCO-LATITUDE-MIB", "mpSysUnit"), ("CISCO-LATITUDE-MIB", "mpHwDev"), ("CISCO-LATITUDE-MIB", "mpHwUnit"), ("CISCO-LATITUDE-MIB", "mpHwSlot"), ("CISCO-LATITUDE-MIB", "mpHwPort"), ("CISCO-LATITUDE-MIB", "mpAlarmDesc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLatitudeAlarmGroupRev1 = ciscoLatitudeAlarmGroupRev1.setStatus('current')
ciscoLatitudeNotifsGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 7185, 3, 1, 1, 2, 2)).setObjects(("CISCO-LATITUDE-MIB", "mpT1Down"), ("CISCO-LATITUDE-MIB", "mpGWSimAlarm"), ("CISCO-LATITUDE-MIB", "mpMajHwAlarm"), ("CISCO-LATITUDE-MIB", "mpMinHwAlarm"), ("CISCO-LATITUDE-MIB", "mpMajSwAlarm"), ("CISCO-LATITUDE-MIB", "mpMinSwAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLatitudeNotifsGroupRev1 = ciscoLatitudeNotifsGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-LATITUDE-MIB", ciscoLatitudeMIBCompliances=ciscoLatitudeMIBCompliances, meetingplace=meetingplace, mpMinSwAlarm=mpMinSwAlarm, mpExCode=mpExCode, latitudeReg=latitudeReg, latitudeComm=latitudeComm, mpHwUnit=mpHwUnit, mpT1Down=mpT1Down, meetingplaceEvents=meetingplaceEvents, mpHwDev=mpHwDev, ciscoLatitudeMIBGroups=ciscoLatitudeMIBGroups, ciscoLatitudeAlarmGroupRev1=ciscoLatitudeAlarmGroupRev1, mpMinHwAlarm=mpMinHwAlarm, mpSysUnit=mpSysUnit, latitudeModules=latitudeModules, mpMajSwAlarm=mpMajSwAlarm, mpHwPort=mpHwPort, latitudeGeneric=latitudeGeneric, ciscoLatitudeNotifsGroupRev1=ciscoLatitudeNotifsGroupRev1, meetingplaceObjs=meetingplaceObjs, meetingplaceEventsV2=meetingplaceEventsV2, mpGWSimAlarm=mpGWSimAlarm, mpHwSlot=mpHwSlot, mpMajHwAlarm=mpMajHwAlarm, PYSNMP_MODULE_ID=latitudeComm, meetingplaceConfs=meetingplaceConfs, latitudeProducts=latitudeProducts, mpAlarmDesc=mpAlarmDesc, ciscoLatitudeMIBComplianceRev1=ciscoLatitudeMIBComplianceRev1)