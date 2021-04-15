"""GCD and LCM Value"""

import math
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

LCM = (num1*num2)/12
print(LCM)

x = math.gcd(num1,num2)
print(x)