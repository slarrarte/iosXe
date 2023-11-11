# Get running config of a device via RESTCONF
import requests, xml.dom.minidom
from ncclient import manager

def getRunningConfigRESTCONF(host, username, password):
    requests.packages.urllib3.disable_warnings()
    baseUrl = f'https://{host}/restconf/data/'
    nativeEndpoint = 'Cisco-IOS-XE-native:native'
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    }
    with requests.get(
        url = baseUrl + nativeEndpoint,
        headers = headers,
        auth = (
            username,
            password
        ),
        verify=False
    ) as res:
        return res.text

def getRunningConfigNETCONF(host, port, username, password):
    with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': 'iosxe'}
    ) as m:
        netconf_reply = m.get_config(source='running')

    temp = xml.dom.minidom.parseString(str(netconf_reply.xml))
    new_xml = temp.toprettyxml()
    return new_xml
