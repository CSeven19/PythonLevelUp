# # 显示
# # 实例1
# background_image_filename = 'background.png'
#
# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
# screen = pygame.display.set_mode((640, 480), 0, 32)
# background = pygame.image.load(background_image_filename).convert()
#
# Fullscreen = False
#
# while True:
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#     if event.type == KEYDOWN:
#         if event.key == K_f:
#             Fullscreen = not Fullscreen
#             if Fullscreen:
#                 screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)  #按进行窗体切换
#             else:
#                 screen = pygame.display.set_mode((640, 480), 0, 32)
#
#     screen.blit(background, (0, 0))
#     pygame.display.update()


# 实例2 可变窗口
background_image_filename = 'background.png'

import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

background = pygame.image.load(background_image_filename).convert()

while True:

    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)  #可变类型窗口  双缓冲DOUBLEBUF也加上，这就是一个很棒的游戏显示了，不过记得你要使用pygame.display.flip()来刷新显示。pygame.display.update()是将数据画到前面显示，而这个是交替显示的意思。
        pygame.display.set_caption("Window resized to " + str(event.size))

    screen_width, screen_height = SCREEN_SIZE
    # 这里需要重新填满窗口
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

    pygame.display.update()