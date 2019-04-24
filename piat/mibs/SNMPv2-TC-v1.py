#
# PySNMP MIB module SNMPv2-TC-v1 (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/SNMPv2-TC-v1
# Produced by pysmi-0.3.4 at Sun Apr 21 23:36:53 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, Bits, Counter64, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Integer32, MibIdentifier, IpAddress, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Bits", "Counter64", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Integer32", "MibIdentifier", "IpAddress", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PhysAddress(OctetString):
    pass

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class TestAndIncr(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AutonomousType(ObjectIdentifier):
    pass

class InstancePointer(ObjectIdentifier):
    pass

class VariablePointer(ObjectIdentifier):
    pass

class RowPointer(ObjectIdentifier):
    pass

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class TimeStamp(TimeTicks):
    pass

class TimeInterval(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(11, 11)
    fixedLength = 11

class StorageType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("volatile", 2), ("nonVolatile", 3), ("permanent", 4), ("readOnly", 5))

class TDomain(ObjectIdentifier):
    pass

class TAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

mibBuilder.exportSymbols("SNMPv2-TC-v1", PhysAddress=PhysAddress, DateAndTime=DateAndTime, StorageType=StorageType, TDomain=TDomain, RowPointer=RowPointer, DisplayString=DisplayString, TruthValue=TruthValue, TestAndIncr=TestAndIncr, TimeInterval=TimeInterval, AutonomousType=AutonomousType, RowStatus=RowStatus, TimeStamp=TimeStamp, VariablePointer=VariablePointer, TAddress=TAddress, MacAddress=MacAddress, InstancePointer=InstancePointer)
