#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    for row in range(1, 14):
        for step in range(row):
            move_right()
            fill_cell()
        move_left(row)
        move_down()
    move_right()
if __name__ == '__main__':
    run_tasks()
