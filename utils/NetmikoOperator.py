# -*- coding: utf-8 -*-
# inspired by the example found here: https://github.com/tktkban/rfdemo
from netmiko import ConnectHandler
import clitable
import textfsm

NET_TEXTFSM = "./ntc-templates/templates"

class NetmikoOperator():
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.net_connect = {}
        self.device = ""

    def open_session(self,ip,username,password,device,hostname):
        # open session to target device
        if hostname in self.net_connect:
            pass
        else:
            # make SSH session to router
            handler = {
                'device_type': device,
                'ip': ip,
                'username': username,
                'password': password,
                }
            self.net_connect[hostname] = ConnectHandler(**handler)
            self.device = device
            if self.device == "arista_eos":
                self.net_connect[hostname].enable()
            print("[INFO] Successfully make SSH connection to {}".format(hostname))


    def close_session(self,hostname):
        # close existing session
        self.net_connect[hostname].disconnect()
        del self.net_connect[hostname]
        print("[INFO] Successfully close SSH connection to {}".format(hostname))


    def show_ip_int_br(self,hostname, command):
        sh_ip_int_br = self.net_connect[hostname].send_command(command, use_textfsm=True)
        if sh_ip_int_br[0]["status"] == "up":
            return True
        else:
            return False

# sample data for ip int br
# [{'intf': 'GigabitEthernet1', 'ipaddr': '10.0.0.51', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet2', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet2.22', 'ipaddr': '10.0.23.1', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet2.23', 'ipaddr': '10.0.24.1', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet2.33', 'ipaddr': '10.0.34.1', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.1', 'ipaddr': '172.23.42.141', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.10', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.11', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.12', 'ipaddr': '172.23.42.134', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.13', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'}, {'intf': 'GigabitEthernet3.14', 'ipaddr': '172.23.54.131', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.22', 'ipaddr': '10.0.2.2', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.23', 'ipaddr': '10.0.2.2', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.33', 'ipaddr': '10.0.2.2', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet4', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet5', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'}, {'intf': 'Loopback0', 'ipaddr': '172.23.202.56', 'status': 'up', 'proto': 'up'}]
 