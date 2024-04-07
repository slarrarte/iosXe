# Load config of a device via RESTCONF
import requests, xml.dom.minidom
from ncclient import manager

def loadConfigurationRESTCONF(host, string):
    requests.packages.urllib3.disable_warnings()
    baseUrl = f'https://{host}/restconf/data/'
    nativeEndpoint = 'Cisco-IOS-XE-native:native'
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    }
    with requests.put(
        url=baseUrl + nativeEndpoint,
        headers=headers,
        auth=(
            input('Username: '),
            input('Password: ')
        ),
        data=string,
        verify=False
    ) as res:
        return res.status_code

def loadConfigurationNETCONF(host, port, username, password, config):
    with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': 'iosxe'}
    ) as m:
        netconf_reply = m.edit_config(config=config, target='running')
        temp = xml.dom.minidom.parseString(str(netconf_reply.xml))
        new_xml = temp.toprettyxml(indent=" ", newl="")
        return new_xml

