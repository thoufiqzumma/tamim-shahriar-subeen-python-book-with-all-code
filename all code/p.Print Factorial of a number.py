"""Print Factorial of a number!!"""

num = int(input("enter a number: "))
f = 1
for x in range(1,num+1):
   f = f*x
print(f)