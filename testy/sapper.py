import tkinter
import random

gameover = False
score = 0
squaresToClear = 0


def play_bombdodger():
    'create_bombfield'
    window = tkinter.Tk(0)
    'layout_window'
    window.mainloop()


bombfield = []


def create_bombfield(bombfield):
    global squaresToClear
    for row in range(0, 10):
        rowList = []
        for column in range(0, 10):
            if random.randint(1, 100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToClear = squaresToClear + 1
                bombfield.append(rowList)
    printfield(bombfield)


def printfield(bombfield):
    for rowList in bombfield:
        print(rowList)


play_bombdodger()
