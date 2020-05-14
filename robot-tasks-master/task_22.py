#!/usr/bin/python3

from pyrob.api import *


def draw_right():
    while not wall_is_on_the_right():
        move_right()
        fill_cell()


def get_back():
    while not wall_is_on_the_left():
        move_left()

# @task
# def task_5_10():
#     while not wall_is_beneath():
#         fill_cell()
#         draw_right()
#         get_back()
#         move_down()
#     else:
#         fill_cell()
#         draw_right()
#         get_back()

@task
def task_5_10():
    while True:
        fill_cell()
        draw_right()
        get_back()
        if not wall_is_beneath():
            move_down()
        else:
            break

if __name__ == '__main__':
    run_tasks()
