#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/ietf/PerfHist-TC-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:44:11 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Gauge32, Integer32, ObjectIdentity, Bits, ModuleIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, NotificationType, Counter32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Gauge32", "Integer32", "ObjectIdentity", "Bits", "ModuleIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "NotificationType", "Counter32", "IpAddress", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
perfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 58))
perfHistTCMIB.setRevisions(('2003-08-13 00:00', '1998-11-07 11:00',))
if mibBuilder.loadTexts: perfHistTCMIB.setLastUpdated('200308130000Z')
if mibBuilder.loadTexts: perfHistTCMIB.setOrganization('IETF AToM MIB WG')
class PerfCurrentCount(TextualConvention, Gauge32):
    status = 'current'

class PerfIntervalCount(TextualConvention, Gauge32):
    status = 'current'

class PerfTotalCount(TextualConvention, Gauge32):
    status = 'current'

mibBuilder.exportSymbols("PerfHist-TC-MIB", PYSNMP_MODULE_ID=perfHistTCMIB, PerfIntervalCount=PerfIntervalCount, perfHistTCMIB=perfHistTCMIB, PerfTotalCount=PerfTotalCount, PerfCurrentCount=PerfCurrentCount)
