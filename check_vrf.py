#!/usr/bin/env python3
"""
Copyright (c) 2023 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
from genie import testbed
import pandas as pd
from collections import defaultdict

# load the devices from the testbed file
testbed = testbed.load(f"./testbed1.yml")
devices = testbed.devices

# iterate through the devices, connect to the device, and parse the show ip interface and show vlan commands
interface_details = []
interfaces = {}
vlans = {"vlans": {}}
for device in devices:
    switch = devices[device]
    switch.connect(init_exec_commands=[], init_config_commands=[],
                   log_stdout=False, learn_hostname=True)

    interfaces.update(switch.parse("show ip interface"))
    vlans["vlans"].update(switch.parse("show vlan"))

    switch.disconnect()

    # map the interfaces to their VLANs
    intf_to_vlan = defaultdict(list)
    for vlan in vlans["vlans"]:
        vlan_details = vlans["vlans"][vlan]
        if "interfaces" in vlan_details.keys():
            for intf in vlan_details["interfaces"]:
                intf_to_vlan[intf].append(vlan)

    # create dictionary that defines the device name, interface name, and vrf
    for interface in interfaces:
        keys = interfaces[interface].keys()
        if "vrf" in keys:
            if interfaces[interface]["vrf"] == "Mgmt-vrf":
                new_int = {
                    "device": device,
                    "interface": interface,
                    "vrf": interfaces[interface]["vrf"]
                }

            # if the interface has an IPv4 address, save that to the dictionary
            if "ipv4" in keys:
                ip_details = interfaces[interface]["ipv4"]
                new_int["ip"] = []
                for ip in ip_details:
                    new_int["ip"].append(ip)
            else:
                new_int["ip"] = "n/a"

            # if the interface has a VLAN, save that to the dictionary
            if interface in intf_to_vlan.keys():
                new_int["vlan"] = intf_to_vlan[interface]
            else:
                new_int["vlan"] = "n/a"

            # add the dictionary to a list
            interface_details.append(new_int)

# create Excel spreadsheet from the list of dictionaries created
with pd.ExcelWriter("interface_details.xlsx") as writer:
    interface_df = pd.DataFrame.from_dict(interface_details)
    interface_df.to_excel(writer, index=False)
