# import statistics
from statistics import mean
#import statistics
math = int(input("Math Score: "))
english = int(input("English Score: "))
science = int(input("Science Score: "))
shona = int(input("Shona Score: "))
markslist =[math, shona, english,science]
grades = []
avg = mean(markslist)
print (avg)