import xmltodict, netconfActions
from pathlib import Path

# Path to key chain NETCONF filter
xml_filter = open(Path.home()/'pyProjects/projects/iosXeLab/eigrpKeys/keyChain.xml').read()

# List all hosts to update
host_ips = ['172.16.100.12', '172.16.100.13', '172.16.100.14']

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
    for j in range(num_of_keys):
        text_for_document += f"\tKey {xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key'][j]['id']}\n"
        text_for_document += f"\t\tKey String: {xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key'][j]['key-string']['key']}\n"
       text_for_document += f"\t\tSend Lifetime: {xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key'][j]['send-lifetime']['lifetime-group-v1']}\n"
        text_for_document += f"\t\tAccept Lifetime: {xml_to_dict['rpc-reply']['data']['native']['key']['chain']['key'][j]['accept-lifetime']['lifetime-group-v1']}\n\n"

with open(Path.home()/'pyProjects/projects/iosXeLab/eigrpKeys/keyVerification.txt', 'w') as file:
    file.write(text_for_document)
