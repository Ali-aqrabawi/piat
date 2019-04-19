from datetime import datetime
import re
from .vendors_descriptors import all_descriptors, default_desc

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

        self.ip = ip

        self._data = data
        self._pri = None
        self._tag = None
        self._msg = None
        self._parse()

        self.facility, self.severity = self.get_facility_severity()
        self.tag = self._tag
        self.message = self._msg
        self.timestamp = datetime.now()

    def _parse(self):
        for field, regex in self.fields.items():
            field_value = re.search(regex, self._data)
            if field_value:
                setattr(self, field, field_value.group(1))

    def get_facility_severity(self):
        if not self._pri:
            return None, None
        pri_bin = bin(int(self._pri))
        severity = int(pri_bin[-3:], base=2)
        facility = int(pri_bin[2:-3], base=2)
        return _FACILITIES.get(facility, 'unknown'), _SEVERITIES.get(severity, 'unknown')

    @classmethod
    def create_msg(cls, ip, data):

        vendor_desc = detect_vendor_from_msg(data)
        if vendor_desc is None:
            return
        cls.fields = vendor_desc['fields']
        return cls(ip, data)

    def get_dictionary(self):
        return {
            'ip': self.ip,
            'timestamp': str(self.timestamp),
            'tag': self.tag,
            'severity': self.severity,
            'facility': self.facility,
            'msg': self.message
        }

# msgs = """
# <187>: 2019 Apr 18 10:57:54 UTC: %AUTHPRIV-3-SYSTEM_MSG: pam_aaa:Authentication failed from 119.29.170.202 - dcos_sshd[14361]
# <187>: 2019 Apr 18 11:00:27 UTC: last message repeated 180 times
# <149>2647599: vmx01 RP/0/RSP1/CPU0:Mar 28 15:08:30.941 UTC: bgp[1051]: %ROUTING-BGP-5-MAXPFX : No. of IPv4 Unicast prefixes received from 1.2.3.4 has reached 94106, max 125000
# <187>94307: gw2.acy1 LC/0/2/CPU0:Jul  7 20:16:14.834 : ifmgr[214]: %PKT_INFRA-LINK-3-UPDOWN : Interface TenGigE0/2/0/4, changed state to Down
# <187>: 2019 Apr 18 11:00:27 UTC: %AUTHPRIV-3-SYSTEM_MSG: pam_aaa:Authentication failed from 104.248.178.100 - dcos_sshd[15056]
# <187>: 2019 Apr 18 11:00:49 UTC: %AUTHPRIV-3-SYSTEM_MSG: pam_aaa:Authentication failed from 111.231.139.30 - dcos_sshd[15125]
# <25>Jun 21 14:03:12  vmx01 eswd[2902]: ESWD_BPDU_BLOCK_ERROR_DISABLED:ge-0/0/17.0: bpdu-block disabled port
# <149>Apr 16 11:04:17 edge01 Rib: %BGP-3-NOTIFICATION: received from neighbor 194.53.172.97 (AS 2611) 6/1 (Cease/maximum number of prefixes reached) 0 bytes
# <87>Jul  5 05:52:44  vmx01 rpd[1848]: bgp_read_message:2764: NOTIFICATION received from 1.2.3.4 (External AS 1234): code 6 (Cease) subcode 5 (Connection Rejected)
# """
# msgs = msgs.splitlines()
# import json
#
# for msg in msgs:
#     if not msg:
#         continue
#     s = SyslogMsg.create_msg('192.168.1.1', msg)
#     if not s:
#         continue
#     print(json.dumps(s.get_dictionary(), indent=4))
#     print("=============================")
