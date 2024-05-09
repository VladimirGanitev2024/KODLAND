#
# SquareSpiral.py - Рисование квадратной спирали
import turtle

t = turtle.Pen()
for x in range(100):
    t.forward(x)
    t.left(70)
# Лучшее значение цифр 100 и 70. (Даёт пятигранник с красивой спиралью)

