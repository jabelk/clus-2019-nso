# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
import clitable
import textfsm

NET_TEXTFSM = "./templates"

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


    def send_command(self,command,hostname):
        # send command to target device
        out = self.net_connect[hostname].send_command(command)
        print("[INFO] Successfully get output of command<{}> from {}".format(command,hostname))
        print("="*30)
        print(out)
        print("="*30)
        return out


    def check_if_state(self,ifname,hostname, command):
        # check target interface's state
        # return
        #  True  : if the interface is up
        #  False : if the interface is not up
        sh_ip_int_br = self.net_connect[hostname].send_command(command, use_textfsm=True)
        if sh_ip_int_br[0]["status"] == "up":
            return True
        else:
            return False

# sample data for ip int br
# [{'intf': 'GigabitEthernet1', 'ipaddr': '10.0.0.51', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet2', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet2.22', 'ipaddr': '10.0.23.1', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet2.23', 'ipaddr': '10.0.24.1', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet2.33', 'ipaddr': '10.0.34.1', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.1', 'ipaddr': '172.23.42.141', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.10', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.11', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.12', 'ipaddr': '172.23.42.134', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.13', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'}, {'intf': 'GigabitEthernet3.14', 'ipaddr': '172.23.54.131', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.22', 'ipaddr': '10.0.2.2', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.23', 'ipaddr': '10.0.2.2', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet3.33', 'ipaddr': '10.0.2.2', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet4', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'GigabitEthernet5', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'}, {'intf': 'Loopback0', 'ipaddr': '172.23.202.56', 'status': 'up', 'proto': 'up'}]
 

    def commit_configlist(self,config,comment,hostname):
        # commit config to IOS-XR device
        if self.device == "cisco_xr":
            output1 = self.net_connect[hostname].send_config_set(config)
            output2 = self.net_connect[hostname].send_command("show configuration")
            output3 = self.net_connect[hostname].commit(comment=comment)
            output4 = self.net_connect[hostname].exit_config_mode()
            print("[INFO] Successfully change config on {}".format(hostname))
            print("="*30)
            print(output1)
            print(output2)
            print(output3)
            print(output4)
            print("="*30)
        elif self.device == "arista_eos":
            output1 = self.net_connect[hostname].send_config_set(config)
            output2 = self.net_connect[hostname].exit_config_mode()
            print("[INFO] Successfully change config on {}".format(hostname))
            print("="*30)
            print(output1)
            print(output2)
            print("="*30)


    def shutdown_interface(self,ifname,comment,hostname):
        # shutdown interface
        configs = []
        configs.append("interface {}".format(ifname))
        configs.append(' shutdown')
        self.commit_configlist(configs,comment,hostname)
        print("[INFO] Successfully shutdown interface<{}> of {}".format(ifname,hostname))


    def noshutdown_interface(self,ifname,comment,hostname):
        # no shutdown interface
        configs = []
        configs.append("interface {}".format(ifname))
        configs.append(' no shutdown')
        self.commit_configlist(configs,comment,hostname)
        print("[INFO] Successfully unshutdown interface<{}> of {}".format(ifname,hostname))
