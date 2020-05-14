#!/usr/bin/python3

from pyrob.api import *


def draw_right_line():
    for step in range(26):
        fill_cell()
        move_right()

def draw_left_line():
    for step in range(26):
        fill_cell()
        move_left()


@task(delay=0.05)
def task_4_3():
    move_right()
    for row in range(6):
        draw_right_line()
        fill_cell()
        move_down()
        fill_cell()
        draw_left_line()
        fill_cell()
        move_down()

if __name__ == '__main__':
    run_tasks()
