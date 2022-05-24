from ncclient import manager
import xml.dom.minidom

#router = {"host": "ios-xe-mgmt-latest.cisco.com", "port" : "1000", "username": "antonio", "password": "admin"}

#with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"])

device = manager.connect(host='fixpe015', port=830, username='antonio', password='admin', hostkey_verify=False, device_params={}, allow_agent=False, look_for_keys=False)

netconf_filter = """
<filter>
 <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>Port-channel1</interface>
 </interfaces>
 <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>Port-channel1</interface>
 </interfaces-state>
</filter>
"""

get_filter = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE">
 <interface>
  <GigabitEthernet>
   <name>1</name>
  </GigabitEthernet>
 </interface>
</native>
"""
print(device.get_schema('ietf-ip'))
print(device.get_schema('ietf-interfaces'))
interface_netconf = device.get(('subtree', netconf_filter))
xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
print(xmlDom.toprettyxml(indent="   ")) 
print('*' * 25 + 'Break' + '*' * 50)
device.close_session()
