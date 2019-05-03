# (c) 2019, Ali Aqrabawi <aaqrabawn@gmail.com>
#
# This file is part of Piat
#
# Piat is free software licensed under MIT License.
# Piat Server Module has the PiatServer Class which run both Syslog And Traps servers in
# two independent processes
from multiprocessing import Process
from piat.servers.trap_server import SnmpTrapServer
from piat.servers.syslog_server import SyslogServer


class PiatServer:
    """
    PiatServer is the Server that manages and run both Syslog and trap services,
    each service will be running as a independent process.
    """

    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.

    def __init__(self,
                 syslog_callbacks,
                 traps_callbacks,
                 syslog_port=514,
                 trap_port=162,
                 trap_community='public',
                 add_mib_dir=''):

        self._syslog_callbacks = syslog_callbacks
        self._trap_callbacks = traps_callbacks
        self._syslog_port = syslog_port
        self._trap_port = trap_port
        self._trap_community = trap_community
        self._add_mib_dir = add_mib_dir
        self._processes = []

        self._setup()

    def _setup(self):
        syslog_server = SyslogServer(self._syslog_callbacks,
                                     self._syslog_port)

        trap_server = SnmpTrapServer(self._trap_callbacks,
                                     self._trap_community,
                                     self._trap_port,
                                     self._add_mib_dir)

        syslog_proc = Process(target=syslog_server.start)
        trap_proc = Process(target=trap_server.start)
        self._processes = [syslog_proc, trap_proc]

    def start(self):
        for proc in self._processes:
            proc.start()

        for proc in self._processes:
            proc.join()
