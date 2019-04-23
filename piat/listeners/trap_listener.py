from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.smi import view, builder
from pysnmp.entity.rfc3413 import ntfrcv, mibvar
from piat.utils.threads import ThreadsManager
from piat.utils.docerators import restart_on_failure
from piat.parsers.traps.trap import TrapMsg


class TrapsHandler:

    def __init__(self, callbacks, viewer):
        self._callbacks = callbacks
        self._viewer = viewer

    # Callback function for receiving notifications
    # noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
    def handle(self, snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
        print('Notification from ContextEngineId "%s", ContextName "%s"' % (contextEngineId.prettyPrint(),
                                                                            contextName.prettyPrint()))

        trap_log = TrapMsg(varBinds, self._viewer)
        proc_mgr = ThreadsManager()

        for cb in self._callbacks:
            proc_mgr.add(cb, args=[trap_log, ])

        proc_mgr.start()



def create_engine(callbacks, community='public', port=162):
    snmpEngine = engine.SnmpEngine()
    build = snmpEngine.getMibBuilder()
    build.addMibSources(builder.DirMibSource("/home/aaqrabaw/.pysnmp/mibs"))
    build.loadModules()
    viewer = view.MibViewController(build)
    # UDP over IPv4, first listening interface/port
    transport = udp.UdpTransport()
    config.addTransport(snmpEngine, udp.domainName + (1,), transport.openServerMode(('0.0.0.0', port)))
    # SecurityName <-> CommunityName mapping
    config.addV1System(snmpEngine, '????', community)
    # Register SNMP Application at the SNMP engine
    handler = TrapsHandler(callbacks, viewer)
    ntfrcv.NotificationReceiver(snmpEngine, handler.handle)
    return snmpEngine


@restart_on_failure
def start(snmpEngine):
    snmpEngine.transportDispatcher.jobStarted(1)
    snmpEngine.transportDispatcher.runDispatcher()


def run(callbacks, community='public', port=162):
    snmpEngine = create_engine(callbacks, community, port)
    start(snmpEngine)
