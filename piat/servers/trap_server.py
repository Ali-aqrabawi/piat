import os
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.smi import view, builder
from pysnmp.entity.rfc3413 import ntfrcv
from piat.utils.threads import ThreadsManager
from piat.utils.decorators import restart_on_failure
from piat.parsers.traps.trap import TrapMsg
from piat.utils.logger import get_logger
from piat.exceptions import PiatError

LOGGER = get_logger(__name__)


class TrapsHandler:
    """ Trap Msg Handler"""

    def __init__(self, callbacks, viewer):
        self._callbacks = callbacks
        self._viewer = viewer
        LOGGER.info("registered %r callbacks to Trap server",
                    [func.__name__ for func in self._callbacks])

    def handle(self, snmp_engine,
               state_reference, context_engine_id,
               context_name, var_binds, cb_ctx):
        """ Msg method Handler """

        LOGGER.debug('Notification from ContextEngineId "%s", ContextName "%s"',
                     context_engine_id.prettyPrint(),
                     context_name.prettyPrint())

        trap_log = TrapMsg(var_binds, self._viewer)
        proc_mgr = ThreadsManager()

        for callback in self._callbacks:
            proc_mgr.add(callback, args=[trap_log, ])

        proc_mgr.start()


class SnmpTrapServer:
    """ Snmp Trap Server """

    def __init__(self,
                 callbacks,
                 community='public',
                 port=162,
                 add_mib_dir=''):
        self._callbacks = callbacks
        self._port = port
        self._community = community
        self._add_mib_dir = add_mib_dir
        self._setup()

    def _setup(self):
        """ Setup Server """
        assert isinstance(self._callbacks, list), \
            "callbacks should be list of functions type not %s" % type(
                self._callbacks)

        snmp_engine = engine.SnmpEngine()
        build = snmp_engine.getMibBuilder()

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
        config.addTransport(snmp_engine, udp.domainName + (1,), transport.openServerMode(('0.0.0.0', self._port)))
        # SecurityName <-> CommunityName mapping
        config.addV1System(snmp_engine, '????', self._community)
        # Register SNMP Application at the SNMP engine
        handler = TrapsHandler(self._callbacks, viewer)
        ntfrcv.NotificationReceiver(snmp_engine, handler.handle)
        self._snmpEngine = snmp_engine

    @restart_on_failure
    def start(self):
        """ Start the Server"""
        LOGGER.info("Trap service Started...")
        self._snmpEngine.transportDispatcher.jobStarted(1)
        self._snmpEngine.transportDispatcher.runDispatcher()
