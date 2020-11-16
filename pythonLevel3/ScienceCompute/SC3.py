# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import leastsq
import pylab as pl

# # 3.1 最小二乘
# def func(x, p):
#     """
#     数据拟合所用的函数: A*sin(2*pi*k*x + theta)
#     """
#     A, k, theta = p
#     return A*np.sin(2*np.pi*k*x+theta)
#
# def residuals(p, y, x):
#     """
#     实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
#     """
#     return y - func(x, p)
#
# x = np.linspace(0, -2*np.pi, 100)
# A, k, theta = 10, 0.34, np.pi/6 # 真实数据的函数参数
# y0 = func(x, [A, k, theta]) # 真实数据
# y1 = y0 + 2 * np.random.randn(len(x)) # 加入噪声之后的实验数据
#
# p0 = [7, 0.2, 0] # 第一次猜测的函数拟合参数
#
# # 调用leastsq进行数据拟合
# # residuals为计算误差的函数
# # p0为拟合参数的初始值
# # args为需要拟合的实验数据
# plsq = leastsq(residuals, p0, args=(y1, x))
#
# print("真实参数:", [A, k, theta])
# print("拟合参数:", plsq[0]) # 实验数据拟合后的参数
#
# pl.plot(x, y0, label=u"真实数据")
# pl.plot(x, y1, label=u"带噪声的实验数据")
# pl.plot(x, func(x, plsq[0]), label=u"拟合数据")
# pl.legend()
# pl.show()


# # 3.2 函数最小值(fmin, fmin_powell, fmin_cg, fmin_bfgs)
# # 下面的程序通过求解卷积(y = x ∗ h)的逆运算(反卷积(去光滑化))演示fmin的功能。
# # -*- coding: utf-8 -*-
#
# import scipy.optimize as opt
# import numpy as np
#
# def fmin_convolve(fminfunc, x, h, y, yn, x0):
#     """
#     x (*) h = y, (*)表示卷积
#     yn为在y的基础上添加一些干扰噪声的结果
#     x0为求解x的初始值
#     """
#     def convolve_func(h):
#         """
#         计算 yn - x (*) h 的power
#         fmin将通过计算使得此power最小
#         """
#         return np.sum((yn - np.convolve(x, h))**2)
#
#     # 调用fmin函数，以x0为初始值, 求得使convolve_func(损失函数)最小的被卷函数h的估计h0 (参考最小二乘例子)
#     h0 = fminfunc(convolve_func, x0)
#
#     print(fminfunc.__name__)
#     print("*"*40)
#     # 输出 x (*) h0 和 y 之间的相对误差
#     print("error of y:", np.sum((np.convolve(x, h0)-y)**2)/np.sum(y**2))
#     # 输出 h0 和 h 之间的相对误差
#     print("error of h:", np.sum((h0-h)**2)/np.sum(h**2))
#     print()
#
# def n(m,n,nscale):
#     """
#     随机产生x, h, y, yn, x0等数列，调用各种fmin函数求解b
#     m为x的长度, n为h的长度, nscale为干扰的强度
#     """
#     x = np.random.rand(m)  #被卷函数1
#     h = np.random.rand(n)  #被卷函数2
#     y = np.convolve(x, h)  #卷积函数
#     yn = y + np.random.rand(len(y)) * nscale  #带噪声的卷积函数模拟信号
#     x0 = np.random.rand(n)  #被卷函数1的初始值.
#
#     fmin_convolve(opt.fmin, x, h, y, yn, x0)
#     fmin_convolve(opt.fmin_powell, x, h, y, yn, x0)
#     fmin_convolve(opt.fmin_cg, x, h, y, yn, x0)
#     fmin_convolve(opt.fmin_bfgs, x, h, y, yn, x0)
#
# if __name__ == "__main__":
#     n(200,20,0.1)


