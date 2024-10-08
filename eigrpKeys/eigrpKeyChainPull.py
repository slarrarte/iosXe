import xmltodict, netconfActions
from pathlib import Path

# Path to key chain NETCONF filter
xml_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <key>
            <chain xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-crypto"/>
        </key>
    </native>
</filter>
"""

# List all hosts to update
host_ips = ['']

text_for_document = """"""

# Obtain all key chains for verification, then put output in a file
for i in host_ips:
    xml_to_dict = xmltodict.parse(
        netconfActions.netconfGetConfig(
            i,
            '830',
            'test',
            'test',
            'iosxe',
            xml_filter
        )
    )
    key_chain_name = xml_to_dict['rpc-reply']['data']['native']['key']['chain']['name']
    num_of_keys = len(xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key'])
    text_for_document+= f"Host: {i}\nKey Chain: {key_chain_name}\n"

    # key_chain_path is just a shortcut for me to parse through the dict data, as you will see below in the for loop
    key_chain_path = xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key']
    # Aformentioned for loop that generates text for the key chain report
    for j in range(num_of_keys):
        # Finite key
        try:
            text_for_document += f'''Key {key_chain_path[j]['id']}
    Key String: {key_chain_path[j]['key-string']['key']}
    Send Lifetime:
        Start Time: {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['start-hh-mm-ss']}
        Start Date: {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['start-month']} {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['start-day']} {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['start-year']}
        End Time: {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['end-hh-mm-ss']}
        End Date: {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['end-month']} {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['end-day']} {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['end-year']}
    Accept Lifetime:
        Start Time: {key_chain_path[j]['accept-lifetime']['lifetime-group-v1']['start-hh-mm-ss']}
        Start Date: {key_chain_path[j]['accept-lifetime']['lifetime-group-v1']['start-month']} {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['start-day']} {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['start-year']}
        End Time: {key_chain_path[j]['accept-lifetime']['lifetime-group-v1']['end-hh-mm-ss']}
        End Date: {key_chain_path[j]['accept-lifetime']['lifetime-group-v1']['end-month']} {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['end-day']} {key_chain_path[j]['send-lifetime']['lifetime-group-v1']['end-year']}\n\n'''
        # Infinite key
        except:
            text_for_document += f'''Key {key_chain_path[j]['id']}
    Key String: {key_chain_path[j]['key-string']['key']}
    INFINITE KEY\n\n'''
            
with open(Path.home()/'', 'w') as file:
    file.write(text_for_document)
