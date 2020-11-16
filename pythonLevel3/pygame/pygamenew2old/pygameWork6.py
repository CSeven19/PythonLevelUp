# # 图像
# # python支持图像:
# # JPEG（Join Photograhpic Exper Group)，极为常用，一般后缀名为.jpg或者.jpeg。数码相机、网上的图片基本都是这种格式。这是一种有损压缩方式，尽管对图片质量有些损坏，但对于减小文件尺寸非常棒。优点很多只是不支持透明。
# # PNG（Portable Network Graphics）将会大行其道的一种格式，支持透明，无损压缩。对于网页设计，软件界面设计等等都是非常棒的选择！
# # GIF 网上使用的很多，支持透明和动画，只是只能有256种颜色，软件和游戏中使用很少
# # BMP Windows上的标准图像格式，无压缩，质量很高但尺寸很大，一般不使用
# # PCX
# # TGA
# # TIF
# # LBM, PBM
# # XPM
#
# import pygame
# from pygame import Rect
# background_image_filename = "background.png"
# mouse_image_filename = "flame.png"
#
# pygame.init()
# screen = pygame.display.set_mode((640, 480), 0, 32)
#
# # 1创建空白surface
# #HWSURFACE – 类似于前面讲的，更快！不过最好不设定，Pygmae可以自己优化。SRCALPHA – 有Alpha通道的surface，如果你需要透明，就要这个选项。这个选项的使用需要第二个参数为32~
# bland_alpha_surface = pygame.Surface((256, 256), flags=pygame.SRCALPHA, depth=32)
# # 2加载图片并转化成surface对象
# background = pygame.image.load(background_image_filename).convert()
# mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()  #RGBA转化.
# # 3矩形对象
# my_rect1 = (100, 100, 200, 150)
# my_rect2 = ((100, 100), (200, 150))
# #上两种为基础方法，表示的矩形也是一样的
# my_rect3 = Rect(100, 100, 200, 150)
# my_rect4 = Rect((100, 100), (200, 150))
# # 4裁剪区域(定义了哪部分会被绘制，也就是说一旦定义了这个区域，那么只有这个区域内的像素会被修改，其他的位置保持不变，默认情况下，这个区域是所有地方。用于处理固定栏(菜单)及变动部分的(打架界面),)
# screen.set_clip(0, 400, 200, 600)
# # draw_map()
# #在左下角画地图
# screen.set_clip(0, 0, 800, 60)
# # draw_panel()
# #在上方画菜单面板
# # 5子表面(Subsurfaces,Subsurface就是在一个Surface中再提取一个Surface)
# my_font_image = pygame.image.load("background.png")
# letters = [my_font_image.subsurface((0,0), (80,80)),my_font_image.subsurface((80,0), (80,80))]
# # 6填充
# screen.fill((0, 0, 0))
# # 7设置surface坐标及色彩
# import pygame
# from pygame.locals import *
# from sys import exit
# from random import randint
#
# pygame.init()
# screen = pygame.display.set_mode((640, 480), 0, 32)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#
#     rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
#     #当Pygame往surface上画东西的时候，首先会把surface锁住，以保证不会有其它的进程来干扰，画完之后再解锁。
#     #比如此处，每次画100个点，那么就得锁解锁100次，现在我们把两句注释去掉，再执行看看是不是更快了
#     screen.lock()
#     for _ in range(100):  #无应用变量循环
#         rand_pos = (randint(0, 639), randint(0, 479))
#         screen.set_at(rand_pos, rand_col)  # set_at(position,color)设置对应position像素以color  get_at()获取对应position像素色彩。不过很慢谨慎使用.
#     screen.unlock()
#
#     pygame.display.update()
# 8Blitting(图像块复制)\
# blit是对表面做的最多的操作，我们在前面的程序中已经多次用到，不多说了；blit的还有一种用法，往往用在对动画的表现上，
# 比如下例通过对frame_no的值的改变，我们可以把不同的帧（同一副图的不同位置）画到屏幕上：
# screen.blit(ogre, (300, 200), (100 * frame_no, 0, 100, 100))