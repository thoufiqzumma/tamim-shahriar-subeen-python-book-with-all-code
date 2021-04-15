import turtle
turtle.shape("turtle")
turtle.speed(1)
res = 0
for x in range(10):
    res = res+1
print(res) #Output is 10


res = 0
for x in range(1,51):
    res = res+x
print(res) #output is 1275
turtle.exitonclick()