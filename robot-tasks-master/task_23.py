#!/usr/bin/python3

from pyrob.api import *


def is_corridor():
    return not wall_is_above()


def fill_corridor():
    while not wall_is_above():
        move_up()
        fill_cell()
    while not wall_is_beneath():
        move_down()


@task(delay=0.01)
def task_6_6():
    while not wall_is_on_the_right():
        move_right()
        if is_corridor():
            fill_corridor()
    while wall_is_beneath():
        move_left()


if __name__ == '__main__':
    run_tasks()
