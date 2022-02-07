import os 

def Clearscreen():
    if os.name == "nt":
        os.system("clr")
    else:
        os.system("clear")
    