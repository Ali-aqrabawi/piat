#
# PySNMP MIB module CISCO-LWAPP-WEBAUTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-LWAPP-WEBAUTH-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:31:44 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoURLString, = mibBuilder.importSymbols("CISCO-TC", "CiscoURLString")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, NotificationType, TimeTicks, Gauge32, ModuleIdentity, IpAddress, Bits, Integer32, Counter64, ObjectIdentity, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "IpAddress", "Bits", "Integer32", "Counter64", "ObjectIdentity", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
ciscoLwappWebAuthMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 515))
ciscoLwappWebAuthMIB.setRevisions(('2007-03-04 00:00', '2006-04-05 11:50',))
if mibBuilder.loadTexts: ciscoLwappWebAuthMIB.setLastUpdated('200703040000Z')
if mibBuilder.loadTexts: ciscoLwappWebAuthMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappWebAuthMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 515, 0))
ciscoLwappWebAuthMIBNotifObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 515, 1))
ciscoLwappWebAuthMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 515, 2))
ciscoLwappWebAuthMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 515, 3))
ciscoLwappWebAuthConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1))
ciscoLwappWebAuthExtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2))
ciscoLwappLocalNetUserConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3))
cLWAWebAuthType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("internalDefault", 1), ("internalCustom", 2), ("external", 3))).clone('internalDefault')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWAWebAuthType.setStatus('current')
cLWAManufacturerLogo = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWAManufacturerLogo.setStatus('current')
cLWACustomLogoFileName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWACustomLogoFileName.setStatus('current')
cLWACustomWebTitle = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWACustomWebTitle.setStatus('current')
cLWACustomWebMessage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 5), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWACustomWebMessage.setStatus('current')
cLWACustomWebRedirectURL = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 6), CiscoURLString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWACustomWebRedirectURL.setStatus('current')
cLWAExternalWebAuthURL = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 7), CiscoURLString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWAExternalWebAuthURL.setStatus('current')
cLWAExternalWebServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1), )
if mibBuilder.loadTexts: cLWAExternalWebServerTable.setStatus('current')
cLWAExternalWebServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerIndex"))
if mibBuilder.loadTexts: cLWAExternalWebServerEntry.setStatus('current')
cLWAExternalWebServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: cLWAExternalWebServerIndex.setStatus('current')
cLWAExternalWebServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLWAExternalWebServerAddrType.setStatus('current')
cLWAExternalWebServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLWAExternalWebServerAddr.setStatus('current')
cLWAExternalWebServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLWAExternalWebServerRowStatus.setStatus('current')
cLWALocalNetUserTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1), )
if mibBuilder.loadTexts: cLWALocalNetUserTable.setStatus('current')
cLWALocalNetUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserName"))
if mibBuilder.loadTexts: cLWALocalNetUserEntry.setStatus('current')
cLWALocalNetUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 50)))
if mibBuilder.loadTexts: cLWALocalNetUserName.setStatus('current')
cLWALocalNetUserIsGuest = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWALocalNetUserIsGuest.setStatus('current')
cLWAGuestUserName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 515, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 24))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cLWAGuestUserName.setStatus('current')
cLWAGuestUserRemoved = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 515, 0, 1)).setObjects(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserName"))
if mibBuilder.loadTexts: cLWAGuestUserRemoved.setStatus('current')
ciscoLwappWebAuthMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 1))
ciscoLwappWebAuthMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2))
cLWebAuthMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 1, 1)).setObjects(("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebAuthGroup"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebAuthGroup"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifObjGroup"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLWebAuthMIBCompliance = cLWebAuthMIBCompliance.setStatus('deprecated')
cLWebAuthMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 1, 2)).setObjects(("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebAuthGroup"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebAuthGroup"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifObjGroup"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifGroup"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLWebAuthMIBComplianceRev1 = cLWebAuthMIBComplianceRev1.setStatus('current')
cLWACustomWebAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 1)).setObjects(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAWebAuthType"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAManufacturerLogo"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomLogoFileName"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebTitle"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebMessage"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebRedirectURL"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebAuthURL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLWACustomWebAuthGroup = cLWACustomWebAuthGroup.setStatus('current')
cLWAExternalWebAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 2)).setObjects(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerAddrType"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerAddr"), ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLWAExternalWebAuthGroup = cLWAExternalWebAuthGroup.setStatus('current')
cLWAGuestAccessNotifObjGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 3)).setObjects(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLWAGuestAccessNotifObjGroup = cLWAGuestAccessNotifObjGroup.setStatus('current')
cLWAGuestAccessNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 4)).setObjects(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserRemoved"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLWAGuestAccessNotifGroup = cLWAGuestAccessNotifGroup.setStatus('current')
cLWAGuestUserConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 5)).setObjects(("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserIsGuest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLWAGuestUserConfigGroup = cLWAGuestUserConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-WEBAUTH-MIB", cLWAExternalWebServerIndex=cLWAExternalWebServerIndex, cLWAExternalWebServerAddrType=cLWAExternalWebServerAddrType, cLWAGuestUserRemoved=cLWAGuestUserRemoved, cLWAGuestUserName=cLWAGuestUserName, cLWACustomWebMessage=cLWACustomWebMessage, cLWACustomWebRedirectURL=cLWACustomWebRedirectURL, ciscoLwappWebAuthMIBObjects=ciscoLwappWebAuthMIBObjects, ciscoLwappWebAuthMIB=ciscoLwappWebAuthMIB, PYSNMP_MODULE_ID=ciscoLwappWebAuthMIB, ciscoLwappWebAuthMIBConform=ciscoLwappWebAuthMIBConform, cLWAExternalWebServerEntry=cLWAExternalWebServerEntry, cLWAExternalWebServerTable=cLWAExternalWebServerTable, ciscoLwappLocalNetUserConfig=ciscoLwappLocalNetUserConfig, cLWALocalNetUserIsGuest=cLWALocalNetUserIsGuest, cLWALocalNetUserEntry=cLWALocalNetUserEntry, ciscoLwappWebAuthConfig=ciscoLwappWebAuthConfig, cLWAGuestAccessNotifObjGroup=cLWAGuestAccessNotifObjGroup, cLWAExternalWebAuthGroup=cLWAExternalWebAuthGroup, ciscoLwappWebAuthMIBNotifObjs=ciscoLwappWebAuthMIBNotifObjs, cLWACustomWebAuthGroup=cLWACustomWebAuthGroup, ciscoLwappWebAuthMIBCompliances=ciscoLwappWebAuthMIBCompliances, cLWebAuthMIBCompliance=cLWebAuthMIBCompliance, cLWebAuthMIBComplianceRev1=cLWebAuthMIBComplianceRev1, ciscoLwappWebAuthExtConfig=ciscoLwappWebAuthExtConfig, cLWAExternalWebServerAddr=cLWAExternalWebServerAddr, cLWALocalNetUserName=cLWALocalNetUserName, cLWALocalNetUserTable=cLWALocalNetUserTable, ciscoLwappWebAuthMIBGroups=ciscoLwappWebAuthMIBGroups, cLWACustomLogoFileName=cLWACustomLogoFileName, cLWAExternalWebAuthURL=cLWAExternalWebAuthURL, cLWAWebAuthType=cLWAWebAuthType, cLWACustomWebTitle=cLWACustomWebTitle, ciscoLwappWebAuthMIBNotifs=ciscoLwappWebAuthMIBNotifs, cLWAExternalWebServerRowStatus=cLWAExternalWebServerRowStatus, cLWAManufacturerLogo=cLWAManufacturerLogo, cLWAGuestUserConfigGroup=cLWAGuestUserConfigGroup, cLWAGuestAccessNotifGroup=cLWAGuestAccessNotifGroup)
