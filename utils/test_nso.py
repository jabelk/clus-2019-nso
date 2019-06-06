import ncs

def check_sync(nso_devicename):
    with ncs.maapi.single_read_trans('admin', 'python', groups=['ncsadmin']) as t:
        root = ncs.maagic.get_root(t)
        output = root.devices.device[nso_devicename].check_sync()
        if output.result.string == "in-sync":
            return True
        elif output.result.string == "out-of-sync":
            return False
        else:
            return False

def send_cli_cmd(nso_devicename,command=None):
    """
    Sends a CLI command directly to a device and returns its output as a new line separated list.
    """
    try:
        if command:
            with ncs.maapi.single_read_trans('admin', 'python', groups=['ncsadmin']) as t:
                    root = ncs.maagic.get_root(t)
                    device = root.devices.device[nso_devicename]
                    input1 = device.live_status.ios_stats__exec.show.get_input()
                    input1.args = [command]
                    output = device.live_status.ios_stats__exec.any(input1).result
                    return output
    except:
        return False


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
            for acl in root.devices.device[box.name].config.ip.access_list.standard.std_named_acl:
                print("checking ip access-list standard " + str(acl.name))
                for rule in root.devices.device[box.name].config.ip.access_list.standard.std_named_acl[acl.name].std_access_list_rule:
                    if ip in rule.rule:
                        print(ip + " Is in acl " + str(acl.name))
                        acl_answer.append({"name":str(acl.name),"rule":rule.rule})
            print("checking Extended Access Lists for " + str(box.name))
            for acl in root.devices.device[box.name].config.ip.access_list.extended.ext_named_acl:
                print("checking ip access-list extended " + str(acl.name))
                for rule in root.devices.device[box.name].config.ip.access_list.extended.ext_named_acl[acl.name].ext_access_list_rule:
                    if ip in rule.rule:
                        print(ip + " Is in acl " + str(acl.name))
                        acl_answer.append({"name":str(acl.name),"rule":rule.rule})
    return acl_answer 
