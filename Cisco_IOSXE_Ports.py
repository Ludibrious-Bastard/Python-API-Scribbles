from operator import contains
from netmiko import ConnectHandler


def FindNonRoutedPorts(username, password, IPAddress, DeviceType,):
    cisco = { 
   'device_type': DeviceType, 
   'host': IPAddress, 
   'username': username, 
   'password': password, 
   }  

    net_connect = ConnectHandler(**cisco)
    output = net_connect.send_command('show int status', use_textfsm=True)
    PortArray = []
    for i in range(len(output)):
        if not output[i]['vlan'] == 'trunk' and not output[i]['vlan'] == 'routed' and not output[i]["port"].find("Gi") :
            test = output[i]['port']
            PortArray.append(test)
    
    return PortArray


def FindAccessPort(username, password, IPAddress, DeviceType):
    cisco = { 
   'device_type': DeviceType, 
   'host': IPAddress, 
   'username': username, 
   'password': password, 
   }  

    net_connect = ConnectHandler(**cisco)
    output = net_connect.send_command('show int status', use_textfsm=True)
    PortArray = []
    for i in range(len(output)):
        if not output[i]['vlan'] == 'routed' and not output[i]["vlan"].find("trunk") :
            test = output[i]['port']
            PortArray.append(test)
            
    return PortArray
    

def FindTrunkPorts(username, password, IPAddress, DeviceType):
    cisco = { 
   'device_type': DeviceType, 
   'host': IPAddress, 
   'username': username,
   'password': password, 
   }  

    net_connect = ConnectHandler(**cisco)
    output = net_connect.send_command('show int status', use_textfsm=True)
    l = len(output)
    PortArray = []
    for i in range(0,l):
        if output[i]['vlan'] == 'trunk':
            test = output[i]['port']
            PortArray.append(test)
            
    return PortArray
    