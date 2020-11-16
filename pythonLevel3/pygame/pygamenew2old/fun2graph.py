# import pygame
# class getFuncGraph():
#     def __init__(self):
#         pass
#     # 连续型函数转图表
#     def Func2Graph(self,func,*args):
#         for a,b in args:
#             for x in range(a,b):
#                 position_x = x*10
#                 position_y = func(x)*10
#                 position = (position_x,position_y)
#                 pygame.draw.circle(screen, (0, 0, 0), position, 5)
# def f(x):
#     return x^2
#
# while __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((640,480),0,32)
#     screen.fill((255, 255, 255))
#
#     pygame.draw.line(screen,(111,111,111),(10,420),(510,420),2)
#     pygame.draw.line(screen,(111,111,111),(10,420),(10,10),2)
#
#     func2graph = getFuncGraph()
#     func2graph.Func2Graph(f,(1,20))
#
#     pygame.display.update()


# from pylab import *
# from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#
# xmajorLocator = MultipleLocator(20)  # 将x主刻度标签设置为20的倍数
# xmajorFormatter = FormatStrFormatter('%1.1f')  # 设置x轴标签文本的格式
# xminorLocator = MultipleLocator(5)  # 将x轴次刻度标签设置为5的倍数
#
# ymajorLocator = MultipleLocator(0.5)  # 将y轴主刻度标签设置为0.5的倍数
# ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
# yminorLocator = MultipleLocator(0.1)  # 将此y轴次刻度标签设置为0.1的倍数
#
# t = arange(0.0, 100.0, 1)
# s = sin(0.1 * pi * t) * exp(-t * 0.01)
#
# ax = subplot(111)  # 注意:一般都在ax中设置,不再plot中设置
# plot(t, s, '--b*')
#
# # 设置主刻度标签的位置,标签文本的格式
# ax.xaxis.set_major_locator(xmajorLocator)
# ax.xaxis.set_major_formatter(xmajorFormatter)
#
# ax.yaxis.set_major_locator(ymajorLocator)
# ax.yaxis.set_major_formatter(ymajorFormatter)
#
# # 显示次刻度标签的位置,没有标签文本
# ax.xaxis.set_minor_locator(xminorLocator)
# ax.yaxis.set_minor_locator(yminorLocator)
#
# ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
# ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
#
# show()# import pygame
# class getFuncGraph():
#     def __init__(self):
#         pass
#     # 连续型函数转图表
#     def Func2Graph(self,func,*args):
#         for a,b in args:
#             for x in range(a,b):
#                 position_x = x*10
#                 position_y = func(x)*10
#                 position = (position_x,position_y)
#                 pygame.draw.circle(screen, (0, 0, 0), position, 5)
# def f(x):
#     return x^2
#
# while __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((640,480),0,32)
#     screen.fill((255, 255, 255))
#
#     pygame.draw.line(screen,(111,111,111),(10,420),(510,420),2)
#     pygame.draw.line(screen,(111,111,111),(10,420),(10,10),2)
#
#     func2graph = getFuncGraph()
#     func2graph.Func2Graph(f,(1,20))
#
#     pygame.display.update()


# from pylab import *
# from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#
# xmajorLocator = MultipleLocator(20)  # 将x主刻度标签设置为20的倍数
# xmajorFormatter = FormatStrFormatter('%1.1f')  # 设置x轴标签文本的格式
# xminorLocator = MultipleLocator(5)  # 将x轴次刻度标签设置为5的倍数
#
# ymajorLocator = MultipleLocator(0.5)  # 将y轴主刻度标签设置为0.5的倍数
# ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
# yminorLocator = MultipleLocator(0.1)  # 将此y轴次刻度标签设置为0.1的倍数
#
# t = arange(0.0, 100.0, 1)
# s = sin(0.1 * pi * t) * exp(-t * 0.01)
#
# ax = subplot(111)  # 注意:一般都在ax中设置,不再plot中设置
# plot(t, s, '--b*')
#
# # 设置主刻度标签的位置,标签文本的格式
# ax.xaxis.set_major_locator(xmajorLocator)
# ax.xaxis.set_major_formatter(xmajorFormatter)
#
# ax.yaxis.set_major_locator(ymajorLocator)
# ax.yaxis.set_major_formatter(ymajorFormatter)
#
# # 显示次刻度标签的位置,没有标签文本
# ax.xaxis.set_minor_locator(xminorLocator)
# ax.yaxis.set_minor_locator(yminorLocator)
#
# ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
# ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
#
# show()