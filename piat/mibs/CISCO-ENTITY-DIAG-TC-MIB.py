#
# PySNMP MIB module CISCO-ENTITY-DIAG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-ENTITY-DIAG-TC-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:32:00 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, ObjectIdentity, MibIdentifier, Unsigned32, iso, Counter64, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Unsigned32", "iso", "Counter64", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEntityDiagTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 584))
ciscoEntityDiagTcMIB.setRevisions(('2009-07-01 00:00', '2006-12-21 00:00',))
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setLastUpdated('200907010000Z')
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setOrganization('Cisco Systems, Inc.')
class CeDiagDiagnosticLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("bypass", 1), ("minimal", 2), ("complete", 3))

class CeDiagDiagnosticMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("bootup", 1), ("onDemand", 2), ("scheduled", 3), ("healthMonitor", 4), ("none", 5))

class CeDiagTestIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagErrorIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagErrorIdentifierOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CeDiagJobIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagPortList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CeDiagTestList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CeDiagJobSuite(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("complete", 2), ("minimal", 3), ("nonDisruptive", 4), ("perPort", 5))

mibBuilder.exportSymbols("CISCO-ENTITY-DIAG-TC-MIB", CeDiagErrorIdentifierOrZero=CeDiagErrorIdentifierOrZero, CeDiagJobIdentifier=CeDiagJobIdentifier, PYSNMP_MODULE_ID=ciscoEntityDiagTcMIB, CeDiagDiagnosticMethod=CeDiagDiagnosticMethod, CeDiagPortList=CeDiagPortList, ciscoEntityDiagTcMIB=ciscoEntityDiagTcMIB, CeDiagJobSuite=CeDiagJobSuite, CeDiagDiagnosticLevel=CeDiagDiagnosticLevel, CeDiagTestIdentifier=CeDiagTestIdentifier, CeDiagErrorIdentifier=CeDiagErrorIdentifier, CeDiagTestList=CeDiagTestList)
