from random import *
from tkinter import *
size = 500
window = Tk()
canvas = Canvas(window, width=size, height=size)
canvas.pack()
while True:
    col = choice(['pink', 'orange', 'purple', 'yellow'])
    xO = randint(0, size)
    yO = randint(0,size)
    d = randint(0,size/5)
    canvas.create_oval(xO, yO, xO + d, yO + d, fill=col)
    window.update()