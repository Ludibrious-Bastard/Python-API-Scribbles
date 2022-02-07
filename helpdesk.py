from urllib.parse import urlencode
from xxlimited import new

from numpy import character
import HelpdeskAPI 
import ast
import requests
import urllib3
import urllib.parse

def HelpdeskToDict(d):
    input1 = str(d)
    input2 = ""
    for i in input1:
        input2 = input1.replace("'", "\"").replace("(", "").replace(")", "")
    new_dict = ast.literal_eval(input2)
    new_list = list(new_dict)
    listoftickets = []
    for i in range(len(new_list)):
        if not new_list[i]['id'] == int():
            test = new_list[i]['id']
            listoftickets.append(test)
    return listoftickets

def ListOfTicketsbyName(name="", api=""):
    urllib3.disable_warnings()
    test = urllib.parse.quote(name)
    url = "http://172.16.16.16/helpdesk/WebObjects/Helpdesk.woa/ra/Tickets?list=mine&qualifier=(location.locationName%3D'" + test + "')"+"&apiKey=" + api



    r = requests.get(url, verify=False)
    return HelpdeskToDict(r.json())
    

test = ListOfTicketsbyName("testsite", "WATKxxRVM0x5jpsUHxdMMCWDTxTzjWtG50ke54Id")
print(test)

