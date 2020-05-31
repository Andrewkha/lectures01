import graphics as gr

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

#  Начальное положение шарика
coords = gr.Point(200, 200)
#  Скорость
velocity = gr.Point(1, -2)

# Ускорение
acceleration = gr.Point(1, 1)

def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


def draw_circle(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def check_coords(coords, velocity):
    if coords.x < 10 or coords.x > SIZE_X - 10:
        velocity.x = -velocity.x

    if coords.y < 10 or coords.y > SIZE_Y - 10:
        velocity.y = -velocity.y


while True:

    clear_window()

    draw_circle(coords)
    coords = add(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)

    gr.time.sleep(0.02)
