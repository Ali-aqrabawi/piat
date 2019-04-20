from pysnmp.carrier.asyncore.dispatch import AsyncoreDispatcher
from pysnmp.carrier.asyncore.dgram import udp, udp6, unix
from pyasn1.codec.ber import decoder
from pysnmp.proto import api
from pysnmp.smi import compiler, builder, view, rfc1902


# noinspection PyUnusedLocal
def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
    mibBuilder = builder.MibBuilder()
    mibViewController = view.MibViewController(mibBuilder)
    compiler.addMibCompiler(mibBuilder, sources=['file:///usr/share/snmp/mibs',
                                                 'http://mibs.snmplabs.com/asn1/@mib@'])

    # Pre-load MIB modules we expect to work with
    mibBuilder.loadModules('SNMPv2-MIB', 'SNMP-COMMUNITY-MIB')

    while wholeMsg:
        msgVer = int(api.decodeMessageVersion(wholeMsg))
        if msgVer in api.protoModules:
            pMod = api.protoModules[msgVer]
        else:
            print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(
            wholeMsg, asn1Spec=pMod.Message(),
        )
        print('Notification message from %s:%s: ' % (
            transportDomain, transportAddress
        )
              )
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:
                print('Enterprise: %s' % (pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()))
                print('Agent Address: %s' % (pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()))
                print('Generic Trap: %s' % (pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()))
                print('Specific Trap: %s' % (pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()))
                print('Uptime: %s' % (pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()))
                varBinds = pMod.apiTrapPDU.getVarBinds(reqPDU)
            else:
                varBinds = pMod.apiPDU.getVarBinds(reqPDU)
            print('Var-binds:')




            for oid, val in varBinds:
                oid_str = oid.prettyPrint()

                print(rfc1902.ObjectIdentity(oid_str, 12345).resolveWithMib(mibViewController).prettyPrint())
                #print(rfc1902.ObjectIdentity(str(oid), val._value).resolveWithMib(mibViewController))
    return wholeMsg


transportDispatcher = AsyncoreDispatcher()

transportDispatcher.registerRecvCbFun(cbFun)

# UDP/IPv4
transportDispatcher.registerTransport(
    udp.domainName, udp.UdpSocketTransport().openServerMode(('localhost', 162))
)

# UDP/IPv6
transportDispatcher.registerTransport(
    udp6.domainName, udp6.Udp6SocketTransport().openServerMode(('::1', 162))
)

## Local domain socket
# transportDispatcher.registerTransport(
#    unix.domainName, unix.UnixSocketTransport().openServerMode('/tmp/snmp-manager')
# )

transportDispatcher.jobStarted(1)

try:
    # Dispatcher will never finish as job#1 never reaches zero
    transportDispatcher.runDispatcher()
except:
    transportDispatcher.closeDispatcher()
    raise
