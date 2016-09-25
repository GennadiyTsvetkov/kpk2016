from turtle import Turtle

def init_draw_man():
    global t, x_current,  y_current
    t = Turtle()
    t.penup()
    t.shape('turtle')
    x_current = 0
    y_current = 0
    t.goto (x_current,y_current)


def test_drawman():
    """"Тестирование работы чертежника
    :return: None"""
    pen_down()
    for i in range(5):
        on_vector(10,20)
        on_vector(0,-20)
    pen_up()
    to_point(0,0)

def pen_down():
    """"Опустить перо"""
    t.pendown()

def pen_up():
    """"поднять перо"""
    t.penup()

def on_vector(dx,dy):
    """"Переместить на вектор (x,y)"""
    global x_current,  y_current
    t.goto(x_current+dx,y_current+dy)
    x_current += dx
    y_current += dy

def to_point(x,y):
    """"Переместить в точку (x,y)"""
    global x_current,  y_current
    x_current = x
    y_current = y
    t.goto(x,y)

init_draw_man()
if __name__ == '__main__':
    import time
    test_drawman()
    t.hideturtle()
    time.sleep(10)
