# # 事件
# # 实例1 鼠标事件
# ##这个程序在你移动鼠标的时候产生了海量的信息，让我们知道了Pygame是多么的繁忙……
# ##我们第一个程序那样是调用pygame.mouse.get_pos()来得到当前鼠标的位置，而现在利用事件可以直接获得！
# import pygame
# from pygame.locals import *
# from sys import exit
# import math
#
# pygame.init()
# SCREEN_SIZE = (640, 480)
# screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
#
# font = pygame.font.SysFont("arial", 16)
# font_height = font.get_linesize()
# event_text = []
#
# while True:
#
#     event = pygame.event.wait()#如果我们使用pygame.event.wait()，Pygame就会等到发生一个事件才继续下去，就好像你在门的猫眼上盯着外面一样，来一个放一个……一般游戏中不太实用，因为游戏往往是需要动态运作的；
#     event_text.append(str(event))
#     # 获得时间的名称
#     event_text = event_text[math.ceil(-SCREEN_SIZE[1] / font_height):]
#     # 这个切片操作保证了event_text里面只保留一个屏幕的文字
#
#     if event.type == QUIT:
#         exit()
#
#     screen.fill((255, 255, 255))  #填充RPG背景色
#
#     y = SCREEN_SIZE[1] - font_height
#     # 找一个合适的起笔位置，最下面开始但是要留一行的空
#     for text in reversed(event_text):
#         screen.blit(font.render(text, True, (0, 0, 0)), (0, y))
#         # 以后会讲
#         y -= font_height
#         # 把笔提一行
#
#     pygame.display.update()


# 实例2 键盘
background_image_filename = 'flame.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            # 键盘有按下？
            if event.key == K_LEFT:
                # 按下的是左方向键的话，把x坐标减一
                move_x = -10
            elif event.key == K_RIGHT:
                # 右方向键则加一
                move_x = 10
            elif event.key == K_UP:
                # 类似了
                move_y = -10
            elif event.key == K_DOWN:
                move_y = 10
        elif event.type == KEYUP:
            # 如果用户放开了键盘，图就不要动了
            move_x = 0
            move_y = 0

        # 计算出新的坐标
        x += move_x
        y += move_y

        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))  # 将子弹放到x，y
        # 在新的位置上画图
        pygame.display.update()