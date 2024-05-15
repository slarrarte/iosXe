import netconfActions, xmltodict
from pathlib import Path

# Path to key chain NETCONF filter
xml_filter = open(Path.home()/'python/iosXe/configFiles/keyChain.xml').read()

# List all hosts to update
host_ips = ['172.16.100.12', '172.16.100.13']

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
    text_for_document = f"""
    Host: {i}
    Key Chain: {key_chain_name}

    """
    for i in range(num_of_keys):






    file = open(Path.home()/f'python/iosXe/keyChains/{i}.txt', 'w')
    # file.write(
    #     netconfActions.netconfGetConfig(
    #         i,
    #         '830',
    #         'test',
    #         'test',
    #         'iosxe',
    #         xml_filter
    #     )
    # )
    # file.close()
