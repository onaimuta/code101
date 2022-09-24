# This is program says hello and asks for my name.

from turtle import clear


print ("Hello, User!")
print ("What Is your name?: ")
myname = input()
print ('It is good to meet you, ' + myname)
print ('The length of your name is:')
print (len(myname))
print('What is your age?') # ask for their age
myage = input()
print('You will be ' + str(int(myage) + 1) + ' in a year\'s time.')

print ("Thanks for participating!")