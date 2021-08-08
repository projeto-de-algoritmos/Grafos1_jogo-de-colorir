from tkinter import *
from collections import deque


def changeColor(newColor):
    global new_color
    new_color = newColor


def locate_xy(event):
    global selected_x, selected_y
    selected_x, selected_y = event.x, event.y
    # colorPixel(selected_x, selected_y)
    # print(selected_x, selected_y)
    # image.put(new_color, (selected_x, selected_y))
    fill(selected_x, selected_y)


def fill(x, y):
    areaColor = image.get(x, y)

    if new_color == areaColor:
        return

    q = deque()
    q.append((x, y))

    v = []
    while q:
        px, py = q.popleft()

        if px - 1 >= 0 and image.get(px-1, py) == areaColor and (px-1, py) not in v:
            v.append((px-1, py))
            q.append((px-1, py))
        if px + 1 < w and image.get(px+1, py) == areaColor and (px+1, py) not in v:
            v.append((px+1, py))
            q.append((px+1, py))
        if py - 1 > 0 and image.get(px, py-1) == areaColor and (px, py-1) not in v:
            v.append((px, py-1))
            q.append((px, py-1))
        if py + 1 < w and image.get(px, py+1) == areaColor and (px, py+1) not in v:
            v.append((px, py+1))
            q.append((px, py+1))

    for i in v:
        image.put(new_color, (i[0], i[1]))


new_color = 'red'
w = 444
h = 512

# def fill(x, y):
#     areaColor = image.get(x, y)
#     q = deque()
#     q.append((x, y))

selected_x, selected_y = 0, 0

root = Tk()

image = PhotoImage(file="mario.ppm")

canvas = Canvas(root, background='white', width=w, height=h)
canvas.grid(row=0, column=0)
canvas.bind('<Button-1>', locate_xy)
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()

menubar = Menu(root)
root.config(menu=menubar)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Cor', menu=submenu)
submenu.add_command(
    label='Vermelho', command=changeColor('red'))
# submenu.add_command(label='Verde', command=changeColor('green'))
# submenu.add_command(label='Azul', command=changeColor('blue'))
# submenu.add_command(label='Roxo', command=changeColor('purple'))
# submenu.add_command(label='Marrom', command=changeColor('brown4'))

root.mainloop()
