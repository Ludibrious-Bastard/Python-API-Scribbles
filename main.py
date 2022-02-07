from GetInfo import GetInfo
from SendConfigs import SendConfig
from StartingMenu import *

def begin():
    model, IPAddress, username, password = GetInfo()
    SendConfig(username, password, IPAddress, model)


begin()
