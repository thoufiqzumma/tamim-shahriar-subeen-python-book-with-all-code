break_program = False
while not break_program:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    while True:
         string = input("Enter add/sub for program and quit to exit: ")
         if string=="quit":
             break_program = True
             break
         if string == "add":
             print(num1+num2)
             break
         if string =="sub":
             print(num1-num2)
             break