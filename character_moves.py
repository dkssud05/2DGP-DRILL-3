from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

def move_triangle():
    print("move_triangle")
    pass

def move_rectangle():
    print("move_rectangle")
    pass

def move_circle():
    print("move_circle")
    pass

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    move_triangle()
    move_rectangle()
    move_circle()

    delay(0.001)

close_canvas()
