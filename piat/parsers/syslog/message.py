from datetime import datetime
import re
from piat.utils.logger import get_logger
from .vendors_descriptors import all_descriptors, default_desc

LOGGER = get_logger(__name__)

_SEVERITIES = {
    0: 'emergency',
    1: 'alert',
    2: 'critical',
    3: 'error',
    4: 'warning',
    5: 'notice',
    6: 'informational',
    7: 'debug'
}

_FACILITIES = {
    0: 'kernel',
    1: 'user',
    2: 'mail',
    3: 'daemon',
    4: 'auth',
    5: 'syslogd',
    6: 'line_printer',
    7: 'news',
    8: 'uucp',
    9: 'cron',
    10: 'authpriv',
    11: 'ftp',
    12: 'ntp',
    13: 'audit',
    14: 'alert',
    15: 'clock',
    16: 'local0',
    17: 'local1',
    18: 'local2',
    19: 'local3',
    20: 'local4',
    21: 'local5',
    22: 'local6',
    23: 'local7'
}


def detect_vendor_from_msg(msg):
    for desc in all_descriptors:
        desc_match = re.search(desc['sig'], msg)
        if desc_match:
            return desc
    return default_desc


class SyslogMsg:
    fields = {}

    def __init__(self, ip, data):
        """
        syslog Msg Object.
        :param ip: string
        :param data: string: raw packet data
        """

        self.ip = ip

        self._data = data
        self._pri = None
        self._tag = None
        self._msg = None
        self._parse()

        self.facility, self.severity = self._get_facility_severity()
        self.tag = self._tag
        self.message = self._msg
        self.timestamp = datetime.now()

    def _parse(self):
        """ pasre the syslog msg """
        for field, regex in self.fields.items():
            field_value = re.search(regex, self._data)
            if field_value:
                setattr(self, field, field_value.group(1))
            else:
                LOGGER.error(
                    "failed to parse field: %r regex: %r, source: %r, data: %s" % (field, regex, self.ip, self._data)
                )

    def _get_facility_severity(self):
        """ exttact facility and serverity from self._pri """
        if not self._pri:
            LOGGER.error("failed to parse pri field from syslog message, source: %r, data: %s" % (self.ip, self._data)
                         )
            return None, None
        pri_bin = bin(int(self._pri))
        severity = int(pri_bin[-3:], base=2)
        facility = int(pri_bin[2:-3], base=2)
        return _FACILITIES.get(facility, 'unknown'), _SEVERITIES.get(severity, 'unknown')

    @classmethod
    def create_msg(cls, ip, data):
        """
        class method to create a Syslog Msh based on the source msg vendor.
        :param ip: str
        :param data: str: raw packet data
        :return:
        """

        vendor_desc = detect_vendor_from_msg(data)
        if vendor_desc is None:
            LOGGER.error("failed to detect source syslog msg vendor, source: %r, data: %s" % (ip, data)
                         )
            return None
        cls.fields = vendor_desc['fields']
        return cls(ip, data)

    def get_dictionary(self):
        return {
            'ip': self.ip,
            'timestamp': self.timestamp,
            'tag': self.tag,
            'severity': self.severity,
            'facility': self.facility,
            'msg': self.message
        }
