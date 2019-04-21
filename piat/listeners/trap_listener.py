from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.smi import view, builder
from pysnmp.entity.rfc3413 import ntfrcv, mibvar

from piat.utils.threads import ThreadsManager
from piat.utils.docerators import restart_on_failure
from piat.parsers.traps.trap import TrapMsg

snmpEngine = engine.SnmpEngine()
build = snmpEngine.getMibBuilder()
build.addMibSources(builder.DirMibSource("/home/aaqrabaw/.pysnmp/mibs"))
#build.addMibSources(builder.DirMibSource("/home/aaqrabaw/PycharmProjects/piat_project/pre_comp"))
build.loadModules()

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


@restart_on_failure
def run(callbacks, community='public', port=162):
    # Create SNMP engine with autogenernated engineID and pre-bound
    # to socket transport dispatcher

    viewer = view.MibViewController(build)

    handler = TrapsHandler(callbacks, viewer)

    # UDP over IPv4, first listening interface/port
    config.addTransport(
        snmpEngine,
        udp.domainName + (1,),
        udp.UdpTransport().openServerMode(('0.0.0.0', port))
    )

    # SNMPv1/2c setup

    # SecurityName <-> CommunityName mapping
    config.addV1System(snmpEngine, '????', community)

    # Register SNMP Application at the SNMP engine
    ntfrcv.NotificationReceiver(snmpEngine, handler.handle)

    snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish
    import time

    # Run I/O dispatcher which would receive queries and send confirmations

    snmpEngine.transportDispatcher.runDispatcher()
