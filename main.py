from tkinter import *
import numpy as np
import tool
import math
GRID_HEIGHT = 10
GRID_WIDTH = 10
GAME_WIDTH = 400
GAME_HEIGHT = 400
GAME_UNIT = GAME_WIDTH/GRID_HEIGHT
WORLD = np.zeros((GRID_HEIGHT, GRID_WIDTH))
WORLD[:, 0] = 2
WORLD[:, -1] = 2
WORLD[0,:] = 2
WORLD[-1,:] = 2
WORLD[5, 5] = 2
PI = float(3.141)
def move(event):
    if event == 'right':
        player.a += 10
        if player.a > 360:
            player.a = 0
    elif event == 'left':
        player.a -= 10
        if (player.a < 0):
            player.a = 360
    elif event == 'back':
        player.x -= player.deltax
        player.y -= player.deltay
    elif event == 'forward':
        player.x += player.deltax
        player.y += player.deltay

    player.deltax = round((math.cos(math.radians(player.a)))*5, 2)
    player.deltay = round((math.sin(math.radians(player.a)))*5, 2)

class PLAYER:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.a = 90
        self.deltax = round((math.cos(math.radians(self.a)))*5, 2)
        self.deltay = round((math.sin(math.radians(self.a)))*5, 2)
    def draw(self):
        canvas.create_oval(self.x-5, self.y-5, self.x + 5, self.y + 5, fill = "red", tag = 'player')
        canvas.create_line(self.x,
        self.y,
        self.x+(self.deltax)*5,
        self.y+(self.deltay)*5,
        fill = "red", width = 3, tag = 'player')
def ray():
    x0 = int
    y0 = int
    x1 = int
    y1 = int
    ra = player.a
    if ra != 0:
        atan = -1/math.atan(ra)
    else:
        ra = 0.001
    if math.tan(ra>180):
        y0 = int(player.y/GAME_UNIT)
        y0 = y0*GAME_UNIT
        x0 = (player.y-y0)*atan+player.x
    elif math.tan(ra<180):
        y0 = int((player.y+GAME_UNIT)/GAME_UNIT)
        y0 = y0 * GAME_UNIT
        x0 = (player.y+y0)*atan+player.x
        x0 = round(x0, 2)

    label.config(text = "X0: {}  Y0:{}  Angle:{}".format (x0, y0, player.a))
def draw_grid():
    for i in range (0, GRID_WIDTH):
        canvas.create_line(GAME_UNIT*i, 0, GAME_UNIT*i, GAME_HEIGHT, fill = 'green')
    for i in range (0, GRID_HEIGHT):
        canvas.create_line(0, GAME_UNIT*i, GAME_WIDTH, GAME_UNIT*i, fill = 'green')
def draw_map():
    global WORLD
    for i in range (0, GRID_HEIGHT):
        for j in range (0, GRID_WIDTH):
            if WORLD[i][j] == 2:
                rect = canvas.create_rectangle(i*(GAME_WIDTH/GRID_WIDTH), j*(GAME_HEIGHT/GRID_WIDTH),
                i*(GAME_WIDTH/GRID_WIDTH)+GAME_UNIT, j*(GAME_HEIGHT/GRID_WIDTH)+GAME_UNIT, fill = 'blue', tag = 'obstacle')
def next():
    canvas.delete("player")
    player.draw()
    ray()
    window.after(100, next)

window = Tk()
window.bind("<s>", lambda event: move('back'))
window.bind("<z>", lambda event: move('forward'))
window.bind("<q>", lambda event: move('left'))
window.bind("<d>", lambda event: move('right'))

canvas = Canvas(window, bg = 'black', height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()
draw_grid()
draw_map()
player = PLAYER()
label = Label (window, text = "DeltaX: {}  Deltay:{}  Angle:{}".format (player.deltax, player.deltay, player.a),
        font = ('consolas', 10))
label.pack()
next()
window.mainloop()
