import tkinter

window = tkinter.Tk()
drawing = tkinter.Canvas(window, height=500, width=500)
drawing.pack()
rect1 = drawing.create_rectangle(100, 100, 300, 200)
square1 = drawing.create_rectangle(30, 30, 80, 80)
oval = drawing.create_oval(100, 100, 300, 200)
circle1 = drawing.create_oval(30, 30, 80, 80)
drawing.create_rectangle(50, 50, 250, 350)
drawing.create_oval(30, 30, 80, 80, outline='red', fill='blue')

btn=tkinter.Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)
window.title('Hello Python')


window.mainloop() # Обязательный элемент для запуска нового окна
