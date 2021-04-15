def mul_table(number):
    try:
        if number:
             for i in range(1,11):
                 var = int(number)*i
                 print(var)
    except:
             for x in range(1,11):
                 res = 1*x
                 print(res)

number = input("Enter Number Or Another Input: ")

mul_table(number)