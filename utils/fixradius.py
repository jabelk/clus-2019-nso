import ncs
import logging
import csv


log = logging.getLogger()
LOG_FILENAME = 'radius.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)



def simple_audit():
    #simple audit of password, without CSV output and dictionaries
    #Audit Radius Server Passwords for only those that have "ISE/ise" in the name of the server_key
    with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:
            root = ncs.maagic.get_root(t)
            device_list = root.devices.device
            mydict_radius_with_bad_pass = {}
            for device in device_list:
                for server in device.config.ios__radius.server:
                    if 'ise' in str(server.id).lower():
                        print server.key.secret
                        server.key.type = "7"
                        #set new password
                        server.key.secret = "NEWPASSWORDTOCHANGETOHASHEDALREADY"
                        #log the changed output
                        log.info( device.name + " " + str(server.id))
                        print "new password"
                        print server.key.secret
            #uncomment to apply the change
            #t.apply()

def simple_audit_with_csv_and_dict_usage():

    with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:
            listofdicts_tocsv = []
            root = ncs.maagic.get_root(t)
            device_list = root.devices.device
            mydict_radius_with_bad_pass = {}
            for device in device_list:
                for server in device.config.ios__aaa.server.radius.dynamic_author.client:
                    mydict = { 'server': str( server.address), "password" :str(server.server_key.secret), "devicename" :  device.name}
                    if mydict["password"] == "OLDPASSWORDTOCHANGEHASHED":
                        server.server_key.secret = "NEWPASSWORDTOCHANGETO"
                        mydict_radius_with_bad_pass.update(mydict)
                        listofdicts_tocsv.append(mydict)
                        print mydict.keys()
                    print mydict
                for server in device.config.ios__radius.server:
                #Audit Radius Server Passwords for only those that have "ISE/ise" in the name of the server_key
                    if 'ise' in str(server.id).lower():
                        print server.key.secret
                        server.key.type = "7"
                        #set new password
                        server.key.secret = "NEWPASSWORDTOCHANGETOHASHEDALREADY"
                        #log the changed output
                        log.info( device.name + " " + str(server.id))
                        print "new password"
                        print server.key.secret
                    mydict = { 'server': str( server.address.ipv4.host), "password" :str(server.key.secret), "devicename" :  device.name}
                    if mydict["password"] == "OLDPASSWORDTOCHANGE":
                        #uncomment to change the radius server password
                        server.key.secret = "NEWPASSWORDTOCHANGETO"
                        mydict_radius_with_bad_pass.update(mydict)
                        listofdicts_tocsv.append(mydict)
                        #print mydict.keys()
                    print mydict
            #t.apply()
            keys = listofdicts_tocsv[0].keys()
            print "keys here"
            print keys
            with open('radius_server.csv','wb') as f:
                w = csv.DictWriter(f,keys)
                w.writeheader()
                w.writerows( listofdicts_tocsv)
