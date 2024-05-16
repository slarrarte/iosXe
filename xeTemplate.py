import getRunningConfig, json, loadConfiguration, getCapabilities, customRESTCONF, saveConfig
from pathlib import Path

# Change hostname
newHostname = """
{
  "Cisco-IOS-XE-native:hostname": "sancorp-r1"
}
"""

print(
    customRESTCONF.customRESTCONF(
        'patch',
        '10.10.20.48',
        'Cisco-IOS-XE-native:native/hostname',
        'developer',
        'C1sco12345',
        strData=newHostname
    )
)

# Change banner
newBanner = """
{
  "Cisco-IOS-XE-native:login": {
      "banner": "Banner updated via RESTCONF"
  }
}
"""

print(
    customRESTCONF.customRESTCONF(
        'patch',
        '10.10.20.48',
        'Cisco-IOS-XE-native:native/banner/login',
        'developer',
        'C1sco12345',
        strData=newBanner
    )
)

# Create local account
newLocalAccount = """
{
  "Cisco-IOS-XE-native:username": [
    {
      "name": "sysAdmin",
      "privilege": 1,
      "secret": {
        "encryption": "9",
        "secret": "$9$2uJqUsbtLlISaE$2BvT6b.W0phNXnUxNPzjppa19H0N1JbTT0PDXcWZfdM"
      }
    }
  ]
}
"""

print(
    customRESTCONF.customRESTCONF(
        'patch',
        '10.10.20.48',
        'Cisco-IOS-XE-native:native/username',
        'developer',
        'C1sco12345',
        strData=newLocalAccount
    )
)

# Create keychain
keyChain = """
{
  "Cisco-IOS-XE-crypto:chain": [
    {
      "name": "EIGRP69",
      "key": [
        {
          "id": "69",
          "cryptographic-algorithm-choice": {
            "default": "hmac-sha-256"
          },
          "cryptographic-algorithm": "hmac-sha-256",
          "key-string": {
            "encryption": "7",
            "key": "1423373838"
          },
          "accept-lifetime": {
            "lifetime-group-v1": {
              "start-hh-mm-ss": "00:00:00",
              "start-month": "Oct",
              "start-day": 31,
              "start-year": 2023,
              "infinite": [null]
            }
          }
        }
      ]
    }
  ]
}
"""

print(
    customRESTCONF.customRESTCONF(
        'patch',
        '10.10.20.48',
        'Cisco-IOS-XE-native:native/key/Cisco-IOS-XE-crypto:chain',
        'developer',
        'C1sco12345',
        strData=keyChain
    )
)

# Create routing domain
eigrpInstance = """
{
  "Cisco-IOS-XE-eigrp:router-eigrp": {
    "eigrp": {
      "classic-mode": [
        {
          "autonomous-system": 69,
          "eigrp": {
            "router-id": "1.1.1.1"
          },
          "network": {
            "address-wildcard": [
              {
                "ipv4-address": "100.64.0.0",
                "wildcard": "0.0.255.255"
              }
            ]
          }
        }
      ]
    }
  }
}
"""

print(
    customRESTCONF.customRESTCONF(
        'patch',
        '10.10.20.48',
        'Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-eigrp:router-eigrp',
        'developer',
        'C1sco12345',
        strData=eigrpInstance
    )
)

