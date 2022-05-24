#!/usr/bin/python3.7
from ncclient import manager
device = manager.connect(host='mivpe035', port=830, username='antonio', password='admin', hostkey_verify=False, device_params={}, allow_agent=False, look_for_keys=False)
print(device)
get_filter = """
<config>
<bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-bgp-cfg"> 
   <instance> 
    <instance-name>default</instance-name> 
    <instance-as> 
     <as>0</as> 
     <four-byte-as> 
      <as>65000</as> 
      <bgp-running></bgp-running> 
      <default-vrf> 
       <global> 
        <router-id>60.1.1.1</router-id> 
        <global-afs> 
         <global-af> 
          <af-name>ipv4-unicast</af-name> 
          <enable></enable> 
         </global-af> 
        </global-afs> 
       </global> 
       <bgp-entity> 
        <neighbors> 
         <neighbor> 
          <neighbor-address>50.1.1.1</neighbor-address> 
          <remote-as> 
           <as-xx>0</as-xx> 
           <as-yy>65000</as-yy> 
          </remote-as> 
          <update-source-interface>Loopback0</update-source-interface> 
          <neighbor-afs> 
           <neighbor-af> 
            <af-name>ipv4-unicast</af-name> 
            <activate></activate> 
           </neighbor-af> 
          </neighbor-afs> 
         </neighbor> 
        </neighbors> 
       </bgp-entity> 
      </default-vrf> 
     </four-byte-as> 
    </instance-as> 
   </instance> 
  </bgp>
</config>
"""
nc_get_reply = device.get(('subtree', get_filter))
#print(etree.tostring(nc_get_reply.data, pretty_print=True))
print(nc_get_reply.xml)
print(nc_get_reply)
