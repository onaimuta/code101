#Python Test Bench
import datetime
from re import X 
now = datetime.datetime.now()
format =  "%d-%m-%Y %H:%M:%S %Z%z"
print(now.strftime(format))
#Apo is a Shona word!
x=5
X=6
y="Apo"
x=float(5)

print("Hello World!")

if 5 > 2:
    print("Five is greater than two!")
print("Current date and time: ")
print(now.strftime(format))

print(y)
print(X)

def myfunc():
    global X
    x = "fantastic"
print(x)

x = y = z = "Orange"
print(x)
print(y)
print(z)