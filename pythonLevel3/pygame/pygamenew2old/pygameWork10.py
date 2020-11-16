# 输入

# 1键盘事件
# key.get_focused —— 返回当前的pygame窗口是否激活
# key.get_pressed —— 刚刚解释过了
# key.get_mods —— 按下的组合键（Alt, Ctrl, Shift）
# key.set_mods —— 你也可以模拟按下组合键的效果（KMOD_ALT, KMOD_CTRL, KMOD_SHIFT）
# key.set_repeat —— 无参数调用设置pygame不产生重复按键事件，二参数(delay, interval)调用设置重复事件发生的时间
# key.name —— 接受键值返回键名

import math
class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return (self.x, self.y)

    @classmethod
    def from_points(cls, P1, P2):
        return cls(P2[0]-P1[0], P2[1]-P1[1])  # 我们可以使用下面的方法来计算两个点之间的向量

    def get_magnitude(self):  #向量大小
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):  #单位向量
        magnitude = self.get_magnitude()
        if magnitude!=0:
            self.x /= magnitude
            self.y /= magnitude

    def get_normalized(self):  # 单位向量
        magnitude = self.get_magnitude()
        if magnitude != 0:
            self.x /= magnitude
            self.y /= magnitude
    # 向量运算 向量AC = 向量AB + 向量BC
    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)
    def get_length(self):
        return math.sqrt(math.fabs(self.x)+math.fabs(self.y))
    def get_distance_to(self):
        return math.sqrt(self.x+self.y)

# # 实例1
# import pygame
# from pygame.locals import *
# from sys import exit
# # from gameobjects.vector2 import Vector2
#
# pygame.init()
#
# screen = pygame.display.set_mode((640, 480), 0, 32)
# background_image_filename = 'background.png'
# sprite_image_filename = 'flame.png'
#
# background = pygame.image.load(background_image_filename).convert()
# sprite = pygame.image.load(sprite_image_filename).convert_alpha()
#
# clock = pygame.time.Clock()
#
# sprite_pos = Vector2(200, 150)
# sprite_speed = 300.
#
# while True:
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#
#     pressed_keys = pygame.key.get_pressed()
#
#     key_direction = Vector2(0, 0)
#     if pressed_keys[K_LEFT]:
#         key_direction.x = -10
#     elif pressed_keys[K_RIGHT]:
#         key_direction.x = +10
#     if pressed_keys[K_UP]:
#         key_direction.y = -10
#     elif pressed_keys[K_DOWN]:
#         key_direction.y = +10
#
#     key_direction.normalize()
#
#     screen.blit(background, (0, 0))
#     screen.blit(sprite, sprite_pos.__str__())
#
#     time_passed = clock.tick(30)
#     time_passed_seconds = time_passed / 1000.0
#
#     sprite_pos += key_direction * sprite_speed * time_passed_seconds
#
#     pygame.display.update()

# 实例2
background_image_filename = 'background.png'
sprite_image_filename = 'flame.png'

import pygame
from pygame.locals import *
from sys import exit
# from gameobjects.vector2 import Vector2
from math import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

sprite_pos = Vector2(200, 150)  # 初始位置
sprite_speed = 300.  # 每秒前进的像素数（速度）
sprite_rotation = 0.  # 初始角度
sprite_rotation_speed = 360.  # 每秒转动的角度数（转速）

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    rotation_direction = 0.
    movement_direction = 0.

    # 更改角度
    if pressed_keys[K_LEFT]:
        rotation_direction = +1.
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.
    # 前进、后退
    if pressed_keys[K_UP]:
        movement_direction = +1.
    if pressed_keys[K_DOWN]:
        movement_direction = -1.

    screen.blit(background, (0, 0))

    # 获得一条转向后的鱼
    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    # 转向后，图片的长宽会变化，因为图片永远是矩形，为了放得下一个转向后的矩形，外接的矩形势必会比较大
    w, h = rotated_sprite.get_size()
    # 获得绘制图片的左上角（感谢pltc325网友的指正）
    sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
    screen.blit(rotated_sprite, sprite_draw_pos.__str__())

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 图片的转向速度也需要和行进速度一样，通过时间来控制
    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds

    # 获得前进（x方向和y方向），这两个需要一点点三角的知识
    heading_x = sin(sprite_rotation * pi / 180.)
    heading_y = cos(sprite_rotation * pi / 180.)
    # 转换为单位速度向量
    heading = Vector2(heading_x, heading_y)
    # 转换为速度
    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_seconds

    pygame.display.update()
