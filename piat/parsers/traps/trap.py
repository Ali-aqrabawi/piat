from datetime import datetime
from pysnmp.smi import rfc1902
from piat.utils.logger import get_logger

LOGGER = get_logger(__name__)


class TrapMsg:
    """ Trap msg Object """

    def __init__(self, var_binds, viewer):
        """
        Trap Msg Object.
        :param var_binds: pysnmp var_binds.
        :param viewer: pysnmp MibViewController
        """
        self._var_binds = var_binds
        self._viewer = viewer

        self.timestamp = datetime.now()

        self._parsed_data = {}
        self._parse()

        self.result = {'ip': self._parsed_data['snmpTrapAddress'],
                       'timestamp': self.timestamp, **self._parsed_data}

    def _parse(self):
        """ translate the trap msg with the mib viewer """
        for name, val in self._var_binds:
            var_bind = rfc1902.ObjectType(rfc1902.ObjectIdentity(name), val)
            var_bind.resolveWithMib(self._viewer)
            obj_name = var_bind[0].getMibSymbol()[1]
            value = var_bind[1].prettyPrint()
            self._parsed_data[obj_name] = value

    def get_dictionary(self):
        return self.result
