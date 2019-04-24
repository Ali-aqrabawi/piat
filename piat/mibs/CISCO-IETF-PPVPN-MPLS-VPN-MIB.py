#
# PySNMP MIB module CISCO-IETF-PPVPN-MPLS-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-IETF-PPVPN-MPLS-VPN-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:35:38 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsVpnVrfPerfCurrNumRoutes, mplsVpnVrfConfHighRouteThreshold = mibBuilder.importSymbols("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes", "mplsVpnVrfConfHighRouteThreshold")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Counter32, NotificationType, iso, ModuleIdentity, Unsigned32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Counter32", "NotificationType", "iso", "ModuleIdentity", "Unsigned32", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMplsVpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 999))
ciscoMplsVpnMIB.setRevisions(('2003-04-17 12:00',))
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setLastUpdated('200304171200Z')
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setOrganization('Cisco Systems, Inc.')
cMplsVpnNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 0))
cMplsVpnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 1))
cMplsVpnConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2))
cMplsNumVrfRouteMaxThreshCleared = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 1)).setObjects(("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes"), ("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold"))
if mibBuilder.loadTexts: cMplsNumVrfRouteMaxThreshCleared.setStatus('current')
cMplsVpnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1))
cMplsVpnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2))
cMplsVpnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1)).setObjects(("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsVpnNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMplsVpnCompliance = cMplsVpnCompliance.setStatus('current')
cMplsVpnNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2, 1)).setObjects(("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsNumVrfRouteMaxThreshCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMplsVpnNotificationGroup = cMplsVpnNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PPVPN-MPLS-VPN-MIB", cMplsVpnCompliance=cMplsVpnCompliance, cMplsVpnObjects=cMplsVpnObjects, cMplsVpnNotifs=cMplsVpnNotifs, cMplsNumVrfRouteMaxThreshCleared=cMplsNumVrfRouteMaxThreshCleared, cMplsVpnNotificationGroup=cMplsVpnNotificationGroup, cMplsVpnGroups=cMplsVpnGroups, PYSNMP_MODULE_ID=ciscoMplsVpnMIB, cMplsVpnConform=cMplsVpnConform, ciscoMplsVpnMIB=ciscoMplsVpnMIB, cMplsVpnCompliances=cMplsVpnCompliances)
