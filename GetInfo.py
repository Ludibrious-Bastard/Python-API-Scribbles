from getpass import getpass
import ipaddress
from statistics import mode
from StartingMenu import startmenu
from Utilities import *

def GetInfo():
    model = input("Please Enter model: ")
    if model == "1":
            model = "cisco_ios"
    else:
        print("Not A Valid Selection..")
        input("Press Any Key to Continue")
        Clearscreen()
        startmenu()
        GetInfo()
        
    IPAddress = input("Please Enter IP Address (v4): ")
    try:
        test = ipaddress.IPv4Address(IPAddress)
    except:
        print("Not a Valid IP Address...")
        input("Press Any Key to Continue")
        Clearscreen()
        startmenu()
        GetInfo()
    try:
        username = input("Please Enter Username: ")
        password = getpass("Please Enter Password: ")

    except:
        print("Did not Enter Username or Password")
        Clearscreen()
        startmenu()
        GetInfo()
    return [model, IPAddress, username, password]