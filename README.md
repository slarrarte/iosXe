# iosXe
NETCONF/RESCONF interaction scripts for IOS XE devices

REQUIRED PYTHON PACKAGES:
- requests
- netmiko (really only used to automate the enabling of NETCONF & RESTCONF on devices)

THE MEAT AND POTATOES: customRESTCONF.py
- customRESTCONF.py is my easy way to handle RESTCONF calls.  All main HTTP methods (GET, PUT, POST, PATCH, & DELETE) are covered in this script.
- To see it in action, look at xeTemplate.py.  I make various configurations using my customRESTCONF.py script.  All configuration data passed to the function is json-formatted data modeled according to the respective YANG models.

This project has some random shit, such as tree-views of YANG models, that I have been using to experiment with.  If you'd like, look at the tree-view YANG models like xeEigrpYangModel.txt to get a feel of what a YANG model is.
