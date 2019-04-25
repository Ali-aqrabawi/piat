import socketserver

from piat.parsers.syslog import SyslogMsg
from piat.utils.threads import ThreadsManager
from piat.utils.docerators import restart_on_failure
from piat.utils.logger import get_logger

LOGGER = get_logger(__name__)


class _SyslogHandler(socketserver.BaseRequestHandler):
    callbacks = []

    def handle(self):
        data = bytes.decode(self.request[0].strip())
        ip = self.client_address[0]

        LOGGER.debug("received syslog message from %s, msg=%s" % (ip, data))

        syslog_msg = SyslogMsg.create_msg(ip, data)
        socket = self.request[1]
        proc_mgr = ThreadsManager()
        for cb in self.callbacks:
            proc_mgr.add(cb, args=[syslog_msg, ])

        proc_mgr.start()


class SyslogServer:

    def __init__(self, callbacks, port=514):
        self._callbacks = callbacks
        self._port = port
        self._setup()
        LOGGER.debug("adding %r callbacks to Trap server" % ([func.__name__ for func in self._callbacks]))

    def _setup(self):
        assert isinstance(self._callbacks, list), "callbacks should be list of functions type not %s" % type(
            self._callbacks)
        _SyslogHandler.callbacks = self._callbacks
        self.server = socketserver.UDPServer(('0.0.0.0', self._port), _SyslogHandler)

    @restart_on_failure
    def start(self):
        LOGGER.info("Syslog Server Started...")
        self.server.serve_forever(poll_interval=0.5)
