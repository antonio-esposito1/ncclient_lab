#!/usr/bin/python3.9

def main():
 from ncclient import manager
 device = manager.connect(host='fixpe015', port=830, username='antonio', password='admin', hostkey_verify=False, device_params={}, allow_agent=False, look_for_keys=False)
 print(device)
 get_filter = """
    <native xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<GigabitEthernet>
              <name>1</name>
            </GigabitEthernet>
		</interface> 
    </native>
    """

 nc_get_reply = device.get(('subtree', get_filter))
 print(nc_get_reply)
 print(device.get_schema('ietf-interfaces'))
if __name__ == '__main__':
    main()
    
