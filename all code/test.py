"""If else"""

# saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]

# country = input("enter contry name: ")

# if country in saarc:
#     print(country, "is a part of saarc")
# else:
#     print(country, "is not a member of saarc")



""" Letter Grade"""
# marks = int(input("enter your marks: "))

# if marks>=80:
#     grade = 'A+'
# elif marks>=70:
#     grade = 'A'
# elif marks>60:
#     grade = 'A-'
# elif marks>50:
#     grade = 'B+'
# elif marks>40:
#     grade = 'B'
# else:
#     grade = "F"

# print("Your grade is", grade)


"""Positive and Negative Number"""

# num = int(input("enter a number: "))

# if num>=0:
#     print("positive number")
# else:
#     print("Number is negative")

"""Leap year Calculation"""

# year = int(input("Enter a year: "))
# if year%4==0 or year%400==0 and year%100!=0:
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")

"""even and odd finding"""
# num = int(input("enter a number: "))
# if num%2==0:
#     print("Even Number")
# elif num%2!=0:
#     print("Not even number")


"""Python Game"""
# import random
# num = int(input("enter a number: "))
# x = random.randint(1,10)
# print("User Input Number",num)
# print("Random Number", x)
# if num==x:
#     print("Hurrah! Joy Bangla")
# else:
#     print("Joy Sir IS MC")


""" Turtle Graphical Works"""
# import turtle
# turtle.forward(100)
# turtle.exitonclick()

""" Somobahu Trivuj or Equilateral triangle using Turtle"""

# import turtle
# turtle.shape("turtle")
# turtle.speed(1)

# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)

# turtle.exitonclick()
"""Turtle using Loop,,,,, Somobahu Trivuj or Equilateral triangle"""
# for x in range(3):
#     turtle.forward(100)
#     turtle.left(120)
# turtle.exitonclick()
"""Turtle using Loop,,,,, Somobahu Trivuj or Equilateral triangle"""

"""Choturvuj or Quadrilateral Using Turtle using loop"""
# for x in range(4):
#     turtle.forward(100)
#     turtle.left(90)
# turtle.exitonclick()
"""Choturvuj or Quadrilateral Using Turtle using loop"""

# res = 0
# for x in range(10):
#     res = res+1
# print(res) #Output is 10


# res = 0
# for x in range(1,51):
#     res = res+x
# print(res) #output is 1275


"""Need to be very clear loop concept"""

# result = 0
# num = 1
# for i in range(4):
#     result = result + num
#     num = num + 1
# print(num)
# print(result)
"""Need to be very clear loop concept"""

""" Same two problem solution with loop"""
# res = 0
# for num in range(1,101):
#     if num%5==0:
#         res = res + num
#         print(num)
# print(res) #Output will be  5,10..95,100 and another is 1050

# res = 0
# for num in range(5,101,5):
#     res = res + num
#     print(num)
# print(res)
""" Same two problem solution with loop"""

"""Nested While Loop"""
# break_program = False
# while not break_program:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     while True:
#         string = input("Enter add/sub for program and quit to exit: ")
#         if string=="quit":
#             break_program = True
#             break
#         if string == "add":
#             print(num1+num2)
#             break
#         if string =="sub":
#             print(num1-num2)
#             break
"""Nested While Loop end"""

# def add_number(numbers):
#     res = 0
#     for x in numbers:
#         res = res + x
#     return res
# var = add_number([1,3,5,7,9])
# print(var)









