from datetime import datetime
now = datetime.now()
print ("The day is: ", now.strftime("%d-%m-%y"))
print ("********************************************************")
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
from concurrent.futures.process import _check_system_limits
import os, platform
from socket import socket
print ("--------------------------------------------------------")
# print ("The current working dir is: ", os.getcwd())
print ("No. of CPU cores is: ",os.cpu_count())
print ("The logged on user is: ", os.getlogin())
print ("The machine Architecture is: ", platform.architecture())
print ("The current CPU is: ", platform.processor())
print ("The OS is: ", platform.system())
print ("The hostname is: ", platform.node())
print("--------------------- The End ---------------------------")