#! /usr/bin/env python

import os
import sys
import argparse
import logging
from utils.nso_lib import get_devs, NetDev, create_csv_list_of_tuples
import ncs
from functools import partial
# Check for module dependencies:
not_installed_modules = []


try:
    from prettytable import PrettyTable
except ImportError:
    not_installed_modules.append('prettytable')


try:
    import yaml
except ImportError:
    not_installed_modules.append('PyYAML')

try:
    from consolemenu import ConsoleMenu
    from consolemenu.items import FunctionItem
except ImportError:
    not_installed_modules.append('console-menu')


if not_installed_modules:
    print("Please install following Python modules:")

    for module in not_installed_modules:
        print("  - {module}".format(module=module))

    sys.exit(1)

def submain(args):

    def get_device_list():
        device_list = get_devs()
        for device in device_list:
            net_dev = NetDev(device)
            print("Device {} and os type {}".format(net_dev.name, net_dev.os_type))
        user_input = input('Press enter to return to menu... ')

    def check_ip_in_acl():
        print("\n\nEver Have the problem, \nWhere is the IP in the midst of all your ACLs?")
        print("For example, \n\ncsr1#show run | i 91.118.192.128\n  permit 91.118.192.128\ncsr1#\n\n")
        user_input = input('Enter an IP Address to Check in the Extended ACLs (default is 91.118.192.128), good choices for Nexus (10.246.84.201 or 10.246.84.201):  ') or "91.118.192.128"
        device_list = get_devs()
        csv_header = ["ACL Name", "ACL Rule"]
        type_of_audit = "acl"
        for device in device_list:
            nso_device = NetDev(device)
            nso_device.find_ip_access_list(user_input)
            if nso_device.acl_answer == []:
                print("The IP address {} was not found in {}".format(user_input, device))
                continue
            print("Creating CSV for Audit Output for Device {}".format(device))
            # print(nso_device.acl_answer)
            create_csv_list_of_tuples(nso_device.acl_answer, csv_header, device, type_of_audit)
        user_input = input('Press enter to return to menu... ')

    def interface_t_shoot():
        print("\n\nEver Have the problem, \nWhere is the IP in the midst of all your Interfaces?")
        print("For example, \n\ncsr1#show run | i 10.0.0.51\nip address 10.0.0.51 255.255.255.0\ncsr1#\n\n")
        print("Of course you could just read through the inteface config like this:"+ 
        "\ncsr1#show run int gig 1\nBuilding configuration...\nCurrent configuration : 145 bytes"+
            "\n!\ninterface GigabitEthernet1\n vrf forwarding MANAGEMENT\n ip address 10.0.0.51 255.255.255.0\n"+
                " negotiation auto\n no mop enabled\n no mop sysid\nend\n\n")
        print("\n\n But what about across many devices?")
        user_input = input('Enter one, or many IP Address(es) to Check in the Extended ACLs (default is 10.0.0.51), also try 10.0.0.52, 10.0.0.53, 10.0.0.71, 10.0.0.72:  ') or "10.0.0.51"
        device_list = get_devs()
        csv_header = ["Interface Type", "Interface Name"]
        type_of_audit = "interface"
        for device in device_list:
            nso_device = NetDev(device)
            list_of_tup_ints = nso_device.view(partial(nso_device.get_ip_ints, ip=user_input))
            # print(list_of_tup_ints)
            if list_of_tup_ints == [[]]:
                print("The IP address {} was not found in {}".format(user_input, device))
                continue
            print("Creating CSV for Audit Output for Device {}".format(device))
            create_csv_list_of_tuples(list_of_tup_ints, csv_header, device, type_of_audit)
        user_input = input('Press enter to return to menu... ')

    def show_menu():
        menu = ConsoleMenu("NTC NSO Demo Menu", "Choose an Option Below")

        menu_items = [
            ("View All Devices", get_device_list),
            ("Audit All ACLs from Input", check_ip_in_acl),
            ("Audit Interfaces for an IP Address", interface_t_shoot)
        ]

        for item in menu_items:
            menu.append_item(FunctionItem(item[0], item[1]))

        menu.show()

    show_menu()


def main(argv=None):
    parser = argparse.ArgumentParser()
    named_args = parser.add_argument_group('Named arguments')
    named_args.add_argument('-v', '--verbose',
                                default=False, action="store_true",
                                required=False)
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)

    submain(args)



if __name__ == '__main__':
    main()