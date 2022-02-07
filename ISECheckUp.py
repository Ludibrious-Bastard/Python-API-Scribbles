import requests
from GetCreds import *
import urllib3
from WhatOS import *
from CheckPing import *
from WebCodeChecker import *
from ISEUploader import * 
import json

def ISECheckUp(username, password):
    urllib3.disable_warnings()
    SystemOS = WhatOS()
    CredPair = username, password
    
    url = "https://172.16.16.250:9060/ers/sdk"

    headers = {
        "accept": "application/json", 
        "ContentType": "application/json", 
    }

    data = {

    }
    print(data)
    print("Checking if ISE is Reachable...")
    ISEStatus = PingCheck("172.16.16.250", SystemOS)
    print(ISEStatus)
    if ISEStatus == "ISE is Reachable":
        print("Checking Log in Info: ...")
        WebRequest = requests.get(url, auth=CredPair, headers=headers, verify=False)
        WebRequest.raise_for_status()
        WebRequest.status_code
    
    return WebRequest.status_code

ISECheckUp("test1996", "Test123")