import turtle
from math import pi, sin, radians

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
        turtle.left(360 / n)
        turtle.forward(2 * pi * radius / n)


def opposite_circle(radius, n=100):
    turtle.shape("turtle")
    for step in range(0, n):
        turtle.right(360 / n)
        turtle.forward(2 * pi * radius / n)


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


def square_spiral():
    side = 5
    turtle.shape("turtle")
    for _ in range(0, 100):
        turtle.forward(side)
        turtle.left(90)
        side += 5


def get_radius(side, n):
    return side / (2 * sin(360 / (2 * n)))


def get_side(radius, n):
    return radius * 2 * sin(radians(360 / (2 * n)))


def n_cornerer(n, side):
    turtle.shape("turtle")
    corner = 180 * (n - 2) / n
    turtle.left(180 - corner / 2)
    for _ in range(0, n):
        turtle.forward(side)
        turtle.left(360 / n)


def mult_cornerers(count, radius):
    for n in range(3, count + 1):
        side = get_side(radius, n)
        turtle.penup()
        turtle.goto(radius, 0)
        turtle.right(turtle.heading())
        turtle.pendown()
        n_cornerer(n, side)
        radius += 10


def flower():
    circle(50, 50)
    opposite_circle(50, 50)
    turtle.left(60)
    circle(50, 50)
    opposite_circle(50, 50)
    turtle.left(60)
    circle(50, 50)
    opposite_circle(50, 50)


def butterfly():
    for radius in range(10, 100, 10):
        circle(radius, 50)
        opposite_circle(radius, 50)


butterfly()