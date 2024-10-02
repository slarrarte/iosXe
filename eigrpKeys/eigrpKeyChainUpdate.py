import netconfActions, saveConfig
import random, string
from pathlib import Path


# Import key chain creation NETCONF filter for formatting
key_chain_filter = open(Path.cwd()/'eigrpKeyCreation.xml').read()

# List all hosts to update
host_ips = ['']

# KEY STRING GENERATION FUNCTION
def generatePassword(num_of_keys, keyLength):
    keys = []
    for key in range(num_of_keys):
        characters = [random.choice(string.ascii_letters + string.digits) for i in range(keyLength)]
        random.shuffle(characters)
        keys.append(''.join(characters))
    return keys

# This will be the netconf payload we will push to the devices to update the keys
netconf_filter_body = f""""""

# Keychain name
key_chain_name = 'TEST'
# NOTE: ALL BELOW LISTS ARE TO BE THE EXACT SAME LENGTH.
# List of all the keys you want to update
id = ['5', '6', '7']
# Key string list (Keep in same order as the key IDs that you want to be assigned to)
key_string = generatePassword(len(id), 25)
# All vars below are for Accept-Lifetime
a_start_hh_mm_ss = ['00:00:00'] * len(id)
a_start_month = ['Jan', 'Feb', 'Mar']
a_start_day = ['1'] * len(id)
a_start_year = ['2027'] * len(id)
a_end_hh_mm_ss = ['23:59:59'] * len(id)
a_end_month = ['Jan', 'Feb', 'Mar']
a_end_day = ['31', '28', '31']
a_end_year = ['2027'] * len(id)
# All vars below are for Send-Lifetime
s_start_hh_mm_ss = ['00:00:00'] * len(id)
s_start_month = ['Jan', 'Feb', 'Mar']
s_start_day = ['1'] * len(id)
s_start_year = ['2027'] * len(id)
s_end_hh_mm_ss = ['23:59:59'] * len(id)
s_end_month = ['Jan', 'Feb', 'Mar']
s_end_day = ['31', '28', '31']
s_end_year = ['2027'] * len(id)

# Format key_chain_filter with desired vars (vars that start with _ are from key_chain_filter
for i in range(len(id)):
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
        netconf_filter_body += mod_key_chain_filter + '\n'
    else:
        netconf_filter_body += mod_key_chain_filter

# Adding the <config><native><all_remaining_tags/></native></config> tags to beginning and end of payload
final_netconf_filter = (f"""<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <key>
            <chain xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-crypto">
                <name>TEST</name>
                {netconf_filter_body}
            </chain>
        </key>
    </native>
</config>
""")

for router in host_ips:
    # Create new keys
    print(
        netconfActions.netconfEditConfig(
            router,
            '830',
            'test',
            'test',
            'iosxe',
            final_netconf_filter
        )
    )
    print(f'Host {router} new keys configured successfully. Now saving configuration.\n')
    # Save changes
    saveConfig.saveConfig(
        router,
        '830',
        'test',
        'test'
    )
    print('Changes saved.\n\n')
