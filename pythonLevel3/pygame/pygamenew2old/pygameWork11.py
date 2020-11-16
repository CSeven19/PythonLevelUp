# 鼠标

# pygame.mouse.get_pressed —— 返回按键按下情况，返回的是一元组，分别为(左键, 中键, 右键)，如按下则为True
# pygame.mouse.get_rel —— 返回相对偏移量，(x方向, y方向)的一元组
# pygame.mouse.get_pos —— 返回当前鼠标位置(x, y)
# pygame.mouse.set_pos —— 显而易见，设置鼠标位置
# pygame.mouse.set_visible —— 设置鼠标光标是否可见
# pygame.mouse.get_focused —— 如果鼠标在pygame窗口内有效，返回True
# pygame.mouse.set_cursor —— 设置鼠标的默认光标式样，是不是感觉我们以前做的事情白费了？哦不会，我们使用的方法有着更好的效果。
# pyGame.mouse.get_cursor —— 不再解释。

import pygame
from pygame.locals import *
from sys import exit
from pythonLevel3.pygame.pygamenew2old.pygameWork10 import Vector2
from math import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background_image_filename = 'background.png'
sprite_image_filename = 'flame.png'
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

# 让pygame完全控制鼠标,来完全控制鼠标，这样鼠标的光标看不见，也不会跑到pygame窗口外面去，一个副作用就是无法使用鼠标关闭窗口了，所以你得准备一句代码来退出程序。
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)  #分享鼠标给当前应用

# 初始化
sprite_pos = Vector2(200, 150)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 360.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # 按Esc则退出游戏
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    pressed_keys = pygame.key.get_pressed()
    # 这里获取鼠标的按键情况
    pressed_mouse = pygame.mouse.get_pressed()

    rotation_direction = 0.
    movement_direction = 0.

    # 通过移动偏移量计算转动,来获得x方向上的偏移量，除以5是把动作放慢一点
    rotation_direction = pygame.mouse.get_rel()[0] / 5.0

    # 1旋转
    if pressed_keys[K_LEFT]:
        rotation_direction = +1.
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.
    # 2移动距离
    # 多了一个鼠标左键按下的判断
    if pressed_keys[K_UP] or pressed_mouse[0]:
        movement_direction = +1.
    # 多了一个鼠标右键按下的判断
    if pressed_keys[K_DOWN] or pressed_mouse[2]:
        movement_direction = -1.

    screen.blit(background, (0, 0))

    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotated_sprite.get_size()
    sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
    screen.blit(rotated_sprite, sprite_draw_pos.__str__())

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 3再次计算旋转量
    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds

    # 4再次计算移动距离
    heading_x = sin(sprite_rotation * pi / 180.)
    heading_y = cos(sprite_rotation * pi / 180.)
    heading = Vector2(heading_x, heading_y)
    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_seconds

    pygame.display.update()