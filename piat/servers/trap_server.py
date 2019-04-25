from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.smi import view, builder
from pysnmp.entity.rfc3413 import ntfrcv, mibvar
from piat.utils.threads import ThreadsManager
from piat.utils.docerators import restart_on_failure
from piat.parsers.traps.trap import TrapMsg
from piat.utils.logger import get_logger
from piat.exceptions import PiatError
import os

LOGGER = get_logger(__name__)


class TrapsHandler:

    def __init__(self, callbacks, viewer):
        self._callbacks = callbacks
        self._viewer = viewer
        LOGGER.debug("adding %r callbacks to Trap server" % ([func.__name__ for func in self._callbacks]))

    def handle(self, snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
        LOGGER.debug('Notification from ContextEngineId "%s", ContextName "%s"' % (contextEngineId.prettyPrint(),
                                                                                   contextName.prettyPrint()))

        trap_log = TrapMsg(varBinds, self._viewer)
        proc_mgr = ThreadsManager()

        for cb in self._callbacks:
            proc_mgr.add(cb, args=[trap_log, ])

        proc_mgr.start()


class SnmpTrapServer:

    def __init__(self, callbacks, community='public', port=162, use_precombiled_mibs=True, add_mib_dir=''):
        self._callbacks = callbacks
        self._port = port
        self._community = community
        self._use_precombiled_mibs = use_precombiled_mibs
        self._add_mib_dir = add_mib_dir
        self._setup()

    def _setup(self):
        assert isinstance(self._callbacks, list), "callbacks should be list of functions type not %s" % type(
            self._callbacks)
        snmpEngine = engine.SnmpEngine()
        build = snmpEngine.getMibBuilder()
        if self._use_precombiled_mibs:
            build.addMibSources(builder.DirMibSource(os.environ['PIAT_MIB_PATH']))

        if self._add_mib_dir:
            if not os.path.exists(self._add_mib_dir):
                raise PiatError("mib dir does not exist, dir=%r" % self._add_mib_dir)
            if not os.path.isdir(self._add_mib_dir):
                raise PiatError("add_mib_dir should be a directory not a file, add_mib_dir=%r" % self._add_mib_dir)
            build.addMibSources(builder.DirMibSource(self._add_mib_dir))

        build.loadModules()
        viewer = view.MibViewController(build)
        # UDP over IPv4, first listening interface/port
        transport = udp.UdpTransport()
        config.addTransport(snmpEngine, udp.domainName + (1,), transport.openServerMode(('0.0.0.0', self._port)))
        # SecurityName <-> CommunityName mapping
        config.addV1System(snmpEngine, '????', self._community)
        # Register SNMP Application at the SNMP engine
        handler = TrapsHandler(self._callbacks, viewer)
        ntfrcv.NotificationReceiver(snmpEngine, handler.handle)
        self._snmpEngine = snmpEngine

    @restart_on_failure
    def start(self):
        LOGGER.info("Syslog Server Started...")
        self._snmpEngine.transportDispatcher.jobStarted(1)
        self._snmpEngine.transportDispatcher.runDispatcher()
