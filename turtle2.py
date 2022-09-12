import turtle

turtle.speed(100)

h = 1
d = 1

def makeASquare():
        turtle.goto(-h, -h)
        turtle.pendown()
        turtle.forward(d)
        turtle.left(90)
        turtle.forward(d)
        turtle.left(90)
        turtle.forward(d)
        turtle.left(90)
        turtle.forward(d)
        turtle.left(90)
        turtle.penup()

for x in range(50):
    makeASquare()
    h = h + 4
    d = d + 8

turtle.exitonclick()