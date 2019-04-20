from pysnmp.smi import rfc1902
from datetime import datetime


class TrapMsg:
    def __init__(self, var_binds, viewer):
        self._var_binds = var_binds
        self._viewer = viewer

        self.timestamp = datetime.now()

        self._parsed_data = {}
        self._parse()

        self.result = {'ip': self.snmpTrapAddress, 'timestamp': str(self.timestamp), **self._parsed_data}

    def _parse(self):
        for name, val in self._var_binds:
            symbol = rfc1902.ObjectIdentity(name).resolveWithMib(self._viewer).getMibSymbol()
            # val = rfc1902.ObjectIdentity(val).resolveWithMib(viewer)
            self._parsed_data[symbol[1]] = val.prettyPrint()
            setattr(self, symbol[1], val.prettyPrint())

    def get_dictionary(self):
        return self.result
