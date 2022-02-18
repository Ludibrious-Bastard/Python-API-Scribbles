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
    
    def Get_Access_Interfaces(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command('show int status', use_textfsm=True)
        AccessPortArray = []
        for i in range(len(output)):
            if not output[i]['vlan'] == 'trunk' and not output[i]['vlan'] == 'routed':
                test = output[i]['port']
                AccessPortArray.append(test)
        net_connect.disconnect()
        return AccessPortArray

    def Get_Routed_Interfaces(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command('show int status', use_textfsm=True)
        RoutedPortArray = []
        for i in range(len(output)):
            if output[i]['vlan'] == 'routed':
                test = output[i]['port']
                RoutedPortArray.append(test)
        net_connect.disconnect()
        return RoutedPortArray
    
    def Get_Trunk_Interfaces(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command('show int status', use_textfsm=True)
        TrunkPortArray = []
        for i in range(len(output)):
            if output[i]['vlan'] == 'trunk':
                test = output[i]['port']
                TrunkPortArray.append(test)
        net_connect.disconnect()  
        return TrunkPortArray

    def Get_Interface_Details(self, interface="Gi1/0/1"):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command('show int ' + interface, use_textfsm=True)
        output = str(output)
        cleanedupoutput = output.lstrip("[").rstrip("]")
        finalout = ast.literal_eval(cleanedupoutput)
        net_connect.disconnect()
        return finalout
    
    def GetInterfaceDetails_MTU(self, interface="Gi1/0/1"):
        output = self.GetInterfaceDetails(interface)
        return output['mtu']
    
    def GetInterfaceDetails_Link_Status(self, interface="Gi1/0/1"):
        output = self.GetInterfaceDetails(interface)
        return output['link_status']

    def GetInterfaceDetails_Media(self, interface="Gi1/0/1"):
        output = self.GetInterfaceDetails(interface)
        return output['media_type']

    def GetInterfaceDetails_Bandwidth(self, interface="Gi1/0/1"):
        output = self.GetInterfaceDetails(interface)
        return output['bandwidth']
    
    def GetInterfaceDetails_Duplex(self, interface="Gi1/0/1"):
        output = self.GetInterfaceDetails(interface)
        return output['duplex']

    def GetInterfaceDetails_Speed(self, interface="Gi1/0/1"):
        output = self.GetInterfaceDetails(interface)
        return output['speed']

    def GetInterfaceDetails_CRC_Errors(self, interface="Gi1/0/1"):
        output = self.GetInterfaceDetails(interface)
        return output['crc']

    def GetInterfaceDetails_Input_Errors(self, interface="Gi1/0/1"):
        output = self.GetInterfaceDetails(interface)
        return output['input_errors']
    
    def Get_Interface_Details_Output_Errors(self, interface="Gi1/0/1"):
        output = self.GetInterfaceDetails(interface)
        return output['output_errors']

    def Get_Device_Version(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command("show version",  use_textfsm=True)
        output = str(output)
        cleanedupoutput = output.lstrip("[").rstrip("]")
        finalout = ast.literal_eval(cleanedupoutput)
        net_connect.disconnect()
        return finalout['running_image']

    def Get_Device_Up_Time(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        output = net_connect.send_command("show version",  use_textfsm=True)
        output = str(output)
        cleanedupoutput = output.lstrip("[").rstrip("]")
        finalout = ast.literal_eval(cleanedupoutput)
        net_connect.disconnect()
        return finalout['uptime']

    def SendGlobalConfig(self, Commands=[]):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        for command in tqdm(range(len(Commands)), desc="Sending List of Commands"):
                net_connect.send_command(Commands[command])
        net_connect.disconnect()
                
    def SendConfigFromFile(self, FileName="Path to File"):
        f = open(FileName)
        data = f.read().splitlines()
        f.close()
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        for command in tqdm(range(len(data)), desc="Sending File Contents"):
            net_connect.send_command(data[command])
        net_connect.disconnect()

    def GetPortAuthorization(self, Port="Gi1/0/1"):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        output = net_connect.send_command("Show auth sess int " + Port, use_textfsm=True)
        net_connect.disconnect()
        return output

    def GetCDPNeighbors(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        output = net_connect.send_command("Show cdp neighbors", use_textfsm=True)
        delete = 49 
        output = str(output).split()
        newline = output[delete: len(output) - 6]
        net_connect.disconnect()
        return newline

    def GetDefaultRoute(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        output = net_connect.send_command("Show ip route", use_textfsm=True)
        net_connect.disconnect()
        output = str(output).split()
        return [output[122]]

    def Get_All_Static_Routes(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        output = net_connect.send_command("Show ip route", use_textfsm=True)
        net_connect.disconnect()
        output = str(output).split()
        newlist = output[125:len(output) - 6]
        return newlist

    def SendRangeCommand(self, FirstPort="Gi1/0/1", LastPort=int(2), Commands=[]):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        net_connect.send_command("int " + FirstPort + "-" + str(LastPort))
        for command in tqdm(range(len(Commands)), desc="Send Configs"):
            net_connect.send_command(Commands[command])

    def Get_AAA_Server(self):
        net_connect = ConnectHandler(**self.devicetemplate)
        net_connect.enable()
        net_connect.find_prompt()
        output = net_connect.send_command("sh aaa servers", use_textfsm=True)
        output = str(output)
        Lst = ""
        for i in range(len(output)):
            Lst = output.replace(",", "").replace("-", "").replace(":", "").replace("", "")
        output = Lst.split()
        Id = output[2::204]
        Priority = output[4::204]
        Host = output[6::204]
        AuthPort = output[8::204]
        AcctPort = output[10::204]
        State = output[13::204]
        Duration = output[15::204]
        DeadTime = output[22::204]
        Count = output[24::204]
        Quarantined = output[26::204]
        AuthenticationRequests = output[29::204]
        Timeouts = output[31::204]
        failover = output[33::204]
        Retransmission = output[35::204]
        Response = output[37::204]
        Rejection = output[39::204]
        Challange = output[41::204]
        UnexpcectedResponses = output[44::204]
        ServerError = output[48::204]
        IncorrectRequest = output[50::204]
        return Id, Priority, Host, AuthPort, AcctPort, State, Duration, DeadTime, Count, Quarantined, AuthenticationRequests, Timeouts, failover, Retransmission, Response, Rejection, Challange, UnexpcectedResponses, ServerError, IncorrectRequest
    