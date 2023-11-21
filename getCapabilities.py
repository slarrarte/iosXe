# Obtain YANG capabilities via NETCONF <hello>
# Cisco device_params:
#     CSR: device_params={'name':'csr'}
#     Nexus: device_params={'name':'nexus'}
#     IOS XR: device_params={'name':'iosxr'}
#     IOS XE: device_params={'name':'iosxe'}

from ncclient import manager

def getCapabilities(host, port, username, password, os_version):
    with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': os_version}
    ) as m:
        for capability in m.server_capabilities:
            print(capability)
