#
# PySNMP MIB module CISCO-ENTITY-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-ENTITY-SENSOR-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:38:17 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, Bits, Integer32, NotificationType, Counter64, ModuleIdentity, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ObjectIdentity, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Integer32", "NotificationType", "Counter64", "ModuleIdentity", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ObjectIdentity", "Gauge32", "MibIdentifier")
TimeStamp, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TruthValue", "TextualConvention")
ciscoEntitySensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 91))
ciscoEntitySensorMIB.setRevisions(('2017-01-19 00:00', '2015-01-15 00:00', '2013-09-21 00:00', '2007-11-12 00:00', '2006-01-01 00:00', '2005-09-08 00:00', '2003-01-07 00:00', '2002-10-16 00:00', '2000-06-20 00:00',))
if mibBuilder.loadTexts: ciscoEntitySensorMIB.setLastUpdated('201701190000Z')
if mibBuilder.loadTexts: ciscoEntitySensorMIB.setOrganization('Cisco Systems, Inc.')
entitySensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1))
entitySensorMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 2))
entitySensorMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3))
class SensorDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("voltsAC", 3), ("voltsDC", 4), ("amperes", 5), ("watts", 6), ("hertz", 7), ("celsius", 8), ("percentRH", 9), ("rpm", 10), ("cmm", 11), ("truthvalue", 12), ("specialEnum", 13), ("dBm", 14), ("dB", 15))

class SensorDataScale(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class SensorPrecision(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-8, 9)

class SensorValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class SensorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3))

class SensorValueUpdateRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 999999999)

class SensorThresholdSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30))
    namedValues = NamedValues(("other", 1), ("minor", 10), ("major", 20), ("critical", 30))

class SensorThresholdRelation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("lessThan", 1), ("lessOrEqual", 2), ("greaterThan", 3), ("greaterOrEqual", 4), ("equalTo", 5), ("notEqualTo", 6))

