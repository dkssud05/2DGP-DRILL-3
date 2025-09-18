from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
angle = 0
r = 200
circle_x = 400
circle_y = 300
triangle_state = 0
state = 0

def move_rectangle():
    global x, y, state

    if x < 780 and y == 90:
        x += 2
        if x == 398:
            x = 400
            state = 1
    elif x == 780 and y < 550:
        y += 2
    elif x > 20 and y == 550:
        x -= 2
    elif x == 20 and y > 90:
        y -= 2

def move_triangle():
    global x, y, triangle_state, state

    if triangle_state == 0:
        if x < 600 and y < 400:
            x += 2
            y += 3
        else:
            triangle_state = 1
    elif triangle_state == 1:
        if x > 200 and y < 400:
            x -= 2
        else:
            triangle_state = 2
    elif triangle_state == 2:
        if x < 400 and y > 90:
            x += 2
            y -= 3
        else:
            triangle_state = 0
            x = 400
            y = 90
            state = 2

def move_circle():
    global x, y, r, angle, state
    x = circle_x + r * math.sin(math.radians(angle))
    y = circle_y + r * math.cos(math.radians(angle))
    angle += 2

    if angle > 360:
        angle = 0
        x = 400
        y = 90
        state = 0

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    if state == 0:
        move_rectangle()
    if state == 1:
        move_triangle()
    if state == 2:
        move_circle()

    delay(0.01)

close_canvas()
