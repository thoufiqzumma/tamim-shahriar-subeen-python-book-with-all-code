num = int(input("enter a number: "))

if num > 1:
     for x in range(2,num):
         if num%x==0:
             print(num,"Is not a prime number")
             break
     else:
         print(num,"is a prime number")

else:
     print(num,"is a prime number")