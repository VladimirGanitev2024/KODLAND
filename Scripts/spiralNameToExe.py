
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", ]
your_name = turtle.textinput("Введите своё имя",
                             "Как тебя зовут?")
for x in range(100):
    t.pencolor(colors[x%5])
    t.penup()
    t.forward(x*5)
    t.pendown()
    t.write(your_name, font=("Arial", int((x + 5) / 5),
"bold"))
    t.left(92)


