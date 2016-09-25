from turtle import Turtle
defaul_scale=25

def init_draw_man():
    global t, x_current,  y_current, drawman_scale
    t = Turtle()
    t.penup()
    t.shape('turtle')
    x_current = 0
    y_current = 0
    t.goto (x_current,y_current)
    drawman_scale(defaul_scale)

def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale


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
    """"Опустить ○перо"""
    t.pendown()

def pen_up():
    """"поднять перо"""
    t.penup()

def on_vector(dx,dy):
    """"Переместить на вектор (x,y)"""
    to_point(x_current+dx,  y_current+dy)

def to_point(x,y):
    """"Переместить в точку (x,y)"""
    global x_current,  y_current
    x_current = x
    y_current = y
    t.goto(x_current*_drawman_scale,y_current*_drawman_scale)


def draw_setka():
    t.speed(0)
    t.pencolor("grey")
    pen_up()
    n=600//_drawman_scale
    t.goto(-300,0)
    for x in range(-300,301,_drawman_scale):
        t.goto(x,300)
        pen_down()
        t.goto(x,-300)
        pen_up()
    for y in range(-300,301,_drawman_scale):
        t.goto(300,y)
        pen_down()
        t.goto(-300,y)
        pen_up()
    t.pencolor("black")
    t.pensize(3)
    t.goto(0,-300)
    pen_down()
    t.goto(0,300)
    pen_up()
    t.goto(-300,0)
    pen_down()
    t.goto(300,0)
    pen_up()
    t.goto(-15,-300)
    n = int(-n//2)
    for y in range(-300+_drawman_scale,301-_drawman_scale, _drawman_scale):
        t.write(n)
        t.goto(-15,y)
        n += 1
init_draw_man()
if __name__ == '__main__':
    import time
    draw_setka()
    t.hideturtle()
    time.sleep(10)
