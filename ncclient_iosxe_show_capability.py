from ncclient import manager

#router = {"host": "ios-xe-mgmt-latest.cisco.com", "port" : "1000", "username": "antonio", "password": "admin"}

#with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"])

device = manager.connect(host='fixpe015', port=830, username='antonio', password='admin', hostkey_verify=False, device_params={}, allow_agent=False, look_for_keys=False)
print(device)
for capability in device.server_capabilities:
    print('*' * 50)
    print(capability)
