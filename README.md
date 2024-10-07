# iosXe
NETCONF/RESTCONF interaction scripts for IOS XE devices

REQUIRED PYTHON PACKAGES:
- requests
- ncclient
- netmiko (really only used to automate the enabling of NETCONF & RESTCONF on devices)

THE MEAT AND POTATOES: netconfActions.py
- netconfActions.py is my easy way to handle NETCONF calls.  All main HTTP methods (GET, PUT, POST, PATCH, & DELETE) are covered in this script, as well as all NETCONF actions.

This repository has some random shit, such as tree-views of YANG models, that I have been using to experiment with.  If you'd like, look at the tree-view YANG models like xeEigrpYangModel.txt to get a feel of what a YANG model is.
