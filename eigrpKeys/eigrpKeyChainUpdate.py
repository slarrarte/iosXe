import netconfActions, xmltodict
from pathlib import Path

# Import key chain NETCONF filter for editing
key_chain_filter = open(Path.home()/'pyProjects/projects/iosXeLab/eigrpKeys/eigrpKeyCreation.xml').read()

# List all hosts to update
host_ips = ['172.16.100.12', '172.16.100.13']

# This will be the netconf payload we will push to the devices to update the keys
updated_key_chain = """"""

# Keychain name
key_chain_name = ''
# NOTE: ALL BELOW LISTS ARE TO BE THE EXACT SAME LENGTH.
# List of all the keys you want to update
id = ['']
# Key string list (Keep in same order as the key IDs that you want to be assigned to)
key_string = ['']
# All vars below are for Accept-Lifetime
a_start_hh_mm_ss = ['']
a_start_month = ['']
a_start_day = ['']
a_start_year = ['']
a_end_hh_mm_ss = ['']
a_end_month = ['']
a_end_day = ['']
a_end_year = ['']
# All vars below are for Send-Lifetime
s_start_hh_mm_ss = ['']
s_start_month = ['']
s_start_day = ['']
s_start_year = ['']
s_end_hh_mm_ss = ['']
s_end_month = ['']
s_end_day = ['']
s_end_year = ['']



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
    for j in range(num_of_keys):
        text_for_document+= f"\tKey {xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key'][j]['id']}\n"
        text_for_document+=f"\t\tKey String: {xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key'][0]['key-string']}\n"
        text_for_document+=f"\t\tExpiration Date: {xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key'][0]['send-lifetime']['lifetime-group-v1']['end-month']} "
        text_for_document+=f"{xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key'][0]['send-lifetime']['lifetime-group-v1']['end-day']} "
        text_for_document+=f"{xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key'][0]['send-lifetime']['lifetime-group-v1']['end-year']}\n\n"

with open(Path.home()/'pyProjects/projects/iosXeLab/eigrpKeys/keyVerification.txt', 'w') as file:
    file.write(text_for_document)
