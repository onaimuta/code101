import datetime
from re import X 
now = datetime.datetime.now()
format =  "%d-%m-%Y %H:%M:%S %Z%z"
print(now.strftime(format))

if 5 > 2:
    print("Five is greater than two!")
    print("Current date and time is "+now.strftime(format))