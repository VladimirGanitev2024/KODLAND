from tkinter import *


class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent


def main():
    root = Tk()
    root.geometry("800x600+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == "__main__":
    main()


def setUI(self):
    self.parent.title("Simple Paint")
    self.pack(fill=BOTH, expand=1)

    self.columnconfigure(6, weight=1)
    self.rowconfigure(2, weight=1)

    self.canvas = Canvas(self, bg="white")
    self.canv.grid(row=2, column=0, columnspan=7,
                   padx=5, pady=5, sticky=E + W + S + N)
    color_lab = Label(self, text="Цвет: ")
    color_lab.grid(row=0, column=0, padx=6)

    red_btn = Button(self, text="Kpacный", width=10)
    red_btn.grid(row=0, column=1)

    green_btn = Button(self, text="Зeлeный", width=10)
    green_btn.grid(row=0, column=2)

    blue_btn = Button(self, text=" Синий ", width=10)
    blue_btn.grid(row=0, column=3)

    black_btn = Button(self, text="Черный", width=10)
    black_btn.grid(row=0, column=4)

    white_btn = Button(self, text="Бeлый", width=10)
    white_btn.grid(row=0, column=5)

    size_lab = Label(self, text="Размер кисти: ")
    size_lab.grid(row=1, column=0, padx=5)

    one_btn = Button(self, text="2x", width=10)
    one_btn.grid(row=1, column=1)

    two_btn = Button(self, text="5x", width=10)
    two_btn.grid(row=1, column=2)

    five_btn = Button(self, text="7x", width=10)
    five_btn.grid(row=1, column=3)

    seven_btn = Button(self, text="10x", width=10)
    seven_btn.grid(row=1, column=4)

    ten_btn = Button(self, text="20x", width=10)
    ten_btn.grid(row=1, column=5)

    twenty_btn = Button(self, text="50x", width=10)
    twenty_btn.grid(row=1, column=6, sticky=W)

    self.brush_size = 10
    self.color = "red"


def draw(self, event):
    self.canv.create_oval(event.x - self.brush_size,
                          event.у - self.brush_size,
                          event.x + self.brush_size,
                          event.у + self.brush_size,
                          fill=self.color, outline=self.color)

    self.canv.bind("<Bl-Motion>", self.draw)


def set_color(self, new_color):
    self.color = new_color
    red_btn = Button(self, text="Kpacный"
                                "", width=10, command=lambda:
    self.set_color("red"))
    red_btn.grid(row=0, column=1)


def set_brush_size(self, new_size):
    self.brush_size = new_size
    one_btn = Button(self, text="2x", width=10, command=lambda:
    self.set_brush_size(2))








