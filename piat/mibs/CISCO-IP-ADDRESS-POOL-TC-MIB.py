#
# PySNMP MIB module CISCO-IP-ADDRESS-POOL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-IP-ADDRESS-POOL-TC-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:25:21 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Unsigned32, MibIdentifier, Gauge32, Counter32, NotificationType, Integer32, Counter64, Bits, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Unsigned32", "MibIdentifier", "Gauge32", "Counter32", "NotificationType", "Integer32", "Counter64", "Bits", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIpAddressPoolTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 742))
ciscoIpAddressPoolTcMIB.setRevisions(('2010-02-02 00:00',))
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setLastUpdated('201005030000Z')
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setOrganization('Cisco Systems, Inc.')
class IpAddrPoolInstanceIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IpAddrPoolInstanceIdentifierOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class IpAddressPoolName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class IpAddressPoolNameOrNull(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IpAddressPoolGroupName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class IpAddressPoolGroupNameOrNull(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IpAddressPoolThresholdUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("absolute", 2), ("percent", 3))

mibBuilder.exportSymbols("CISCO-IP-ADDRESS-POOL-TC-MIB", IpAddressPoolGroupNameOrNull=IpAddressPoolGroupNameOrNull, IpAddressPoolThresholdUnits=IpAddressPoolThresholdUnits, IpAddressPoolNameOrNull=IpAddressPoolNameOrNull, IpAddrPoolInstanceIdentifierOrZero=IpAddrPoolInstanceIdentifierOrZero, PYSNMP_MODULE_ID=ciscoIpAddressPoolTcMIB, IpAddressPoolName=IpAddressPoolName, IpAddrPoolInstanceIdentifier=IpAddrPoolInstanceIdentifier, IpAddressPoolGroupName=IpAddressPoolGroupName, ciscoIpAddressPoolTcMIB=ciscoIpAddressPoolTcMIB)
