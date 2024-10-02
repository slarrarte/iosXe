import netconfActions, xmltodict
from pathlib import Path

# Path to key chain NETCONF filter
xml_filter = open(Path.home()/'pyProjects/projects/iosXeLab/eigrpKeys/keyChain.xml').read()

# List all hosts to update
host_ips = ['']

text_for_document = """"""

# Obtain device key chain xml data for verification, then put output in a file
for i in host_ips:
    test_file = open(Path.home()/f'', 'w')
    test_file.write(
        netconfActions.netconfGetConfig(
            i,
            '830',
            'test',
            'test',
            'iosxe',
            xml_filter
        )
    )
    test_file.close()
