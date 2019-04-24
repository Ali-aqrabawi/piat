#
# PySNMP MIB module CISCO-APPLICATION-ACCELERATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-APPLICATION-ACCELERATION-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:44:59 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetPortNumber, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Bits, Gauge32, Counter32, ObjectIdentity, IpAddress, ModuleIdentity, iso, NotificationType, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Gauge32", "Counter32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "iso", "NotificationType", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier")
TruthValue, TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DateAndTime", "DisplayString")
ciscoApplicationAccelerationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 594))
ciscoApplicationAccelerationMIB.setRevisions(('2006-10-30 00:00',))
if mibBuilder.loadTexts: ciscoApplicationAccelerationMIB.setLastUpdated('200610300000Z')
if mibBuilder.loadTexts: ciscoApplicationAccelerationMIB.setOrganization('Cisco Systems, Inc.')
caaMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 594, 0))
caaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 594, 1))
caaMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 594, 2))
caaStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1))
caaNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 2))
class CaaState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("impaired", 2), ("down", 3))

caaStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1), )
if mibBuilder.loadTexts: caaStatTable.setStatus('current')
caaStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-APPLICATION-ACCELERATION-MIB", "caaPort"))
if mibBuilder.loadTexts: caaStatEntry.setStatus('current')
caaPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 1), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: caaPort.setStatus('current')
caaState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 2), CaaState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caaState.setStatus('current')
caaRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 3), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaRequests.setStatus('current')
caaNoncondensableRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 4), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaNoncondensableRequests.setStatus('current')
caaRequestedObjectSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 5), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaRequestedObjectSize.setStatus('current')
caaFinalResponseSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 6), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaFinalResponseSize.setStatus('current')
caaLastRestartedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caaLastRestartedTime.setStatus('current')
caaTransformed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 8), Counter32()).setUnits('transformations').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaTransformed.setStatus('current')
caaUntransformed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 9), Counter32()).setUnits('transformations').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaUntransformed.setStatus('current')
caaTransformedObjectRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 10), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaTransformedObjectRequests.setStatus('current')
caaTransformedObjectIMSRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 11), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaTransformedObjectIMSRequests.setStatus('current')
caaStaticObjectHits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 12), Counter32()).setUnits('cache-hits').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaStaticObjectHits.setStatus('current')
caaStaticObjectHitSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 13), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaStaticObjectHitSize.setStatus('current')
caaStaticObjectMisses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 14), Counter32()).setUnits('cache-misses').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaStaticObjectMisses.setStatus('current')
caaStaticObjectMissSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 15), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaStaticObjectMissSize.setStatus('current')
caaRefreshHits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 16), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaRefreshHits.setStatus('current')
caaIMSHits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 17), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaIMSHits.setStatus('current')
caaIMSMisses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 18), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaIMSMisses.setStatus('current')
caaDirectRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 19), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaDirectRequests.setStatus('current')
caaRequestSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 20), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaRequestSize.setStatus('current')
caaDeltaAbandons = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 1, 1, 1, 21), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: caaDeltaAbandons.setStatus('current')
caaStateChangeNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 594, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: caaStateChangeNotifEnabled.setStatus('current')
caaStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 594, 0, 1)).setObjects(("CISCO-APPLICATION-ACCELERATION-MIB", "caaState"))
if mibBuilder.loadTexts: caaStateChange.setStatus('current')
caaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 1))
caaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 2))
caaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 1, 1)).setObjects(("CISCO-APPLICATION-ACCELERATION-MIB", "caaMIBStatsGroup"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaMIBNotificationsGroup"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaMIBNotifObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caaMIBCompliance = caaMIBCompliance.setStatus('current')
caaMIBStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 2, 1)).setObjects(("CISCO-APPLICATION-ACCELERATION-MIB", "caaState"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaRequests"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaNoncondensableRequests"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaRequestedObjectSize"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaFinalResponseSize"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaLastRestartedTime"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaTransformed"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaUntransformed"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaTransformedObjectRequests"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaTransformedObjectIMSRequests"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaStaticObjectHits"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaStaticObjectHitSize"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaStaticObjectMisses"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaStaticObjectMissSize"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaRefreshHits"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaIMSHits"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaIMSMisses"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaDirectRequests"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaRequestSize"), ("CISCO-APPLICATION-ACCELERATION-MIB", "caaDeltaAbandons"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caaMIBStatsGroup = caaMIBStatsGroup.setStatus('current')
caaMIBNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 2, 2)).setObjects(("CISCO-APPLICATION-ACCELERATION-MIB", "caaStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caaMIBNotificationsGroup = caaMIBNotificationsGroup.setStatus('current')
caaMIBNotifObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 594, 2, 2, 3)).setObjects(("CISCO-APPLICATION-ACCELERATION-MIB", "caaStateChangeNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caaMIBNotifObjectGroup = caaMIBNotifObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-APPLICATION-ACCELERATION-MIB", caaTransformedObjectRequests=caaTransformedObjectRequests, caaMIBConformance=caaMIBConformance, caaMIBObjects=caaMIBObjects, caaStats=caaStats, caaDeltaAbandons=caaDeltaAbandons, caaMIBNotificationsGroup=caaMIBNotificationsGroup, PYSNMP_MODULE_ID=ciscoApplicationAccelerationMIB, caaMIBCompliance=caaMIBCompliance, caaNotificationObjects=caaNotificationObjects, CaaState=CaaState, caaMIBStatsGroup=caaMIBStatsGroup, caaTransformedObjectIMSRequests=caaTransformedObjectIMSRequests, caaStateChangeNotifEnabled=caaStateChangeNotifEnabled, caaPort=caaPort, caaIMSMisses=caaIMSMisses, caaNoncondensableRequests=caaNoncondensableRequests, caaMIBNotifications=caaMIBNotifications, ciscoApplicationAccelerationMIB=ciscoApplicationAccelerationMIB, caaIMSHits=caaIMSHits, caaRequests=caaRequests, caaStaticObjectHitSize=caaStaticObjectHitSize, caaMIBCompliances=caaMIBCompliances, caaStaticObjectMisses=caaStaticObjectMisses, caaTransformed=caaTransformed, caaStatEntry=caaStatEntry, caaStaticObjectMissSize=caaStaticObjectMissSize, caaStaticObjectHits=caaStaticObjectHits, caaFinalResponseSize=caaFinalResponseSize, caaStatTable=caaStatTable, caaRequestSize=caaRequestSize, caaMIBGroups=caaMIBGroups, caaUntransformed=caaUntransformed, caaStateChange=caaStateChange, caaLastRestartedTime=caaLastRestartedTime, caaMIBNotifObjectGroup=caaMIBNotifObjectGroup, caaRequestedObjectSize=caaRequestedObjectSize, caaDirectRequests=caaDirectRequests, caaState=caaState, caaRefreshHits=caaRefreshHits)
