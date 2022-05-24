#!/usr/bin/python3.9

def main():
 from ncclient import manager
 device = manager.connect(host='mivpe016', port=830, username='antonio', password='admin', hostkey_verify=False, device_params={}, allow_agent=False, look_for_keys=False)
 print(device)
 get_filter = """
             <interfaces xmlns="http://openconfig.net/yang/interfaces">
		<interface>
			<name></name>
			<state>
			  <description></description>
			  <type></type>
			  <counters>
		            <in-octets></in-octets>
             		    <in-pkts></in-pkts>
         		    <out-octets></out-octets>
         		    <out-pkts></out-pkts>
        		  </counters>
			</state>
		</interface> 
             </interfaces>
             """
 nc_get_reply = device.get(('subtree', get_filter))
 print(nc_get_reply)
if __name__ == '__main__':
    main()

