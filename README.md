# CLUS NSO + ROBOT Demo

# NSO Device List

```
(clus-2018-nso) clus-2019-nso$ python ntc_nso_clus.py

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                                                                         │
  │  NTC NSO Demo Menu                                                      │
  │                                                                         │
  │  Choose an Option Below                                                 │
  │                                                                         │
  │                                                                         │
  │    1 - View All Devices                                                 │
  │    2 - Audit All IOS ACLs from Input                                    │
  │    3 - Audit All Nexus ACLs from Input                                  │
  │    4 - Audit Interfaces for an IP Address                               │
  │    5 - Exit                                                             │
  │                                                                         │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘
  >> 1
Device csr1 and os type ios-xe
Device csr2 and os type ios-xe
Device csr3 and os type ios-xe
Device nxos-spine1 and os type NX-OS
Device nxos-spine2 and os type NX-OS
Press enter to return to menu...

```

## NSO IOS ACL Audit

Sample output or Check the `CSV Archive` Directory!
```

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                                                                         │
  │  NTC NSO Demo Menu                                                      │
  │                                                                         │
  │  Choose an Option Below                                                 │
  │                                                                         │
  │                                                                         │
  │    1 - View All Devices                                                 │
  │    2 - Audit All IOS ACLs from Input                                    │
  │    3 - Audit All Nexus ACLs from Input                                  │
  │    4 - Audit Interfaces for an IP Address                               │
  │    5 - Exit                                                             │
  │                                                                         │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘
  >> 2


Ever Have the problem,
Where is the IP in the midst of all your ACLs?
For example,

csr1#show run | i 91.118.192.128
  permit 91.118.192.128
csr1#


Enter an IP Address to Check in the Extended ACLs (default is 91.118.192.128):
checking Standard Access Lists for csr1
checking ip access-list standard ise-acl
checking ip access-list standard servicenow-acl
checking Extended Access Lists for csr1
checking ip access-list extended vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
checking ip access-list extended vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
checking ip access-list extended vpn-customer-3-us
91.118.192.128 Is in acl vpn-customer-3-us
91.118.192.128 Is in acl vpn-customer-3-us
checking Standard Access Lists for csr2
checking ip access-list standard ise-acl
checking ip access-list standard servicenow-acl
checking Extended Access Lists for csr2
checking ip access-list extended vpn-customer-1-emea-location
checking ip access-list extended vpn-customer-2-emear-location
checking Standard Access Lists for csr3
checking ip access-list standard ise-acl
checking ip access-list standard servicenow-acl
checking Extended Access Lists for csr3
checking ip access-list extended vpn-customer-1-latam-location
checking ip access-list extended vpn-customer-2-latam-location
Creating CSV for Audit Output for Device csr1
checking Standard Access Lists for csr1
checking ip access-list standard ise-acl
checking ip access-list standard servicenow-acl
checking Extended Access Lists for csr1
checking ip access-list extended vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
checking ip access-list extended vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
checking ip access-list extended vpn-customer-3-us
91.118.192.128 Is in acl vpn-customer-3-us
91.118.192.128 Is in acl vpn-customer-3-us
checking Standard Access Lists for csr2
checking ip access-list standard ise-acl
checking ip access-list standard servicenow-acl
checking Extended Access Lists for csr2
checking ip access-list extended vpn-customer-1-emea-location
checking ip access-list extended vpn-customer-2-emear-location
checking Standard Access Lists for csr3
checking ip access-list standard ise-acl
checking ip access-list standard servicenow-acl
checking Extended Access Lists for csr3
checking ip access-list extended vpn-customer-1-latam-location
checking ip access-list extended vpn-customer-2-latam-location
Creating CSV for Audit Output for Device csr2
checking Standard Access Lists for csr1
checking ip access-list standard ise-acl
checking ip access-list standard servicenow-acl
checking Extended Access Lists for csr1
checking ip access-list extended vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
91.118.192.128 Is in acl vpn-customer-1-amer-location
checking ip access-list extended vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
91.118.192.128 Is in acl vpn-customer-2-amer-location
checking ip access-list extended vpn-customer-3-us
91.118.192.128 Is in acl vpn-customer-3-us
91.118.192.128 Is in acl vpn-customer-3-us
checking Standard Access Lists for csr2
checking ip access-list standard ise-acl
checking ip access-list standard servicenow-acl
checking Extended Access Lists for csr2
checking ip access-list extended vpn-customer-1-emea-location
checking ip access-list extended vpn-customer-2-emear-location
checking Standard Access Lists for csr3
checking ip access-list standard ise-acl
checking ip access-list standard servicenow-acl
checking Extended Access Lists for csr3
checking ip access-list extended vpn-customer-1-latam-location
checking ip access-list extended vpn-customer-2-latam-location
Creating CSV for Audit Output for Device csr3
Press enter to return to menu...
```

## NSO NX-OS ACL Audit

