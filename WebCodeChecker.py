
def WebResponseCode(statuscode):
    Codes = {200: "Completed", 201: "Device Created", 401: "Unauthorized", 404: "Url Not Found", 405: "Method Not Allowed", 500: "Internal Server Error"}
    
    return Codes.get(statuscode)

