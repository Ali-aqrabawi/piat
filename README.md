# Piat Project
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/piat.svg)
![PyPI](https://img.shields.io/pypi/v/piat.svg)
![PyPI - Status](https://img.shields.io/pypi/status/piat.svg)
![PyPI - License](https://img.shields.io/pypi/l/piat.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5d3fa6d31e37482c8cf95036816f7397)](https://app.codacy.com/app/Ali-aqrabawi/piat?utm_source=github.com&utm_medium=referral&utm_content=Ali-aqrabawi/piat&utm_campaign=Badge_Grade_Dashboard)


Piat is a syslog and trap listeners APIs which are easy to use,
it support syslog parsing for multiple vendors

### Installing

   `pip install piat`

### Getting Started

#### Example 1:

to run both listeners/servers use the PiatServer API:

    from piat.servers import PiatServer

    def syslog_cb(syslog_msg):
        """ callback to be executed on received syslog msg """
        data = syslog_msg.get_dictionary()
        # do something with syslog data
        print(data)

    def trap_cb(trap_msg):
        """ callback to be executed on received trap msg """
        data = trap_msg.get_dictionary()
        # do something with trap data
        print(data)

    if __name__ == '__main__':
        server = PiatServer(traps_callbacks=[trap_cb],
                            syslog_callbacks=[syslog_cb],
                            trap_community='my_community')
        server.start()

syslog data example :

    {'ip': '192.168.1.1',
     'timestamp': 
     '2019-04-28 21:26:40.809271',
     'tag': 'LSD-4-LABEL_RESOURCE',
     'severity': 'warning',
     'facility': 'syslogd',
      'msg': 'label range 100-150 exhausted'}
       
    {'ip': '192.168.1.9',
     'timestamp': '2019-04-28 21:26:41.741839',
     'tag': 'SYS-6-LOGGINGHOST_STARTSTOP',
     'severity': 'informational',
     'facility': 'syslogd',
     'msg': 'Logging to host 192.1.1.8 port 514 started - CLI initiated'}


trap data example :

    {'ip': '192.168.1.1',
     'timestamp': '2019-04-28 21:30:11.536344',
     'sysUpTime': '88847929',
     'snmpTrapOID': 'CISCO-SMI::cisco.0.1',
     'snmpTrapAddress': '192.168.1.1',
     'snmpTrapCommunity': 'public',
     'snmpTrapEnterprise': 'CISCO-SMI::cisco',
     'local': 'root',
     'tcpConnState': 'finWait2'}
     
    {'ip': '192.168.1.9',
     'timestamp': '2019-04-28 21:30:11.544577',
     'sysUpTime': '88847996',
     'snmpTrapOID': 'CISCO-SYSLOG-MIB::clogMessageGenerated',
     'snmpTrapAddress': '192.168.1.9',
     'snmpTrapCommunity': 'public',
     'snmpTrapEnterprise': 'CISCO-SYSLOG-MIB::ciscoSyslogMIBNotificationPrefix',
     'clogHistFacility': 'LSD',
     'clogHistSeverity': 'warning',
     'clogHistMsgName': 'LABEL_RESOURCE',
     'clogHistMsgText': 'label range 100-150 exhausted',
     'clogHistTimestamp': '88847996'}

#### Example 2:
to run only syslog server:

    from piat.servers import SyslogServer

    def syslog_cb(syslog_msg):
        data = syslog_msg.get_dictionary()
        print(data)
        # do something with syslog data
        
    if __name__ == '__main__':
        server = SyslogServer(callbacks=[syslog_cb])
        server.start()


also you can run only trap server:

    from piat.servers import SnmpTrapServer
    
    def trap_cb(trap_msg):
        data = trap_msg.get_dictionary()
        # do something with trap data
        print(data)
        
    if __name__ == '__main__':
        server = SnmpTrapServer(callbacks=[trap_cb],community='my_comm')
        server.start()

#### Supported Vendors:
1) Cisco.
2) Arista.:
3) Juniper.
4) Huawei.
5) HP.
6) F5.
7) Fortinet.

#### Features:
1) you can pass as many callback as you want, all callbacks will be running concurrently
in separate threads.
2) both syslog and trap will be running as an independent process.
3) you can add more mib dir to be used by the trap server, use `add_mib_dir` kwarg 
to pass the mib dir location.
4) Piat uses `pysnmp` for trap listening, so if you want to extend the mib support you
need to combile the mib files using `mibdump.py` command provided by `pysnmp` to combile
the new mibs, then add the compiled mibs dir to piat server using `add_mib_dir`.
5) we only support Syslog parsing described by [rfc3164](https://tools.ietf.org/html/rfc3164).