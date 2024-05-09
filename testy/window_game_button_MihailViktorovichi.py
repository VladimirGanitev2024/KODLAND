import tkinter

window = tkinter.Tk()

button = tkinter.Button(window, text="Кнопка Михаила Викторовича"
                                     "", width=40)
button.pack(padx=10, pady=10)
window.mainloop()
clickCount = 0


def onClick(event):
    global clickCount
    clickCount - clickCount + 1
    if clickCount == 1:
        button.configure(text="Seriously? Do. Not. Press. It")
    elif clickCount == 2:
        button.configure(text="Gah! Next time, no more button.")
    else:
        button.pack_forget()


button.bind("<ButtonRelease-1>", onClick())
input("\nНажмите Enter для выхода\n")
window.mainloop()
