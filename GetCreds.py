from getpass import getpass

def GetCreds():
    username = input("Please Enter Username: ")
    password = getpass("Please Enter Password: ")
    return username, password