# # 3.3 非线性方程组求解fsolve(func, x0) x0为未知数矢量的初始值
# # 求如下方程组解
# # • 5*x1 + 3 = 0
# # • 4*x0*x0 - 2*sin(x1*x2) = 0
# # • x1*x2 - 1.5 = 0
#
# from scipy.optimize import fsolve
# from math import sin,cos
#
# def f(x):
#     x0 = float(x[0])
#     x1 = float(x[1])
#     x2 = float(x[2])
#     return [
#         5*x1+3,
#         4*x0*x0 - 2*sin(x1*x2),
#         x1*x2 - 1.5
#     ]
#
# result = fsolve(f, [1,1,1])
#
# print(result)
# print(f(result))
# #
# # [-0.70622057 -0.6        -2.5       ] # 未知系数结果集[x0,x1,x2] 如-0.6*-2.5 -1.5 = 0
# # [0.0, -9.126033262418787e-14, 5.329070518200751e-15]  #f(result)各方程代入估计后的计算结果
#
# # 2 使用雅可比矩阵的fsolve实例(可大幅提高收敛速度)
# # -*- coding: utf-8 -*-
# from scipy.optimize import fsolve
# from math import sin,cos
# def f(x):
#     x0 = float(x[0])
#     x1 = float(x[1])
#     x2 = float(x[2])
#     return [
#         5*x1+3,
#         4*x0*x0 - 2*sin(x1*x2),
#         x1*x2 - 1.5
#     ]
#
# # 雅可比矩阵(参考P58)
# # 雅可比矩阵(参考P58)
# def j(x):
#     x0 = float(x[0])
#     x1 = float(x[1])
#     x2 = float(x[2])
#     return [
#         [0, 5, 0],
#         [8*x0, -2*x2*cos(x1*x2), -2*x1*cos(x1*x2)],
#         [0, x2, x1]
#     ]
#
# result = fsolve(f, [1,1,1], fprime=j)
# print(result)
# print(f(result))


# # 3.4 B-Spline样条曲线(插值)
# # 下面是使用直线和B-Spline对正弦波上的点进行插值的例子。
# # -*- coding: utf-8 -*-
# import numpy as np
# import pylab as pl
# from scipy import interpolate
#
# x = np.linspace(0, 2*np.pi+np.pi/4, 10)
# y = np.sin(x)
#
# x_new = np.linspace(0, 2*np.pi+np.pi/4, 100)
# f_linear = interpolate.interp1d(x, y)
# tck = interpolate.splrep(x, y)
# y_bspline = interpolate.splev(x_new, tck)
#
# pl.plot(x, y, "o", label=u"原始数据")
# pl.plot(x_new, f_linear(x_new), label=u"线性插值")
# pl.plot(x_new, y_bspline, label=u"B-spline插值")
# pl.legend()
# pl.show()
# #
# # 2 一维插值
# # 插值不同于拟合。插值函数经过样本点，拟合函数一般基于最小二乘法尽量靠近所有样本点穿过。常见插值方法有拉格朗日插值法、分段插值法、样条插值法。
# # 样条插值
# # !/usr/bin/env python
# # -*-coding:utf-8 -*-
# import numpy as np
# from scipy import interpolate
# import pylab as pl
#
# x = np.linspace(0, 10, 11)
# # x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
# y = np.sin(x)
# xnew = np.linspace(0, 10, 101)
# pl.plot(x, y, "ro")
#
# for kind in ["nearest", "zero", "slinear", "quadratic", "cubic"]:  # 插值方式
#     # "nearest","zero"为阶梯插值
#     # slinear 线性插值
#     # "quadratic","cubic" 为2阶、3阶B样条曲线插值
#     f = interpolate.interp1d(x, y, kind=kind)
#     # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
#     ynew = f(xnew)
#     pl.plot(xnew, ynew, label=str(kind))
# pl.legend(loc="lower right")
# pl.show()
# #
# # 3 二维插值
# # -*- coding: utf-8 -*-
# """
# 演示二维插值。
# """
# import numpy as np
# from scipy import interpolate
# import pylab as pl
# import matplotlib as mpl
#
#
# def func(x, y):
#     return (x + y) * np.exp(-5.0 * (x ** 2 + y ** 2))
#
#
# # X-Y轴分为15*15的网格
# y, x = np.mgrid[-1:1:15j, -1:1:15j]
#
# fvals = func(x, y)  # 计算每个网格点上的函数值  15*15的值
# print(len(fvals[0]))
#
# # 三次样条二维插值
# newfunc = interpolate.interp2d(x, y, fvals, kind='cubic')
#
# # 计算100*100的网格上的插值
# xnew = np.linspace(-1, 1, 100)  # x
# ynew = np.linspace(-1, 1, 100)  # y
# fnew = newfunc(xnew, ynew)  # 仅仅是y值   100*100的值
#
# # 绘图
# # 为了更明显地比较插值前后的区别，使用关键字参数interpolation='nearest'
# # 关闭imshow()内置的插值运算。
# pl.subplot(121)
# im1 = pl.imshow(fvals, extent=[-1, 1, -1, 1], cmap=mpl.cm.hot, interpolation='nearest', origin="lower")  # pl.cm.jet
# # extent=[-1,1,-1,1]为x,y范围  favals为
# pl.colorbar(im1)
#
# pl.subplot(122)
# im2 = pl.imshow(fnew, extent=[-1, 1, -1, 1], cmap=mpl.cm.hot, interpolation='nearest', origin="lower")
# pl.colorbar(im2)
#
# pl.show()


