import tkinter
from random import choice, randint
ball_initial_number = 10
ball_min_radius = 15
ball_max_radius = 40
ball_available_colors = ['green', 'blue', 'red', 'orange', '#FF00FF' , '#AAAA00']



def click_ball(event):
    """
    Обработчик событий для мышки для игрового холста canvas
    :param event: событие с координатами клика
    :return: None
    По клику мышкой нужно удалять тот объект, на который указывает мышка.
    А также засчитывать его в очки пользователя.
    """
    obj = canvas.find_closest(event.x,event.y)
    x1, y1, x2, y2=canvas.coords(obj)
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        create_random_ball()
    #print(event.x, event.y)

def move_all_balls(event):
    """передвигаем все шарики на чуть-чуть"""
    for obj in canvas.find_all():
        dx = randint(-1,1)
        dy = randint(-1,1)
        canvas.move(obj, dx, dy)


def create_random_ball():
    """Создает шарик произвольного размера,
    причем он не вылазиет за границы холста"""
    R = randint(ball_min_radius,ball_max_radius)
    x = randint(1, int(canvas['width'])-2*R-1)
    y = randint(1, int(canvas['height'])-2*R-1)
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())

def random_color():
    """Возвращает цвет из некоторого набора цветов"""
    return choice(ball_available_colors)

def init_ball_catch_game():
    """Создаем необходимое для игры количество шариков, по которым нужно будет кликать мышью
    """
    for i in range(ball_initial_number):
        create_random_ball()

def init_main_window():
    global root, canvas

    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()


if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()

print("Приходите играть ещё!")
