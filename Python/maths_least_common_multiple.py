import math

print("Calculates LCM of two numbers \n ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = (math.gcd(a,b))
least_common_multiple = str(a*b/gcd)
print("LCM = "+ least_common_multiple)
input("\nPress enter to continue..")
