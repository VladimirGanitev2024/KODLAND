#Здесь есть два кода это две залипалки(Наверное и коту понятно:) 2 вариант это запасная залипалка.Приятного залипания!

z_1 = str (input ("Какую залипалку вы хотите выбрать? Напишите 1 или 2:"))
print (" ")

if z_1 == "1":
        import turtle
        t=turtle.Turtle()
        t.color("Green")
        t.speed(0)
        t.begin_fill()
        for i in range(300):
            t.circle(i)
            t.left(45)
            t.circle(i)
            t.left(45)
            t.circle(i)
            t.left(45)
            t.circle(i)
            t.left(45)
        t.color("Red")
        t.speed(0)
        t.begin_fill()
        for i in range(300):
            t.forward(30)
            t.left(39)
            t.forward(40)
            t.left(58)
            t.circle(i)
            t.left(79)
            t.forward(50)
            t.left(57)
            t.circle(i)
            t.left(34)
            t.forward(50)

elif z_1 == "2":
        import turtle
        from turtle import *
        pensize(3)
        speed(100)
        for i in range(13):
            for c in ["orange","blue","red","blue","green","pink","yellow"]:
                pencolor(c)
                circle(150)
                right(4)

#By Stepanov Nikita