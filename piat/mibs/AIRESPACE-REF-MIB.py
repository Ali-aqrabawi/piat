#
# PySNMP MIB module AIRESPACE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/AIRESPACE-REF-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:39:33 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, TimeTicks, Integer32, enterprises, Gauge32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, ModuleIdentity, Unsigned32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "TimeTicks", "Integer32", "enterprises", "Gauge32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Unsigned32", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
airespace = ModuleIdentity((1, 3, 6, 1, 4, 1, 14179))
airespace.setRevisions(('2005-12-19 00:00',))
if mibBuilder.loadTexts: airespace.setLastUpdated('200512190000Z')
if mibBuilder.loadTexts: airespace.setOrganization('Airespace, Inc.')
mibBuilder.exportSymbols("AIRESPACE-REF-MIB", airespace=airespace, PYSNMP_MODULE_ID=airespace)
