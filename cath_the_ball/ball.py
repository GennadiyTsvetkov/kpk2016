import tkinter

def button1_command():
    print ('Button1_defolt_command')

def print_hello(event):
    #print(event.char)
    #print(event.keycode)

    print(event.num)
    print(event.x,event.y)
    #print(event.x_root,event.y_root)
    me = event.widget
    if me == button1:
        print('Hello!')
    elif me == button2:
        print('you press button2')
    else:
        raise ValueError()

def init_main_window():
    """Инициализация главного окна, создание всех виджетов и их упаковка
    :return: None"""
    global root, button1, button2, lable, text, scale
    root = tkinter.Tk()

    button1=tkinter.Button(root, text="Button1", command=button1_command)
    button1.bind("<Button>", print_hello)

    button2=tkinter.Button(root, text="Button2")
    button2.bind("<Button>", print_hello)

    variable=tkinter.IntVar(0)
    lable = tkinter.Label(root, textvariable=variable)
    scale = tkinter.Scale(root, orient=tkinter.HORIZONTAL, length=300, from_=0, to=100, tickinterval=10, resolution=5, variable=variable)
    text = tkinter.Entry(root, textvariable=variable)

    for obj in button1, button2, lable, scale, text:
        obj.pack()

if __name__ == "__main__":
    init_main_window()
    root.mainloop()

