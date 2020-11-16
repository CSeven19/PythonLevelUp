# 绘图，可视化



import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import json
import pylab
import os.path
from datetime import datetime


# # 8.1 matplotlib入门
# #

# # 1 Figure对象(matplotlib整个图表为一个Figure对象)
# fig = plt.figure()  #创建一个空白窗口
# # 或者使用plt.gcf()获取fig
# # print(plt.gcf())  #获得当前figue的引用

# # 2 add_subplot子绘图plot(figure相当于Frame)
# # 添加3个子视图
# ax1 = fig.add_subplot(2,2,1)  #add_subplot(行数，列数，序数(默认x,y坐标标尺))
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)

# 三种基本图类型
# # plt.plot([1.5,3.5,-2,1.6])  #于最后一个subplot显示.
# ax3.plot(np.random.randn(50).cumsum(),"k--")
# # plt.plot(np.random.randn(50).cumsum(),"k--")  #plot普通图，"k--"线型选项,黑色虚线 ,x轴=50，y轴=随机数
# plt.show() # 显示
# _ = ax1.hist(np.random.randn(100),bins=20,color="k",alpha=0.3)  #hist直方图
# plt.show()
# ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))  #散点图
# plt.show()

# # 3subplots() 综合Figure+subplot，返回一个含有已创建的subplot对象的数组(参考P245 参数一览)

# fig,axes = plt.subplots(2,3)
# # plt.show()
# print(fig)
# print(axes)
# print(axes[0,1])

# # 4subplots_adjust()修改边距
# # 格式:plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=None,hspace=None)
# fig,axes = plt.subplots(2,2,sharex=True,sharey=True)
# for i in range(2):
#     for j in range(2):
#         axes[i,j].hist(np.random.randn(500),bins=500,color="k",alpha=1)  #bins=x轴显示样本数,alpha=x轴显示样本数相关参数
# plt.subplots_adjust(wspace=1,hspace=0)  # 各子图对应x,y轴的间距
# plt.show()

# # 5颜色，标记，线型
# plt.plot(np.random.randn(30).cumsum(),"ko--")  #cumsum()元素累积和
# plt.plot(np.random.randn(30),"ko--")
# # color:
# # b---blue   c---cyan  g---green    k----black
# # m---magenta r---red  w---white    y----yellow
# # linestyle:
# # -      实线
# # --     短线
# # -.     短点相间线
# # ：     虚点线
# # maker:
# # ``'-'``             solid line style
# #     ``'--'``            dashed line style
# #     ``'-.'``            dash-dot line style
# #     ``':'``             dotted line style
# #     ``'.'``             point marker
# #     ``','``             pixel marker
# #     ``'o'``             circle marker
# #     ``'v'``             triangle_down marker
# #     ``'^'``             triangle_up marker
# #     ``'<'``             triangle_left marker
# #     ``'>'``             triangle_right marker
# #     ``'1'``             tri_down marker
# #     ``'2'``             tri_up marker
# #     ``'3'``             tri_left marker
# #     ``'4'``             tri_right marker
# #     ``'s'``             square marker
# #     ``'p'``             pentagon marker
# #     ``'*'``             star marker
# #     ``'h'``             hexagon1 marker
# #     ``'H'``             hexagon2 marker
# #     ``'+'``             plus marker
# #     ``'x'``             x marker
# #     ``'D'``             diamond marker
# #     ``'d'``             thin_diamond marker
# #     ``'|'``             vline marker
# #     ``'_'``             hline marker
# plt.plot(np.random.randn(30).cumsum(),color="#054E9F",linestyle="dashed",marker="s")
# data = np.random.randn(30).cumsum()
# # 标签
# plt.plot(data,"k--",label="Default")  #默认线性图
# plt.plot(data,"k-",drawstyle="steps-post",label="steps-post")  #drawstyle=绘图型类
# plt.legend(loc="best")  #标签显示
# plt.show()

# # 6刻度，标签，图例
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.plot(np.random.randn(1000).cumsum(),"k--",label="one")
# ticks = ax.set_xticks([0,250,500,750,1000])  #设置x轴刻度位置
# labels = ax.set_xticklabels(["one","two","three","four","five"],rotation=30,fontsize="small")  #设置x轴刻度标签
# ax.set_title("my first custome matplotlib plot")  #设置标题
# ax.set_xlabel("stages")  #x轴标签名
# ax.legend(loc="best")  #设置显示图例
# plt.show()

