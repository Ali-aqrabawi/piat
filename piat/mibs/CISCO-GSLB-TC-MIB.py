#
# PySNMP MIB module CISCO-GSLB-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-GSLB-TC-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:31:41 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, IpAddress, MibIdentifier, NotificationType, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, Counter32, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "Counter32", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGslbTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 583))
ciscoGslbTcMIB.setRevisions(('2007-02-23 00:00', '2006-09-26 00:00',))
if mibBuilder.loadTexts: ciscoGslbTcMIB.setLastUpdated('200702230000Z')
if mibBuilder.loadTexts: ciscoGslbTcMIB.setOrganization('Cisco Systems, Inc.')
class CiscoGslbNodeServices(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("primary", 1), ("standby", 2), ("secondary", 3))

class CiscoGslbPeerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inactive", 1), ("offline", 2), ("online", 3))

class CiscoGslbAnswerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("vip", 2), ("ns", 3), ("cra", 4))

class CiscoGslbKeepaliveTargetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("vip", 2), ("ns", 3), ("cra", 4), ("shared", 5))

class CiscoGslbKeepaliveMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("other", 1), ("none", 2), ("icmp", 3), ("tcp", 4), ("httphead", 5), ("kalap", 6), ("ns", 7), ("cra", 8), ("scriptedKal", 9))

class CiscoGslbKeepaliveConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("suspend", 2))

class CiscoGslbKeepaliveRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("standard", 2), ("fast", 3))

class CiscoGslbTerminationMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("reset", 2), ("graceful", 3))

class CiscoGslbKeepaliveStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("offline", 2), ("online", 3), ("suspended", 4), ("init", 5))

class CiscoGslbAnswerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("offline", 2), ("online", 3), ("suspended", 4), ("init", 5))

class CiscoGslbAnswerAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("suspended", 1), ("active", 2))

class CiscoGslbKalapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("kalapByVip", 2), ("kalapByTag", 3))

class CiscoGslbBalanceMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("orderedList", 2), ("roundRobin", 3), ("weightedRR", 4), ("leastLoaded", 5), ("hashed", 6), ("boomerang", 7))

mibBuilder.exportSymbols("CISCO-GSLB-TC-MIB", CiscoGslbKeepaliveConfigState=CiscoGslbKeepaliveConfigState, CiscoGslbKeepaliveStatus=CiscoGslbKeepaliveStatus, CiscoGslbKeepaliveMethod=CiscoGslbKeepaliveMethod, CiscoGslbKeepaliveRate=CiscoGslbKeepaliveRate, CiscoGslbTerminationMethod=CiscoGslbTerminationMethod, CiscoGslbAnswerStatus=CiscoGslbAnswerStatus, ciscoGslbTcMIB=ciscoGslbTcMIB, PYSNMP_MODULE_ID=ciscoGslbTcMIB, CiscoGslbBalanceMethod=CiscoGslbBalanceMethod, CiscoGslbKalapType=CiscoGslbKalapType, CiscoGslbAnswerType=CiscoGslbAnswerType, CiscoGslbNodeServices=CiscoGslbNodeServices, CiscoGslbAnswerAdminState=CiscoGslbAnswerAdminState, CiscoGslbKeepaliveTargetType=CiscoGslbKeepaliveTargetType, CiscoGslbPeerStatus=CiscoGslbPeerStatus)
