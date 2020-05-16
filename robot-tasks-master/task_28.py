#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    step = 0
    while step < 5 and not wall_is_on_the_right():
        if cell_is_filled():
            step += 1
        if step != 5:
            move_right()


if __name__ == '__main__':
    run_tasks()
