#
# PySNMP MIB module CISCO-UDLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-UDLDP-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:26:18 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, ifName = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifName")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, NotificationType, ObjectIdentity, MibIdentifier, Gauge32, ModuleIdentity, Counter32, IpAddress, Integer32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "NotificationType", "ObjectIdentity", "MibIdentifier", "Gauge32", "ModuleIdentity", "Counter32", "IpAddress", "Integer32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoUdldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 118))
ciscoUdldpMIB.setRevisions(('2009-11-09 09:00', '2007-11-27 00:00', '2003-02-21 00:00', '2002-10-10 00:00', '2000-04-10 00:00', '1998-11-10 00:00',))
if mibBuilder.loadTexts: ciscoUdldpMIB.setLastUpdated('200911090900Z')
if mibBuilder.loadTexts: ciscoUdldpMIB.setOrganization('Cisco Systems, Inc.')
ciscoUdldpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 0))
ciscoUdldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 1))
cudldpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1))
cudldpInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2))
cudldpFastHello = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3))
cudldpGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpGlobalEnable.setStatus('deprecated')
cudldpHelloInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(7, 90))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpHelloInterval.setStatus('current')
cudldpGlobalMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("aggressive", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpGlobalMode.setStatus('current')
cudldpHelloIntervalExt = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 90))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpHelloIntervalExt.setStatus('current')
cudldpFastHelloLinkFailRptNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpFastHelloLinkFailRptNotifEnable.setStatus('current')
cudldpFastHelloStatusChangeNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpFastHelloStatusChangeNotifEnable.setStatus('current')
cudldpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1), )
if mibBuilder.loadTexts: cudldpInterfaceTable.setStatus('current')
cudldpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cudldpInterfaceEntry.setStatus('current')
cudldpInterfaceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpInterfaceEnable.setStatus('deprecated')
cudldpInterfaceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("shutdown", 1), ("indeterminant", 2), ("biDirectional", 3), ("notApplicable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpInterfaceOperStatus.setStatus('current')
cudldpInterfaceAggressiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpInterfaceAggressiveMode.setStatus('deprecated')
cudldpInterfaceAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("aggressive", 3), ("default", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpInterfaceAdminMode.setStatus('current')
cudldpInterfaceOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("aggressive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpInterfaceOperMode.setStatus('current')
cudldpIfFastHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 6), Unsigned32()).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpIfFastHelloInterval.setStatus('current')
cudldpIfOperHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 7), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpIfOperHelloInterval.setStatus('current')
cudldpIfFastHelloOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("operational", 1), ("notOperational", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpIfFastHelloOperStatus.setStatus('current')
cudldpFastHelloErrorReportEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cudldpFastHelloErrorReportEnable.setStatus('current')
cudldpFastHelloMaxPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpFastHelloMaxPorts.setStatus('current')
cudldpFastHelloConfigPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpFastHelloConfigPorts.setStatus('current')
cudldpFastHelloOperationalPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cudldpFastHelloOperationalPorts.setStatus('current')
cudldpFastHelloLinkFailRptNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 118, 0, 1)).setObjects(("IF-MIB", "ifName"))
if mibBuilder.loadTexts: cudldpFastHelloLinkFailRptNotification.setStatus('current')
cudldpFastHelloStatusChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 118, 0, 2)).setObjects(("CISCO-UDLDP-MIB", "cudldpHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpIfFastHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpIfOperHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpIfFastHelloOperStatus"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: cudldpFastHelloStatusChangeNotification.setStatus('current')
ciscoUdldpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 3))
ciscoUdldpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1))
ciscoUdldpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2))
ciscoUdldpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 1)).setObjects(("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBCompliance = ciscoUdldpMIBCompliance.setStatus('deprecated')
ciscoUdldpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 2)).setObjects(("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup"), ("CISCO-UDLDP-MIB", "ciscoUdldpAggreModeOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBComplianceRev1 = ciscoUdldpMIBComplianceRev1.setStatus('deprecated')
ciscoUdldpMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 3)).setObjects(("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBComplianceRev2 = ciscoUdldpMIBComplianceRev2.setStatus('deprecated')
ciscoUdldpMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 4)).setObjects(("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup2"), ("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBComplianceRev3 = ciscoUdldpMIBComplianceRev3.setStatus('deprecated')
ciscoUdldpMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 5)).setObjects(("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup2"), ("CISCO-UDLDP-MIB", "ciscoUdldpMIBGroup3"), ("CISCO-UDLDP-MIB", "ciscoUdldpFastHelloGroup"), ("CISCO-UDLDP-MIB", "ciscoUdldpFastHelloNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBComplianceRev4 = ciscoUdldpMIBComplianceRev4.setStatus('current')
ciscoUdldpMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 1)).setObjects(("CISCO-UDLDP-MIB", "cudldpGlobalEnable"), ("CISCO-UDLDP-MIB", "cudldpInterfaceEnable"), ("CISCO-UDLDP-MIB", "cudldpInterfaceOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBGroup = ciscoUdldpMIBGroup.setStatus('deprecated')
ciscoUdldpAggreModeOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 2)).setObjects(("CISCO-UDLDP-MIB", "cudldpInterfaceAggressiveMode"), ("CISCO-UDLDP-MIB", "cudldpHelloInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpAggreModeOptionalGroup = ciscoUdldpAggreModeOptionalGroup.setStatus('deprecated')
ciscoUdldpMIBGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 3)).setObjects(("CISCO-UDLDP-MIB", "cudldpGlobalMode"), ("CISCO-UDLDP-MIB", "cudldpInterfaceAdminMode"), ("CISCO-UDLDP-MIB", "cudldpInterfaceOperMode"), ("CISCO-UDLDP-MIB", "cudldpHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpInterfaceOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBGroup2 = ciscoUdldpMIBGroup2.setStatus('current')
ciscoUdldpMIBGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 4)).setObjects(("CISCO-UDLDP-MIB", "cudldpHelloIntervalExt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpMIBGroup3 = ciscoUdldpMIBGroup3.setStatus('current')
ciscoUdldpFastHelloGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 5)).setObjects(("CISCO-UDLDP-MIB", "cudldpIfFastHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpIfOperHelloInterval"), ("CISCO-UDLDP-MIB", "cudldpIfFastHelloOperStatus"), ("CISCO-UDLDP-MIB", "cudldpFastHelloErrorReportEnable"), ("CISCO-UDLDP-MIB", "cudldpFastHelloLinkFailRptNotifEnable"), ("CISCO-UDLDP-MIB", "cudldpFastHelloStatusChangeNotifEnable"), ("CISCO-UDLDP-MIB", "cudldpFastHelloMaxPorts"), ("CISCO-UDLDP-MIB", "cudldpFastHelloConfigPorts"), ("CISCO-UDLDP-MIB", "cudldpFastHelloOperationalPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpFastHelloGroup = ciscoUdldpFastHelloGroup.setStatus('current')
ciscoUdldpFastHelloNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 6)).setObjects(("CISCO-UDLDP-MIB", "cudldpFastHelloLinkFailRptNotification"), ("CISCO-UDLDP-MIB", "cudldpFastHelloStatusChangeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpFastHelloNotificationGroup = ciscoUdldpFastHelloNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-UDLDP-MIB", cudldpInterfaceOperMode=cudldpInterfaceOperMode, cudldpFastHelloStatusChangeNotification=cudldpFastHelloStatusChangeNotification, PYSNMP_MODULE_ID=ciscoUdldpMIB, ciscoUdldpMIBComplianceRev1=ciscoUdldpMIBComplianceRev1, ciscoUdldpMIBConformance=ciscoUdldpMIBConformance, cudldpIfFastHelloOperStatus=cudldpIfFastHelloOperStatus, cudldpInterfaceOperStatus=cudldpInterfaceOperStatus, cudldpGlobalMode=cudldpGlobalMode, cudldpInterfaceTable=cudldpInterfaceTable, cudldpFastHelloErrorReportEnable=cudldpFastHelloErrorReportEnable, ciscoUdldpMIBComplianceRev3=ciscoUdldpMIBComplianceRev3, ciscoUdldpAggreModeOptionalGroup=ciscoUdldpAggreModeOptionalGroup, ciscoUdldpMIBNotifs=ciscoUdldpMIBNotifs, ciscoUdldpMIBGroup2=ciscoUdldpMIBGroup2, cudldpInterface=cudldpInterface, ciscoUdldpMIBGroup3=ciscoUdldpMIBGroup3, ciscoUdldpMIBObjects=ciscoUdldpMIBObjects, cudldpHelloInterval=cudldpHelloInterval, cudldpInterfaceEnable=cudldpInterfaceEnable, cudldpGlobal=cudldpGlobal, ciscoUdldpMIBGroup=ciscoUdldpMIBGroup, ciscoUdldpMIB=ciscoUdldpMIB, cudldpFastHelloStatusChangeNotifEnable=cudldpFastHelloStatusChangeNotifEnable, cudldpInterfaceAggressiveMode=cudldpInterfaceAggressiveMode, cudldpFastHelloConfigPorts=cudldpFastHelloConfigPorts, ciscoUdldpMIBComplianceRev2=ciscoUdldpMIBComplianceRev2, cudldpFastHelloLinkFailRptNotifEnable=cudldpFastHelloLinkFailRptNotifEnable, ciscoUdldpMIBComplianceRev4=ciscoUdldpMIBComplianceRev4, cudldpInterfaceAdminMode=cudldpInterfaceAdminMode, cudldpFastHelloMaxPorts=cudldpFastHelloMaxPorts, ciscoUdldpMIBGroups=ciscoUdldpMIBGroups, cudldpHelloIntervalExt=cudldpHelloIntervalExt, cudldpIfOperHelloInterval=cudldpIfOperHelloInterval, ciscoUdldpMIBCompliance=ciscoUdldpMIBCompliance, ciscoUdldpFastHelloNotificationGroup=ciscoUdldpFastHelloNotificationGroup, cudldpFastHello=cudldpFastHello, cudldpIfFastHelloInterval=cudldpIfFastHelloInterval, cudldpGlobalEnable=cudldpGlobalEnable, cudldpInterfaceEntry=cudldpInterfaceEntry, ciscoUdldpMIBCompliances=ciscoUdldpMIBCompliances, cudldpFastHelloLinkFailRptNotification=cudldpFastHelloLinkFailRptNotification, ciscoUdldpFastHelloGroup=ciscoUdldpFastHelloGroup, cudldpFastHelloOperationalPorts=cudldpFastHelloOperationalPorts)