# import statistics
from statistics import mean
#import statistics


math = int(input("Math: "))
english = int(input("English: "))
science = int(input("Science: "))
shona = int(input("Shona: "))
markslist =[math, shona, english,science]
avg = mean(markslist)
print (avg)
