from ncclient import manager
import xml.dom.minidom

# Get Capabilities function (aka <hello> rpc)
def netconfGetCapabilities(
        host,
        port,
        username,
        password,
        ios
):
    capabilities = []
    with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
            device_params={'name': ios}
    ) as m:
        for capability in m.server_capabilities:
            capabilities.append(capability)
        capabilities.sort()
        capabilities_str = '\n'.join(capabilities)
        return capabilities_str

# <get> (Only targets running datastore)
def netconfGet(
        host,
        port,
        username,
        password,
        ios,
        filter
):
    with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
            device_params={'name': ios}
    ) as m:
        netconfReply = m.get(filter)
        # Make returned XML data more human-readable
        temp = xml.dom.minidom.parseString(str(netconfReply.xml))
        new_xml = temp.toprettyxml(indent=" ", newl="\n")
        return new_xml

# <get-config> (Targets any specified datastore)
def netconfGetConfig(
        host,
        port,
        username,
        password,
        ios,
        filter
):
    with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
            device_params={'name': ios}
    ) as m:
        netconfReply = m.get_config(
            filter=filter,
            source='running'
        )
        # Make returned XML data more human-readable
        temp = xml.dom.minidom.parseString(str(netconfReply.xml))
        new_xml = temp.toprettyxml(indent=" ", newl="\n")
        return new_xml

# <edit-config>
def netconfEditConfig(
        host,
        port,
        username,
        password,
        ios,
        filter
):
    with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
            device_params={'name': ios}
    ) as m:
        netconfReply = m.edit_config(
            target='running',
            config=filter
        )
        # Make returned XML data more human-readable
        temp = xml.dom.minidom.parseString(str(netconfReply.xml))
        new_xml = temp.toprettyxml(indent=" ", newl="\n")
        return new_xml