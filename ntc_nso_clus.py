#! /usr/bin/env python

import os
import sys
import argparse
import logging
from utils.nso_lib import get_devs, NetDev, create_csv_list_of_tuples, create_csv_list_of_dicts
import ncs
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
        print(device_list)
        user_input = input('Press enter to return to menu... ')

    def check_ip_in_acl():
        print("\n\nEver Have the problem, \nWhere is the IP in the midst of all your ACLs?")
        print("For example, \n\ncsr1#show run | i 91.118.192.128\n  permit 91.118.192.128\ncsr1#\n\n")
        user_input = input('Enter an IP Address to Check in the Extended ACLs (default is 91.118.192.128):  ') or "91.118.192.128"
        device_list = get_devs()
        for device in device_list:
            nso_device = NetDev(device)
            nso_device.find_ip_access_list(user_input, device)
            print("Creating CSV for Audit Output for Device {}".format(device))
            create_csv_list_of_dicts(nso_device.acl_answer, device)
        user_input = input('Press enter to return to menu... ')

    def interface_t_shoot():
        device_list = get_devs()
        csv_header = ["Interface Type", "Interface Name"]
        for device in device_list:
            nso_device = NetDev(device)
            list_of_tup_ints = nso_device.ints
            print(list_of_tup_ints)
            create_csv_list_of_tuples(list_of_tup_ints, csv_header, device)
        user_input = input('Press enter to return to menu... ')

    def show_menu():
        menu = ConsoleMenu("NTC NSO Demo Menu", "Choose an Option Below")

        menu_items = [
            ("View All Devices", get_device_list),
            ("Audit All ACLs from Input", check_ip_in_acl),
            ("Audit Interfaces", interface_t_shoot)
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