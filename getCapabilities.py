# Obtain YANG capabilities via NETCONF <hello>
from ncclient import manager

def getCapabilities(host, port, username, password):
    with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': 'iosxe'}
    ) as m:
        for capability in m.server_capabilities:
            print(capability)
