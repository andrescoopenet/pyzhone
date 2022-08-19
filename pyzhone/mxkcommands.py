"""
Commands for MXK Configuration Library
================================================================

This library allows users to send premade commands to configure ONTs on DZN-Zhone's MXK Chassis
"""


from mxktelnet import MXKConfig


class Commands(MXKConfig):
    """This class inherits functions from mxktelnet
    """

    def __init__(self, user='admin', passw='zhone', host='192.168.254.1', port=23, timeout=10):
        super().__init__(user, passw, host, port, timeout)

    def onushow(self, slot, port):
        """Summary:
            Show discovered ont and logicals ports avaibles, in a phisical port (onu show 2/1)
        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
        Returns: 
            Str  : Telnet string

        """
        return self.sendcmdmxk(f'onu show {slot}/{port}')

    def onushowid(self, slot, port, idonu):
        """Summary:
            Show ont configurated in an especific logical port (onu show 2/1/5)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port

        Returns: 
            Str  : Telnet string
        """
        return self.sendcmdmxk(f'onu show {slot}/{port}/{idonu}')

    def wlanshow(self, slot, port, idonu):
        """Summary:
            Show data of WiFi Interfaces (cpe wlan show 3/2/2 showhidden)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port

        Returns: 
            Str : Telnet string
        """
        return self.sendcmdmxk(f'cpe wlan show {slot}/{port}/{idonu} showhidden')

    def onuclear(self, slot, port, idonu):
        """Summary:
            Erease fsan data, but not configuration, use this to replace ONT (onu clear 3/2/8)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port  

        Returns:
            Str : Telnet string

        """
        return self.sendcmdmxk(f'onu clear {slot}/{port}/{idonu}')

    def onuset(self, slot, port, idonu, fsan, model):
        """Summary:
            Set ONT in logical port (onu set 2/3/9 vendorid vendorid ZNTS serno fsan 03A77FAC meprof zhone-2428)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port 
            fsan(Str): ont's serial id
            model(Str): ont's model

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(
            f'onu set {slot}/{port}/{idonu} vendorid ZNTS serno fsan {fsan} meprof zhone-{model}')

    def onusetforeing(self, slot, port, idonu, fsan, model, vendorid):
        """Summary:
            Set ont in logical when ont is from a diferent vendor (onu set 2/3/9 vendorid vendorid DATACOM serno fsan 912F36B9 meprof dm980)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port 
            fsan(Str): ont's serial id
            model(Str): ont's model
            vendorid(Str): ont's vendors setted in mxk

        Returns:
            Str : Telnet string

        """
        return self.sendcmdmxk(
            f'onu set {slot}/{port}/{idonu} vendorid {vendorid} serno fsan {fsan} meprof {model}')

    def bridgeaddpppoe(self, mxk, slot, port, idonu, vlan, gtp, interfaces):
        """Summary:
            Set PPPoE bridge (bridge add 1-2-3-10/gpononu gtp 100 downlink-pppoe vlan 1000 tagged eth [1-4] rg-bpppoe)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port
            vlan(Str): id of vlan for pppoe service
            gtp(Str): gpon traffic profile
            interfaces(Str): tagged interfaces

        Returns: 
            Str : Telnet string

        """

        return self.sendcmdmxk(
            f'bridge add {mxk}-{slot}-{port}-{idonu}/gpononu gtp {gtp} downlink-pppoe vlan {vlan} tagged {interfaces} rg-bpppoe')

    def bridgeaddtls(self, mxk, slot, port, idonu, vlan, gtp, interfaces):
        """Summary:
            Set tls bridge (bridge add 1-2-3-10/gpononu gtp 100 tls vlan 1000 tagged eth [1-4])

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port
            vlan(Str): id of vlan for pppoe service
            gtp(Str): gpon traffic profile
            interfaces(Str): tagged interfaces

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(
            f'bridge add {mxk}-{slot}-{port}-{idonu}/gpononu gtp {gtp} tls vlan {vlan} tagged {interfaces}')

    def bridgeaddmgmt(self, mxk, slot, port, idonu, vlan, gtp):
        """Summary:
            Set management interface (bridge add 1-2-3-10/gpononu gtp 50 downlink-data vlan 800 tagged rg-bridged mgmt)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port
            vlan(Str): id of vlan for pppoe service
            gtp(Str): gpon traffic profile

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(
            f'bridge add {mxk}-{slot}-{port}-{idonu}/gpononu gtp {gtp} downlink-data vlan {vlan} tagged rg-bridged mgmt')

    def bridgeaddvoip(self, mxk, slot, port, idonu, vlan):
        """Summary:
            Set VOIP bridge (bridge add 1-2-3-10/gpononu downlink-voince vlan 123 tagged rg-bridged sip)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port
            vlan(Str): id of vlan for pppoe service

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(
            f'bridge add {mxk}-{slot}-{port}-{idonu}/gpononu downlink-voice vlan {vlan} tagged rg-bridged sip')

    def bridgedelete(self, mxk, slot, port, gemport, interface):
        """Summary:
            Delete bridge (bridge delete 1-2-3-234 eht1)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            gemport(Str): id of bridge port
            interfaces(Str): tagged interfaces

        Returns: 
            Str : Telnet string

        """

        return self.sendcmdmxk(
            f'bridge delete {mxk}-{slot}-{port}-{gemport} {interface}')

    def cpeshow(self, slot, port, idonu):
        """Summary:
            Shows cpe interfaces configuration (cpe show 1/3/2)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(f'cpe show {slot}/{port}/{idonu}')

    def recoveront(self, slot, port, idonu):
        """Summary:
            Reset ont and olt port optical communication (onu recover 3/2/1)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port

        Returns: 
            Str : Telnet string
        """
        return self.sendcmdmxk(f'onu recover {slot}/{port}/{idonu}')

    def wificonfig(self, slot, port, idonu, interface, ssid, passwifi, wlanprofile):
        """Summary:
            Add WLAN interfaces configuration (cpe wlan add 1/2/3/1 admin-state up ssid Wifi-Zhone encrypt-key password123 Profile-WiFi Profile-WiFi)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(
            f'cpe wlan add {slot}/{port}/{idonu}/{interface} admin-state up ssid {ssid} encrypt-key {passwifi} {wlanprofile}')

    def pppoeconfig(self, slot, port, idonu, vlan, userpppoe, passpppoe):
        """Summary:
            Add PPPoE WAN configuration (cpe rg wan modify 2/6/29 vlan 150 pppoe-usr-id testpppoe pppoe-password 1234567890)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port
            vlan(Str): id of vlan for pppoe service
            userpppoe(Str): pppoe user
            passpppoe(Str): pppoe password

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(
            f'cpe rg wan modify {slot}/{port}/{idonu} vlan {vlan} pppoe-usr-id {userpppoe} pppoe-password {passpppoe}')

    def mgmtip(self, slot, port, idonu, vlan, ipaddress):
        """Summary:
            Add MGMT IP Address (cpe rg wan modify 1/2/3 vlan 4 ip-addr 10.0.0.2 ip-com-profile MANAGEMENT)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port
            vlan(Str): id of vlan for pppoe service
            ipaddress(Str): managment ip address

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxkn(
            f'cpe rg wan modify {slot}/{port}/{idonu} vlan {vlan} ip-addr {ipaddress} ip-com-profile MANAGEMENT')

    def wansip(self, slot, port, idonu, vlan, sipcommprofile):
        """Summary:
            Add MGMT IP Address (cpe rg wan modify 1/2/3 vlan 4 ip-addr 10.0.0.2 ip-com-profile MANAGEMENT)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port
            vlan(Str): id of vlan for pppoe service
            ipaddress(Str): managment ip address

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(
            f'cpe rg wan modify {slot}/{port}/{idonu} vlan {vlan} ip-com-profile {sipcommprofile}')

    def sipnumber(self, slot, port, idonu, pot, rxgain, txgain, number, password, voipprofile):
        """Summary:
            Add SIP line number (cpe voip modify 1/1/64/1 rx-gain -7 tx-gain -2 dial-number 100001 username 100001 password 123abc voip-server-profile 1 display-name 100001 description 100001)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port
            pot(Str): number of phisical sip interface
            rxgain(Str): rx gain
            txgain(Str): tx gain
            number(Str): sip line number
            password(Str): sip password
            voipprofile(Str): voip Profile

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(
            f'cpe voip add {slot}/{port}/{idonu}/{pot} rx-gain {rxgain} tx-gain {txgain} dial-number {number} username {number} password {password} voip-server-profile {voipprofile} display-name {number} description {number}')

    def onupower(self, slot, port, idonu):
        """Summary:
            Show onu power (onu power show 1/2/3)


        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port


        Returns: 
            Str : Telnet string
        """
        return self.sendcmdmxk(f'onu power show {slot}/{port}/{idonu}')

    def onustatus(self, slot, port, idonu):
        """Summary:
            Return an specific onu status (onu status 1/2/3)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(f'onu status {slot}/{port}/{idonu}')

    def systemcommons(self, slot, port, idonu, sysprofile):
        """Summary:
            Configure system commons profile, such as admin user and password(cpe system add 1/1/64 sys-common-profile Profile1)

        Args:
            slot(Str): number of card in mxk chassis
            port(Str): number of port in slot
            idonu(Str): id of logical port
            sysprofile(Str): common settings profile

        Returns: 
            Str : Telnet string

        """
        return self.sendcmdmxk(
            f'cpe system add {slot}/{port}/{idonu} sys-common-profile {sysprofile}')

    def logout(self):
        """Summary:
            Logout from mxk console
        """
        self.sendcmdmxk('logout')
