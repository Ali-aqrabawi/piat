#
# PySNMP MIB module CISCO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:34:08 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CountryCode, = mibBuilder.importSymbols("CISCO-TC", "CountryCode")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, IpAddress, iso, Bits, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Gauge32, NotificationType, Integer32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "iso", "Bits", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Gauge32", "NotificationType", "Integer32", "ObjectIdentity", "Counter64")
TruthValue, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention")
ciscoSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 131))
ciscoSystemMIB.setRevisions(('2007-09-16 00:00', '2007-05-29 00:00', '2001-06-22 00:00', '2000-01-25 17:00', '1999-02-02 17:00',))
if mibBuilder.loadTexts: ciscoSystemMIB.setLastUpdated('200709160000Z')
if mibBuilder.loadTexts: ciscoSystemMIB.setOrganization('Cisco Systems, Inc.')
ciscoSystemMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 1))
csyClock = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 1))
csyLocation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 2))
csySummerTime = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3))
csyScheduledReset = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 4))
csySnmpAuthentication = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 5))
csyGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 6))
csyClockDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 1, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csyClockDateAndTime.setStatus('current')
csyClockLostOnReboot = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csyClockLostOnReboot.setStatus('current')
csyLocationCountry = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 2, 1), CountryCode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csyLocationCountry.setStatus('current')
csySummerTimeStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csySummerTimeStatus.setStatus('current')
csySummerTimeOffset = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440))).setUnits('Minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: csySummerTimeOffset.setStatus('current')
csySummerTimeRecurringStart = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csySummerTimeRecurringStart.setStatus('current')
csySummerTimeRecurringEnd = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csySummerTimeRecurringEnd.setStatus('current')
csyStandardTmZnGMTOffset = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-720, 720))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: csyStandardTmZnGMTOffset.setStatus('current')
csySummerTmZnGMTOffset = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-720, 720))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: csySummerTmZnGMTOffset.setStatus('current')
csyScheduledResetTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 4, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csyScheduledResetTime.setStatus('current')
csyScheduledResetAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("resetMinDown", 2))).clone('reset')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csyScheduledResetAction.setStatus('current')
csyScheduledResetReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 4, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csyScheduledResetReason.setStatus('current')
csySnmpAuthFail = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 5, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csySnmpAuthFail.setStatus('current')
csySnmpAuthFailAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 5, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csySnmpAuthFailAddressType.setStatus('current')
csySnmpAuthFailAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 5, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csySnmpAuthFailAddress.setStatus('current')
csyNotificationsEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 6, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csyNotificationsEnable.setStatus('current')
ciscoSystemMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 2))
ciscoSystemMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 2, 0))
ciscoSystemClockChanged = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 131, 2, 0, 1)).setObjects(("CISCO-SYSTEM-MIB", "csyClockDateAndTime"))
if mibBuilder.loadTexts: ciscoSystemClockChanged.setStatus('current')
ciscoSystemMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 3))
ciscoSystemMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 1))
ciscoSystemMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2))
ciscoSystemMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 1, 1)).setObjects(("CISCO-SYSTEM-MIB", "ciscoSystemClockGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemLocationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemMIBCompliance = ciscoSystemMIBCompliance.setStatus('deprecated')
ciscoSystemMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 1, 2)).setObjects(("CISCO-SYSTEM-MIB", "ciscoSystemClockGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemLocationGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemSummerTimeGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemScheduledResetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemMIBCompliance2 = ciscoSystemMIBCompliance2.setStatus('deprecated')
ciscoSystemMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 1, 3)).setObjects(("CISCO-SYSTEM-MIB", "ciscoSystemClockGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemLocationGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemSummerTimeGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemScheduledResetGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemSnmpAuthGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemGeneralGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemMIBCompliance3 = ciscoSystemMIBCompliance3.setStatus('deprecated')
ciscoSystemMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 1, 4)).setObjects(("CISCO-SYSTEM-MIB", "ciscoSystemClockGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemLocationGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemSummerTimeGroupRev1"), ("CISCO-SYSTEM-MIB", "ciscoSystemScheduledResetGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemSnmpAuthGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemGeneralGroup"), ("CISCO-SYSTEM-MIB", "ciscoSystemNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemMIBCompliance4 = ciscoSystemMIBCompliance4.setStatus('current')
ciscoSystemClockGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 1)).setObjects(("CISCO-SYSTEM-MIB", "csyClockDateAndTime"), ("CISCO-SYSTEM-MIB", "csyClockLostOnReboot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemClockGroup = ciscoSystemClockGroup.setStatus('current')
ciscoSystemLocationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 2)).setObjects(("CISCO-SYSTEM-MIB", "csyLocationCountry"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemLocationGroup = ciscoSystemLocationGroup.setStatus('current')
ciscoSystemSummerTimeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 3)).setObjects(("CISCO-SYSTEM-MIB", "csySummerTimeStatus"), ("CISCO-SYSTEM-MIB", "csySummerTimeOffset"), ("CISCO-SYSTEM-MIB", "csySummerTimeRecurringStart"), ("CISCO-SYSTEM-MIB", "csySummerTimeRecurringEnd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemSummerTimeGroup = ciscoSystemSummerTimeGroup.setStatus('deprecated')
ciscoSystemScheduledResetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 4)).setObjects(("CISCO-SYSTEM-MIB", "csyScheduledResetTime"), ("CISCO-SYSTEM-MIB", "csyScheduledResetAction"), ("CISCO-SYSTEM-MIB", "csyScheduledResetReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemScheduledResetGroup = ciscoSystemScheduledResetGroup.setStatus('current')
ciscoSystemSnmpAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 5)).setObjects(("CISCO-SYSTEM-MIB", "csySnmpAuthFail"), ("CISCO-SYSTEM-MIB", "csySnmpAuthFailAddressType"), ("CISCO-SYSTEM-MIB", "csySnmpAuthFailAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemSnmpAuthGroup = ciscoSystemSnmpAuthGroup.setStatus('current')
ciscoSystemGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 6)).setObjects(("CISCO-SYSTEM-MIB", "csyNotificationsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemGeneralGroup = ciscoSystemGeneralGroup.setStatus('current')
ciscoSystemNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 7)).setObjects(("CISCO-SYSTEM-MIB", "ciscoSystemClockChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemNotificationsGroup = ciscoSystemNotificationsGroup.setStatus('current')
ciscoSystemSummerTimeGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 8)).setObjects(("CISCO-SYSTEM-MIB", "csySummerTimeStatus"), ("CISCO-SYSTEM-MIB", "csySummerTimeOffset"), ("CISCO-SYSTEM-MIB", "csySummerTimeRecurringStart"), ("CISCO-SYSTEM-MIB", "csySummerTimeRecurringEnd"), ("CISCO-SYSTEM-MIB", "csyStandardTmZnGMTOffset"), ("CISCO-SYSTEM-MIB", "csySummerTmZnGMTOffset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemSummerTimeGroupRev1 = ciscoSystemSummerTimeGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSTEM-MIB", csyGeneral=csyGeneral, csySnmpAuthFailAddress=csySnmpAuthFailAddress, ciscoSystemMIBCompliance3=ciscoSystemMIBCompliance3, ciscoSystemGeneralGroup=ciscoSystemGeneralGroup, csySummerTimeStatus=csySummerTimeStatus, ciscoSystemMIBNotifications=ciscoSystemMIBNotifications, ciscoSystemMIBConformance=ciscoSystemMIBConformance, PYSNMP_MODULE_ID=ciscoSystemMIB, ciscoSystemClockChanged=ciscoSystemClockChanged, ciscoSystemMIBCompliance2=ciscoSystemMIBCompliance2, csySummerTimeRecurringStart=csySummerTimeRecurringStart, ciscoSystemMIBGroups=ciscoSystemMIBGroups, ciscoSystemLocationGroup=ciscoSystemLocationGroup, ciscoSystemNotificationsGroup=ciscoSystemNotificationsGroup, csyLocationCountry=csyLocationCountry, csySummerTimeRecurringEnd=csySummerTimeRecurringEnd, ciscoSystemSummerTimeGroupRev1=ciscoSystemSummerTimeGroupRev1, csyNotificationsEnable=csyNotificationsEnable, ciscoSystemMIBCompliance=ciscoSystemMIBCompliance, csyScheduledResetTime=csyScheduledResetTime, ciscoSystemSummerTimeGroup=ciscoSystemSummerTimeGroup, ciscoSystemMIBCompliance4=ciscoSystemMIBCompliance4, csyScheduledResetReason=csyScheduledResetReason, csySnmpAuthFailAddressType=csySnmpAuthFailAddressType, ciscoSystemMIB=ciscoSystemMIB, csyLocation=csyLocation, csySummerTmZnGMTOffset=csySummerTmZnGMTOffset, csyClockLostOnReboot=csyClockLostOnReboot, ciscoSystemClockGroup=ciscoSystemClockGroup, ciscoSystemSnmpAuthGroup=ciscoSystemSnmpAuthGroup, csySnmpAuthentication=csySnmpAuthentication, csyScheduledReset=csyScheduledReset, csySnmpAuthFail=csySnmpAuthFail, csySummerTimeOffset=csySummerTimeOffset, ciscoSystemMIBObjects=ciscoSystemMIBObjects, csyClockDateAndTime=csyClockDateAndTime, csySummerTime=csySummerTime, ciscoSystemMIBNotificationPrefix=ciscoSystemMIBNotificationPrefix, ciscoSystemScheduledResetGroup=ciscoSystemScheduledResetGroup, csyScheduledResetAction=csyScheduledResetAction, ciscoSystemMIBCompliances=ciscoSystemMIBCompliances, csyStandardTmZnGMTOffset=csyStandardTmZnGMTOffset, csyClock=csyClock)
