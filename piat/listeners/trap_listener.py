from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.smi import view, builder, rfc1902
from pysnmp.entity.rfc3413 import ntfrcv, mibvar

from piat.utils.threads import ThreadsManager
from piat.parsers.traps.trap import TrapMsg


class TrapsHandler:

    def __init__(self, callbacks, viewer):
        self._callbacks = callbacks
        self._viewer = viewer

    # Callback function for receiving notifications
    # noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
    def cbFun(self, snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
        print('Notification from ContextEngineId "%s", ContextName "%s"' % (contextEngineId.prettyPrint(),
                                                                            contextName.prettyPrint()))
        # result = {}
        # for name, val in varBinds:
        #     symbol = rfc1902.ObjectIdentity(name).resolveWithMib(self._viewer).getMibSymbol()
        #     # val = rfc1902.ObjectIdentity(val).resolveWithMib(viewer)
        #     result[symbol[1]] = val

        trap_log = TrapMsg(varBinds, self._viewer)

        proc_mgr = ThreadsManager()
        for cb in self._callbacks:
            proc_mgr.add(cb, args=[trap_log, ])

        proc_mgr.start()


def run(callbacks, community='public', port=162):
    # Create SNMP engine with autogenernated engineID and pre-bound
    # to socket transport dispatcher
    snmpEngine = engine.SnmpEngine()
    build = snmpEngine.getMibBuilder()
    build.addMibSources(builder.DirMibSource("/user/share/snmp/mibs"))
    viewer = view.MibViewController(build)

    handler = TrapsHandler(callbacks, viewer)

    # UDP over IPv4, first listening interface/port
    config.addTransport(
        snmpEngine,
        udp.domainName + (1,),
        udp.UdpTransport().openServerMode(('0.0.0.0', 162))
    )

    # SNMPv1/2c setup
    print(community)

    # SecurityName <-> CommunityName mapping
    config.addV1System(snmpEngine, '????', communityName=community)

    # Register SNMP Application at the SNMP engine
    ntfrcv.NotificationReceiver(snmpEngine, handler.cbFun)

    snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish

    # Run I/O dispatcher which would receive queries and send confirmations
    try:
        snmpEngine.transportDispatcher.runDispatcher()
    except:
        snmpEngine.transportDispatcher.closeDispatcher()
        raise
