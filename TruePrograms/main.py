from turtle import *
color('red', 'black')
begin_fill()
while True:
    forward(500)
    forward(400)
    forward(300)
    forward(200)
    forward(100)
    forward(100)
    left(100)
    if abs(pos()) < 1:
        break
end_fill()
done()
