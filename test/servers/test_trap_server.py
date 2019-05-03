import os
from unittest import TestCase, mock
from piat.servers.trap_server import TrapsHandler, SnmpTrapServer


class TestTrapHandler(TestCase):

    @mock.patch('piat.servers.trap_server.ThreadsManager')
    @mock.patch('piat.servers.trap_server.TrapMsg')
    def test_handler(self, mock_TrapMsg, mock_ThreadsManager):
        def cb1():
            return

        def cb2():
            return

        test_callbacks = [cb1, cb2]
        test_viewer = 'testViewer'
        trap_hanlder = TrapsHandler(callbacks=test_callbacks, viewer=test_viewer)
        mock_snmp_engine = mock.Mock(name='snmp_engine')
        mock_state_reference = mock.Mock(name='state_reference')
        mock_context_engine_id = mock.Mock(name='context_engine_id')
        mock_context_name = mock.Mock(name='context_name')
        mock_var_binds = mock.Mock(name='var_binds')
        mock_cb_ctx = mock.Mock(name='cb_ctx')
        trap_hanlder.handle(mock_snmp_engine, mock_state_reference, mock_context_engine_id,
                            mock_context_name, mock_var_binds, mock_cb_ctx)

        mock_TrapMsg.assert_called_with(mock_var_binds, test_viewer)

        expected_calls = []
        for cb in test_callbacks:
            call = mock.call(cb, args=[mock_TrapMsg(), ])
            expected_calls.append(call)
        mock_ThreadsManager().add.assert_has_calls(expected_calls)

        mock_ThreadsManager().start.assert_called_with()


class TestSnmpTrapServer(TestCase):

    def setUp(self):
        def cb1():
            return

        def cb2():
            return

        self.test_callbacks = [cb1, cb2]

    @mock.patch('piat.servers.trap_server.TrapsHandler')
    @mock.patch('piat.servers.trap_server.builder')
    @mock.patch('piat.servers.trap_server.ntfrcv')
    @mock.patch('piat.servers.trap_server.config')
    @mock.patch('piat.servers.trap_server.udp')
    @mock.patch('piat.servers.trap_server.view')
    @mock.patch('piat.servers.trap_server.engine')
    def test__setup(self, mock_engine, mock_view, mock_udp, mock_config, mock_ntfrcv, mock_builder, mock_TrapsHandler):
        self.assertRaises(AssertionError, SnmpTrapServer, 'bad_cb')

        snmp_server = SnmpTrapServer(self.test_callbacks)

        mock_engine.SnmpEngine().getMibBuilder.assert_called_with()

        # mock_engine.SnmpEngine().getMibBuilder().addMibSources.assert_called_with(
        #     mock_builder.DirMibSource(os.environ['PIAT_MIB_PATH']))

        mock_engine.SnmpEngine().getMibBuilder().loadModules.assert_called_with()

        mock_view.MibViewController.assert_called_with(mock_engine.SnmpEngine().getMibBuilder())

        mock_udp.UdpTransport.assert_called_with()

        mock_config.addTransport.assert_called_with(mock_engine.SnmpEngine(),
                                                    mock_udp.domainName + (1,),
                                                    mock_udp.UdpTransport().openServerMode(
                                                        ('0.0.0.0', snmp_server._port)))

        mock_config.addV1System.assert_called_with(mock_engine.SnmpEngine(),
                                                   '????',
                                                   snmp_server._community)

        handler = mock_TrapsHandler(self.test_callbacks,
                                    mock_view.MibViewController(mock_engine.SnmpEngine().getMibBuilder()))

        mock_ntfrcv.NotificationReceiver.assert_called_with(mock_engine.SnmpEngine(), handler.handle)
