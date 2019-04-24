#
# PySNMP MIB module CISCO-H323-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-H323-TC-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:38:33 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, Integer32, iso, ObjectIdentity, Bits, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, ModuleIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Integer32", "iso", "ObjectIdentity", "Bits", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "ModuleIdentity", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoH323TCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 41))
ciscoH323TCMIB.setRevisions(('1998-10-09 12:00', '2000-03-10 00:00',))
if mibBuilder.loadTexts: ciscoH323TCMIB.setLastUpdated('200003100000Z')
if mibBuilder.loadTexts: ciscoH323TCMIB.setOrganization('Cisco Systems, Inc')
class CgkIA5String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkE164String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkTAddressTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4))

class CgkNAddressTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4))

class CgkNAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkGlobalIdentifier(TextualConvention, OctetString):
    reference = 'ITU-T H225.0, Version 2 section 7.6'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class CgkAliasTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 0), ("e164", 1), ("h323Id", 2), ("urlId", 3), ("transportId", 4), ("emailId", 5), ("partyNumber", 6))

class CgkAliasAddress(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    status = 'current'
    displayHint = '512a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 512)

class CgkEndpointID(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkGatekeeperID(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

mibBuilder.exportSymbols("CISCO-H323-TC-MIB", ciscoH323TCMIB=ciscoH323TCMIB, PYSNMP_MODULE_ID=ciscoH323TCMIB, CgkGlobalIdentifier=CgkGlobalIdentifier, CgkIA5String=CgkIA5String, CgkEndpointID=CgkEndpointID, CgkTAddressTag=CgkTAddressTag, CgkGatekeeperID=CgkGatekeeperID, CgkNAddress=CgkNAddress, CgkAliasAddress=CgkAliasAddress, CgkNAddressTag=CgkNAddressTag, CgkE164String=CgkE164String, CgkAliasTag=CgkAliasTag)
