#
# PySNMP MIB module CISCO-ENTITY-REDUNDANCY-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-ENTITY-REDUNDANCY-TC-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:30:06 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, TimeTicks, Bits, NotificationType, Gauge32, Unsigned32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "TimeTicks", "Bits", "NotificationType", "Gauge32", "Unsigned32", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityRedunTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 494))
ciscoEntityRedunTcMIB.setRevisions(('2005-10-01 00:00',))
if mibBuilder.loadTexts: ciscoEntityRedunTcMIB.setLastUpdated('200510010000Z')
if mibBuilder.loadTexts: ciscoEntityRedunTcMIB.setOrganization('Cisco Systems, Inc.')
class CeRedunType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("yCable", 2), ("aps", 3), ("featureCard", 4), ("externalSwitch", 5), ("slotPair", 6), ("cmts", 7))

class CeRedunScope(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("local", 2), ("remoteChassis", 3), ("remoteSystem", 4))

class CeRedunArch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("oneToOne", 2), ("onePlusOne", 3), ("oneToN", 4), ("mToN", 5), ("loadSharing", 6))

class CeRedunSwitchCommand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("noCmdInEffect", 1), ("clear", 2), ("manualSwitchAway", 3), ("forcedSwitchAway", 4), ("lockoutProtection", 5))

class CeRedunMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class CeRedunMbrStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("protectionLockedOut", 0), ("degraded", 1), ("failure", 2), ("standby", 3), ("protectionProvided", 4), ("forcedStandby", 5), ("manualStandby", 6))

class CeRedunStateCategories(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("other", 1), ("disabled", 2), ("inactive", 3), ("failed", 4), ("initializing", 5), ("negotiation", 6), ("activeOther", 7), ("activeImageInitialize", 8), ("activeConfigInitialize", 9), ("activeRunStateInitialize", 10), ("activeFromStandbyTransition", 11), ("activeReconciliation", 12), ("activeWait", 13), ("active", 14), ("standbyOther", 15), ("standbyImageInitialize", 16), ("standbyConfigInitialize", 17), ("standbyRunStateInitialize", 18), ("standbyReconciliation", 19), ("standbyWait", 20), ("standbyColdFinal", 21), ("standbyWarmFinal", 22), ("standbyHotFinal", 23), ("standbySwitchingToActive", 24))

class CeRedunReasonCategories(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("unsupported", 2), ("notKnown", 3), ("userManual", 4), ("userForced", 5), ("userLockout", 6), ("activeMbrFailed", 7), ("activeMbrRemoved", 8), ("activeMbrDisabled", 9), ("revertiveSwitchover", 10), ("remoteRequest", 11))

mibBuilder.exportSymbols("CISCO-ENTITY-REDUNDANCY-TC-MIB", CeRedunStateCategories=CeRedunStateCategories, CeRedunMbrStatus=CeRedunMbrStatus, PYSNMP_MODULE_ID=ciscoEntityRedunTcMIB, CeRedunMode=CeRedunMode, CeRedunSwitchCommand=CeRedunSwitchCommand, ciscoEntityRedunTcMIB=ciscoEntityRedunTcMIB, CeRedunScope=CeRedunScope, CeRedunArch=CeRedunArch, CeRedunType=CeRedunType, CeRedunReasonCategories=CeRedunReasonCategories)
