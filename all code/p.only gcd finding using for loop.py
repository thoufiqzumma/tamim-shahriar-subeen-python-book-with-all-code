"""only gcd finding using for loop"""

for x in num1,num2:
     if num2!=0:
         num1,num2 = num2,(num1%num2)  
print(num1)