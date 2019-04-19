import logging
import socketserver

from piat.parsers.syslog import SyslogMsg
from piat.utils.threads import ThreadsManager

# LOG_FILE = 'logs/syslog.log'
#
# logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')


class SyslogHandler(socketserver.BaseRequestHandler):
    callbacks = []

    def handle(self):
        data = bytes.decode(self.request[0].strip())
        ip = self.client_address[0]
        #logging.debug("received message from %s, msg=%s" % (ip, data))
        syslog_msg = SyslogMsg.create_msg(ip, data)
        socket = self.request[1]
        proc_mgr = ThreadsManager()
        for cb in self.callbacks:
            proc_mgr.add(cb, args=[syslog_msg, ])

        proc_mgr.start()


def run(callbacks, port=514):
    assert isinstance(callbacks, list), "callbacks should be list type not %s" % type(callbacks)
    SyslogHandler.callbacks = callbacks
    server = socketserver.UDPServer(('0.0.0.0', port), SyslogHandler)
    server.serve_forever(poll_interval=0.5)
