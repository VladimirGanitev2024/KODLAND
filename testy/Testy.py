from tkinter import *


root = Tk()
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Открыть...")
fm.add_command(label="Создать")
fm.add_command(label="Сохранить...")
fm.add_command(label="Выход")

hm = Menu(m)
m.add_cascade(label="?", menu=hm)
hm.add_command(label="Справка")
hm.add_command(label="О программе")

ntm = Menu(fm)
fm.add_cascade(label="Import", menu=ntm)
ntm.add_command(label="Image")
ntm.add_command(label="Text")

root.mainloop()