# # 7注解，以及在subplot上绘图.(参看P252图形)
# # 注解
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# data = pd.read_csv("spx.csv",index_col=0,parse_dates=True)
# spx = data["SPX"]
# spx.plot(ax=ax,style="k-")
# crisis_data = [
#     (datetime(2007,10,11),"Peak of bull market"),
#     (datetime(2008,3,12),"Bear Stearns Fails"),
#     (datetime(2008,9,15),"Lehman Bankruptcy")
# ]
# for data,label in crisis_data:
#     ax.annotate(label,xy=(data,spx.asof(data)+50),  #subplot图形中添加注释
#     xytext = (data,spx.asof(data)+200),
#     arrowprops = dict(facecolor = "black"),
#     horizontalalignment = "left",verticalalignment="top")
# ax.set_xlim("1/1/2007","1/1/2011")  #设置x轴刻度范围.
# ax.set_ylim([600,1800])
# ax.set_title("Important dates in 2008-2009 fin4ancial crisis")

# # 8绘图
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# rect = plt.Rectangle((0.2,0.75),0.4,0.15,color="k",alpha=0.3)
# circ = plt.Circle((0.7,0.2),0.15,color="b",alpha=0.3)
# pgon = plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],color="g",alpha=0.5)
# ax.add_patch(rect)
# ax.add_patch(circ)
# ax.add_patch(pgon)
# plt.show()
# # savefig() 保存图片(P255 参数一览)
# plt.savefig("figpath.svg") #将当前运行中的图标保存到文件.
# plt.savefig("figpath.svg",dpi=400,bbox_inches="tight")  #dpi=分辨率，bbox_inches=剪除当前图表周围的空白
# # savefig可写入流中
# from io import StringIO
# buffer = StringIO()
# plt.savefig(buffer)  #存储到StringIO对象上.
# plot_data = buffer.getvalue()

# # 9 matplotlib配置(matplotlib自定义)
# plt.rc("figure",figsize=(10,10))  # 全局设置默认图像大小为10*10
# font_options = {"family":"monospace",
#                 "weight":"bold",
#                 "size":"small"}
# plt.rc("font",**font_options)


# # 8.2 pandas绘图函数
# # 1Series/DataFrame自带plot()(参考P257 plot() 参数一览)
# randnn = np.random.randn(10)
# print(randnn)
# print(randnn.cumsum())  #累加
# s = Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
# s.plot()
# # 或者使用下面的替代
# # plt.plot(s,"k--")
# # plt.show()
# # DF
# data = np.random.randn(10,4)  #10*4 matrix
# print(data)
# df = DataFrame(data.cumsum(0),columns=["A","B","C","D"],index=np.arange(0,100,10))
# df.plot()

# # 2 柱状图 kind="bar"/kind="barh"
# fig, axes = plt.subplots(2,1)
# data = Series(np.random.randn(16), index=list("abcdefghijklmnop"))
# data.plot(kind="bar", ax=axes[0], color="k", alpha=0.7)
# data.plot(kind="barh", ax=axes[1], color="k", alpha=0.7)
# # df
# df = DataFrame(np.random.rand(6,4),
#                index=["one","two","three","four","five","six"],
#                columns=pd.Index(["A","B","C","D"], name="Genus"))
# df.plot(kind="bar")
# # stacked 堆叠图.
# df.plot(kind="barh", stacked=True, alpha=0.5)  #堆叠Index的柱状图.
#
# # crosstab(index,colums) 交叉表,是一种用于计算分组频率的特殊透视表.
# tips = pd.read_csv("tips.csv")
# party_counts = pd.crosstab(tips.day,tips.size)
# party_pcts = party_counts.div(party_counts.sum(1).astype(float),axis=0)  #div(总量，坐标轴) 除法
# party_pcts.plot(kind="bar",stacked=True)  #显示频率的堆叠图.