# # 3.5 数值积分
# import numpy as np
# from scipy import integrate
#
#
# # 1求单位圆(x=[-,1],y=[-1,1])面积为例
# def half_circle(x):  #单位半圆曲线函数(x^2 + y^2 = 1)
#     return (1-x**2)**0.5
# N = 10000
# x = np.linspace(-1, 1, N)
# dx = 2.0/N
# y = half_circle(x)
# print(y[:-1])
# print(y[1:])
# # print(dx * np.sum(y[:-1] + y[1:]))  # 面积的两倍  使用经典的分小矩形计算面积总和
# print(dx * np.sum(2*y))  # 方法1：半圆面积的两倍=圆面积  使用经典的分小矩形计算面积总和 :dx*y0+dx*y1+...dx*yn = dx*sum(y)
# print(np.trapz(y, x) * 2)  # 方法2：数值积分 此函数计算的是以x,y为顶点坐标的折线与X轴所夹的面积。
# pi_half, err = integrate.quad(half_circle, -1, 1)  # #方法3：对半圆曲线积分
# print(pi_half*2)
# # 2dblquad() 二重积分/ tplquad() 三重积分
# # dblquad(func2d, a, b, gfun, hfun)  对于func2d(x,y)函数进行二重积分，其中a,b为变量x的积分区间，而gfun(x)到hfun(x)为变量y的积分区间。
# def half_sphere(x, y):
#     return (1-x**2-y**2)**0.5
# pi_half, err = integrate.dblquad(half_sphere, -1, 1,lambda x:-half_circle(x),lambda x:half_circle(x))  #注意y区间必须是函数
# print(pi_half)
# print(np.pi*4/3/2) # 通过球体体积公式计算的半球体积


# # 3.6 常微分方程组
# # 洛仑兹吸引子:计算下列的微分方程组
# # dx
# # dt = σ(y − x)
# # dy
# # dt = x(ρ − z) − y
# # dz
# # dt = xy − βz
# # -*- coding: utf-8 -*-
# from scipy.integrate import odeint
# import numpy as np
#
# def lorenz(w, t, p, r, b):
#     # 给出位置矢量w，和三个参数p, r, b计算出
#     # dx/dt, dy/dt, dz/dt的值
#     x, y, z = w
#     # 直接与lorenz的计算公式对应
#     return np.array([p*(y-x), x*(r-z)-y, x*y-b*z])
#
# t = np.arange(0, 30, 0.01) # 创建时间点
# # 调用ode对lorenz进行求解, 用两个不同的初始值
# # 1. lorenz， 它是计算某个位移上的各个方向的速度(位移的微分)
# # 2. (0.0, 1.0, 0.0)，位移初始值。计算常微分方程所需的各个变量的初始值
# # 3. t， 表示时间的数组，odeint对于此数组中的每个时间点进行求解，得出所有时间点的位置
# # 4. args， 这些参数直接传递给lorenz函数，因此它们都是常量
# track1 = odeint(lorenz, (0.0, 1.00, 0.0), t, args=(10.0, 28.0, 3.0))
# track2 = odeint(lorenz, (0.0, 1.01, 0.0), t, args=(10.0, 28.0, 3.0))
#
# # 绘图
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot(track1[:,0], track1[:,1], track1[:,2])
# ax.plot(track2[:,0], track2[:,1], track2[:,2])
# plt.show()


# # 3.7 滤波器
# import scipy.signal as signal
# # 下面的程序设计一个带通IIR滤波器：
# b, a = signal.iirdesign([0.2, 0.5], [0.1, 0.6], 2, 40)
# w, h = signal.freqz(b, a)  #调用freqz计算所得到的滤波器的频率响应：
# power = 20 * np.log10(np.clip(np.abs(h), 1e-8, 1e100))  #损失函数
# pl.plot(w/np.pi*4000, power)  #绘制出滤波器的增益特性图，这里假设取样频率为8kHz：
# t = np.arange(0, 2, 1/8000.0)  #2秒钟取样频率为8kHz的取样时间数组
# sweep = signal.chirp(t, f0=0, t1 = 2, f1=4000.0)  # 调用chirp得到2秒钟的频率扫描波形的数据：
# out = signal.lfilter(b, a, sweep)  #调用lfilter函数计算sweep波形经过带通滤波器之后的结果
# out = 20*np.log10(np.abs(out))  #为了和系统的增益特性图进行比较，需要获取输出波形的包络，因此下面先将输出波形数据转换为能量值：
# index = np.where(np.logical_and(out[1:-1] > out[:-2], out[1:-1] > out[2:]))[0] + 1  #计算包络，找到所有能量大于前后两个取样点(局部最大点)的下标
# pl.plot(t[index]/2.0*4000, out[index] )  #最后将时间转换为对应的频率，绘制所有局部最大点的能量值：


# 用Weave嵌入C语言
