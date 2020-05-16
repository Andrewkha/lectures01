#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while True:
        count = 0

        while not wall_is_on_the_right():
            move_right()
            if not wall_is_beneath():
                move_down()
                count = 0
                break

        if wall_is_on_the_right():
            count = 1

        while not wall_is_on_the_left():
            move_left()
            if not wall_is_beneath():
                move_down()
                count = 0
                break

        if wall_is_on_the_left():
            count += 1

        if wall_is_on_the_left() and wall_is_beneath() and count > 1:
            break



if __name__ == '__main__':
    run_tasks()
