import getRunningConfig, json, loadConfiguration, getCapabilities, customRESTCONF, saveConfig
from pathlib import Path

# Get capabilities
# print(
#     getCapabilities.getCapabilities(
#         '10.10.20.48',
#         '830',
#         'developer',
#         'C1sco12345',
#         'iosxe'
#     )
# )

# Pull entire config via RESTCONF + Cisco-IOS-XE-native YANG model
# with open(
#     Path.home()/'pyProjects/projects/iosXeLab/configFiles/R1.json', 'w'
# ) as file:
#     file.write(getRunningConfig.getRunningConfigRESTCONF('10.10.20.48', 'developer', 'C1sco12345'))

# Change hostname
# newHostname = """
# {
#   "Cisco-IOS-XE-native:hostname": "sancorp-r1"
# }
# """
#
# print(
#     customRESTCONF.customRESTCONF(
#         'patch',
#         '10.10.20.48',
#         'Cisco-IOS-XE-native:native/hostname',
#         'developer',
#         'C1sco12345',
#         strData=newHostname
#     )
# )
#
# # Change banner
# newBanner = """
# {
#   "Cisco-IOS-XE-native:login": {
#       "banner": "Banner updated via RESTCONF"
#   }
# }
# """
#
# print(
#     customRESTCONF.customRESTCONF(
#         'patch',
#         '10.10.20.48',
#         'Cisco-IOS-XE-native:native/banner/login',
#         'developer',
#         'C1sco12345',
#         strData=newBanner
#     )
# )
#
# Create local account
# newLocalAccount = """
# {
#   "Cisco-IOS-XE-native:username": [
#     {
#       "name": "sysAdmin",
#       "privilege": 1,
#       "secret": {
#         "encryption": "9",
#         "secret": "$9$2uJqUsbtLlISaE$2BvT6b.W0phNXnUxNPzjppa19H0N1JbTT0PDXcWZfdM"
#       }
#     }
#   ]
# }
# """
#
# print(
#     customRESTCONF.customRESTCONF(
#         'patch',
#         '10.10.20.48',
#         'Cisco-IOS-XE-native:native/username',
#         'developer',
#         'C1sco12345',
#         strData=newLocalAccount
#     )
# )
#
# Delete local account
# print(
#     customRESTCONF.customRESTCONF(
#         'delete',
#         '10.10.20.48',
#         'Cisco-IOS-XE-native:native/username=sysAdmins',
#         'developer',
#         'C1sco12345'
#     )
# )
#
# keyChain = """
# {
#   "Cisco-IOS-XE-crypto:chain": [
#     {
#       "name": "EIGRP69",
#       "key": [
#         {
#           "id": "69",
#           "cryptographic-algorithm-choice": {
#             "default": "hmac-sha-256"
#           },
#           "cryptographic-algorithm": "hmac-sha-256",
#           "key-string": {
#             "encryption": "7",
#             "key": "1423373838"
#           },
#           "accept-lifetime": {
#             "lifetime-group-v1": {
#               "start-hh-mm-ss": "00:00:00",
#               "start-month": "Oct",
#               "start-day": 31,
#               "start-year": 2023,
#               "infinite": [null]
#             }
#           }
#         }
#       ]
#     }
#   ]
# }
# """
#
# print(
#     customRESTCONF.customRESTCONF(
#         'get',
#         '10.10.20.48',
#         'Cisco-IOS-XE-native:native/key/Cisco-IOS-XE-crypto:chain',
#         'developer',
#         'C1sco12345',
#         strData=keyChain
#     )
# )

# Set on-change telemetry subscription
onChangeSubscription = """
{
    "Cisco-IOS-XE-mdt-cfg:mdt-subscription": [
        {
            "subscription-id": "69",
            "base": {
                "stream": "yang-push",
                "encoding": "encode-kvgpb",
                "dampening period": "0",
                "xpath": "/ietf-interfaces:interfaces-state/interface[name='Loopback69']/oper-status"
            },
            "mdt-receivers": {
                "address": "10.10.20.50",
                "port": "57500",
                "protocol": "grpc-tcp"
            }
        }
    ]
}
"""

print(
    customRESTCONF.customRESTCONF(
        'get',
        '10.10.20.48',
        'Cisco-IOS-XE-mdt-cfg:mdt-config-data/mdt-subscription=69',
        'developer',
        'C1sco12345',
        strData=onChangeSubscription
    )
)

# interfaceStateXPath = '/ietf-interfaces:interfaces-state/interface[name="GigabitEthernet2"]/oper-status'
#
# /if:interfaces-state/interface[name='GigabitEthernet2']/admin-status
