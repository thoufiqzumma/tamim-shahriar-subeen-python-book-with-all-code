""" Multiplication Table"""

num = int(input("enter a number: "))

for x in range(1,11):
     v = num*x
     print(f"{num} x {x} = {v}")