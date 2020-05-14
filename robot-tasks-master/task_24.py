#!/usr/bin/python3

from pyrob.api import *


def fill_cross():
    fill_cell()
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    move_left()
    move_up()
    fill_cell()
    move_down()
    fill_cell()
    move_down()
    fill_cell()


@task
def task_2_1():
    move_down(2)
    move_right()
    fill_cross()
    move_up(2)
    move_left()


if __name__ == '__main__':
    run_tasks()
