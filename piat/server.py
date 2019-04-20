from multiprocessing import Process
from piat.listeners import syslog_listener, trap_listener


class SyslogServer:
    pass


class TrapServer:
    pass


class PiatServer:
    """
    PiatServer is the Server that manages and run both Syslog and trap services,
    each service will be running as a independent process.
    """

    def __init__(self,
                 syslog_callbacks,
                 traps_callbacks,
                 syslog_port=514,
                 trap_port=161,
                 trap_community='public',
                 enable_trap_service=True,
                 enable_syslog_service=True):

        self._syslog_callbacks = syslog_callbacks
        self._traps_callbacks = traps_callbacks
        self._syslog_port = syslog_port
        self._trap_port = trap_port
        self._trap_community = trap_community
        self._enable_trap_service = enable_trap_service
        self._enable_syslog_service = enable_syslog_service
        self._processes = []

        self._create_processes()

    def _create_processes(self):
        syslog_proc = Process(target=syslog_listener.run, args=[self._syslog_callbacks, self._syslog_port])
        trap_proc = Process(target=trap_listener.run,
                            args=[self._traps_callbacks, self._trap_community, self._trap_port])
        self._processes = [syslog_proc, trap_proc]

    def start(self):
        for proc in self._processes:
            proc.start()

        for proc in self._processes:
            proc.join()
