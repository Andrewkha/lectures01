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

# turtle.shape('turtle')
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)

# circle


def circle(radius, n=100):
    turtle.shape("turtle")
    for step in range(0, n):
        turtle.forward(2 * pi * radius / n)
        turtle.left(360 / n)


