#
# PySNMP MIB module CISCO-SLB-DFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-SLB-DFP-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:27:08 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Unsigned32, Bits, TimeTicks, Integer32, MibIdentifier, ModuleIdentity, iso, ObjectIdentity, Counter32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Unsigned32", "Bits", "TimeTicks", "Integer32", "MibIdentifier", "ModuleIdentity", "iso", "ObjectIdentity", "Counter32", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSlbDfpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 689))
ciscoSlbDfpMIB.setRevisions(('2009-01-29 00:00',))
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setLastUpdated('200901290000Z')
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setOrganization('Cisco Systems, Inc.')
ciscoSlbDfpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 0))
ciscoSlbDfpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 1))
ciscoSlbDfpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2))
cslbcDfpCongestionThresholdType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("reject", 1), ("abort", 2), ("redirect", 3), ("drop", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cslbcDfpCongestionThresholdType.setStatus('current')
cslbcProcessorDfpValTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4), )
if mibBuilder.loadTexts: cslbcProcessorDfpValTable.setStatus('current')
cslbcProcessorDfpValEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1), ).setIndexNames((0, "CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValPhysicalIndex"))
if mibBuilder.loadTexts: cslbcProcessorDfpValEntry.setStatus('current')
cslbcProcessorDfpValPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 1), EntPhysicalIndexOrZero())
if mibBuilder.loadTexts: cslbcProcessorDfpValPhysicalIndex.setStatus('current')
cslbcProcessorDfpValDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslbcProcessorDfpValDescription.setStatus('current')
class CslbcDfpValue(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

cslbcDfpCongestionOnsetThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 1), CslbcDfpValue()).setUnits('DFP weight').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslbcDfpCongestionOnsetThreshold.setStatus('current')
cslbcDfpCongestionAbateThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 2), CslbcDfpValue()).setUnits('DFP weight').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslbcDfpCongestionAbateThreshold.setStatus('current')
cslbcProcessorDfpValDfpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 3), CslbcDfpValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslbcProcessorDfpValDfpValue.setStatus('current')
cslbcSlbDfpCongestionOnset = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 689, 0, 1)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionOnsetThreshold"))
if mibBuilder.loadTexts: cslbcSlbDfpCongestionOnset.setStatus('current')
cslbcSlbDfpCongestionAbate = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 689, 0, 2)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionAbateThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"))
if mibBuilder.loadTexts: cslbcSlbDfpCongestionAbate.setStatus('current')
ciscoSlbDfpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 1))
ciscoSlbDfpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2))
ciscoSlbDfpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 1, 1)).setObjects(("CISCO-SLB-DFP-MIB", "ciscoSlbDfpInstanceGroup"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpScalarsGroup"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbDfpMIBCompliance = ciscoSlbDfpMIBCompliance.setStatus('current')
ciscoSlbDfpInstanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 1)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbDfpInstanceGroup = ciscoSlbDfpInstanceGroup.setStatus('current')
cslbcSlbDfpScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 2)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionOnsetThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionAbateThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cslbcSlbDfpScalarsGroup = cslbcSlbDfpScalarsGroup.setStatus('current')
cslbcSlbDfpCongestionGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 3)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionOnset"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionAbate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cslbcSlbDfpCongestionGroup = cslbcSlbDfpCongestionGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SLB-DFP-MIB", ciscoSlbDfpMIBCompliances=ciscoSlbDfpMIBCompliances, cslbcDfpCongestionAbateThreshold=cslbcDfpCongestionAbateThreshold, cslbcSlbDfpCongestionAbate=cslbcSlbDfpCongestionAbate, ciscoSlbDfpInstanceGroup=ciscoSlbDfpInstanceGroup, cslbcSlbDfpCongestionGroup=cslbcSlbDfpCongestionGroup, cslbcProcessorDfpValDescription=cslbcProcessorDfpValDescription, CslbcDfpValue=CslbcDfpValue, cslbcProcessorDfpValEntry=cslbcProcessorDfpValEntry, ciscoSlbDfpMIBGroups=ciscoSlbDfpMIBGroups, cslbcProcessorDfpValPhysicalIndex=cslbcProcessorDfpValPhysicalIndex, ciscoSlbDfpMIBConform=ciscoSlbDfpMIBConform, cslbcDfpCongestionOnsetThreshold=cslbcDfpCongestionOnsetThreshold, ciscoSlbDfpMIBNotifs=ciscoSlbDfpMIBNotifs, cslbcProcessorDfpValDfpValue=cslbcProcessorDfpValDfpValue, ciscoSlbDfpMIBCompliance=ciscoSlbDfpMIBCompliance, ciscoSlbDfpMIB=ciscoSlbDfpMIB, ciscoSlbDfpMIBObjects=ciscoSlbDfpMIBObjects, cslbcProcessorDfpValTable=cslbcProcessorDfpValTable, cslbcSlbDfpCongestionOnset=cslbcSlbDfpCongestionOnset, cslbcDfpCongestionThresholdType=cslbcDfpCongestionThresholdType, PYSNMP_MODULE_ID=ciscoSlbDfpMIB, cslbcSlbDfpScalarsGroup=cslbcSlbDfpScalarsGroup)
