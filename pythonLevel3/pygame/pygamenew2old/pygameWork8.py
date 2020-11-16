# # 运动
#
# # 1 实例1 直线运动(循环改变position_x)
# background_image_filename = 'background.png'
# sprite_image_filename = 'flame.png'
#
# import pygame
# from pygame.locals import *
# from sys import exit
# import time
#
# pygame.init()
#
# screen = pygame.display.set_mode((640, 480), 0, 32)
#
# background = pygame.image.load(background_image_filename).convert()
# sprite = pygame.image.load(sprite_image_filename)
#
# # sprite的起始x坐标
# x = 680.
#
# while True:
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#
#     screen.blit(background, (0, 0))
#     screen.blit(sprite, (x, 100))
#     x -= 10.  # 如果你的机器性能太好以至于看不清，可以把这个数字改小一些
#     time.sleep(0.1)
#     # 如果移动出屏幕了，就搬到开始位置继续
#     if x < 0.:
#         x = 680
#
#     pygame.display.update()


# # # 2时间控制
# # import pygame
# # # 第一行初始化了一个Clock对象；第二行的意识是返回一个上次调用的时间（以毫秒计）；第三行非常有用，在每一个循环中加上它，
# # # 那么给tick方法加上的参数就成为了游戏绘制的最大帧率，这样的话，游戏就不会用掉你所有的CPU资源了！但是这仅仅是“最大帧率”，
# # # 并不能代表用户看到的就是这个数字，有些时候机器性能不足，或者动画太复杂，实际的帧率达不到这个值，我们需要一种更有效的手段来控制我们的动画效果。
# # clock = pygame.time.Clock()
# # time_passed = clock.tick()
# # time_passed = clock.tick(30)
# # # 实例1
# background_image_filename = 'background.png'
# sprite_image_filename = 'flame.png'
#
# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
#
# screen = pygame.display.set_mode((640, 480), 0, 32)
#
# background = pygame.image.load(background_image_filename).convert()
# sprite = pygame.image.load(sprite_image_filename)
#
# # Clock对象
# clock = pygame.time.Clock()
#
# x = 640.
# # 速度（像素/秒）
# speed = 250.
#
# while True:
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#
#     screen.blit(background, (0, 0))
#     screen.blit(sprite, (x, 100))
#
#     time_passed = clock.tick()  #返回一个上次调用的时间（以毫秒计
#     time_passed_seconds = time_passed / 1000.0  #毫秒转秒
#
#     distance_moved = time_passed_seconds * speed  #时间*速度=距离
#     x -= distance_moved  #每次循环移动的距离来移动x
#
#     # 想一下，这里减去640和直接归零有何不同？
#     if x < 0.:
#         x += 640.
#
#     pygame.display.update()

# 3
background_image_filename = 'background.png'
sprite_image_filename = 'flame.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

x, y = 100., 100.
speed_x, speed_y = 133., 170.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds

    # 到达边界则把速度反向
    # x坐标上到达边界
    if x > 640 - sprite.get_width():
        speed_x = -speed_x
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0.

    # y坐标轴到达边界
    if y > 480 - sprite.get_height():
        speed_y = -speed_y
        y = 480 - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0

    pygame.display.update()