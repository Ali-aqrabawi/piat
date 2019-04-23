import logging
import socketserver

from piat.parsers.syslog import SyslogMsg
from piat.utils.threads import ThreadsManager
from piat.utils.docerators import restart_on_failure


class _SyslogHandler(socketserver.BaseRequestHandler):
    callbacks = []

    def handle(self):
        data = bytes.decode(self.request[0].strip())
        ip = self.client_address[0]
        # logging.debug("received message from %s, msg=%s" % (ip, data))
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

    def _setup(self):
        assert isinstance(self._callbacks, list), "callbacks should be list of functions type not %s" % type(
            self._callbacks)
        _SyslogHandler.callbacks = self._callbacks
        self.server = socketserver.UDPServer(('0.0.0.0', self._port), _SyslogHandler)

    @restart_on_failure
    def start(self):
        self.server.serve_forever(poll_interval=0.5)


