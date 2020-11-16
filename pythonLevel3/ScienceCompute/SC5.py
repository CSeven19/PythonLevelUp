# matplotlib

import numpy as np
import matplotlib.pyplot as plt

# # 5.1快速绘制
#
# x = np.linspace(0, 10, 1000)
# y = np.sin(x)
# z = np.cos(x ** 2)
#
# plt.figure(figsize=(8, 4)) # figsize = (宽，高) 单位为英寸dpi == 800*400像素
# plt.plot(x, y, label="$sin(x)$", color="r", linewidth=2)
# plt.plot(x, z, "b--", label="$cos(x**2)$")
# plt.xlabel("Time(s)")
# plt.ylabel("Volt")
# plt.title("PyPlot First Example")
# plt.ylim(-1.2, 1.2)
# plt.legend()
# plt.show()

# # 5.2 配置
# x = np.arange(0, 5, 0.1)
# line, = plt.plot(x, x * x, "k--")
# # 单独调用属性
# line.set_antialiased(False) #关闭对象的反锯齿效果
# print(line.get_linewidth())
# # 使用setp()统一配置属性.
# lines = plt.plot(x, np.sin(x), x, np.cos(x))
# plt.setp(lines, color="r", linewidth=2.0)
# # 获取各个属性
# print(plt.getp(lines[0], "color")) # 输出颜色属性
# print(plt.getp(lines[1]))  # 输出全属性
# plt.show()

# 5.3 绘制子图集合
# for idx, color in enumerate("rgbyck"):
#     plt.subplot(320+idx+1, axisbg=color)
# plt.show()

# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
# if __name__ == '__main__' :
#     t1 = np.arange(0, 5, 0.1)
#     t2 = np.arange(0, 5, 0.02)
#
#     plt.figure(12)
#     plt.subplot(221) # 等价于plt.subplot(2,2,1)
#     plt.plot(t1, f(t1), 'bo', t2, f(t2), 'r--')
#
#     plt.subplot(222)
#     plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
#
#     plt.subplot(212)
#     plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
#
#     plt.show()

# # 5.4 Artist对象
# artist对象有容器(figure,axes,axis),简单类型2种.
# 5.4.1 Artist的属性
# fig = plt.figure()
# ax = fig.add_axes([0.15, 0.1, 0.7, 0.3])  # 类似add_subplot() 都可以往图表中添加轴(或子图)
# line, = ax.plot([1,2,3],[1,2,1])
# ax.set_xlabel("time")
# plt.show()

# # figure/artist对象都包含了patch背景属性
# fig = plt.figure()
# fig.show()
# fig.patch.set_color("g")
# fig.set_alpha(0.5*fig.get_alpha())
# fig.set(alpha=0.5, zorder=2) # 复合设置
# fig.canvas.draw() # 更新显示
# plt.getp(fig.patch) # 获取Artist对象的所有属性名和值
# plt.show()

# # 5.4.2 figure容器
# 最大的Artist容器是 matplotlib.figure.Figure
# from matplotlib.lines import Line2D
# fig = plt.figure()
# line1 = Line2D([0,1],[0,1], transform=fig.transFigure, figure=fig, color="r")
# line2 = Line2D([0,1],[1,0], transform=fig.transFigure, figure=fig, color="g")
# fig.lines.extend([line1, line2])
# fig.show() # 需要ipython执行

# # 5.4.3 Axes容器
# # Axes容器是整个matplotlib库的核心，它包含了组成图表的众多Artist对象
# # 和Figure一样，它有一个patch属性作为背景
# # 参考DA8绘图
# fig = plt.figure()
# ax = fig.add_subplot(111)
# t = ax.scatter(np.random.rand(20), np.random.rand(20))
# print(t)  # 返回值为CircleCollection对象
# print(ax.collections)  # 返回的对象已经添加进了collections列表中
# fig.show()
# t.get_sizes()  # 获得Collectio

# 5.4.4 axis容器
# Axis容器包括坐标轴上的刻度线、刻度文本、坐标网格以及坐标轴标题等内容。刻度包括主刻度和
# 副刻度，分别通过Axis.get_major_ticks和Axis.get_minor_ticks方法获得
plt.plot([1, 2, 3], [4, 5, 6])
# plt.show()
axis = plt.gca().xaxis  # 获取x轴的Axis容器
print(axis.get_ticklocs())  # 获得刻度的位置列表
print(axis.get_ticklabels())  # 获得刻度标签列表
print([x.get_text() for x in axis.get_ticklabels()])  # 获得刻度的文本字符串
print(axis.get_ticklines())  # 获得主刻度线列表，图的上下刻度线共10条
print(axis.get_ticklines(minor=True))  # 获得副刻度线列表
# 获得刻度线或者刻度标签之后，可以设置其各种属性，下面设置刻度线为绿色粗线，文本为红色并且旋转45度
for label in axis.get_ticklabels():
    label.set_color("red")
    label.set_rotation(45)
    label.set_fontsize(16)
for line in axis.get_ticklines():
    line.set_color("green")
    line.set_markersize(25)
    line.set_markeredgewidth(3)
plt.show()
