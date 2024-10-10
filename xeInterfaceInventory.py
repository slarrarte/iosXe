# xeInterfaceInventory.py
# The purpose of this script is to automate the obtaining of interface data for all IOS XE nodes
# in your network (as many nodes as you list)
from netconfActions import netconfGet as get
from getpass import getpass
import xmltodict, csv

# Path to csv file
database_path = ''

# List all the router IPs that you'd like included in the data gathering
router_loopbacks = ['']

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

# Row-generating function
def interface_rows(router_response):
    # Reference global variable interface_data_list for row appending
    global interface_data_list
    # Hostname
    hostname = router_response['rpc-reply']['data']['native']['hostname']
    # Shortcut for parsing
    interfaces = router_response['rpc-reply']['data']['interfaces']['interface']
    # Row-generating loop
    for interface in interfaces:
        row = []
        # Hostname
        if interfaces[0] == interface:
            row.append(hostname)
        else:
            row.append('')
        # Interface
        row.append(interface.get('name', ''))
        # IP
        row.append(interface.get('ipv4', {}).get('address', {}).get('ip', ''))
        # Mask
        row.append(interface.get('ipv4', {}).get('address', {}).get('netmask', ''))
        # Description
        row.append(interface.get('description', ''))
        # Append row to interface_data_list
        interface_data_list.append(row)

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
        # Append rows to interface_data_list
        interface_rows(router_response)
        print(f'Successfully connected to router {router}')
    except:
        print(f'Issue connecting to or pulling data from router {router}')
        interface_data_list.append(['', '', '', '', ''])
        continue

# Import csv file into program and modify it with gathered NETCONF data
with open(database_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(interface_data_list)
