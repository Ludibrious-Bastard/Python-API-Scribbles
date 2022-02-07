import ipaddress
from netmiko import ConnectHandler
from tqdm import tqdm
import Cisco_IOSXE_Ports
from GetCreds import GetCreds
from CheckPing import *
from WhatOS import *
from Syslog import *


def SendConfig(username, password, IPAddress, DeviceType,):
    OStype = WhatOS()
    Result = PingCheck(IPAddress, OStype)
    print("Checking if Device is Reachable...")
    if Result == 0:
        print("Able to reach device")
    #Get a list of Access ports from the switch.
        print("Fetching Access Ports from Device") 
        IPs = Cisco_IOSXE_Ports.FindNonRoutedPorts(username, password, IPAddress, DeviceType)
    
        details = []
        command=[]

        print("Generating Command Set...")
    #load conetent of what we want to send to EACH access port
        try:
            data = open("details.txt", "r")
            datacontent = data.read().splitlines()
            data.close()
        except:
            print("File Not Found.")
            pass
    
    #load the contents into a list
        for i in datacontent:
            details.append(i)

    #now we want a nested loop to append the contents of each switchport in bewtween the list of ports we got from the switch...
        for port in range(len(IPs)):
            IP = "int " + IPs[port]
            command.append(IP)
            for i in range(len(details)):
                    test = details[i]
                    command.append(test)
        

    #Device connection Template
        cisco = { 
        'device_type': DeviceType, 
        'host': IPAddress, 
        'username': username, 
        'password': password,
        'session_log': "OutputFor" + IPAddress + ".txt",
        'fast_cli': True,
        'global_delay_factor': 1,
        }  
        print("Uploading Config to Device...")
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        net_connect.find_prompt()
        net_connect.config_mode()
        for i in tqdm(range(len(command)), desc='Sending Interface Config: '):
            net_connect.find_prompt()
            net_connect.send_command(command[i], expect_string="#")
            Syslog_Forwarder(4, username, IPAddress, "Sent Command: " + command[i])
        net_connect.save_config()
        net_connect.disconnect()
        print("Device Completed...")
    else:
        print("Device is not reachable via Ping")
        pass
    

