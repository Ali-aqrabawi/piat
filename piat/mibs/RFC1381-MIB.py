#
# PySNMP MIB module RFC1381-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/ietf/RFC1381-MIB
# Produced by pysmi-0.3.4 at Sun Apr 21 23:31:10 2019
# On host aaqrabaw platform Linux version 4.15.0-47-generic by user aaqrabaw
# Using Python version 3.6.5 (default, Apr  1 2018, 05:46:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Bits, Integer32, Counter32, Counter64, Gauge32, Unsigned32, iso, ModuleIdentity, TimeTicks, MibIdentifier, transmission = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Bits", "Integer32", "Counter32", "Counter64", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "TimeTicks", "MibIdentifier", "transmission")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lapb = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16))
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class IfIndexType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

lapbAdmnTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 1), )
if mibBuilder.loadTexts: lapbAdmnTable.setStatus('mandatory')
lapbAdmnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 1, 1), ).setIndexNames((0, "RFC1381-MIB", "lapbAdmnIndex"))
if mibBuilder.loadTexts: lapbAdmnEntry.setStatus('mandatory')
lapbAdmnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbAdmnIndex.setStatus('mandatory')
lapbAdmnStationType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2), ("dxe", 3))).clone('dte')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnStationType.setStatus('mandatory')
lapbAdmnControlField = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("modulo8", 1), ("modulo128", 2))).clone('modulo8')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnControlField.setStatus('mandatory')
lapbAdmnTransmitN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 4), PositiveInteger().clone(36000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnTransmitN1FrameSize.setStatus('mandatory')
lapbAdmnReceiveN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 5), PositiveInteger().clone(36000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnReceiveN1FrameSize.setStatus('mandatory')
lapbAdmnTransmitKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnTransmitKWindowSize.setStatus('mandatory')
lapbAdmnReceiveKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnReceiveKWindowSize.setStatus('mandatory')
lapbAdmnN2RxmitCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnN2RxmitCount.setStatus('mandatory')
lapbAdmnT1AckTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 9), PositiveInteger().clone(3000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnT1AckTimer.setStatus('mandatory')
lapbAdmnT2AckDelayTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 10), PositiveInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnT2AckDelayTimer.setStatus('mandatory')
lapbAdmnT3DisconnectTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 11), PositiveInteger().clone(60000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnT3DisconnectTimer.setStatus('mandatory')
lapbAdmnT4IdleTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 12), PositiveInteger().clone(2147483647)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnT4IdleTimer.setStatus('mandatory')
lapbAdmnActionInitiate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("sendSABM", 1), ("sendDISC", 2), ("sendDM", 3), ("none", 4), ("other", 5))).clone('sendSABM')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnActionInitiate.setStatus('mandatory')
lapbAdmnActionRecvDM = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sendSABM", 1), ("sendDISC", 2), ("other", 3))).clone('sendSABM')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbAdmnActionRecvDM.setStatus('mandatory')
lapbOperTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 2), )
if mibBuilder.loadTexts: lapbOperTable.setStatus('mandatory')
lapbOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 2, 1), ).setIndexNames((0, "RFC1381-MIB", "lapbOperIndex"))
if mibBuilder.loadTexts: lapbOperEntry.setStatus('mandatory')
lapbOperIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperIndex.setStatus('mandatory')
lapbOperStationType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2), ("dxe", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperStationType.setStatus('mandatory')
lapbOperControlField = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("modulo8", 1), ("modulo128", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperControlField.setStatus('mandatory')
lapbOperTransmitN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperTransmitN1FrameSize.setStatus('mandatory')
lapbOperReceiveN1FrameSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 5), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperReceiveN1FrameSize.setStatus('mandatory')
lapbOperTransmitKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperTransmitKWindowSize.setStatus('mandatory')
lapbOperReceiveKWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperReceiveKWindowSize.setStatus('mandatory')
lapbOperN2RxmitCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperN2RxmitCount.setStatus('mandatory')
lapbOperT1AckTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 9), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperT1AckTimer.setStatus('mandatory')
lapbOperT2AckDelayTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 10), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperT2AckDelayTimer.setStatus('mandatory')
lapbOperT3DisconnectTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 11), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperT3DisconnectTimer.setStatus('mandatory')
lapbOperT4IdleTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 12), PositiveInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbOperT4IdleTimer.setStatus('mandatory')
lapbOperPortId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 13), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperPortId.setStatus('mandatory')
lapbOperProtocolVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 14), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperProtocolVersionId.setStatus('mandatory')
lapbFlowTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 3), )
if mibBuilder.loadTexts: lapbFlowTable.setStatus('mandatory')
lapbFlowEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 3, 1), ).setIndexNames((0, "RFC1381-MIB", "lapbFlowIfIndex"))
if mibBuilder.loadTexts: lapbFlowEntry.setStatus('mandatory')
lapbFlowIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowIfIndex.setStatus('mandatory')
lapbFlowStateChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowStateChanges.setStatus('mandatory')
lapbFlowChangeReason = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("notStarted", 1), ("abmEntered", 2), ("abmeEntered", 3), ("abmReset", 4), ("abmeReset", 5), ("dmReceived", 6), ("dmSent", 7), ("discReceived", 8), ("discSent", 9), ("frmrReceived", 10), ("frmrSent", 11), ("n2Timeout", 12), ("other", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowChangeReason.setStatus('mandatory')
lapbFlowCurrentMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("disconnected", 1), ("linkSetup", 2), ("frameReject", 3), ("disconnectRequest", 4), ("informationTransfer", 5), ("rejFrameSent", 6), ("waitingAcknowledgement", 7), ("stationBusy", 8), ("remoteStationBusy", 9), ("bothStationsBusy", 10), ("waitingAckStationBusy", 11), ("waitingAckRemoteBusy", 12), ("waitingAckBothBusy", 13), ("rejFrameSentRemoteBusy", 14), ("xidFrameSent", 15), ("error", 16), ("other", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowCurrentMode.setStatus('mandatory')
lapbFlowBusyDefers = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowBusyDefers.setStatus('mandatory')
lapbFlowRejOutPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowRejOutPkts.setStatus('mandatory')
lapbFlowRejInPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowRejInPkts.setStatus('mandatory')
lapbFlowT1Timeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowT1Timeouts.setStatus('mandatory')
lapbFlowFrmrSent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowFrmrSent.setStatus('mandatory')
lapbFlowFrmrReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowFrmrReceived.setStatus('mandatory')
lapbFlowXidReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8206))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowXidReceived.setStatus('mandatory')
lapbXidTable = MibTable((1, 3, 6, 1, 2, 1, 10, 16, 4), )
if mibBuilder.loadTexts: lapbXidTable.setStatus('mandatory')
lapbXidEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 16, 4, 1), ).setIndexNames((0, "RFC1381-MIB", "lapbXidIndex"))
if mibBuilder.loadTexts: lapbXidEntry.setStatus('mandatory')
lapbXidIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbXidIndex.setStatus('mandatory')
lapbXidAdRIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidAdRIdentifier.setStatus('mandatory')
lapbXidAdRAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidAdRAddress.setStatus('mandatory')
lapbXidParameterUniqueIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidParameterUniqueIdentifier.setStatus('mandatory')
lapbXidGroupAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidGroupAddress.setStatus('mandatory')
lapbXidPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidPortNumber.setStatus('mandatory')
lapbXidUserDataSubfield = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8206)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbXidUserDataSubfield.setStatus('mandatory')
lapbProtocolVersion = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5))
lapbProtocolIso7776v1986 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5, 1))
lapbProtocolCcittV1980 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5, 2))
lapbProtocolCcittV1984 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 16, 5, 3))
mibBuilder.exportSymbols("RFC1381-MIB", IfIndexType=IfIndexType, lapbXidUserDataSubfield=lapbXidUserDataSubfield, lapbFlowIfIndex=lapbFlowIfIndex, lapbAdmnEntry=lapbAdmnEntry, lapbOperStationType=lapbOperStationType, lapbAdmnControlField=lapbAdmnControlField, lapbXidParameterUniqueIdentifier=lapbXidParameterUniqueIdentifier, lapbOperT2AckDelayTimer=lapbOperT2AckDelayTimer, lapbAdmnTable=lapbAdmnTable, lapbFlowTable=lapbFlowTable, lapbFlowBusyDefers=lapbFlowBusyDefers, lapbOperT4IdleTimer=lapbOperT4IdleTimer, lapbFlowFrmrSent=lapbFlowFrmrSent, lapbProtocolIso7776v1986=lapbProtocolIso7776v1986, lapbOperReceiveN1FrameSize=lapbOperReceiveN1FrameSize, lapbOperIndex=lapbOperIndex, lapbAdmnN2RxmitCount=lapbAdmnN2RxmitCount, lapbAdmnActionInitiate=lapbAdmnActionInitiate, lapbAdmnT2AckDelayTimer=lapbAdmnT2AckDelayTimer, lapbXidAdRIdentifier=lapbXidAdRIdentifier, lapbOperTransmitN1FrameSize=lapbOperTransmitN1FrameSize, lapbFlowRejInPkts=lapbFlowRejInPkts, lapbXidGroupAddress=lapbXidGroupAddress, lapbXidIndex=lapbXidIndex, lapbOperReceiveKWindowSize=lapbOperReceiveKWindowSize, lapbOperProtocolVersionId=lapbOperProtocolVersionId, lapbOperEntry=lapbOperEntry, lapbAdmnActionRecvDM=lapbAdmnActionRecvDM, lapbFlowChangeReason=lapbFlowChangeReason, lapbXidAdRAddress=lapbXidAdRAddress, lapbXidPortNumber=lapbXidPortNumber, lapbAdmnTransmitKWindowSize=lapbAdmnTransmitKWindowSize, lapbOperTransmitKWindowSize=lapbOperTransmitKWindowSize, lapbFlowCurrentMode=lapbFlowCurrentMode, lapbXidEntry=lapbXidEntry, lapbFlowStateChanges=lapbFlowStateChanges, PositiveInteger=PositiveInteger, lapbOperN2RxmitCount=lapbOperN2RxmitCount, lapbAdmnTransmitN1FrameSize=lapbAdmnTransmitN1FrameSize, lapbProtocolCcittV1984=lapbProtocolCcittV1984, lapbOperT1AckTimer=lapbOperT1AckTimer, lapbAdmnT1AckTimer=lapbAdmnT1AckTimer, lapbFlowXidReceived=lapbFlowXidReceived, lapbFlowRejOutPkts=lapbFlowRejOutPkts, lapbFlowFrmrReceived=lapbFlowFrmrReceived, lapbXidTable=lapbXidTable, lapbOperPortId=lapbOperPortId, lapbFlowEntry=lapbFlowEntry, lapbOperControlField=lapbOperControlField, lapb=lapb, lapbAdmnStationType=lapbAdmnStationType, lapbProtocolCcittV1980=lapbProtocolCcittV1980, lapbOperTable=lapbOperTable, lapbProtocolVersion=lapbProtocolVersion, lapbOperT3DisconnectTimer=lapbOperT3DisconnectTimer, lapbAdmnReceiveKWindowSize=lapbAdmnReceiveKWindowSize, lapbFlowT1Timeouts=lapbFlowT1Timeouts, lapbAdmnIndex=lapbAdmnIndex, lapbAdmnT3DisconnectTimer=lapbAdmnT3DisconnectTimer, lapbAdmnT4IdleTimer=lapbAdmnT4IdleTimer, lapbAdmnReceiveN1FrameSize=lapbAdmnReceiveN1FrameSize)