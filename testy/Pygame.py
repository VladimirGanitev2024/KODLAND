import random
from this import s, c

from testy.Testy import root

WIDTH = 800
HEIGHT = 600
SEG_SIZE =20
IN_GAME = True
def create_block(с=None):
    """ Создает еду змейки - яблоко """
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
    BLOCK = с.create_oval(posx, posy,
                          posx + SEG_SIZE, posy + SEG_SIZE,
                          fill="red")

    def main(с=None, х2=None):
        """ Управляет игровым процессом """
        global IN_GAME
        if IN_GAME:
            s.move()
            # Определяем координаты головы
            head_coords = с.coords(s.segments[-1].instance)
            xl, yl, x2, y2 = head_coords
            # Столкновения с краями игрового поля
            if х2 > WIDTH or xl < 0 or yl < 0 or y2 > HEIGHT:
                IN_GAME = False
                # Поедание яблока
            elif head_coords == c.coords(BLOCK):
                s.add_segment()
                с.delete(BLOCK)
                create_block()
                # Поедание змейки
            else:
                for index in range(len(s.segments) - 1):
                    if head_coords == c.coords(s.segments[index].instance):
                        IN_GAME = False
            root.after(100, main)
            # He IN_GAME -> выводы сообщение
        else:
            с.create_text(WIDTH / 2, HEIGHT / 2,)












