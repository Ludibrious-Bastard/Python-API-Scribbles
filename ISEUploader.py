import requests
from GetCreds import *
import urllib3
from WhatOS import *
from CheckPing import *
from WebCodeChecker import *



def ISEUploader(username, password, statuscode):
    urllib3.disable_warnings()
    SystemOS = WhatOS()
    CredPair = username, password
    
    url = "https://172.16.16.250:9060/ers/sdk"

    headers = {
        "accept": "application/json", 
        "ContentType": "application/json", 
    }
    
    WebRequest = requests.get(url, auth=CredPair, headers=headers, verify=False)
    