Output below or in csv files
```

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                                                                         │
  │  NTC NSO Demo Menu                                                      │
  │                                                                         │
  │  Choose an Option Below                                                 │
  │                                                                         │
  │                                                                         │
  │    1 - View All Devices                                                 │
  │    2 - Audit All IOS ACLs from Input                                    │
  │    3 - Audit All Nexus ACLs from Input                                  │
  │    4 - Audit Interfaces for an IP Address                               │
  │    5 - Exit                                                             │
  │                                                                         │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘
  >> 3


Ever Have the problem,
Where is the IP in the midst of all your ACLs?
For example,

nxos-spine1# show running-config | include 10.6.196.5
  10 permit tcp 10.6.196.5/16 169.112.3.171/32 eq 143
  20 permit tcp 10.6.196.5/16 169.112.3.171/32 eq 993
  30 permit tcp 10.6.196.5/16 169.112.3.171/32 eq 995
  40 permit tcp 10.6.196.5/16 169.112.3.248/32 eq www


Enter an IP Address to Check in the Extended ACLs (default is 10.246.84.201), good choices for Nexus (10.246.84.201 or 10.6.196.5):
checking Standard Access Lists for nxos-spine1
checking ip access-list nexus-dc-customer-1-amer-location
checking ip access-list nexus-dc-customer-2-amer-location
checking ip access-list nexus-dc-customer-3-amer-location
checking ip access-list standard
checking Standard Access Lists for nxos-spine2
checking ip access-list nexus-dc-customer-1-emear-location
checking ip access-list nexus-dc-customer-2-emear-location
checking ip access-list nexus-dc-customer-3-emear-location
checking ip access-list standard
Creating CSV for Audit Output for Device nxos-spine1
checking Standard Access Lists for nxos-spine1
checking ip access-list nexus-dc-customer-1-amer-location
checking ip access-list nexus-dc-customer-2-amer-location
checking ip access-list nexus-dc-customer-3-amer-location
checking ip access-list standard
checking Standard Access Lists for nxos-spine2
checking ip access-list nexus-dc-customer-1-emear-location
checking ip access-list nexus-dc-customer-2-emear-location
checking ip access-list nexus-dc-customer-3-emear-location
checking ip access-list standard
Creating CSV for Audit Output for Device nxos-spine2
Press enter to return to menu...
```

## NSO Interface IP Audit

Sample output or Check the `CSV Archive` Directory

```

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                                                                         │
  │  NTC NSO Demo Menu                                                      │
  │                                                                         │
  │  Choose an Option Below                                                 │
  │                                                                         │
  │                                                                         │
  │    1 - View All Devices                                                 │
  │    2 - Audit All IOS ACLs from Input                                    │
  │    3 - Audit All Nexus ACLs from Input                                  │
  │    4 - Audit Interfaces for an IP Address                               │
  │    5 - Exit                                                             │
  │                                                                         │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘
  >> 4


Ever Have the problem,
Where is the IP in the midst of all your Interfaces?
For example,

csr1#show run | i 10.0.0.51
ip address 10.0.0.51 255.255.255.0
csr1#


Of course you could just read through the inteface config like this:
csr1#show run int gig 1
Building configuration...
Current configuration : 145 bytes
!
interface GigabitEthernet1
 vrf forwarding MANAGEMENT
 ip address 10.0.0.51 255.255.255.0
 negotiation auto
 no mop enabled
 no mop sysid
end




 But what about across many devices?
Enter one, or many IP Address(es) to Check in the Interfaces (default is 10.0.0.51), also try 10.0.0.52, 10.0.0.53, 10.0.0.71, 10.0.0.72:
Creating CSV for Audit Output for Device csr1
The IP address 10.0.0.51 was not found in csr2
The IP address 10.0.0.51 was not found in csr3
The IP address 10.0.0.51 was not found in nxos-spine1
The IP address 10.0.0.51 was not found in nxos-spine2
Press enter to return to menu...
```

## Robot NSO

```
(clus-2018-nso) clus-2018-nso$ robot nso.robot
==============================================================================
Nso
==============================================================================
Check Sync NSO against a Live Device: Initial check                   | PASS |
------------------------------------------------------------------------------
Verify IOS Version is Correct                                         | PASS |
------------------------------------------------------------------------------
Verify IP is in ACL                                                   | PASS |
------------------------------------------------------------------------------
Nso                                                                   | PASS |
3 critical tests, 3 passed, 0 failed
3 tests total, 3 passed, 0 failed
==============================================================================
Output:  /Users/jabelk/PycharmProjects/clus-2019-nso/output.xml
Log:     /Users/jabelk/PycharmProjects/clus-2019-nso/log.html
Report:  /Users/jabelk/PycharmProjects/clus-2019-nso/report.html
(clus-2018-nso) clus-2018-nso$
```

## Robot Netmiko

```
(clus-2018-nso) clus-2018-nso$ robot netmiko.robot
==============================================================================
Netmiko
==============================================================================
Login to device                                                       | PASS |
------------------------------------------------------------------------------
Check if state : Initial check                                        | PASS |
------------------------------------------------------------------------------
Clean up Connection with device                                       | PASS |
------------------------------------------------------------------------------
Netmiko                                                               | PASS |
3 critical tests, 3 passed, 0 failed
3 tests total, 3 passed, 0 failed
==============================================================================
Output:  /Users/jabelk/PycharmProjects/clus-2019-nso/output.xml
Log:     /Users/jabelk/PycharmProjects/clus-2019-nso/log.html
Report:  /Users/jabelk/PycharmProjects/clus-2019-nso/report.html
(clus-2018-nso) clus-2018-nso$
```