# # 向量
#
# 1向量类
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
# A = (10.0, 20.0)
# B = (30.0, 35.0)
# AB = Vector2.from_points(A, B)
# print(AB)

# # # 2向量库
# # from gameobjects.vector2 import *
# # A = (10.0, 20.0)
# # B = (30.0, 35.0)
# # AB = Vector2.from_points(A, B)
# # print("Vector AB is", AB)
# # print("AB * 2 is", AB * 2)
# # print("AB / 2 is", AB / 2)
# # print("AB + (–10, 5) is", AB + (-10, 5))
# # print("Magnitude of AB is", AB.get_magnitude())
# # print("AB normalized is", AB.get_normalized())
#
# background_image_filename = 'background.png'
# sprite_image_filename = 'flame.png'
#
# import pygame
# from pygame.locals import *
# from sys import exit
# # from gameobjects.vector2 import Vector2
#
# pygame.init()
#
# screen = pygame.display.set_mode((640, 480), 0, 32)
#
# background = pygame.image.load(background_image_filename).convert()
# sprite = pygame.image.load(sprite_image_filename).convert_alpha()
#
# clock = pygame.time.Clock()
#
# position = Vector2(100, 100).__str__()
# heading = Vector2()
#
# while True:
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#
#     screen.blit(background, (0, 0))
#     screen.blit(sprite, position)
#
#     time_passed = clock.tick()
#     time_passed_seconds = time_passed / 1000.0
#
#     # 参数前面加*意味着把列表或元组展开
#     destination = ((pygame.mouse.get_pos()[0]-sprite.get_size()[0])/2,(pygame.mouse.get_pos()[1]-sprite.get_size()[1])/2)
#     # destination = (Vector2(*pygame.mouse.get_pos()) - Vector2(*sprite.get_size())) / 2
#     # 计算鱼儿当前位置到鼠标位置的向量
#     vector_to_mouse = Vector2.from_points(position, destination)
#     # 向量规格化
#     vector_to_mouse.normalize()
#
#     # 这个heading可以看做是鱼的速度，但是由于这样的运算，鱼的速度就不断改变了
#     # 在没有到达鼠标时，加速运动，超过以后则减速。因而鱼会在鼠标附近晃动。
#     heading = heading + (vector_to_mouse * .6)
#
#     position += heading.__str__() * int(time_passed_seconds)
#     pygame.display.update()