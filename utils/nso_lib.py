import ncs
import logging
import csv

def get_devs():
    device_list = []
    with ncs.maapi.single_read_trans('admin', 'python', groups=['ncsadmin']) as t:
        root = ncs.maagic.get_root(t)
        for netdev in root.devices.device:
            device_list.append(netdev.name)
    return device_list

def get_os_type (devicename):
    with ncs.maapi.single_read_trans('admin', 'python', groups=['ncsadmin']) as t:
     root = ncs.maagic.get_root(t)
     os_type = root.devices.device[devicename].platform.name
     return os_type

def find_ip_access_list(ip):
    """
    Single search to see if a provided IP address
    is present inside any of a devices extended ACLs.
    """
    acl_answer = []
    with ncs.maapi.single_read_trans('admin', 'python', groups=['ncsadmin']) as t:
        root = ncs.maagic.get_root(t)
        for box in root.devices.device:
            print("checking Standard Access Lists for " + str(box.name))
            if get_os_type(devicename) == "ios-xe": 
                for acl in root.devices.device[box.name].config.ios_ip.access_list.standard.std_named_acl:
                    print("checking ip access-list standard " + str(acl.name))
                    for rule in root.devices.device[box.name].config.ios_ip.access_list.standard.std_named_acl[acl.name].std_access_list_rule:
                        if ip in rule.rule:
                            print(ip + " Is in acl " + str(acl.name))
                            acl_answer.append({"name":str(acl.name),"rule":rule.rule})
                print("checking Extended Access Lists for " + str(box.name))
                for acl in root.devices.device[box.name].config.ios_ip.access_list.extended.ext_named_acl:
                    print("checking ip access-list extended " + str(acl.name))
                    for rule in root.devices.device[box.name].config.ios_ip.access_list.extended.ext_named_acl[acl.name].ext_access_list_rule:
                        if ip in rule.rule:
                            print(ip + " Is in acl " + str(acl.name))
                            acl_answer.append({"name":str(acl.name),"rule":rule.rule})
            if get_os_type(devicename) == "NX-OS": 
                for acl in root.devices.device[box.name].config.nx__ip.access_list.list_name:
                    print("checking ip access-list " + str(acl.id))
                    for sequence in acl.sequence:
                        print("{} {} {} {} {}".format(str(sequence.id), str(sequence.action),str(sequence.source.address_and_prefix), 
                            str(sequence.address_and_prefix), 
                            str(sequence.protocol)))
    return acl_answer


def create_csv_list_of_dicts(listofdicts_tocsv):
    headers = listofdicts_tocsv[0].keys()
    with open('csv_archive/acl_audit.csv','w') as f:
        w = csv.DictWriter(f,headers)
        w.writeheader()
        w.writerows( listofdicts_tocsv)    

def create_csv_list_of_tuples(listoftuples_tocsv, headers, device):
    with open('csv_archive/interface_audit_{}.csv'.format(device),'w') as f:
        w = csv.writer(f,headers)
        w.writerow(headers)
        for line in listoftuples_tocsv:
            w.writerow(line)    

class NetDev:

    def __init__(self, name):
        self.name = name
        self.get_os_type(self.name)
        # ios-xe, NX-OS common optoins
        #self.chg(partial(self.chg_admin_state, state="unlocked"))

        #self.check_sync()
        self.view(#self.fetch_ssh_keys,
                  self.get_ints,
                  self.get_lines)


    def get_os_type ():
        with ncs.maapi.single_read_trans('admin', 'python', groups=['ncsadmin']) as t:
            root = ncs.maagic.get_root(t)
            self.os_type = root.devices.device[self.name].platform.name
        return os_type

    def find_ip_access_list(self, ip, device_name):
        """
        Single search to see if a provided IP address
        is present inside any of a devices extended ACLs.
        acl_answer is list of dicts with keys name and rule
        """
        self.acl_answer = []