# # # 3直方图(histogram)，密度图(KDE)
# # tips["tip_pct"] = tips["tip"]/tips["total_bill"]
# # tips["tip_pct"].hist(bins=50)  #直方图
# # tips["tip_pct"].plot(kind="kde")  #密度图
# comp1 = np.random.normal(0,1,size=200)  #N(0,1)
# comp2 = np.random.normal(10,2,size=200)  #N(10,4)
# values = Series(np.concatenate([comp1,comp2]))
# values.hist(bins=100, alpha=0.3, color="k", normed=True)
# values.plot(kind="kde", style="k--")
#
# # 4散布图 scatter()
# macro = pd.read_csv("pythonLevel3/pythonDataAnalysis/macrodata.csv")
# data = macro[["cpi", "m1", "tbilrate", "unemp"]]
# trans_data = np.log(data).diff().dropna()  # diff() 返回一个由相邻数组元素的差值构成的数组,有点类似于微积分中的微分。
# plt.scatter(trans_data["m1"], trans_data["unemp"])  #散点图
# plt.title("Chages in log %s vs. log %s" % ("m1","unemp"))
# pd.scatter_matrix(trans_data, diagonal="kde", color="k", alpha="0.3")  #散布图矩阵.

# # 5绘制地图
# # data = pd.read_csv("pythonLevel3/pythonDataAnalysis/Haiti.csv")
# data = pd.read_csv("Haiti.csv")
# # print(data)
# # print(data.describe())
# # 清楚错位位置及缺失分类信息
# data = data[(data.LATITUDE > 18) &
#             (data.LATITUDE < 20) &
#             (data.LONGITUDE > -75) &
#             (data.LONGITUDE < -70) &
#             (data.CATEGORY.notnull())]
# # 规划函数集
# def to_cat_list(catstr):
#     stripped = (x.strip() for x in catstr.split(","))
#     return [x for x in stripped if x]
# def get_all_categories(cat_series):
#     cat_sets = (set(to_cat_list(x)) for x in cat_series)
#     return sorted(set.union(*cat_sets))
# def get_english(cat):
#     code, names = cat.split(".")
#     if "|" in names:
#         names = names.split("|")[1]
#     return code,names.strip()
# def get_code(seq):
#     return [x.split(".")[0] for x in seq if x]
# # 列表跟名称映射
# all_cats = get_all_categories(data.CATEGORY)
# english_mapping = dict(get_english(x) for x in all_cats)
# # print(english_mapping["2a"])
# all_codes = get_code(all_cats)
# code_index = pd.Index(np.unique(all_codes))
# dummy_frame = DataFrame(np.zeros((len(data),len(code_index))),index=data.index,columns=code_index)
# # print(dummy_frame.ix[:, :6])
# for row,cat in zip(data.index,data.CATEGORY):
#     codes = get_code(to_cat_list(cat))
#     dummy_frame.ix[row,codes] = 1
# data = data.join(dummy_frame.add_prefix("category_"))
# 省略(参考P269)

# # 8.3 相关模块
# chaco
# mayavi
# 基于Web的图形化技术(趋势)


# 野怪1
# import numpy as np
# import matplotlib.pyplot as plt
# from pylab import *
#
# x = np.arange(-5.0, 5.0, 0.02)
# y1 = np.sin(x)
#
# plt.figure(1)
# plt.subplot(211)
# plt.plot(x, y1)
#
# plt.subplot(212)
# # 设置x轴范围
# xlim(-2.5, 2.5)
# # 设置y轴范围
# ylim(-1, 1)
# plt.plot(x, y1)
# plt.show()

# 野怪2
# # 来源https://matplotlib.org/examples/animation/animate_decay.html的matplotlib样本集合之一
# """
# =====
# Decay
# =====
#
# This example showcases a sinusoidal decay animation.
# """
#
#
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
#
# def data_gen(t=0):
#     cnt = 0
#     while cnt < 1000:
#         cnt += 1
#         t += 0.1
#         yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
#
#
# def init():
#     ax.set_ylim(-1.1, 1.1)
#     ax.set_xlim(0, 10)
#     del xdata[:]
#     del ydata[:]
#     line.set_data(xdata, ydata)
#     return line,
#
# fig, ax = plt.subplots()
# line, = ax.plot([], [], lw=2)
# ax.grid()
# xdata, ydata = [], []
#
#
# def run(data):
#     # update the data
#     t, y = data
#     xdata.append(t)
#     ydata.append(y)
#     xmin, xmax = ax.get_xlim()
#
#     if t >= xmax:
#         ax.set_xlim(xmin, 2*xmax)
#         ax.figure.canvas.draw()
#     line.set_data(xdata, ydata)
#
#     return line,
#
# ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
#                               repeat=False, init_func=init)
# plt.show()