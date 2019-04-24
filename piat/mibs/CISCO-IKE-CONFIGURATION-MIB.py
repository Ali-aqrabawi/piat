#
# PySNMP MIB module CISCO-IKE-CONFIGURATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-IKE-CONFIGURATION-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:26:53 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
CIPsecEncryptAlgorithm, CIPsecIkePRFAlgorithm, CIPsecPhase1PeerIdentityType, CIPsecIkeHashAlgorithm, CIKELifetime, CIPsecIkeAuthMethod, CIKELifesize, CIPsecControlProtocol, CIKEIsakmpDoi, CIPsecDiffHellmanGrp = mibBuilder.importSymbols("CISCO-IPSEC-TC", "CIPsecEncryptAlgorithm", "CIPsecIkePRFAlgorithm", "CIPsecPhase1PeerIdentityType", "CIPsecIkeHashAlgorithm", "CIKELifetime", "CIPsecIkeAuthMethod", "CIKELifesize", "CIPsecControlProtocol", "CIKEIsakmpDoi", "CIPsecDiffHellmanGrp")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressPrefixLength, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressPrefixLength", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, TimeTicks, Counter32, iso, IpAddress, MibIdentifier, ModuleIdentity, Unsigned32, Bits, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "TimeTicks", "Counter32", "iso", "IpAddress", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
ciscoIkeConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 423))
ciscoIkeConfigMIB.setRevisions(('2004-09-16 00:00',))
if mibBuilder.loadTexts: ciscoIkeConfigMIB.setLastUpdated('200409160000Z')
if mibBuilder.loadTexts: ciscoIkeConfigMIB.setOrganization('Cisco Systems')
cicIkeConfigMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 0))
cicIkeConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1))
cicIkeConfigMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 2))
cicIkeCfgOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 1))
cicIkeCfgIdentities = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2))
cicIkeCfgFailureRecovery = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3))
cicIkeCfgPeerAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4))
cicIkeCfgPskAuthConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1))
cicIkeCfgNonceAuthConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 2))
cicIkeCfgPkiAuthConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 3))
cicIkeCfgPolicies = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5))
cicIkeCfgServiceControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 6))
cicIkeCfgCallAdmssionnCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 6, 1))
cicIkeCfgQoSControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 6, 2))
cicIkeConfigMibNotifCntl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7))
class CicIkeConfigPskIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class CicIkeConfigInitiatorIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

cicIkeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicIkeEnabled.setStatus('current')
cicIkeAggressModeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicIkeAggressModeEnabled.setStatus('current')
cicIkeCfgIdentityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 1), )
if mibBuilder.loadTexts: cicIkeCfgIdentityTable.setStatus('current')
cicIkeCfgIdentityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentityDoi"))
if mibBuilder.loadTexts: cicIkeCfgIdentityEntry.setStatus('current')
cicIkeCfgIdentityDoi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 1, 1, 1), CIKEIsakmpDoi())
if mibBuilder.loadTexts: cicIkeCfgIdentityDoi.setStatus('current')
cicIkeCfgIdentityType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 1, 1, 2), CIPsecPhase1PeerIdentityType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicIkeCfgIdentityType.setStatus('current')
cicIkeCfgInitiatorNextAvailTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 2), )
if mibBuilder.loadTexts: cicIkeCfgInitiatorNextAvailTable.setStatus('current')
cicIkeCfgInitiatorNextAvailEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 2, 1), )
cicIkeCfgIdentityEntry.registerAugmentions(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorNextAvailEntry"))
cicIkeCfgInitiatorNextAvailEntry.setIndexNames(*cicIkeCfgIdentityEntry.getIndexNames())
if mibBuilder.loadTexts: cicIkeCfgInitiatorNextAvailEntry.setStatus('current')
cicIkeCfgInitiatorNextAvailIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 2, 1, 1), CicIkeConfigInitiatorIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicIkeCfgInitiatorNextAvailIndex.setStatus('current')
cicIkeCfgInitiatorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3), )
if mibBuilder.loadTexts: cicIkeCfgInitiatorTable.setStatus('current')
cicIkeCfgInitiatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentityDoi"), (0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorIndex"))
if mibBuilder.loadTexts: cicIkeCfgInitiatorEntry.setStatus('current')
cicIkeCfgInitiatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1, 1), CicIkeConfigInitiatorIndex())
if mibBuilder.loadTexts: cicIkeCfgInitiatorIndex.setStatus('current')
cicIkeCfgInitiatorPAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1, 2), CIPsecPhase1PeerIdentityType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgInitiatorPAddrType.setStatus('current')
cicIkeCfgInitiatorPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgInitiatorPAddr.setStatus('current')
cicIkeCfgInitiatorVer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1, 4), CIPsecControlProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgInitiatorVer.setStatus('current')
cicIkeCfgInitiatorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 2, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgInitiatorStatus.setStatus('current')
cicIkeCfgFailureRecovConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1), )
if mibBuilder.loadTexts: cicIkeCfgFailureRecovConfigTable.setStatus('current')
cicIkeCfgFailureRecovConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1), )
cicIkeCfgIdentityEntry.registerAugmentions(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgFailureRecovConfigEntry"))
cicIkeCfgFailureRecovConfigEntry.setIndexNames(*cicIkeCfgIdentityEntry.getIndexNames())
if mibBuilder.loadTexts: cicIkeCfgFailureRecovConfigEntry.setStatus('current')
cicIkeKeepAliveEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicIkeKeepAliveEnabled.setStatus('current')
cicIkeKeepAliveType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("periodic", 2), ("ondemand", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicIkeKeepAliveType.setStatus('current')
cicIkeKeepAliveInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicIkeKeepAliveInterval.setStatus('current')
cicIkeKeepAliveRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicIkeKeepAliveRetryInterval.setStatus('current')
cicIkeInvalidSpiNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 3, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicIkeInvalidSpiNotify.setStatus('current')
cicIkeCfgPskNextAvailTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 1), )
if mibBuilder.loadTexts: cicIkeCfgPskNextAvailTable.setStatus('current')
cicIkeCfgPskNextAvailEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 1, 1), )
cicIkeCfgIdentityEntry.registerAugmentions(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskNextAvailEntry"))
cicIkeCfgPskNextAvailEntry.setIndexNames(*cicIkeCfgIdentityEntry.getIndexNames())
if mibBuilder.loadTexts: cicIkeCfgPskNextAvailEntry.setStatus('current')
cicIkeCfgPskNextAvailIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 1, 1, 1), CicIkeConfigPskIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicIkeCfgPskNextAvailIndex.setStatus('current')
cicIkeCfgPskTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2), )
if mibBuilder.loadTexts: cicIkeCfgPskTable.setStatus('current')
cicIkeCfgPskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1), ).setIndexNames((0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentityDoi"), (0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskIndex"))
if mibBuilder.loadTexts: cicIkeCfgPskEntry.setStatus('current')
cicIkeCfgPskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 1), CicIkeConfigPskIndex())
if mibBuilder.loadTexts: cicIkeCfgPskIndex.setStatus('current')
cicIkeCfgPskKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPskKey.setStatus('current')
cicIkeCfgPskRemIdentType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 3), CIPsecPhase1PeerIdentityType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPskRemIdentType.setStatus('current')
cicIkeCfgPskRemIdentTypeStand = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicIkeCfgPskRemIdentTypeStand.setStatus('current')
cicIkeCfgPskRemIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPskRemIdentity.setStatus('current')
cicIkeCfgPskRemIdAddrOrRg1OrSn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPskRemIdAddrOrRg1OrSn.setStatus('current')
cicIkeCfgPskRemIdAddrRange2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPskRemIdAddrRange2.setStatus('current')
cicIkeCfgPskRemIdSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 8), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPskRemIdSubnetMask.setStatus('current')
cicIkeCfgPskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 4, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPskStatus.setStatus('current')
cicIkeCfgPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1), )
if mibBuilder.loadTexts: cicIkeCfgPolicyTable.setStatus('current')
cicIkeCfgPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1), ).setIndexNames((0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentityDoi"), (0, "CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyPriority"))
if mibBuilder.loadTexts: cicIkeCfgPolicyEntry.setStatus('current')
cicIkeCfgPolicyPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534)))
if mibBuilder.loadTexts: cicIkeCfgPolicyPriority.setStatus('current')
cicIkeCfgPolicyEncr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 2), CIPsecEncryptAlgorithm().clone('esp3des')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPolicyEncr.setStatus('current')
cicIkeCfgPolicyHash = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 3), CIPsecIkeHashAlgorithm().clone('sha')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPolicyHash.setStatus('current')
cicIkeCfgPolicyPRF = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 4), CIPsecIkePRFAlgorithm().clone('prfHmacSha1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPolicyPRF.setStatus('current')
cicIkeCfgPolicyAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 5), CIPsecIkeAuthMethod().clone('preSharedKey')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPolicyAuth.setStatus('current')
cicIkeCfgPolicyDHGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 6), CIPsecDiffHellmanGrp().clone('modp1024')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPolicyDHGroup.setStatus('current')
cicIkeCfgPolicyLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 7), CIKELifetime().clone(86400)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPolicyLifetime.setStatus('current')
cicIkeCfgPolicyLifesize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 8), CIKELifesize().clone(2560)).setUnits('kbytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPolicyLifesize.setStatus('current')
cicIkeCfgPolicyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 5, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cicIkeCfgPolicyStatus.setStatus('current')
cicNotifCntlIkeAllNotifs = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicNotifCntlIkeAllNotifs.setStatus('current')
cicNotifCntlIkeOperStateChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicNotifCntlIkeOperStateChanged.setStatus('current')
cicNotifCntlIkePskAdded = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicNotifCntlIkePskAdded.setStatus('current')
cicNotifCntlIkePskDeleted = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicNotifCntlIkePskDeleted.setStatus('current')
cicNotifCntlIkePolicyAdded = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicNotifCntlIkePolicyAdded.setStatus('current')
cicNotifCntlIkePolicyDeleted = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 423, 1, 7, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicNotifCntlIkePolicyDeleted.setStatus('current')
ciscoIkeConfigOperStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 423, 0, 1)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeEnabled"))
if mibBuilder.loadTexts: ciscoIkeConfigOperStateChanged.setStatus('current')
ciscoIkeConfigPskAdded = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 423, 0, 2)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentType"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentity"))
if mibBuilder.loadTexts: ciscoIkeConfigPskAdded.setStatus('current')
ciscoIkeConfigPskDeleted = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 423, 0, 3)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentType"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentity"))
if mibBuilder.loadTexts: ciscoIkeConfigPskDeleted.setStatus('current')
ciscoIkeConfigPolicyAdded = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 423, 0, 4)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyEncr"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyHash"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyAuth"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyDHGroup"))
if mibBuilder.loadTexts: ciscoIkeConfigPolicyAdded.setStatus('current')
ciscoIkeConfigPolicyDeleted = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 423, 0, 5)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyEncr"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyHash"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyAuth"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyDHGroup"))
if mibBuilder.loadTexts: ciscoIkeConfigPolicyDeleted.setStatus('current')
cicIkeCfgMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1))
cicIkeCfgMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 2))
cicIkeCfgMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 2, 1)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgOperGroup"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentitiesGroup"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskAuthGroup"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyGroup"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgOptionalPolicyGroup"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgFailureRecoveryGroup"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgNotificationGroup"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgNotifCntlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicIkeCfgMIBCompliance = cicIkeCfgMIBCompliance.setStatus('current')
cicIkeCfgOperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 1)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeEnabled"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeAggressModeEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicIkeCfgOperGroup = cicIkeCfgOperGroup.setStatus('current')
cicIkeCfgIdentitiesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 2)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgIdentityType"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorNextAvailIndex"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorPAddrType"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorPAddr"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorVer"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgInitiatorStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicIkeCfgIdentitiesGroup = cicIkeCfgIdentitiesGroup.setStatus('current')
cicIkeCfgFailureRecoveryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 3)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeKeepAliveEnabled"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeKeepAliveType"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeKeepAliveInterval"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeKeepAliveRetryInterval"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeInvalidSpiNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicIkeCfgFailureRecoveryGroup = cicIkeCfgFailureRecoveryGroup.setStatus('current')
cicIkeCfgPskAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 4)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskNextAvailIndex"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskKey"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentType"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentTypeStand"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdentity"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdAddrOrRg1OrSn"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdAddrRange2"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskRemIdSubnetMask"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPskStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicIkeCfgPskAuthGroup = cicIkeCfgPskAuthGroup.setStatus('current')
cicIkeCfgPolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 5)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyEncr"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyHash"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyPRF"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyAuth"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyDHGroup"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyLifetime"), ("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicIkeCfgPolicyGroup = cicIkeCfgPolicyGroup.setStatus('current')
cicIkeCfgOptionalPolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 6)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicIkeCfgPolicyLifesize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicIkeCfgOptionalPolicyGroup = cicIkeCfgOptionalPolicyGroup.setStatus('current')
cicIkeCfgNotifCntlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 7)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkeAllNotifs"), ("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkeOperStateChanged"), ("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkePskAdded"), ("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkePskDeleted"), ("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkePolicyAdded"), ("CISCO-IKE-CONFIGURATION-MIB", "cicNotifCntlIkePolicyDeleted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicIkeCfgNotifCntlGroup = cicIkeCfgNotifCntlGroup.setStatus('current')
cicIkeCfgNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 423, 2, 1, 8)).setObjects(("CISCO-IKE-CONFIGURATION-MIB", "ciscoIkeConfigOperStateChanged"), ("CISCO-IKE-CONFIGURATION-MIB", "ciscoIkeConfigPskAdded"), ("CISCO-IKE-CONFIGURATION-MIB", "ciscoIkeConfigPskDeleted"), ("CISCO-IKE-CONFIGURATION-MIB", "ciscoIkeConfigPolicyAdded"), ("CISCO-IKE-CONFIGURATION-MIB", "ciscoIkeConfigPolicyDeleted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicIkeCfgNotificationGroup = cicIkeCfgNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IKE-CONFIGURATION-MIB", cicIkeCfgPolicyLifesize=cicIkeCfgPolicyLifesize, cicIkeCfgInitiatorPAddrType=cicIkeCfgInitiatorPAddrType, cicIkeConfigMIBNotifs=cicIkeConfigMIBNotifs, cicNotifCntlIkeOperStateChanged=cicNotifCntlIkeOperStateChanged, cicIkeCfgPskRemIdAddrOrRg1OrSn=cicIkeCfgPskRemIdAddrOrRg1OrSn, cicIkeCfgPskTable=cicIkeCfgPskTable, cicIkeCfgInitiatorNextAvailTable=cicIkeCfgInitiatorNextAvailTable, ciscoIkeConfigMIB=ciscoIkeConfigMIB, cicIkeCfgPolicyGroup=cicIkeCfgPolicyGroup, cicIkeCfgPolicyStatus=cicIkeCfgPolicyStatus, cicIkeCfgPskRemIdentity=cicIkeCfgPskRemIdentity, cicIkeAggressModeEnabled=cicIkeAggressModeEnabled, cicIkeCfgPkiAuthConfig=cicIkeCfgPkiAuthConfig, ciscoIkeConfigOperStateChanged=ciscoIkeConfigOperStateChanged, ciscoIkeConfigPskAdded=ciscoIkeConfigPskAdded, cicIkeCfgPolicyPRF=cicIkeCfgPolicyPRF, cicNotifCntlIkePskAdded=cicNotifCntlIkePskAdded, cicIkeKeepAliveRetryInterval=cicIkeKeepAliveRetryInterval, cicIkeCfgPolicyTable=cicIkeCfgPolicyTable, cicIkeCfgIdentityType=cicIkeCfgIdentityType, cicIkeCfgPskNextAvailTable=cicIkeCfgPskNextAvailTable, cicIkeCfgFailureRecovery=cicIkeCfgFailureRecovery, cicIkeCfgInitiatorVer=cicIkeCfgInitiatorVer, cicIkeCfgInitiatorNextAvailEntry=cicIkeCfgInitiatorNextAvailEntry, cicIkeKeepAliveType=cicIkeKeepAliveType, cicIkeCfgNotifCntlGroup=cicIkeCfgNotifCntlGroup, cicIkeKeepAliveEnabled=cicIkeKeepAliveEnabled, cicIkeCfgOperGroup=cicIkeCfgOperGroup, PYSNMP_MODULE_ID=ciscoIkeConfigMIB, cicIkeCfgInitiatorIndex=cicIkeCfgInitiatorIndex, cicIkeCfgPskNextAvailEntry=cicIkeCfgPskNextAvailEntry, cicIkeCfgIdentityDoi=cicIkeCfgIdentityDoi, cicIkeCfgFailureRecovConfigEntry=cicIkeCfgFailureRecovConfigEntry, cicIkeCfgPolicyEncr=cicIkeCfgPolicyEncr, cicIkeCfgIdentitiesGroup=cicIkeCfgIdentitiesGroup, cicNotifCntlIkePolicyDeleted=cicNotifCntlIkePolicyDeleted, cicIkeCfgNotificationGroup=cicIkeCfgNotificationGroup, cicIkeCfgMIBCompliances=cicIkeCfgMIBCompliances, cicIkeCfgInitiatorNextAvailIndex=cicIkeCfgInitiatorNextAvailIndex, cicIkeCfgPskRemIdentType=cicIkeCfgPskRemIdentType, cicIkeCfgPskRemIdAddrRange2=cicIkeCfgPskRemIdAddrRange2, cicIkeCfgPskAuthConfig=cicIkeCfgPskAuthConfig, cicIkeCfgFailureRecoveryGroup=cicIkeCfgFailureRecoveryGroup, cicIkeCfgIdentityEntry=cicIkeCfgIdentityEntry, cicIkeCfgNonceAuthConfig=cicIkeCfgNonceAuthConfig, cicIkeCfgMIBGroups=cicIkeCfgMIBGroups, cicIkeCfgCallAdmssionnCtrl=cicIkeCfgCallAdmssionnCtrl, cicIkeCfgInitiatorPAddr=cicIkeCfgInitiatorPAddr, cicIkeCfgIdentities=cicIkeCfgIdentities, cicNotifCntlIkeAllNotifs=cicNotifCntlIkeAllNotifs, cicIkeCfgPskStatus=cicIkeCfgPskStatus, cicIkeCfgOptionalPolicyGroup=cicIkeCfgOptionalPolicyGroup, cicIkeCfgIdentityTable=cicIkeCfgIdentityTable, cicIkeCfgPskAuthGroup=cicIkeCfgPskAuthGroup, cicIkeCfgMIBCompliance=cicIkeCfgMIBCompliance, ciscoIkeConfigPskDeleted=ciscoIkeConfigPskDeleted, cicIkeCfgInitiatorEntry=cicIkeCfgInitiatorEntry, cicIkeCfgFailureRecovConfigTable=cicIkeCfgFailureRecovConfigTable, cicIkeCfgPolicyLifetime=cicIkeCfgPolicyLifetime, cicIkeCfgPeerAuth=cicIkeCfgPeerAuth, cicNotifCntlIkePskDeleted=cicNotifCntlIkePskDeleted, cicIkeCfgInitiatorStatus=cicIkeCfgInitiatorStatus, cicIkeCfgPskKey=cicIkeCfgPskKey, cicIkeCfgServiceControl=cicIkeCfgServiceControl, cicIkeInvalidSpiNotify=cicIkeInvalidSpiNotify, ciscoIkeConfigPolicyAdded=ciscoIkeConfigPolicyAdded, cicIkeCfgPolicyPriority=cicIkeCfgPolicyPriority, cicIkeCfgPskEntry=cicIkeCfgPskEntry, CicIkeConfigInitiatorIndex=CicIkeConfigInitiatorIndex, ciscoIkeConfigPolicyDeleted=ciscoIkeConfigPolicyDeleted, cicIkeCfgPskRemIdSubnetMask=cicIkeCfgPskRemIdSubnetMask, cicIkeCfgOperations=cicIkeCfgOperations, cicIkeCfgPskNextAvailIndex=cicIkeCfgPskNextAvailIndex, cicIkeKeepAliveInterval=cicIkeKeepAliveInterval, cicIkeCfgPolicyAuth=cicIkeCfgPolicyAuth, cicIkeCfgPolicyDHGroup=cicIkeCfgPolicyDHGroup, cicIkeCfgPolicyEntry=cicIkeCfgPolicyEntry, cicIkeConfigMIBObjects=cicIkeConfigMIBObjects, cicIkeCfgPolicies=cicIkeCfgPolicies, cicIkeCfgInitiatorTable=cicIkeCfgInitiatorTable, cicIkeCfgPolicyHash=cicIkeCfgPolicyHash, cicIkeConfigMIBConform=cicIkeConfigMIBConform, cicIkeCfgPskRemIdentTypeStand=cicIkeCfgPskRemIdentTypeStand, cicIkeCfgQoSControl=cicIkeCfgQoSControl, CicIkeConfigPskIndex=CicIkeConfigPskIndex, cicIkeCfgPskIndex=cicIkeCfgPskIndex, cicNotifCntlIkePolicyAdded=cicNotifCntlIkePolicyAdded, cicIkeEnabled=cicIkeEnabled, cicIkeConfigMibNotifCntl=cicIkeConfigMibNotifCntl)
