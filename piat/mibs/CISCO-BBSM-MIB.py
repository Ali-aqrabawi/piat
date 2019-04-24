#
# PySNMP MIB module CISCO-BBSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-BBSM-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:44:13 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Unsigned32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, iso, NotificationType, Integer32, ModuleIdentity, Gauge32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "iso", "NotificationType", "Integer32", "ModuleIdentity", "Gauge32", "Bits", "IpAddress")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
ciscoBbsmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 358))
ciscoBbsmMIB.setRevisions(('2004-04-03 00:00',))
if mibBuilder.loadTexts: ciscoBbsmMIB.setLastUpdated('200404030000Z')
if mibBuilder.loadTexts: ciscoBbsmMIB.setOrganization('Cisco Systems, Inc.')
ciscoBbsmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 0))
ciscoBbsmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 1))
ciscoBbsmEventInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1))
cbbsmEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 1), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventDescription.setStatus('current')
cbbsmEventSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventSource.setStatus('current')
cbbsmEventID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventID.setStatus('current')
cbbsmEventType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("error", 1), ("warning", 2), ("information", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventType.setStatus('current')
cbbsmEventTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 5), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventTime.setStatus('current')
ciscoBbsmEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 358, 0, 1)).setObjects(("CISCO-BBSM-MIB", "cbbsmEventDescription"), ("CISCO-BBSM-MIB", "cbbsmEventSource"), ("CISCO-BBSM-MIB", "cbbsmEventID"), ("CISCO-BBSM-MIB", "cbbsmEventType"), ("CISCO-BBSM-MIB", "cbbsmEventTime"))
if mibBuilder.loadTexts: ciscoBbsmEvent.setStatus('current')
ciscoBbsmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 2))
ciscoBbsmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 1))
ciscoBbsmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2))
ciscoBbsmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 1, 1)).setObjects(("CISCO-BBSM-MIB", "ciscoBbsmMIBGroup"), ("CISCO-BBSM-MIB", "ciscoBbsmMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBbsmMIBCompliance = ciscoBbsmMIBCompliance.setStatus('current')
ciscoBbsmMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2, 1)).setObjects(("CISCO-BBSM-MIB", "cbbsmEventDescription"), ("CISCO-BBSM-MIB", "cbbsmEventSource"), ("CISCO-BBSM-MIB", "cbbsmEventID"), ("CISCO-BBSM-MIB", "cbbsmEventType"), ("CISCO-BBSM-MIB", "cbbsmEventTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBbsmMIBGroup = ciscoBbsmMIBGroup.setStatus('current')
ciscoBbsmMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2, 2)).setObjects(("CISCO-BBSM-MIB", "ciscoBbsmEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBbsmMIBNotificationGroup = ciscoBbsmMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-BBSM-MIB", cbbsmEventID=cbbsmEventID, cbbsmEventTime=cbbsmEventTime, ciscoBbsmMIB=ciscoBbsmMIB, ciscoBbsmNotifications=ciscoBbsmNotifications, ciscoBbsmMIBGroup=ciscoBbsmMIBGroup, cbbsmEventType=cbbsmEventType, ciscoBbsmMIBObjects=ciscoBbsmMIBObjects, ciscoBbsmMIBConformance=ciscoBbsmMIBConformance, ciscoBbsmEventInfo=ciscoBbsmEventInfo, ciscoBbsmMIBGroups=ciscoBbsmMIBGroups, ciscoBbsmMIBCompliances=ciscoBbsmMIBCompliances, ciscoBbsmEvent=ciscoBbsmEvent, ciscoBbsmMIBCompliance=ciscoBbsmMIBCompliance, PYSNMP_MODULE_ID=ciscoBbsmMIB, ciscoBbsmMIBNotificationGroup=ciscoBbsmMIBNotificationGroup, cbbsmEventDescription=cbbsmEventDescription, cbbsmEventSource=cbbsmEventSource)
