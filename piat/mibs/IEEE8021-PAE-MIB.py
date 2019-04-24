#
# PySNMP MIB module IEEE8021-PAE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/IEEE8021-PAE-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:32:38 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Integer32, NotificationType, MibIdentifier, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ModuleIdentity, iso, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "NotificationType", "MibIdentifier", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ModuleIdentity", "iso", "Gauge32", "IpAddress")
DisplayString, TextualConvention, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "MacAddress")
ieee8021paeMIB = ModuleIdentity((1, 0, 8802, 1, 1, 1))
if mibBuilder.loadTexts: ieee8021paeMIB.setLastUpdated('200101160000Z')
if mibBuilder.loadTexts: ieee8021paeMIB.setOrganization('IEEE 802.1 Working Group')
paeMIBObjects = MibIdentifier((1, 0, 8802, 1, 1, 1, 1))
class PaeControlledDirections(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("both", 0), ("in", 1))

class PaeControlledPortStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("authorized", 1), ("unauthorized", 2))

class PaeControlledPortControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forceUnauthorized", 1), ("auto", 2), ("forceAuthorized", 3))

dot1xPaeSystem = MibIdentifier((1, 0, 8802, 1, 1, 1, 1, 1))
dot1xPaeAuthenticator = MibIdentifier((1, 0, 8802, 1, 1, 1, 1, 2))
dot1xPaeSupplicant = MibIdentifier((1, 0, 8802, 1, 1, 1, 1, 3))
dot1xPaeSystemAuthControl = MibScalar((1, 0, 8802, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xPaeSystemAuthControl.setStatus('current')
dot1xPaePortTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 1, 2), )
if mibBuilder.loadTexts: dot1xPaePortTable.setStatus('current')
dot1xPaePortEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xPaePortEntry.setStatus('current')
dot1xPaePortNumber = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dot1xPaePortNumber.setStatus('current')
dot1xPaePortProtocolVersion = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xPaePortProtocolVersion.setStatus('current')
dot1xPaePortCapabilities = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 3), Bits().clone(namedValues=NamedValues(("dot1xPaePortAuthCapable", 0), ("dot1xPaePortSuppCapable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xPaePortCapabilities.setStatus('current')
dot1xPaePortInitialize = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xPaePortInitialize.setStatus('current')
dot1xPaePortReauthenticate = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xPaePortReauthenticate.setStatus('current')
dot1xAuthConfigTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 2, 1), )
if mibBuilder.loadTexts: dot1xAuthConfigTable.setStatus('current')
dot1xAuthConfigEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xAuthConfigEntry.setStatus('current')
dot1xAuthPaeState = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("aborting", 6), ("held", 7), ("forceAuth", 8), ("forceUnauth", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthPaeState.setStatus('current')
dot1xAuthBackendAuthState = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("request", 1), ("response", 2), ("success", 3), ("fail", 4), ("timeout", 5), ("idle", 6), ("initialize", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendAuthState.setStatus('current')
dot1xAuthAdminControlledDirections = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 3), PaeControlledDirections()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthAdminControlledDirections.setStatus('current')
dot1xAuthOperControlledDirections = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 4), PaeControlledDirections()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthOperControlledDirections.setStatus('current')
dot1xAuthAuthControlledPortStatus = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 5), PaeControlledPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthControlledPortStatus.setStatus('current')
dot1xAuthAuthControlledPortControl = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 6), PaeControlledPortControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthAuthControlledPortControl.setStatus('current')
dot1xAuthQuietPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 7), Unsigned32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthQuietPeriod.setStatus('current')
dot1xAuthTxPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 8), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthTxPeriod.setStatus('current')
dot1xAuthSuppTimeout = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 9), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthSuppTimeout.setStatus('current')
dot1xAuthServerTimeout = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 10), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthServerTimeout.setStatus('current')
dot1xAuthMaxReq = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 11), Unsigned32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthMaxReq.setStatus('current')
dot1xAuthReAuthPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 12), Unsigned32().clone(3600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthReAuthPeriod.setStatus('current')
dot1xAuthReAuthEnabled = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthReAuthEnabled.setStatus('current')
dot1xAuthKeyTxEnabled = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xAuthKeyTxEnabled.setStatus('current')
dot1xAuthStatsTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 2, 2), )
if mibBuilder.loadTexts: dot1xAuthStatsTable.setStatus('current')
dot1xAuthStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xAuthStatsEntry.setStatus('current')
dot1xAuthEapolFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolFramesRx.setStatus('current')
dot1xAuthEapolFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolFramesTx.setStatus('current')
dot1xAuthEapolStartFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolStartFramesRx.setStatus('current')
dot1xAuthEapolLogoffFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolLogoffFramesRx.setStatus('current')
dot1xAuthEapolRespIdFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolRespIdFramesRx.setStatus('current')
dot1xAuthEapolRespFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolRespFramesRx.setStatus('current')
dot1xAuthEapolReqIdFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolReqIdFramesTx.setStatus('current')
dot1xAuthEapolReqFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapolReqFramesTx.setStatus('current')
dot1xAuthInvalidEapolFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthInvalidEapolFramesRx.setStatus('current')
dot1xAuthEapLengthErrorFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapLengthErrorFramesRx.setStatus('current')
dot1xAuthLastEapolFrameVersion = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthLastEapolFrameVersion.setStatus('current')
dot1xAuthLastEapolFrameSource = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthLastEapolFrameSource.setStatus('current')
dot1xAuthDiagTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 2, 3), )
if mibBuilder.loadTexts: dot1xAuthDiagTable.setStatus('current')
dot1xAuthDiagEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xAuthDiagEntry.setStatus('current')
dot1xAuthEntersConnecting = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEntersConnecting.setStatus('current')
dot1xAuthEapLogoffsWhileConnecting = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEapLogoffsWhileConnecting.setStatus('current')
dot1xAuthEntersAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthEntersAuthenticating.setStatus('current')
dot1xAuthAuthSuccessWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthSuccessWhileAuthenticating.setStatus('current')
dot1xAuthAuthTimeoutsWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthTimeoutsWhileAuthenticating.setStatus('current')
dot1xAuthAuthFailWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthFailWhileAuthenticating.setStatus('current')
dot1xAuthAuthReauthsWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthReauthsWhileAuthenticating.setStatus('current')
dot1xAuthAuthEapStartsWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthEapStartsWhileAuthenticating.setStatus('current')
dot1xAuthAuthEapLogoffWhileAuthenticating = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthEapLogoffWhileAuthenticating.setStatus('current')
dot1xAuthAuthReauthsWhileAuthenticated = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthReauthsWhileAuthenticated.setStatus('current')
dot1xAuthAuthEapStartsWhileAuthenticated = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthEapStartsWhileAuthenticated.setStatus('current')
dot1xAuthAuthEapLogoffWhileAuthenticated = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthAuthEapLogoffWhileAuthenticated.setStatus('current')
dot1xAuthBackendResponses = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendResponses.setStatus('current')
dot1xAuthBackendAccessChallenges = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendAccessChallenges.setStatus('current')
dot1xAuthBackendOtherRequestsToSupplicant = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendOtherRequestsToSupplicant.setStatus('current')
dot1xAuthBackendNonNakResponsesFromSupplicant = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendNonNakResponsesFromSupplicant.setStatus('current')
dot1xAuthBackendAuthSuccesses = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendAuthSuccesses.setStatus('current')
dot1xAuthBackendAuthFails = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthBackendAuthFails.setStatus('current')
dot1xAuthSessionStatsTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 2, 4), )
if mibBuilder.loadTexts: dot1xAuthSessionStatsTable.setStatus('current')
dot1xAuthSessionStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xAuthSessionStatsEntry.setStatus('current')
dot1xAuthSessionOctetsRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionOctetsRx.setStatus('current')
dot1xAuthSessionOctetsTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionOctetsTx.setStatus('current')
dot1xAuthSessionFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionFramesRx.setStatus('current')
dot1xAuthSessionFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionFramesTx.setStatus('current')
dot1xAuthSessionId = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionId.setStatus('current')
dot1xAuthSessionAuthenticMethod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("remoteAuthServer", 1), ("localAuthServer", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionAuthenticMethod.setStatus('current')
dot1xAuthSessionTime = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionTime.setStatus('current')
dot1xAuthSessionTerminateCause = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 999))).clone(namedValues=NamedValues(("supplicantLogoff", 1), ("portFailure", 2), ("supplicantRestart", 3), ("reauthFailed", 4), ("authControlForceUnauth", 5), ("portReInit", 6), ("portAdminDisabled", 7), ("notTerminatedYet", 999)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionTerminateCause.setStatus('current')
dot1xAuthSessionUserName = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xAuthSessionUserName.setStatus('current')
dot1xSuppConfigTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 3, 1), )
if mibBuilder.loadTexts: dot1xSuppConfigTable.setStatus('current')
dot1xSuppConfigEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xSuppConfigEntry.setStatus('current')
dot1xSuppPaeState = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disconnected", 1), ("logoff", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("acquired", 6), ("held", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppPaeState.setStatus('current')
dot1xSuppHeldPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 2), Unsigned32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xSuppHeldPeriod.setStatus('current')
dot1xSuppAuthPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 3), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xSuppAuthPeriod.setStatus('current')
dot1xSuppStartPeriod = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 4), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xSuppStartPeriod.setStatus('current')
dot1xSuppMaxStart = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 5), Unsigned32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xSuppMaxStart.setStatus('current')
dot1xSuppStatsTable = MibTable((1, 0, 8802, 1, 1, 1, 1, 3, 2), )
if mibBuilder.loadTexts: dot1xSuppStatsTable.setStatus('current')
dot1xSuppStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: dot1xSuppStatsEntry.setStatus('current')
dot1xSuppEapolFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolFramesRx.setStatus('current')
dot1xSuppEapolFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolFramesTx.setStatus('current')
dot1xSuppEapolStartFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolStartFramesTx.setStatus('current')
dot1xSuppEapolLogoffFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolLogoffFramesTx.setStatus('current')
dot1xSuppEapolRespIdFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolRespIdFramesTx.setStatus('current')
dot1xSuppEapolRespFramesTx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolRespFramesTx.setStatus('current')
dot1xSuppEapolReqIdFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolReqIdFramesRx.setStatus('current')
dot1xSuppEapolReqFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapolReqFramesRx.setStatus('current')
dot1xSuppInvalidEapolFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppInvalidEapolFramesRx.setStatus('current')
dot1xSuppEapLengthErrorFramesRx = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppEapLengthErrorFramesRx.setStatus('current')
dot1xSuppLastEapolFrameVersion = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppLastEapolFrameVersion.setStatus('current')
dot1xSuppLastEapolFrameSource = MibTableColumn((1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1xSuppLastEapolFrameSource.setStatus('current')
dot1xPaeConformance = MibIdentifier((1, 0, 8802, 1, 1, 1, 2))
dot1xPaeGroups = MibIdentifier((1, 0, 8802, 1, 1, 1, 2, 1))
dot1xPaeCompliances = MibIdentifier((1, 0, 8802, 1, 1, 1, 2, 2))
dot1xPaeSystemGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 1)).setObjects(("IEEE8021-PAE-MIB", "dot1xPaeSystemAuthControl"), ("IEEE8021-PAE-MIB", "dot1xPaePortProtocolVersion"), ("IEEE8021-PAE-MIB", "dot1xPaePortCapabilities"), ("IEEE8021-PAE-MIB", "dot1xPaePortInitialize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeSystemGroup = dot1xPaeSystemGroup.setStatus('current')
dot1xPaeAuthConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 2)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthPaeState"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthState"), ("IEEE8021-PAE-MIB", "dot1xAuthAdminControlledDirections"), ("IEEE8021-PAE-MIB", "dot1xAuthOperControlledDirections"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthControlledPortStatus"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthControlledPortControl"), ("IEEE8021-PAE-MIB", "dot1xAuthQuietPeriod"), ("IEEE8021-PAE-MIB", "dot1xAuthTxPeriod"), ("IEEE8021-PAE-MIB", "dot1xAuthSuppTimeout"), ("IEEE8021-PAE-MIB", "dot1xAuthServerTimeout"), ("IEEE8021-PAE-MIB", "dot1xAuthMaxReq"), ("IEEE8021-PAE-MIB", "dot1xAuthReAuthPeriod"), ("IEEE8021-PAE-MIB", "dot1xAuthReAuthEnabled"), ("IEEE8021-PAE-MIB", "dot1xAuthKeyTxEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeAuthConfigGroup = dot1xPaeAuthConfigGroup.setStatus('current')
dot1xPaeAuthStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 3)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthEapolFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolFramesTx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolStartFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolLogoffFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolRespIdFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolRespFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolReqIdFramesTx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapolReqFramesTx"), ("IEEE8021-PAE-MIB", "dot1xAuthInvalidEapolFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthEapLengthErrorFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthLastEapolFrameVersion"), ("IEEE8021-PAE-MIB", "dot1xAuthLastEapolFrameSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeAuthStatsGroup = dot1xPaeAuthStatsGroup.setStatus('current')
dot1xPaeAuthDiagGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 4)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthEntersConnecting"), ("IEEE8021-PAE-MIB", "dot1xAuthEapLogoffsWhileConnecting"), ("IEEE8021-PAE-MIB", "dot1xAuthEntersAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthSuccessWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthTimeoutsWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthFailWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthReauthsWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapStartsWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapLogoffWhileAuthenticating"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthReauthsWhileAuthenticated"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapStartsWhileAuthenticated"), ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapLogoffWhileAuthenticated"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendResponses"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAccessChallenges"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendOtherRequestsToSupplicant"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendNonNakResponsesFromSupplicant"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthSuccesses"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthFails"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeAuthDiagGroup = dot1xPaeAuthDiagGroup.setStatus('current')
dot1xPaeAuthSessionStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 5)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthSessionOctetsRx"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionOctetsTx"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionFramesRx"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionFramesTx"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionId"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionAuthenticMethod"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionTime"), ("IEEE8021-PAE-MIB", "dot1xAuthSessionTerminateCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeAuthSessionStatsGroup = dot1xPaeAuthSessionStatsGroup.setStatus('current')
dot1xPaeSuppConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 6)).setObjects(("IEEE8021-PAE-MIB", "dot1xSuppPaeState"), ("IEEE8021-PAE-MIB", "dot1xSuppHeldPeriod"), ("IEEE8021-PAE-MIB", "dot1xSuppAuthPeriod"), ("IEEE8021-PAE-MIB", "dot1xSuppStartPeriod"), ("IEEE8021-PAE-MIB", "dot1xSuppMaxStart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeSuppConfigGroup = dot1xPaeSuppConfigGroup.setStatus('current')
dot1xPaeSuppStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 1, 2, 1, 7)).setObjects(("IEEE8021-PAE-MIB", "dot1xSuppEapolFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolStartFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolLogoffFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolRespIdFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolRespFramesTx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolReqIdFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapolReqFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppInvalidEapolFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppEapLengthErrorFramesRx"), ("IEEE8021-PAE-MIB", "dot1xSuppLastEapolFrameVersion"), ("IEEE8021-PAE-MIB", "dot1xSuppLastEapolFrameSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeSuppStatsGroup = dot1xPaeSuppStatsGroup.setStatus('current')
dot1xPaeCompliance = ModuleCompliance((1, 0, 8802, 1, 1, 1, 2, 2, 1)).setObjects(("IEEE8021-PAE-MIB", "dot1xPaeSystemGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthConfigGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthStatsGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthDiagGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeAuthSessionStatsGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeSuppConfigGroup"), ("IEEE8021-PAE-MIB", "dot1xPaeSuppStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xPaeCompliance = dot1xPaeCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-PAE-MIB", dot1xAuthBackendAuthFails=dot1xAuthBackendAuthFails, dot1xSuppConfigEntry=dot1xSuppConfigEntry, dot1xPaePortProtocolVersion=dot1xPaePortProtocolVersion, PaeControlledPortControl=PaeControlledPortControl, dot1xAuthEapLengthErrorFramesRx=dot1xAuthEapLengthErrorFramesRx, dot1xAuthBackendNonNakResponsesFromSupplicant=dot1xAuthBackendNonNakResponsesFromSupplicant, dot1xAuthAuthControlledPortControl=dot1xAuthAuthControlledPortControl, dot1xPaeSupplicant=dot1xPaeSupplicant, dot1xAuthAdminControlledDirections=dot1xAuthAdminControlledDirections, dot1xSuppEapolRespIdFramesTx=dot1xSuppEapolRespIdFramesTx, dot1xAuthSessionAuthenticMethod=dot1xAuthSessionAuthenticMethod, dot1xSuppMaxStart=dot1xSuppMaxStart, dot1xAuthEapLogoffsWhileConnecting=dot1xAuthEapLogoffsWhileConnecting, dot1xPaePortNumber=dot1xPaePortNumber, dot1xAuthEntersConnecting=dot1xAuthEntersConnecting, dot1xAuthTxPeriod=dot1xAuthTxPeriod, dot1xPaeSystemGroup=dot1xPaeSystemGroup, dot1xAuthAuthEapLogoffWhileAuthenticated=dot1xAuthAuthEapLogoffWhileAuthenticated, dot1xPaePortReauthenticate=dot1xPaePortReauthenticate, dot1xAuthAuthReauthsWhileAuthenticating=dot1xAuthAuthReauthsWhileAuthenticating, dot1xAuthEntersAuthenticating=dot1xAuthEntersAuthenticating, dot1xAuthLastEapolFrameSource=dot1xAuthLastEapolFrameSource, dot1xAuthAuthControlledPortStatus=dot1xAuthAuthControlledPortStatus, ieee8021paeMIB=ieee8021paeMIB, PaeControlledDirections=PaeControlledDirections, dot1xAuthSessionTerminateCause=dot1xAuthSessionTerminateCause, dot1xPaeConformance=dot1xPaeConformance, dot1xPaeAuthDiagGroup=dot1xPaeAuthDiagGroup, dot1xSuppStatsTable=dot1xSuppStatsTable, dot1xAuthEapolRespIdFramesRx=dot1xAuthEapolRespIdFramesRx, dot1xAuthEapolFramesRx=dot1xAuthEapolFramesRx, dot1xSuppEapLengthErrorFramesRx=dot1xSuppEapLengthErrorFramesRx, dot1xPaeSystemAuthControl=dot1xPaeSystemAuthControl, PYSNMP_MODULE_ID=ieee8021paeMIB, dot1xAuthSessionId=dot1xAuthSessionId, dot1xAuthEapolLogoffFramesRx=dot1xAuthEapolLogoffFramesRx, dot1xSuppStartPeriod=dot1xSuppStartPeriod, dot1xSuppHeldPeriod=dot1xSuppHeldPeriod, dot1xSuppEapolFramesRx=dot1xSuppEapolFramesRx, dot1xAuthBackendAuthSuccesses=dot1xAuthBackendAuthSuccesses, dot1xPaeSuppStatsGroup=dot1xPaeSuppStatsGroup, dot1xAuthAuthEapLogoffWhileAuthenticating=dot1xAuthAuthEapLogoffWhileAuthenticating, dot1xPaeAuthStatsGroup=dot1xPaeAuthStatsGroup, dot1xPaeAuthenticator=dot1xPaeAuthenticator, dot1xPaeSuppConfigGroup=dot1xPaeSuppConfigGroup, dot1xAuthSessionStatsEntry=dot1xAuthSessionStatsEntry, dot1xSuppLastEapolFrameVersion=dot1xSuppLastEapolFrameVersion, dot1xAuthMaxReq=dot1xAuthMaxReq, dot1xAuthEapolFramesTx=dot1xAuthEapolFramesTx, dot1xAuthSessionOctetsTx=dot1xAuthSessionOctetsTx, dot1xAuthSessionOctetsRx=dot1xAuthSessionOctetsRx, dot1xSuppConfigTable=dot1xSuppConfigTable, dot1xAuthEapolStartFramesRx=dot1xAuthEapolStartFramesRx, dot1xAuthReAuthPeriod=dot1xAuthReAuthPeriod, dot1xAuthStatsTable=dot1xAuthStatsTable, dot1xAuthSuppTimeout=dot1xAuthSuppTimeout, dot1xSuppPaeState=dot1xSuppPaeState, dot1xSuppStatsEntry=dot1xSuppStatsEntry, dot1xAuthAuthEapStartsWhileAuthenticated=dot1xAuthAuthEapStartsWhileAuthenticated, dot1xAuthAuthEapStartsWhileAuthenticating=dot1xAuthAuthEapStartsWhileAuthenticating, dot1xAuthBackendResponses=dot1xAuthBackendResponses, dot1xAuthSessionStatsTable=dot1xAuthSessionStatsTable, dot1xAuthBackendOtherRequestsToSupplicant=dot1xAuthBackendOtherRequestsToSupplicant, dot1xAuthQuietPeriod=dot1xAuthQuietPeriod, dot1xAuthKeyTxEnabled=dot1xAuthKeyTxEnabled, dot1xAuthDiagEntry=dot1xAuthDiagEntry, dot1xAuthEapolReqIdFramesTx=dot1xAuthEapolReqIdFramesTx, dot1xPaeCompliance=dot1xPaeCompliance, dot1xAuthAuthReauthsWhileAuthenticated=dot1xAuthAuthReauthsWhileAuthenticated, dot1xAuthAuthTimeoutsWhileAuthenticating=dot1xAuthAuthTimeoutsWhileAuthenticating, dot1xAuthEapolRespFramesRx=dot1xAuthEapolRespFramesRx, dot1xSuppLastEapolFrameSource=dot1xSuppLastEapolFrameSource, dot1xAuthLastEapolFrameVersion=dot1xAuthLastEapolFrameVersion, dot1xPaeGroups=dot1xPaeGroups, dot1xPaePortCapabilities=dot1xPaePortCapabilities, dot1xAuthSessionFramesRx=dot1xAuthSessionFramesRx, paeMIBObjects=paeMIBObjects, dot1xPaeCompliances=dot1xPaeCompliances, dot1xAuthBackendAccessChallenges=dot1xAuthBackendAccessChallenges, dot1xSuppEapolRespFramesTx=dot1xSuppEapolRespFramesTx, dot1xAuthConfigEntry=dot1xAuthConfigEntry, dot1xAuthOperControlledDirections=dot1xAuthOperControlledDirections, dot1xAuthStatsEntry=dot1xAuthStatsEntry, dot1xPaeAuthConfigGroup=dot1xPaeAuthConfigGroup, dot1xAuthPaeState=dot1xAuthPaeState, PaeControlledPortStatus=PaeControlledPortStatus, dot1xAuthAuthSuccessWhileAuthenticating=dot1xAuthAuthSuccessWhileAuthenticating, dot1xAuthInvalidEapolFramesRx=dot1xAuthInvalidEapolFramesRx, dot1xSuppEapolReqFramesRx=dot1xSuppEapolReqFramesRx, dot1xPaePortInitialize=dot1xPaePortInitialize, dot1xPaeAuthSessionStatsGroup=dot1xPaeAuthSessionStatsGroup, dot1xAuthReAuthEnabled=dot1xAuthReAuthEnabled, dot1xAuthSessionFramesTx=dot1xAuthSessionFramesTx, dot1xSuppEapolStartFramesTx=dot1xSuppEapolStartFramesTx, dot1xPaeSystem=dot1xPaeSystem, dot1xAuthEapolReqFramesTx=dot1xAuthEapolReqFramesTx, dot1xAuthSessionUserName=dot1xAuthSessionUserName, dot1xAuthSessionTime=dot1xAuthSessionTime, dot1xAuthBackendAuthState=dot1xAuthBackendAuthState, dot1xAuthConfigTable=dot1xAuthConfigTable, dot1xSuppInvalidEapolFramesRx=dot1xSuppInvalidEapolFramesRx, dot1xPaePortTable=dot1xPaePortTable, dot1xPaePortEntry=dot1xPaePortEntry, dot1xSuppAuthPeriod=dot1xSuppAuthPeriod, dot1xSuppEapolFramesTx=dot1xSuppEapolFramesTx, dot1xAuthServerTimeout=dot1xAuthServerTimeout, dot1xSuppEapolReqIdFramesRx=dot1xSuppEapolReqIdFramesRx, dot1xSuppEapolLogoffFramesTx=dot1xSuppEapolLogoffFramesTx, dot1xAuthDiagTable=dot1xAuthDiagTable, dot1xAuthAuthFailWhileAuthenticating=dot1xAuthAuthFailWhileAuthenticating)
