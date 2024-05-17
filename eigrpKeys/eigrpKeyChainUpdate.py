import netconfActions, saveConfig
from pathlib import Path

# PROCESS:
# 1.) Set all variables
# 2.) Delete old keys
# 3.) Recreate new replacement keys

# Import key chain deletion NETCONF filter for formatting
del_key_chain_filter = open(Path.home()/'pyProjects/projects/iosXeLab/eigrpKeys/eigrpKeyDeletion.xml').read()

# Import key chain creation NETCONF filter for formatting
key_chain_filter = open(Path.home()/'pyProjects/projects/iosXeLab/eigrpKeys/eigrpKeyCreation.xml').read()

# List all hosts to update
host_ips = ['172.16.100.12', '172.16.100.13', '172.16.100.14']

# This will be the netconf payload used to delete keys
del_netconf_filter_body = f""""""

# This will be the netconf payload we will push to the devices to update the keys
netconf_filter_body = f""""""

# Keychain name
key_chain_name = 'TEST'
# NOTE: ALL BELOW LISTS ARE TO BE THE EXACT SAME LENGTH.
# List of all the keys you want to update
id = ['100']
# Key string list (Keep in same order as the key IDs that you want to be assigned to)
key_string = ['ONLYkeyREVISED']
# All vars below are for Accept-Lifetime
a_start_hh_mm_ss = ['00:00:00'] * len(id)
a_start_month = ['Jan', 'Feb', 'Mar']
a_start_day = ['1'] * len(id)
a_start_year = ['2027']
a_end_hh_mm_ss = ['23:59:59'] * len(id)
a_end_month = ['Mar']
a_end_day = ['31']
a_end_year = ['2027']
# All vars below are for Send-Lifetime
s_start_hh_mm_ss = ['00:00:00'] * len(id)
s_start_month = ['Mar']
s_start_day = ['1'] * len(id)
s_start_year = ['2027']
s_end_hh_mm_ss = ['23:59:59'] * len(id)
s_end_month = ['Mar']
s_end_day = ['31']
s_end_year = ['2027']

# Format key_chain_filter with desired vars (vars that start with _ are from key_chain_filter
for i in range(len(id)):
    # Format del_key_chain_filter with variables
    mod_del_key_chain_filter = del_key_chain_filter.format(
        _key_chain_name=key_chain_name,
        _id=id[i]
    )
    # Format key_chain_filter with variables
    mod_key_chain_filter = key_chain_filter.format(
        _key_chain_name = key_chain_name,
        _id = id[i],
        _key_string = key_string[i],
        _a_start_hh_mm_ss = a_start_hh_mm_ss[i],
        _a_start_month = a_start_month[i],
        _a_start_day = a_start_day[i],
        _a_start_year = a_start_year[i],
        _a_end_hh_mm_ss = a_end_hh_mm_ss[i],
        _a_end_month = a_end_month[i],
        _a_end_day = a_end_day[i],
        _a_end_year = a_end_year[i],
        _s_start_hh_mm_ss = s_start_hh_mm_ss[i],
        _s_start_month = s_start_month[i],
        _s_start_day = s_start_day[i],
        _s_start_year = s_start_year[i],
        _s_end_hh_mm_ss = s_end_hh_mm_ss[i],
        _s_end_month = s_end_month[i],
        _s_end_day = s_end_day[i],
        _s_end_year = s_end_year[i],
    )
    if i != range(len(id))[-1]:
        del_netconf_filter_body += mod_del_key_chain_filter + '\n'
        netconf_filter_body += mod_key_chain_filter + '\n'
    else:
        del_netconf_filter_body += mod_del_key_chain_filter
        netconf_filter_body += mod_key_chain_filter

# Adding the <config><native></native></config> tags to beginning and end of payload
del_final_netconf_filter = '<config>\n<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">\n' + del_netconf_filter_body + '\n</native>\n</config>'
final_netconf_filter = '<config>\n<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">\n' + netconf_filter_body + '\n</native>\n</config>'

# Push config to devices
for router in host_ips:
    try:
        netconfActions.netconfEditConfig(
            router,
            '830',
            'test',
            'test',
            'iosxe',
            del_final_netconf_filter
        )
        print(f'Host {router} keys deleted. Now recreating keys with new key strings.\n')
        try:
            netconfActions.netconfEditConfig(
                router,
                '830',
                'test',
                'test',
                'iosxe',
                final_netconf_filter
            )
            print(f'Host {router} new keys configured successfully. Now saving configuration.\n')
            # Save changes
            saveConfig.saveConfig(
                router,
                '830',
                'test',
                'test'
            )
            print('Changes saved.\n')
        except:
            print(f'Host {router} new keys FAILED to be configured..\n')
    except:
        print(f'Host {router} keys failed to be deleted.\n')


