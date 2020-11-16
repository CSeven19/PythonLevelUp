# # 色彩
# # 实例1 显示所有色彩.卡。
# import pygame
#
# pygame.init()
#
# screen = pygame.display.set_mode((640, 480))
#
# all_colors = pygame.Surface((4096, 4096), depth=24)
#
# for r in range(256):
#     print(r + 1, "out of 256")
#     x = (r & 15) * 256
#     y = (r >> 4) * 256
#     for g in range(256):
#         for b in range(256):
#             all_colors.set_at((x + g, y + b), (r, g, b))
#
# pygame.image.save(all_colors, "allcolors.bmp")


# # 实例2 调色板
# # !/usr/bin/env python
# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
#
# screen = pygame.display.set_mode((640, 480), 0, 32)
#
#
# def create_scales(height):
#     # 设置RGB的3个滑动条
#     red_scale_surface = pygame.surface.Surface((640, height))
#     green_scale_surface = pygame.surface.Surface((640, height))
#     blue_scale_surface = pygame.surface.Surface((640, height))
#     for x in range(640):
#         # 设置RGB三色色彩值
#         c = int((x / 640.) * 255.)
#         red = (c, 0, 0)
#         green = (0, c, 0)
#         blue = (0, 0, c)
#         # 绘制渐变矩形的滑动框。
#         line_rect = Rect(x, 0, 1, height)
#         pygame.draw.rect(red_scale_surface, red, line_rect)
#         pygame.draw.rect(green_scale_surface, green, line_rect)
#         pygame.draw.rect(blue_scale_surface, blue, line_rect)
#     return red_scale_surface, green_scale_surface, blue_scale_surface
#
#
# red_scale, green_scale, blue_scale = create_scales(80)
#
# color = [127, 127, 127]
#
# while True:
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#
#     screen.fill((0, 0, 0))
#
#     screen.blit(red_scale, (0, 00))
#     screen.blit(green_scale, (0, 80))
#     screen.blit(blue_scale, (0, 160))
#
#     x, y = pygame.mouse.get_pos()
#
#     # 监听并响应鼠标按住滑动按钮事件.
#     if pygame.mouse.get_pressed()[0]:
#         for component in range(3):
#             if y > component * 80 and y < (component + 1) * 80:  #  控制鼠标在y轴的范围(RGB三色滑动框范围内)
#                 color[component] = int((x / 639.) * 255.)  #  Position_x -> 对应RGB的color值
#         pygame.display.set_caption("PyGame Color Test - " + str(tuple(color)))  #  窗口标题动态显示RGB三色值。
#
#     # 绘制滑动按钮
#     for component in range(3):
#         pos = (int((color[component] / 255.) * 639), component * 80 + 40)
#         pygame.draw.circle(screen, (255, 255, 255), pos, 20)
#
#     # 绘制混合RGB后的矩形显示部分
#     pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))
#
#     pygame.display.update()


# 实例3 颜色的混合

# !/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

color1 = (221, 99, 20)
color2 = (96, 130, 51)
factor = 0.

# 混合颜色
def blend_color(color1, color2, blend_factor):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = r1 + (r2 - r1) * blend_factor
    g = g1 + (g2 - g1) * blend_factor
    b = b1 + (b2 - b1) * blend_factor
    return int(r), int(g), int(b)


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255, 255, 255))

    tri = [(0, 120), (639, 100), (639, 140)]
    pygame.draw.polygon(screen, (0, 255, 0), tri)  #绘制放射图
    pygame.draw.circle(screen, (0, 0, 0), (int(factor * 639.0), 120), 10)   #绘制滑动按钮

    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        factor = x / 639.0
        pygame.display.set_caption("Pygame Color Blend Test - %.3f" % factor)  #窗口标题动态显示混合颜色系数

    color = blend_color(color1, color2, factor)    #根据坐标x混合颜色
    pygame.draw.rect(screen, color, (0, 240, 640, 240))  #显示混合后颜色的矩形部分。

    pygame.display.update()