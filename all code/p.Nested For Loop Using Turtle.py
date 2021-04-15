import turtle

turtle.shape("turtle")
turtle.speed(1)

for side_length in range(10,60,10):
     print(side_length)
     for x in range(4):
         turtle.forward(side_length)
         turtle.left(90)
turtle.exitonclick()