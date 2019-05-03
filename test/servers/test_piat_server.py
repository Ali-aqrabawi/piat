from unittest import TestCase, mock
from piat.servers.piat_server import PiatServer


class TestPiatServer(TestCase):

    @mock.patch('piat.servers.piat_server.Process')
    @mock.patch('piat.servers.piat_server.SnmpTrapServer')
    @mock.patch('piat.servers.piat_server.SyslogServer')
    def test__setup(self, mock_syslog_server, mock_snmp_trap_server, mock_process):
        s = PiatServer([], [])

        mock_syslog_server.assert_called_with([], 514)
        mock_snmp_trap_server.assert_called_with([], 'public', 162, '')

        calls = [mock.call(target=mock_syslog_server().start),
                 mock.call(target=mock_snmp_trap_server().start)]
        mock_process.assert_has_calls(calls)

        self.assertEqual(len(s._processes), 2)
        self.assertIsInstance(s._processes, list)

    @mock.patch('piat.servers.piat_server.Process')
    @mock.patch('piat.servers.piat_server.SnmpTrapServer')
    @mock.patch('piat.servers.piat_server.SyslogServer')
    def test_start(self, mock_syslog_server, mock_snmp_trap_server, mock_process):
        s = PiatServer([], [])
        s.start()

        for proc in s._processes:
            proc.start.assert_called_with()
            proc.join.assert_called_with()
