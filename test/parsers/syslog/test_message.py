from unittest import TestCase

TEST_MSGS_CASE1 = {
    'cisco': '<187>: 2019 Apr 18 10:57:54 UTC: %AUTHPRIV-3-SYSTEM_MSG: pam_aaa:Authentication failed from 119.29.170.202 - dcos_sshd[14361]',
    'juniper': '<25>Jun 21 14:03:12  vmx01 eswd[2902]: ESWD_BPDU_BLOCK_ERROR_DISABLED:ge-0/0/17.0: bpdu-block disabled port',
    'default': '<87> Hello this is rabish',
    'fortinet': '<45>date=2019-04-22.time=07:41:15.devname=lab40-fw.devid=FGT90E4Q16000537.logid=0001000014.type=traffic.subtype=local.level=notice.vd=root.srcip=94.249.4.30.srcport=49896.srcintf="wan1".dstip=162.221.4.105.dstport=443.dstintf="root".sessionid=65340489.proto=6.action=close.policyid=0.policytype=local-in-policy.dstcountry="United.States".srccountry="Jordan".trandisp=noop.service="HTTPS".app="Web.Management(HTTPS)".duration=2.sentbyte=880.rcvdbyte=353.sentpkt=6.rcvdpkt=4.appcat="unscanned".devtype="Other.Network.Device".mastersrcmac=00:78:88:e2:35:57.srcmac=00:78:88:e2:35:5',
    'f5': '<11>Sep 16 13:18:21 bigip1 notice tmm1[18901]: 013e0001:5: Tcpdump starting bcast on 127.1.1.2:2 from 127.1.1.254:35727',
    'huawei': '<11>2009-5-21 19:46:52 Switch %%01CMD/4/REBOOT(l):The user chose N when deciding whether to reboot the system.',
    'hp': '<14> Jan 1 00:15:35 HP-2910al-24G 00076 ports: port 2 is now on-line'
}

TEST_MSGS_CASE2 = {
    'cisco': '<149>2647599: vmx01 RP/0/RSP1/CPU0:Mar 28 15:08:30.941 UTC: bgp[1051]: %ROUTING-BGP-5-MAXPFX : No. of IPv4 Unicast prefixes received from 1.2.3.4 has reached 94106, max 125000',
    'juniper': '<87>Jul  5 05:52:44  vmx01 rpd[1848]: bgp_read_message:2764: NOTIFICATION received from 1.2.3.4 (External AS 1234): code 6 (Cease) subcode 5 (Connection Rejected)',
    'default': '<87> Hi There',
    'f5': '<11>Sep 16 13:18:38 bigip1 notice mcpd[5480]: 01070727:5: Pool /Common/http_pool member /Common/my_node_110:80 monitor status up. [ /Common/http: up ]  [ was unchecked for 0hr:0min:38sec ]',
    'huawei': '<14> Aug 6 2011 20:34:46 HUAWEI %% 01HWCM/5/EXIT(l)[1]: exit from configure mode',
    'hp': '<14> Jan 1 00:15:35 HP-2910al-24G 00076 vlan: no vlan like 1'
}


class TestDetectVendorMessage(TestCase):

    def test_detect_vendor_from_msg(self):
        from piat.parsers.syslog.message import detect_vendor_from_msg
        for case in [TEST_MSGS_CASE1,TEST_MSGS_CASE2]:
            for vendor, msg in case.items():
                result = detect_vendor_from_msg(msg)
                self.assertEqual(result['name'],vendor,msg='detect_vendor_from_msg not detecting correct vendor msg')


