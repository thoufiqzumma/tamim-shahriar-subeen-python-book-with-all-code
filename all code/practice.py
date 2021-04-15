# URI-ONLINE-JUDGE
# PROBLEM-NO:1002
# n = 3.14159
# R = float(input())
# A = n*R**2
# print("A=",float("{0:.4f}".format(A)))

# URI-ONLINE-JUDGE
# PROBLEM-NO:1002
# n = 3.14159
# R = float(input())
# A = n*(R*R)
# print(f'A={A:.4f}')

'''
Math library function here
'''
# from math import *
# print(max(20,10))
# print(min(20,10))
# print(abs(-5))
# print(pow(2,3))
# print(sqrt(25))
# print(round(3.8))
# print(ceil(3.4))
# print(floor(3.7))

'''
fstring application. formatted string
'''
# num1 = 20
# num2 = 50
# print(f"{num1} + {num2} = {num1+num2}")

'''
end=" " function to remove new line and print in the same line
'''
# print('Tareq Hasan Remon', end=" ")
# print('01741280765')


"""
Centigrade to Farenhite  formula is c/5=(f-32)/9=(k-273)/5
"""
# centigrade = float((input("enter a number: ")))
# Farenhite = (1.8*centigrade)+32
# print(f'Farenhite={Farenhite:.2f}')

""" Swap Two Variable using temp variable"""
# a = int(input("enter 1st: "))
# b = int(input("enter 2nd: "))
# print("Before Swapping", a,b)
# c = a
# a = b
# b = c
# print("After Swapping", a,b)
""" Swap Two Variable without using temp variable"""
# a = int(input("enter 1st number: "))
# b = int(input("enter 2nd number: "))
# print(a,b)
# a = a-b
# b = a+b
# a = b-a
# print(a,b)


""" Multiplication Table"""

# num = int(input("enter a number: "))

# for x in range(1,11):
#     v = num*x
#     print(f"{num} x {x} = {v}")


"""Print Factorial of a number!!"""

# num = int(input("enter a number: "))
# f = 1
# for x in range(1,num+1):
#     f = f*x
# print(f)


"""Prime Number Check"""

# num = int(input("enter a number: "))

# if num > 1:
#     for x in range(2,num):
#         if num%x==0:
#             print(num,"Is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")

# else:
#     print(num,"is a prime number")
    
"""GCD and LCM Value"""

# # import math
# num1 = int(input("First Number: "))
# num2 = int(input("Second Number: "))

# LCM = (num1*num2)/12
# print(LCM)

# x = math.gcd(num1,num2)
# print(x)
"""GCD and LCM Value"""

"""only gcd finding using while loop"""
# while num2!=0:
#     rem = num1%num2
#     num1 = num2
#     num2 = rem
# print(num1)
"""only gcd finding using while loop"""

"""only gcd finding using for loop"""
# for x in num1,num2:
#     if num2!=0:
#         num1,num2 = num2,(num1%num2)  
# print(num1)
"""only gcd finding using for loop"""


""" Nested For Loop Using Turtle"""

# import turtle

# turtle.shape("turtle")
# turtle.speed(1)

# for side_length in range(10,60,10):
#     print(side_length)
#     for x in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)
# turtle.exitonclick()
""" Nested For Loop  Using Turtle"""

"""Nested while Loop  Using Turtle"""

# import turtle
# turtle.shape("turtle")
# turtle.color('red')
# turtle.speed(7)

# counter = 0
# while counter < 36:
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.right(10)
#     counter+=1
"""Nested while Loop  Using Turtle"""

"""Nested While Loop"""

# terminate_program = False
# while not terminate_program:
#     number1 = int(input("enter a number: "))
#     number2 = int(input("enter another number: "))
#     while True:
#         operation = input("please enter sub/add or quit to exit the program: ")
#         if operation=="quit":
#             terminate_program=True
#             break
#         if operation not in ["add","sub"]:
#             print("continue")
#             continue
#         if operation=="add":
#             print(number1+number2)
#             break
#         if operation=="sub":
#             print(number1-number2)
#             break


# while True:
#     num = int(input("enter a number: "))
#     if num<0:
#         print("Please enter positive number!!")
#         continue
#     if num==0:
#         break
#     print(num*num)

# number = int(input("number: "))
# def sum(number):
#     res = 0
#     for x in range(number+1):
#         res = res+x
#     return res
# var = sum(number)
# print(var)


""" mul_table for enter a number and otherwise print the mul_table for 1"""

# def mul_table(number):
#     try:
#         if number:
#             for i in range(1,11):
#                 var = int(number)*i
#                 print(var)
#     except:
#         for x in range(1,11):
#             res = 1*x
#             print(res)

# number = input("Enter Number Or Another Input: ")

# mul_table(number)
