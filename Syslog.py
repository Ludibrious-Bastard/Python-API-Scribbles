import logging
import logging.handlers
from syslog import LOG_INFO


#**	SEVERITY IN EVENT	Default SMS setting for Syslog Security option. This setting will send all events to remote Syslog system
#0	EMERGENCY	A "panic" condition - notify all tech staff on call? (Earthquake? Tornado?) - affects multiple apps/servers/sites.
#1	ALERT	Should be corrected immediately - notify staff who can fix the problem - example is loss of backup ISP connection.
#2	CRITICAL	Should be corrected immediately, but indicates failure in a primary system - fix CRITICAL problems before ALERT - example is loss of primary ISP connection.
#3	ERROR	Non-urgent failures - these should be relayed to developers or admins; each item must be resolved within a given time.
#4	WARNING	Warning messages - not an error, but indication that an error will occur if action is not taken, e.g. file system 85% full - each item must be resolved within a given time.
#5	NOTICE	Events that are unusual but not error conditions - might be summarized in an email to developers or admins to spot potential problems - no immediate action required.
#6	INFORMATIONAL	Normal operational messages - may be harvested for reporting, measuring throughput, etc. - no action required.
#7	DEBUG	Info useful to developers for debugging the app, not useful during

def Syslog_Forwarder(Facility, username, IPAddress, Message):
    my_logger = logging.getLogger("MyLogger")
    syslog_handler = logging.handlers.SysLogHandler(address=("172.16.16.16", 514))
    my_logger.addHandler(syslog_handler)
    if Facility == 7:       
        my_logger.setLevel(logging.DEBUG)
        my_logger.debug("Switch Config Kit V2.0:  " + "User: " + username + " Configured: " + IPAddress + " Command: " + str(Message))
    
    if Facility == 6:
        my_logger.setLevel(logging.INFO)
        my_logger.info("User: " + username + " Configured: " + IPAddress + " Command: " + str(Message))

    if Facility == 4:
        my_logger.setLevel(logging.WARNING)
        my_logger.warning("User: " + username + " Configured: " + IPAddress + " Command: " + str(Message))

    
araay = ["this is a test", "this is also a test"]
length = len(araay)

for i in range(length):
    username = "Chris.Hillen.sa"
    IPAddress = "172.1.1.1"
    Syslog_Forwarder(4, username, IPAddress, araay[i])

