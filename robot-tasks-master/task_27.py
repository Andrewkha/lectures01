#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    move_right()
    fill_cell()

    step = 2
    while not wall_is_on_the_right():
        for move in range(step):
            if not wall_is_on_the_right():
                move_right()
                if move == step - 1 and not wall_is_on_the_right():
                    fill_cell()
        step += 1



if __name__ == '__main__':
    run_tasks()
