from unittest import TestCase, mock
from piat.servers.syslog_server import _SyslogHandler, SyslogServer


class TestSyslogHanlder(TestCase):

    @mock.patch('piat.servers.syslog_server.ThreadsManager')
    @mock.patch('piat.servers.syslog_server.SyslogMsg')
    @mock.patch('piat.servers.syslog_server.socketserver.BaseRequestHandler')
    def test_handel(self, mock_BaseRequestHandler, mock_SyslogMsg, mock_ThreadsManager):
        _SyslogHandler.callbacks = ['cb1', 'cb2']
        handler = _SyslogHandler([b"raw byte packet", ], ('1.1.1.1', 8000), None)

        mock_SyslogMsg.create_msg.assert_called_with('1.1.1.1', "raw byte packet")
        mock_ThreadsManager.assert_called_with()

        expected_calls = []
        for callback in handler.callbacks:
            call = mock.call(callback, args=[mock_SyslogMsg.create_msg()])
            expected_calls.append(call)
        mock_ThreadsManager().add.assert_has_calls(expected_calls)


class TestSyslogServer(TestCase):
    @mock.patch('piat.servers.syslog_server.LOGGER')
    @mock.patch('piat.servers.syslog_server.socketserver')
    def test__setup(self, mock_socketserver, mock_LOGGER):
        self.assertRaises(AssertionError, SyslogServer, 'callback')

        def cb1():
            return

        def cb2():
            return

        s = SyslogServer([cb1, cb2])

        self.assertEqual(s._port, 514)

        mock_LOGGER.info.assert_called_with("registered ['cb1', 'cb2'] callbacks to Syslog server")
        mock_socketserver.UDPServer.assert_called_with(('0.0.0.0', 514), _SyslogHandler)
