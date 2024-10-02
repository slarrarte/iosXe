# xeInterfaceInventory.py
# The purpose of this script is to automate the obtaining of interface data for all IOS XE nodes
# in your network (as many nodes as you list)
from netconfActions import netconfGet as get
from getpass import getpass
import xmltodict, csv

# Path to csv file
database_path = '/Users/santiagolarrarte/pyProjects/projects/iosXeLab/dataCollection/xeInterfaceInventory.csv'

# List all the router IPs that you'd like included in the data gathering
router_loopbacks = ['172.16.52.13', '172.16.52.14']

# For security purposes, username and password will be entered at user input prompt
enter_username = input('Username: \n')
enter_password = getpass('Password: \n')

# YANG-formatted filter for XML parsing
xml_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname/>
    </native>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
"""

# List of interface data to be written to csv
interface_data_list = [
    ['Hostname', 'Interface', 'IP', 'Mask', 'Description']
]

# <get> each router in router_loopbacks
for router in router_loopbacks:
    # Exception handling for when a node is unreachable
    try:
        router_response = xmltodict.parse(
            get(
                host=router,
                port="830",
                username=enter_username,
                password=enter_password,
                ios="iosxe",
                filter=xml_filter
            )
        )
        # Parsing per interface on router
        for interface in range(len(router_response['rpc-reply']['data']['interfaces']['interface'])):
            # Sub-list to be appended to interface_data_list
            host_list = []
            # Hostname will be added to host_list[0] only if this is the first interface of said host;
            # otherwise, host_list[0] will be empty.
            if interface == 0:
                host_list.append(router_response['rpc-reply']['data']['native']['hostname'])
            else:
                host_list.append('')
            # Interface
            host_list.append(
                router_response['rpc-reply']['data']['interfaces']['interface'][interface]['name']
            )
            # IP
            try:
                host_list.append(
                    router_response['rpc-reply']['data']['interfaces']['interface'][interface]['ipv4']['address']['ip']
                )
            except:
                host_list.append('')
            # Mask
            try:
                host_list.append(
                    router_response['rpc-reply']['data']['interfaces']['interface'][interface]['ipv4']['address']['netmask']
                )
            except:
                host_list.append('')
            # Description
            try:
                host_list.append(
                    router_response['rpc-reply']['data']['interfaces']['interface'][interface]['description']
                )
            except:
                host_list.append('')
            # Write sublist to interface_data_list
            interface_data_list.append(host_list)
    # Writes IP as hostname with blank arguments if router is unreachable
    except:
        interface_data_list.append([router, '', '', '', '', ''])
        continue

# Import csv file into program and modify it with gathered NETCONF data
with open(database_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(interface_data_list)