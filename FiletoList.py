
def ListGenerator(Filein):
    details= []
    try:
        data = open(Filein, "r")
        datacontent = data.read().splitlines()
        data.close()
        #load the contents into a list
        for i in datacontent:
            details.append(i)
        return details

    except:
        print("File Not Found.")
        pass