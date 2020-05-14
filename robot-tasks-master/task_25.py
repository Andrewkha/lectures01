#!/usr/bin/python3

from pyrob.api import *
from task_24 import fill_cross


@task
def task_2_2():
    for one in range(5):
        move_down(2)
        fill_cross()
        if one != 4:
            move_right(3)
            move_up(3)
    move_left()
    move_up(2)

if __name__ == '__main__':
    run_tasks()
