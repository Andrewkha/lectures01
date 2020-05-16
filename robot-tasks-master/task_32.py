#!/usr/bin/python3

from pyrob.api import *


def is_corridor():
    return not wall_is_above()


def fill_corridor():
    found = 0
    while not wall_is_above():
        move_up()
        if not cell_is_filled():
            fill_cell()
        else:
            found += 1
    while not wall_is_beneath():
        move_down()

    return found


@task(delay=0.01)
def task_8_18():
    filled = 0
    while not wall_is_on_the_right():
        if is_corridor():
            filled += fill_corridor()
        else:
            fill_cell()
        move_right()
    while wall_is_beneath():
        move_left()
    ax = 0
    mov('ax', filled)

if __name__ == '__main__':
    run_tasks()
