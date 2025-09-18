from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 캐릭터 시작 위치
x, y = 400, 90

def move_rectangle():
    global x, y
    # 아래 -> 오른쪽
    for x in range(50, 750 + 1, 5):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # 오른쪽 -> 위
    for y in range(90, 550 + 1, 5):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # 위 -> 왼쪽
    for x in range(750, 50 - 1, -5):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    # 왼쪽 -> 아래
    for y in range(550, 90 - 1, -5):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)


def move_triangle():
    global x, y
    # 삼각형 꼭짓점 좌표
    points = [(400, 550), (750, 90), (50, 90)]
    # 현재 위치를 첫 꼭짓점으로 이동
    for t in range(0, 100 + 1, 2):
        x = 400 + (points[0][0] - x) * t / 100
        y = 550 + (points[0][1] - y) * t / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(int(x), int(y))
        delay(0.01)
    # 1->2
    for t in range(0, 100 + 1, 2):
        x = points[0][0] + (points[1][0] - points[0][0]) * t / 100
        y = points[0][1] + (points[1][1] - points[0][1]) * t / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(int(x), int(y))
        delay(0.01)
    # 2->3
    for t in range(0, 100 + 1, 2):
        x = points[1][0] + (points[2][0] - points[1][0]) * t / 100
        y = points[1][1] + (points[2][1] - points[1][1]) * t / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(int(x), int(y))
        delay(0.01)
    # 3->1
    for t in range(0, 100 + 1, 2):
        x = points[2][0] + (points[0][0] - points[2][0]) * t / 100
        y = points[2][1] + (points[0][1] - points[2][1]) * t / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(int(x), int(y))
        delay(0.01)


def move_circle():
    global x, y
    cx, cy, r = 400, 300, 210  # 원 중심, 반지름
    # 90도(아래쪽)부터 시작해서 시계방향으로 그림
    for degree in range(90, 450, 2):
        rad = math.radians(degree)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(int(x), int(y))
        delay(0.01)
    # 원 끝나고 사각형 시작 위치(50, 90)로 바로 이동
    x = 50
    y = 90

while True:
    move_rectangle()
    move_triangle()
    move_circle()
    # 원 끝나고 바로 사각형으로 이동, 추가 움직임 없이 반복


close_canvas()