from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.smi import view, builder, rfc1902
from pysnmp.entity.rfc3413 import ntfrcv, mibvar

# Create SNMP engine with autogenernated engineID and pre-bound
# to socket transport dispatcher
snmpEngine = engine.SnmpEngine()
build = snmpEngine.getMibBuilder()
build.addMibSources(builder.DirMibSource("/user/share/snmp/mibs"))
viewer = view.MibViewController(build)

# Transport setup

# UDP over IPv4, first listening interface/port
config.addTransport(
    snmpEngine,
    udp.domainName + (1,),
    udp.UdpTransport().openServerMode(('0.0.0.0', 162))
)

# SNMPv1/2c setup

# SecurityName <-> CommunityName mapping
config.addV1System(snmpEngine, '????', 'public')


# Callback function for receiving notifications
# noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    print('Notification from ContextEngineId "%s", ContextName "%s"' % (contextEngineId.prettyPrint(),
                                                                        contextName.prettyPrint()))
    for name, val in varBinds:
        print(name)
        symbol = rfc1902.ObjectIdentity(name).resolveWithMib(viewer).getMibSymbol()
        # val = rfc1902.ObjectIdentity(val).resolveWithMib(viewer)
        print(symbol[1])
        print(val)
        print("#########################")


# Register SNMP Application at the SNMP engine
ntfrcv.NotificationReceiver(snmpEngine, cbFun)

snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish

# Run I/O dispatcher which would receive queries and send confirmations
try:
    snmpEngine.transportDispatcher.runDispatcher()
except:
    snmpEngine.transportDispatcher.closeDispatcher()
    raise
