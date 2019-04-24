#
# PySNMP MIB module APPN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/ietf/APPN-TRAP-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:46:22 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
dlurDlusSessnStatus, = mibBuilder.importSymbols("APPN-DLUR-MIB", "dlurDlusSessnStatus")
appnLocalTgCpCpSession, appnIsInP2SNonFmdBytes, appnIsInSessUpTime, appnObjects, appnIsInP2SFmdPius, appnGroups, appnLocalTgOperational, appnIsInS2PFmdPius, appnMIB, appnIsInP2SNonFmdPius, appnCompliances, appnIsInS2PNonFmdBytes, appnIsInS2PNonFmdPius, appnIsInP2SFmdBytes, appnIsInS2PFmdBytes, appnLsOperState, appnPortOperState = mibBuilder.importSymbols("APPN-MIB", "appnLocalTgCpCpSession", "appnIsInP2SNonFmdBytes", "appnIsInSessUpTime", "appnObjects", "appnIsInP2SFmdPius", "appnGroups", "appnLocalTgOperational", "appnIsInS2PFmdPius", "appnMIB", "appnIsInP2SNonFmdPius", "appnCompliances", "appnIsInS2PNonFmdBytes", "appnIsInS2PNonFmdPius", "appnIsInP2SFmdBytes", "appnIsInS2PFmdBytes", "appnLsOperState", "appnPortOperState")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, MibIdentifier, NotificationType, Gauge32, ModuleIdentity, Bits, TimeTicks, Counter32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "ModuleIdentity", "Bits", "TimeTicks", "Counter32", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
appnTrapMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 4, 0))
if mibBuilder.loadTexts: appnTrapMIB.setLastUpdated('9808310000Z')
if mibBuilder.loadTexts: appnTrapMIB.setOrganization('IETF SNA NAU MIB WG / AIW APPN MIBs SIG')
appnIsrAccountingDataTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 1)).setObjects(("APPN-MIB", "appnIsInP2SFmdPius"), ("APPN-MIB", "appnIsInS2PFmdPius"), ("APPN-MIB", "appnIsInP2SNonFmdPius"), ("APPN-MIB", "appnIsInS2PNonFmdPius"), ("APPN-MIB", "appnIsInP2SFmdBytes"), ("APPN-MIB", "appnIsInS2PFmdBytes"), ("APPN-MIB", "appnIsInP2SNonFmdBytes"), ("APPN-MIB", "appnIsInS2PNonFmdBytes"), ("APPN-MIB", "appnIsInSessUpTime"))
if mibBuilder.loadTexts: appnIsrAccountingDataTrap.setStatus('current')
appnLocalTgOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 2)).setObjects(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-MIB", "appnLocalTgOperational"))
if mibBuilder.loadTexts: appnLocalTgOperStateChangeTrap.setStatus('current')
appnLocalTgCpCpChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 3)).setObjects(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-MIB", "appnLocalTgCpCpSession"))
if mibBuilder.loadTexts: appnLocalTgCpCpChangeTrap.setStatus('current')
appnPortOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 4)).setObjects(("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-MIB", "appnPortOperState"))
if mibBuilder.loadTexts: appnPortOperStateChangeTrap.setStatus('current')
appnLsOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 5)).setObjects(("APPN-TRAP-MIB", "appnLsTableChanges"), ("APPN-MIB", "appnLsOperState"))
if mibBuilder.loadTexts: appnLsOperStateChangeTrap.setStatus('current')
dlurDlusStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 6)).setObjects(("APPN-TRAP-MIB", "dlurDlusTableChanges"), ("APPN-DLUR-MIB", "dlurDlusSessnStatus"))
if mibBuilder.loadTexts: dlurDlusStateChangeTrap.setStatus('current')
appnTrapObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 4, 1, 7))
appnTrapControl = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 1), Bits().clone(namedValues=NamedValues(("appnLocalTgOperStateChangeTrap", 0), ("appnLocalTgCpCpChangeTrap", 1), ("appnPortOperStateChangeTrap", 2), ("appnLsOperStateChangeTrap", 3), ("dlurDlusStateChangeTrap", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appnTrapControl.setStatus('current')
appnLocalTgTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnLocalTgTableChanges.setStatus('current')
appnPortTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnPortTableChanges.setStatus('current')
appnLsTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnLsTableChanges.setStatus('current')
dlurDlusTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlurDlusTableChanges.setStatus('current')
appnTrapMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 4, 3, 1, 2)).setObjects(("APPN-TRAP-MIB", "appnTrapMibIsrNotifGroup"), ("APPN-TRAP-MIB", "appnTrapMibTopoConfGroup"), ("APPN-TRAP-MIB", "appnTrapMibTopoNotifGroup"), ("APPN-TRAP-MIB", "appnTrapMibDlurConfGroup"), ("APPN-TRAP-MIB", "appnTrapMibDlurNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibCompliance = appnTrapMibCompliance.setStatus('current')
appnTrapMibIsrNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 21)).setObjects(("APPN-TRAP-MIB", "appnIsrAccountingDataTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibIsrNotifGroup = appnTrapMibIsrNotifGroup.setStatus('current')
appnTrapMibTopoConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 22)).setObjects(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-TRAP-MIB", "appnLsTableChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibTopoConfGroup = appnTrapMibTopoConfGroup.setStatus('current')
appnTrapMibTopoNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 23)).setObjects(("APPN-TRAP-MIB", "appnLocalTgOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLocalTgCpCpChangeTrap"), ("APPN-TRAP-MIB", "appnPortOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLsOperStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibTopoNotifGroup = appnTrapMibTopoNotifGroup.setStatus('current')
appnTrapMibDlurConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 24)).setObjects(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "dlurDlusTableChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibDlurConfGroup = appnTrapMibDlurConfGroup.setStatus('current')
appnTrapMibDlurNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 25)).setObjects(("APPN-TRAP-MIB", "dlurDlusStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibDlurNotifGroup = appnTrapMibDlurNotifGroup.setStatus('current')
mibBuilder.exportSymbols("APPN-TRAP-MIB", appnLsOperStateChangeTrap=appnLsOperStateChangeTrap, appnPortTableChanges=appnPortTableChanges, appnTrapMibTopoNotifGroup=appnTrapMibTopoNotifGroup, dlurDlusStateChangeTrap=dlurDlusStateChangeTrap, dlurDlusTableChanges=dlurDlusTableChanges, appnTrapControl=appnTrapControl, appnLsTableChanges=appnLsTableChanges, appnLocalTgCpCpChangeTrap=appnLocalTgCpCpChangeTrap, appnTrapMibDlurNotifGroup=appnTrapMibDlurNotifGroup, appnTrapMibCompliance=appnTrapMibCompliance, appnTrapMIB=appnTrapMIB, PYSNMP_MODULE_ID=appnTrapMIB, appnLocalTgTableChanges=appnLocalTgTableChanges, appnTrapMibTopoConfGroup=appnTrapMibTopoConfGroup, appnTrapMibDlurConfGroup=appnTrapMibDlurConfGroup, appnTrapMibIsrNotifGroup=appnTrapMibIsrNotifGroup, appnPortOperStateChangeTrap=appnPortOperStateChangeTrap, appnTrapObjects=appnTrapObjects, appnLocalTgOperStateChangeTrap=appnLocalTgOperStateChangeTrap, appnIsrAccountingDataTrap=appnIsrAccountingDataTrap)
