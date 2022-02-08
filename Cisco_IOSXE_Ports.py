from netmiko import ConnectHandler
from tqdm import tqdm 
import ast

class API(object):
    def __init__(self, username, password, IPAddress, devicetype):
        self.devicetemplate = devicetype
        self.IPAddress = IPAddress
        self.password = password
        self.username = username
    
        self.devicetemplate = { 
        'device_type': self.devicetemplate,
        'host': self.IPAddress, 
        'username': self.username, 
        'password': self.password, 
        }  
    
    def FindAccessInterfaces(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command('show int status', use_textfsm=True)
        AccessPortArray = []
        for i in range(len(output)):
            if not output[i]['vlan'] == 'trunk' and not output[i]['vlan'] == 'routed':
                test = output[i]['port']
                AccessPortArray.append(test)
    
        return AccessPortArray


    def FindRoutedInterfaces(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command('show int status', use_textfsm=True)
        RoutedPortArray = []
        for i in range(len(output)):
            if output[i]['vlan'] == 'routed':
                test = output[i]['port']
                RoutedPortArray.append(test)
            
        return RoutedPortArray
    

    def FindTrunkInterfaces(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command('show int status', use_textfsm=True)
        TrunkPortArray = []
        for i in range(len(output)):
            if output[i]['vlan'] == 'trunk':
                test = output[i]['port']
                TrunkPortArray.append(test)
            
        return TrunkPortArray

    def GetInterfaceDetails(self, interface="Gi1/0/1"):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command('show int ' + interface, use_textfsm=True)
        output = str(output)
        cleanedupoutput = output.lstrip("[").rstrip("]")
        finalout = ast.literal_eval(cleanedupoutput)
        return finalout

    def GetDeviceVersion(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command("show version",  use_textfsm=True)
        output = str(output)
        cleanedupoutput = output.lstrip("[").rstrip("]")
        finalout = ast.literal_eval(cleanedupoutput)
        return finalout['running_image']

    def GetDeviceUpTotal(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command("show version",  use_textfsm=True)
        output = str(output)
        cleanedupoutput = output.lstrip("[").rstrip("]")
        finalout = ast.literal_eval(cleanedupoutput)
        return finalout['uptime']

    def SendGlobalConfig(self, Commands=[]):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        for command in tqdm(range(len(Commands)), desc="Sending List of Commands"):
                net_connect.send_command(Commands[command])
                
    
    def SendConfigFromFile(self, FileName="Path to File"):
        f = open(FileName)
        data = f.read().splitlines()
        f.close()
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        for command in tqdm(range(len(data)), desc="Sending File Contents"):
            net_connect.send_command(data[command])

    def GetPortAuthorization(self, Port="Gi1/0/1"):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        output = net_connect.send_command("Show auth sess int " + Port, use_textfsm=True)
        return output

    def GetCDPNeighbors(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        output = net_connect.send_command("Show cdp neighbors", use_textfsm=True)
        return output
    
    def SendRangeCommand(self, FirstPort="Gi1/0/1", LastPort=int(2), Commands=[]):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        net_connect.send_command("int " + FirstPort + "-" + str(LastPort))
        for command in tqdm(range(len(Commands)), desc="Send Configs"):
            net_connect.send_command(Commands[command])