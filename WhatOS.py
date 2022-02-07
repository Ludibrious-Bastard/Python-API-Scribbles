import os

def WhatOS():
    if os.name == 'nt':
        OSType = "Windows"
    else:
        OSType = "Linux"
    return OSType