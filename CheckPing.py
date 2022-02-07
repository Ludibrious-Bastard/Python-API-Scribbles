import os 

def PingCheck(IPAddress, OSType):

    hostname = IPAddress
    if OSType == "Windows":
        response = os.system("ping -n 1 " + str(hostname) + " > NUL")
    elif OSType == "Linux":
        response = os.system("ping -c 1 " + str(hostname) + " > /dev/null")
    
    if response == 0:
        Status = str(IPAddress) + ' is Reachable'
    else:
        Status = str(IPAddress) + ' is Not Reachable'
    return response
