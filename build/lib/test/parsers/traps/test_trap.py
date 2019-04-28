from unittest import TestCase, mock
from piat.parsers.traps.trap import TrapMsg

TEST_VARBINDS = {
    '3.6.7.1.1': '4.5.112.3',
    '9.0.4.3.1': '6.5.4.3.2',
    'snmpTrapAddress': '1.1.1.1'
}


class MockVarbind(mock.Mock):

    def __init__(self, var_bind_dict):
        super().__init__()
        self._varbind_dict = var_bind_dict

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self._varbind_dict.keys()):
            raise StopIteration
        keys = list(self._varbind_dict.keys())
        value = self._varbind_dict[keys[self.i]]
        key_index = self.i
        self.i += 1
        return keys[key_index], value


class TestTrapMsg(TestCase):

    @mock.patch.object(TrapMsg, '__init__')
    @mock.patch('piat.parsers.traps.trap.rfc1902')
    def test__parse(self, mock_rfc1902, mock_trap_msg__init__):
        mock_viewer = mock.Mock()
        mock_trap_msg__init__.return_value = None
        TrapMsg._parsed_data = {'snmpTrapAddress': '1.1.1.1'}
        trap = TrapMsg(MockVarbind(TEST_VARBINDS), mock_viewer)
        trap._var_binds = MockVarbind(TEST_VARBINDS)
        trap._viewer = mock_viewer

        trap._parse()
        # test calling refc.ObjectType with right args
        mock_rfc1902.ObjectType.assert_called_with(mock_rfc1902.ObjectIdentity(), '1.1.1.1')
        # test calling .resolveWithMib() with the mib Viewer controller
        mock_rfc1902.ObjectType(mock_rfc1902.ObjectIdentity(), '1.1.1.1').resolveWithMib.assert_called_with(mock_viewer)

    @mock.patch.object(TrapMsg, '__init__')
    @mock.patch.object(TrapMsg, '_parse')
    def test_get_dictionary(self, mock_trap_msg__parse, mock_trap_msg__init__):
        mock_trap_msg__init__.return_value = None

        trap = TrapMsg(None, None)

        result = {'ip': '1.1.1.1', 'test': 'test'}
        trap.result = result

        self.assertEqual(trap.get_dictionary(), result)
