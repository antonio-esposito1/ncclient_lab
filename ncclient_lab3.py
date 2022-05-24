#!/usr/bin/python3.7

def main():
 from ncclient import manager
 device = manager.connect(host='mivpe015', port=830, username='antonio', password='admin', hostkey_verify=False, device_params={}, allow_agent=False, look_for_keys=False)
 print(device)
 get_filter = """
	     <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-bgp-cfg">
		<instance>
                  <instance-as>
                   <four-byte-as>
		     <as>30722</as>
                   </four-byte-as>
		  </instance-as>
		</instance>
	     </bgp>
	     """
 nc_get_reply = device.get(('subtree', get_filter))
 #print(etree.tostring(nc_get_reply.data, pretty_print=True))
 #print(nc_get_reply.xml)
 print(nc_get_reply)
if __name__ == '__main__':
    main()
