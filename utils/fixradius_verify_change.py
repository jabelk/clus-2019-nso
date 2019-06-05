import ncs
import logging
import csv


log = logging.getLogger()
LOG_FILENAME = 'radius_round_2.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)


with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:
        #listofdicts_tocsv = []
        root = ncs.maagic.get_root(t)
        device_list = root.devices.device
        #mydict_radius_with_bad_pass = {}
        for device in device_list:
           device = root.devices.device[device.name]
           input1 = device.live_status.ios_stats__exec.show.get_input()
           input1.args = [" run | s radius server "]
           try:
               output = device.live_status.ios_stats__exec.show(input1).result
               log.info(output)
           except:
               log.info(device.name)
               log.info("something went wrong")

        # #device = root.devices.device["adl-sw1"]
        #     for server in device.config.ios__radius.server:
        #         if 'ise' in str(server.id).lower():
        #             print server.key.secret
        #             server.key.type = "7"
        #             server.key.secret = "ABCD"
        #             log.info( device.name + " " + str(server.id))
        #             print "new"
        #             print server.key.secret
        t.apply()

        # keys = listofdicts_tocsv[0].keys()
        # print "keys here"
        # print keys
        # #print
        # with open('radius_server_round2.csv','wb') as f:
        #     w = csv.DictWriter(f,keys)
        #     w.writeheader()
        #     w.writerows( listofdicts_tocsv)
