import random
from turtle import *

shape("circle")
speed(2)
pensize(4)
Screen().bgcolor("turquoise")
colours = ["blue", "purple", "cyan", "white", "yellow", "green", "orange"]


def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(30)
    backward(50)
    right(25)
def showflakeArm():
    for x in range (0,4):
        forward(30)
        vshape()
    backward(120)
def showflake():
    for x in range(0,6):
        color(random.choice(colours))
        showflakeArm()
        right(60)
showflake()