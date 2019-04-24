#
# PySNMP MIB module ADSL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/ietf/ADSL-TC-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:44:11 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Gauge32, Integer32, ObjectIdentity, Bits, ModuleIdentity, Counter64, Unsigned32, transmission, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Gauge32", "Integer32", "ObjectIdentity", "Bits", "ModuleIdentity", "Counter64", "Unsigned32", "transmission", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adsltcmib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 94, 2))
adsltcmib.setRevisions(('1999-08-19 00:00',))
if mibBuilder.loadTexts: adsltcmib.setLastUpdated('9908190000Z')
if mibBuilder.loadTexts: adsltcmib.setOrganization('IETF ADSL MIB Working Group')
class AdslLineCodingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("dmt", 2), ("cap", 3), ("qam", 4))

class AdslPerfCurrDayCount(TextualConvention, Gauge32):
    status = 'current'

class AdslPerfPrevDayCount(TextualConvention, Gauge32):
    status = 'current'

class AdslPerfTimeElapsed(TextualConvention, Gauge32):
    status = 'current'

mibBuilder.exportSymbols("ADSL-TC-MIB", AdslPerfCurrDayCount=AdslPerfCurrDayCount, PYSNMP_MODULE_ID=adsltcmib, AdslPerfTimeElapsed=AdslPerfTimeElapsed, AdslPerfPrevDayCount=AdslPerfPrevDayCount, AdslLineCodingType=AdslLineCodingType, adsltcmib=adsltcmib)
