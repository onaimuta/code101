import math

print("Calculates GCD of two numbers \n ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
greatest_common_denomenator = str(math.gcd(a,b)) #calculates the greatest common denominator from given two numbers
print("GCD = "+ greatest_common_denomenator)
input("\nPress enter to continue..")