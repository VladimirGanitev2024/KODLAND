import random
from turtle import *

shape("circle")
speed(4)
pensize(4)
Screen().bgcolor("turquoise")
colours = ["blue", "purple", "cyan", "white", "yellow", "green", "orange"]


def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)


def showflakeArm(size):
    for x in range(0, 4):
        forward(size)
        vshape(size)
    backward(size * 4)


def showflake(size):
    for i in range(0, 10):
        size = random.randint(5, 30)
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        penup()
        goto(x, y)
        pendown()
        showflake(size)
