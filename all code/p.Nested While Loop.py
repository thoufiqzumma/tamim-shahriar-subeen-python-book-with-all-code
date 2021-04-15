terminate_program = False
while not terminate_program:
     number1 = int(input("enter a number: "))
     number2 = int(input("enter another number: "))
     while True:
         operation = input("please enter sub/add or quit to exit the program: ")
         if operation=="quit":
             terminate_program=True
             break
         if operation not in ["add","sub"]:
            print("continue")
         continue
         if operation=="add":
             print(number1+number2)
             break
         if operation=="sub":
             print(number1-number2)
             break


while True:
     num = int(input("enter a number: "))
     if num<0:
         print("Please enter positive number!!")
         continue
     if num==0:
         break
     print(num*num)
number = int(input("number: "))
def sum(number):
     res = 0
     for x in range(number+1):
         res = res+x
     return res
var = sum(number)
print(var)