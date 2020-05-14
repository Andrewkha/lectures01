#!/usr/bin/python3

from pyrob.api import *
from task_24 import fill_cross


def draw_row():
    for step in range(10):
        move_down()
        fill_cross()
        if step != 9:
            move_right(3)
            move_up(2)
        else:
            move_up(2)
            move_left()


@task(delay=0.02)
def task_2_4():
    for one in range(5):
        draw_row()
        if one != 4:
            move_down(4)
        while not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()
