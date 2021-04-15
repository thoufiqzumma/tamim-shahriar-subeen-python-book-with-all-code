res = 0
for num in range(1,101):
     if num%5==0:
         res = res + num
         print(num)
print(res)  #Output will be  5,10..95,100 and another is 1050
print("another code")
res = 0
for num in range(5,101,5):
    res = res + num
    print(num)
print(res)