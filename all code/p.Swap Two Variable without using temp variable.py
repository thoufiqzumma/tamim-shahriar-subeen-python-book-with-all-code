""" Swap Two Variable without using temp variable"""
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
print(a,b)
a = a-b
b = a+b
a = b-a
print(a,b)