entSensorValues = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1))
entSensorThresholds = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2))
entSensorGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 3))
entSensorValueTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1), )
if mibBuilder.loadTexts: entSensorValueTable.setStatus('current')
entSensorValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entSensorValueEntry.setStatus('current')
entSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 1), SensorDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorType.setStatus('current')
entSensorScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 2), SensorDataScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorScale.setStatus('current')
entSensorPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 3), SensorPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorPrecision.setStatus('current')
entSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 4), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValue.setStatus('current')
entSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 5), SensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorStatus.setStatus('current')
entSensorValueTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValueTimeStamp.setStatus('current')
entSensorValueUpdateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 7), SensorValueUpdateRate()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValueUpdateRate.setStatus('current')
entSensorMeasuredEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 8), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorMeasuredEntity.setStatus('current')
entSensorThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1), )
if mibBuilder.loadTexts: entSensorThresholdTable.setStatus('current')
entSensorThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdIndex"))
if mibBuilder.loadTexts: entSensorThresholdEntry.setStatus('current')
entSensorThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99999999)))
if mibBuilder.loadTexts: entSensorThresholdIndex.setStatus('current')
entSensorThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 2), SensorThresholdSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdSeverity.setStatus('current')
entSensorThresholdRelation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 3), SensorThresholdRelation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdRelation.setStatus('current')
entSensorThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 4), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdValue.setStatus('current')
entSensorThresholdEvaluation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorThresholdEvaluation.setStatus('current')
entSensorThresholdNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdNotificationEnable.setStatus('current')
entSensorThreshNotifGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 3, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThreshNotifGlobalEnable.setStatus('current')
entitySensorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0))
entSensorThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdSeverity"))
if mibBuilder.loadTexts: entSensorThresholdNotification.setStatus('current')
entSensorThresholdRecoveryNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0, 2)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdSeverity"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"))
if mibBuilder.loadTexts: entSensorThresholdRecoveryNotification.setStatus('current')
entitySensorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1))
entitySensorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2))
entitySensorMIBComplianceV01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV01 = entitySensorMIBComplianceV01.setStatus('deprecated')
entitySensorMIBComplianceV02 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 2)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV02 = entitySensorMIBComplianceV02.setStatus('deprecated')
entitySensorMIBComplianceV03 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 3)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV03 = entitySensorMIBComplianceV03.setStatus('deprecated')
entitySensorMIBComplianceV04 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 4)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroupSup1"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorNotifCtrlGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV04 = entitySensorMIBComplianceV04.setStatus('deprecated')
entitySensorMIBComplianceV05 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 5)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroupSup1"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorNotifCtrlGlobalGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV05 = entitySensorMIBComplianceV05.setStatus('current')
entitySensorValueGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorType"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorScale"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorPrecision"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorStatus"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValueTimeStamp"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValueUpdateRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorValueGroup = entitySensorValueGroup.setStatus('current')
entitySensorThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 2)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdSeverity"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdRelation"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdEvaluation"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorThresholdGroup = entitySensorThresholdGroup.setStatus('current')
entitySensorThresholdNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 3)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorThresholdNotificationGroup = entitySensorThresholdNotificationGroup.setStatus('deprecated')
entitySensorValueGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 4)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorMeasuredEntity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorValueGroupSup1 = entitySensorValueGroupSup1.setStatus('current')
entitySensorNotifCtrlGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 5)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThreshNotifGlobalEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorNotifCtrlGlobalGroup = entitySensorNotifCtrlGlobalGroup.setStatus('current')
entitySensorNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 6)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotification"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdRecoveryNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorNotificationGroup = entitySensorNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-MIB", entitySensorMIBGroups=entitySensorMIBGroups, entSensorStatus=entSensorStatus, entSensorMeasuredEntity=entSensorMeasuredEntity, SensorValue=SensorValue, entSensorThresholdNotificationEnable=entSensorThresholdNotificationEnable, ciscoEntitySensorMIB=ciscoEntitySensorMIB, entSensorThresholdEntry=entSensorThresholdEntry, SensorThresholdRelation=SensorThresholdRelation, SensorDataScale=SensorDataScale, entitySensorMIBComplianceV04=entitySensorMIBComplianceV04, entitySensorValueGroup=entitySensorValueGroup, entitySensorMIBCompliances=entitySensorMIBCompliances, entitySensorValueGroupSup1=entitySensorValueGroupSup1, entSensorThresholdSeverity=entSensorThresholdSeverity, SensorDataType=SensorDataType, entitySensorMIBComplianceV05=entitySensorMIBComplianceV05, entitySensorMIBNotifications=entitySensorMIBNotifications, entitySensorMIBObjects=entitySensorMIBObjects, entSensorType=entSensorType, entSensorThresholdValue=entSensorThresholdValue, entSensorThresholdRelation=entSensorThresholdRelation, entSensorThreshNotifGlobalEnable=entSensorThreshNotifGlobalEnable, entSensorValueUpdateRate=entSensorValueUpdateRate, entitySensorMIBConformance=entitySensorMIBConformance, entitySensorMIBComplianceV03=entitySensorMIBComplianceV03, entitySensorThresholdGroup=entitySensorThresholdGroup, entSensorThresholds=entSensorThresholds, entSensorValueTable=entSensorValueTable, entSensorValueTimeStamp=entSensorValueTimeStamp, SensorStatus=SensorStatus, entitySensorNotificationGroup=entitySensorNotificationGroup, entSensorGlobalObjects=entSensorGlobalObjects, PYSNMP_MODULE_ID=ciscoEntitySensorMIB, SensorValueUpdateRate=SensorValueUpdateRate, SensorPrecision=SensorPrecision, entSensorValues=entSensorValues, entSensorPrecision=entSensorPrecision, entSensorValue=entSensorValue, entSensorThresholdEvaluation=entSensorThresholdEvaluation, entitySensorMIBNotificationPrefix=entitySensorMIBNotificationPrefix, entSensorValueEntry=entSensorValueEntry, SensorThresholdSeverity=SensorThresholdSeverity, entitySensorMIBComplianceV01=entitySensorMIBComplianceV01, entSensorThresholdRecoveryNotification=entSensorThresholdRecoveryNotification, entSensorThresholdIndex=entSensorThresholdIndex, entSensorThresholdNotification=entSensorThresholdNotification, entitySensorMIBComplianceV02=entitySensorMIBComplianceV02, entitySensorNotifCtrlGlobalGroup=entitySensorNotifCtrlGlobalGroup, entSensorScale=entSensorScale, entitySensorThresholdNotificationGroup=entitySensorThresholdNotificationGroup, entSensorThresholdTable=entSensorThresholdTable)