# /devices/device[name='nxos-spine1']/config/nx:ip/access-list/list-name[id='nexus-dc-customer-1-emear-location']/sequence[id='10']/source/address-and-prefix 10.246.84.201/23
# /devices/device[name='nxos-spine1']/config/nx:ip/access-list/list-name[id='standard']/sequence[id='10']/any
# /devices/device[name='nxos-spine1']/config/nx:ip/access-list/list-name[id='standard']/sequence[id='10']/established
# /devices/device[name='nxos-spine1']/config/nx:ip/access-list/list-name[id='standard']/sequence[id='20']/action permit
# /devices/device[name='nxos-spine1']/config/nx:ip/access-list/list-name[id='standard']/sequence[id='20']/protocol icmp
# /devices/device[name='nxos-spine1']/config/nx:ip/access-list/list-name[id='standard']/sequence[id='20']/source/address-and-prefix 10.246.66.255/19
        with ncs.maapi.single_read_trans('admin', 'python', groups=['ncsadmin']) as t:
            root = ncs.maagic.get_root(t)
            print("checking Standard Access Lists for " + str(device_name))
            for acl in root.devices.device[device_name].config.ios_ip.access_list.standard.std_named_acl:
                print("checking ip access-list standard " + str(acl.name))
                for rule in root.devices.device[device_name].config.ios_ip.access_list.standard.std_named_acl[acl.name].std_access_list_rule:
                    if ip in rule.rule:
                        print(ip + " Is in acl " + str(acl.name))
                        self.append({"Device Name": str(device_name), "ACL name":str(acl.name),"rule in ACL":rule.rule})
            print("checking Extended Access Lists for " + str(device_name))
            for acl in root.devices.device[device_name].config.ios_ip.access_list.extended.ext_named_acl:
                print("checking ip access-list extended " + str(acl.name))
                for rule in root.devices.device[device_name].config.ios_ip.access_list.extended.ext_named_acl[acl.name].ext_access_list_rule:
                    if ip in rule.rule:
                        print(ip + " Is in acl " + str(acl.name))
                        self.append({"Device Name": str(device_name), "ACL name":str(acl.name),"rule in ACL":rule.rule})
        

    def view(self,*args):
        output_list = []
        with ncs.maapi.single_read_trans('admin', 'python') as trans:
            root = ncs.maagic.get_root(trans)
            device_cdb = root.devices.device[self.name]
            for func in args:
                output = func(device_cdb=device_cdb)
                if output != None:
                    output_list.append(output)
            return output_list


    def chg(self,*args):
        with ncs.maapi.single_write_trans('admin', 'python') as trans:
            root = ncs.maagic.get_root(trans)
            device_cdb = root.devices.device[self.name]
            for func in args:
                func(device_cdb=device_cdb)
            trans.apply()


    def send_cli_cmd(self,*args):
        """
        Sends a CLI commands to a device through NSO and get back a list of tuples in the following format:
        (commandA,[outputA_line1,outputA_line2],commandB,[outputB_line1,outputB_line2])
        """
        output_dict = {}
        try:
            with ncs.maapi.Maapi() as m:
                with ncs.maapi.Session(m, 'admin', 'python'):
                    root = ncs.maagic.get_root(m)
                    device = root.devices.device[self.name]
                    if self.os_type == "ios-xe":
                        input1 = device.live_status.ios_stats__exec.any.get_input()
                    if self.os_type == "NX-OS":   
                        input1 = device.live_status.nx_stats__exec.any.get_input()
                    for command in args:
                        if command != "":
                            input1.args = [command]
                            if self.os_type == "ios-xe":
                                output = device.live_status.ios_stats__exec.any(input1).result
                            if self.os_type == "NX-OS":   
                                output = device.live_status.nx_stats__exec.any(input1).result
                            outlist = output.split("\r\n")[1:-1]
                            output_dict[command] = outlist
                        else:
                            input1.args = ["show clock"]
                            output = device.live_status.ios_stats__exec.any(input1).result
                            outlist = [output.split("\r\n")[-1]]
                            output_dict["PROMPT"] =  outlist
        except:
            output_dict["ERROR"] = ["NSO could not SSH to device {}.".format(self.name)]
        return output_dict


    def lock(self, device_cdb):
        device_cdb.state.admin_state = "locked"


    def fetch_ssh_keys(self, device_cdb):
        device_cdb.ssh.fetch_host_keys()


    def check_sync(self):
        if not self.in_sync():
            self.chg(self.sync_from)


    def sync_from(self, device_cdb):
        device_cdb.sync_from()


    def in_sync(self):
        with ncs.maapi.Maapi() as m:
            with ncs.maapi.Session(m, 'admin', 'python', groups=['ncsadmin']):
                root = ncs.maagic.get_root(m)
                output = root.devices.device[self.name].check_sync()
        if output.result.string == "in-sync":
            return True
        elif output.result.string == "out-of-sync":
            return False
        else:
            return False


    def get_ints_of_type(self, int_type, device_cdb):
        """
        Gets a full list of a single type of interfaces.
        """
        int_list = []
        try:
            for interface in device_cdb.config.ios__interface[int_type]:
                if hasattr(interface, 'name'):
                    int_tuple = (int_type,interface.name)
                    int_list.append(int_tuple)
            return int_list
        except:
            return []


    def get_ints(self, device_cdb):
        """
        Returns a full list of all present interfaces on a device in tuple form (int_type,int_num).
        Example  [("GigabitEthernet","1/1"),("TenGigabitEthernet","1/2")]
        """
        int_type_list = []
        self.ints=[]
        try:
            for interface in device_cdb.config.ios__interface:
                int_type_list.append(interface[4:])
            int_type_list = list(set(int_type_list))
            for int_type in int_type_list:
                results = self.get_ints_of_type(int_type=int_type, device_cdb=device_cdb)
                self.ints.extend(results)
        except:
            self.ints = []


    def get_lines_of_type(self, line_type, device_cdb):
        """
        Gets a full list of a single type of line.
        self.view(partial(self.whatever_method,param1=(blah,blah))
        """
        line_list=[]
        try:
            for line in device_cdb.config.ios__line[line_type]:
                if hasattr(line, 'first') and not hasattr(line, 'last'):
                    line_tuple = (line_type, str(line.first))
                    line_list.append(line_tuple)
                elif hasattr(line, 'first') and hasattr(line, 'last'):
                    line_tuple = (line_type, int(line.first), line.last)
                    line_list.append(line_tuple)
            return line_list
        except:
            return []


    def get_lines(self, device_cdb):
        """
        Returns a full list of all present lines on a device in tuple form (line_type_type,first_line,last_line).
        Example  [("aux",0),("vty",0,4)]
        self.view(self.whatever_method)
        """
        line_type_list = []
        self.lines=[]
        try:
            for line in device_cdb.config.ios__line:
                line_type_list.append(line[4:])
            line_type_list = list(set(line_type_list))
            for line_type in line_type_list:
                results = self.get_lines_of_type(line_type=line_type, device_cdb=device_cdb)
                self.lines.extend(results)
        except:
            self.lines = []


    def has_ip(self, interface_tuple, device_cdb, ip=""):
        """
        Checks if an interface has an ip or if given, a particular IP.  Returns booleen True/False
        self.view(partial(self.whatever_method,param1=(blah,blah))
        """
        try:
            int_type,int_num = interface_tuple
            interface = device_cdb.config.ios__interface[int_type][int_num]
            if interface.ip.address.primary.address and not ip:
                return True
            elif interface.ip.address.primary.address == ip:
                return True
            else:
                return False
        except:
            return False


    def get_ip(self, interface_tuple, device_cdb):
        """
        Returns the IP assigned to a provided interface or "" if one doesn't exist.
        self.view(partial(self.whatever_method,param1=(blah,blah))
        """
        try:
            int_type, int_num = interface_tuple
            interface = device_cdb.config.ios__interface[int_type][int_num]
            if interface.ip.address.primary.address:
                return interface.ip.address.primary.address
            else:
                return ""
        except:
            return ""


    def get_ip_ints(self, device_cdb, ip=""):
        """
        Returns a full list of all present interfaces on a device with IP addresses in tuple form (int_type,int_num).
        Example  [("Vlan","310"),("Loopback","0")]
        It also can look for the iped interface with a given IP address.
        self.view(partial(self.whatever_method,param1=(blah,blah))
        """
        iped_int_list = []
        for int in self.ints:
            if self.has_ip(int, ip=ip, device_cdb=device_cdb):
                iped_int_list.append(int)
        return iped_int_list


    def get_admin_state(self, device_cdb):
        """
        self.view(self.whatever_method)
        """
        return device_cdb.state.admin_state.string


    def chg_admin_state(self, device_cdb, state):
        """
        self.view(self.whatever_method)
        self.chg(partial(self.whatever_method,param1=(blah,blah))
        """
        if state == "locked":
            device_cdb.state.admin_state = "locked"
        elif state == "unlocked":
            device_cdb.state.admin_state = "unlocked"