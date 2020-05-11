import turtle
from math import pi

# S letter
#
# turtle.shape('turtle')
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)

# square


def square(side):
    turtle.shape('turtle')
    for step in range(0, 4):
        turtle.forward(side)
        turtle.left(90)

# circle


def circle(radius, n=100):
    turtle.shape("turtle")
    for step in range(0, n):
        turtle.forward(2 * pi * radius / n)
        turtle.left(360 / n)


def mult_squares(step, side):
    x, y = turtle.position()
    for _ in range(0, step):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        square(side)
        x, y = x - 5, y - 5
        side += 10


def spider(n):
    turtle.shape("turtle")
    for _ in range(0, n):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.left(360 / n)
        turtle.forward(100)
        turtle.stamp()


spider(10)