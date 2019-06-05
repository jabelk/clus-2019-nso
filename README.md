# CLUS NSO + ROBOT Demo

# NSO Device List

```
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                                                                         │
  │  NTC NSO Demo Menu                                                      │
  │                                                                         │
  │  Choose an Option Below                                                 │
  │                                                                         │
  │                                                                         │
  │    1 - View All Devices                                                 │
  │    2 - Audit All ACLs from Input                                        │
  │    3 - Audit Interfaces for an IP Address                               │
  │    4 - Exit                                                             │
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

## NSO ACL Audit

Sample output
```

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                                                                         │
  │  NTC NSO Demo Menu                                                      │
  │                                                                         │
  │  Choose an Option Below                                                 │
  │                                                                         │
  │                                                                         │
  │    1 - View All Devices                                                 │
  │    2 - Audit All ACLs from Input                                        │
  │    3 - Audit Interfaces for an IP Address                               │
  │    4 - Exit                                                             │
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
checking Standard Access Lists for nxos-spine1
checking Extended Access Lists for nxos-spine1
checking Standard Access Lists for nxos-spine2
checking Extended Access Lists for nxos-spine2
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
checking Standard Access Lists for nxos-spine1
checking Extended Access Lists for nxos-spine1
checking Standard Access Lists for nxos-spine2
checking Extended Access Lists for nxos-spine2
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
checking Standard Access Lists for nxos-spine1
checking Extended Access Lists for nxos-spine1
checking Standard Access Lists for nxos-spine2
checking Extended Access Lists for nxos-spine2
Creating CSV for Audit Output for Device csr3
checking Standard Access Lists for csr1
checking Standard Access Lists for csr2
checking Standard Access Lists for csr3
checking Standard Access Lists for nxos-spine1
checking ip access-list nexus-dc-customer-1-emear-location
checking ip access-list nexus-dc-customer-2-emear-location
checking ip access-list nexus-dc-customer-3-emear-location
checking ip access-list standard
checking Standard Access Lists for nxos-spine2
checking ip access-list nexus-dc-customer-1-emear-location
checking ip access-list nexus-dc-customer-2-emear-location
checking ip access-list nexus-dc-customer-3-emear-location
checking ip access-list standard
The IP address 91.118.192.128 was not found in nxos-spine1
checking Standard Access Lists for csr1
checking Standard Access Lists for csr2
checking Standard Access Lists for csr3
checking Standard Access Lists for nxos-spine1
checking ip access-list nexus-dc-customer-1-emear-location
checking ip access-list nexus-dc-customer-2-emear-location
checking ip access-list nexus-dc-customer-3-emear-location
checking ip access-list standard
checking Standard Access Lists for nxos-spine2
checking ip access-list nexus-dc-customer-1-emear-location
checking ip access-list nexus-dc-customer-2-emear-location
checking ip access-list nexus-dc-customer-3-emear-location
checking ip access-list standard
The IP address 91.118.192.128 was not found in nxos-spine2
Press enter to return to menu...
```



## NSO Interface IP Audit

Sample output + CSV

```

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                                                                         │
  │  NTC NSO Demo Menu                                                      │
  │                                                                         │
  │  Choose an Option Below                                                 │
  │                                                                         │
  │                                                                         │
  │    1 - View All Devices                                                 │
  │    2 - Audit All ACLs from Input                                        │
  │    3 - Audit Interfaces for an IP Address                               │
  │    4 - Exit                                                             │
  │                                                                         │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘
  >> 3


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
Enter an IP Address to Check in the Extended ACLs (default is 10.0.0.51):
Creating CSV for Audit Output for Device csr1
The IP address 10.0.0.51 was not found in csr2
The IP address 10.0.0.51 was not found in csr3
The IP address 10.0.0.51 was not found in nxos-spine1
The IP address 10.0.0.51 was not found in nxos-spine2
Press enter to return to menu...
```