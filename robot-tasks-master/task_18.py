#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    found = False
    while not wall_is_on_the_left():
        move_left()
        if not wall_is_above():
            found = True
            break

    while not wall_is_on_the_right() and not found:
        move_right()
        if not wall_is_above():
            break
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
