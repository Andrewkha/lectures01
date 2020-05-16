#!/usr/bin/python3

from pyrob.api import *


def get_dimension():
    count = 1
    while not wall_is_on_the_right():
        move_right()
        count += 1
    move_left(count - 1)
    return count


def go_finish():
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()


@task(delay=0.01)
def task_9_3():
    dimension = get_dimension()
    rounds = int((dimension - 1) / 2)

    for one_round in range(rounds):
        for _ in range(dimension - 2):
            move_right()
            fill_cell()
        move_right()
        for _ in range(dimension - 2):
            move_down()
            fill_cell()
        move_down()
        for _ in range(dimension - 2):
            move_left()
            fill_cell()
        move_left()
        for _ in range(dimension - 2):
            move_up()
            fill_cell()
        move_right()

        dimension -= 2

    go_finish()




if __name__ == '__main__':
    run_tasks()
