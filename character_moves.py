from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

def move_triangle():
    pass

def move_rectangle():
    global x, y

    if x < 780 and y == 90:
        x += 2
    elif x == 780 and y < 550:
        y += 2
    elif x > 20 and y == 550:
        x -= 2
    elif x == 20 and y > 90:
        y -= 2

def move_circle():
    pass

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    move_triangle()
    move_rectangle()
    move_circle()

    delay(0.01)

close_canvas()
