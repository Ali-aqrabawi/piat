#
# PySNMP MIB module NORTEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/NORTEL-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:21:39 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Bits, NotificationType, IpAddress, ModuleIdentity, enterprises, MibIdentifier, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Bits", "NotificationType", "IpAddress", "ModuleIdentity", "enterprises", "MibIdentifier", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nortel = ModuleIdentity((1, 3, 6, 1, 4, 1, 562))
if mibBuilder.loadTexts: nortel.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: nortel.setOrganization('Northern Telecom Ltd.')
mibBuilder.exportSymbols("NORTEL-MIB", nortel=nortel, PYSNMP_MODULE_ID=nortel)
