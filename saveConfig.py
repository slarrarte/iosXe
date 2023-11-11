# Save running configuration using NETCONF
from ncclient import manager, xml_

def saveConfig(host, port, username, password):
    with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': 'iosxe'}
    ) as m:
        save_body = '<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>'
        save_rpc = m.dispatch(xml_.to_ele(save_body))
        return save_rpc
