"""only gcd finding using while loop"""
import math
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
while num2!=0:
     rem = num1 % num2
     num1 = num2
     num2 = rem
print(num1)