
import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
s.bgcolor("black")
t.hideturtle()
for i in range (100):
    t.circle(i*2.30)
    t.left(10000)
    t.pencolor("yellow")
turtle.done()