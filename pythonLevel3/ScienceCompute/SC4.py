# SymPy


from sympy import *

# # 4.1表示
# # e^iπ + 1 = 0
# print(E**(I*pi)+1)
# # e^ix = cos x + i sin x  欧拉恒等式
# x = Symbol('x', real=True)  # 在SymPy中，数学符号是Symbol类的对象
# print(expand(exp(I*x), complex=True))  #换形
# pprint(series(exp(I*x),x,0,10))  #series() 泰勒展开式
# pprint(re(series(exp(I*x),x,0,10)))  #实部
# pprint(im(series(exp(I*x),x,0,10)))  #虚部

# # 4.2 体积
# # 不定积分  integrate()
# x = Symbol('x', real=True)
# print(integrate(x*sin(x),x))
# # 定积分
# print(integrate(x*sin(x), (x, 0, 2*pi)))
# # 计算圆体积
# x, y, r = symbols('x,y,r')
# print(2 * integrate(sqrt(r*r-x**2), (x, -r, r)))
# # 很遗憾，integrate函数没有计算出结果，而是直接返回了我们输入的算式。
# # 这是因为SymPy不知道r是大于0的，如下重新定义r，就可以得到正确答案了：
# r = symbols('r', positive=True)
# circle_area = 2 * integrate(sqrt(r**2-x**2), (x, -r, r))
# print(circle_area)
# circle_area = circle_area.subs(r, sqrt(r**2-x**2))  #subs(被替换元素，替换元素)
# print(integrate(circle_area, (x, -r, r)))



# # 将6-11 了解
#
# # -*- coding: utf-8 -*-
# import cv2
# lena = cv2.imread("excellent.png")  ##找一个放了照片的路径
# cv2.imshow("Image",lena)
# cv2.waitKey(0)

# # 15.1 读wave文件
# # -*- coding: utf-8 -*-
# import wave
# import pylab as pl
# import numpy as np
#
# # 1打开WAV文档
# f = wave.open(r"c:\WINDOWS\Media\ding.wav", "rb")  #- WindowsXP的经典''叮''声的波形,open返回一个的是一个Wave_read类的实例
#
# # 2读取返回Wave_read对象的格式信息
# # (nchannels, sampwidth, framerate, nframes, comptype, compname)
# # getparams：一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型的描述。
# params = f.getparams()
# nchannels, sampwidth, framerate, nframes = params[:4]
#
# # 3读取波形数据
# # readframes：读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位），
# # readframes返回的是二进制数据（一大堆bytes)，在Python中用字符串表示二进制数据：
# str_data = f.readframes(nframes)
# f.close()
#
# # 4将波形数据转换为数组
# print(sampwidth)  #16bit,2字节表示一个采样值
# wave_data = np.fromstring(str_data, dtype=np.short)  #因为是2字节，使用short据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
# wave_data.shape = -1, 2  #双声道控制
# wave_data = wave_data.T
# print(wave_data)
# print(wave_data[0][1000])
# print("*"*30)
# print(nframes)
# print("*"*30)
# print(framerate)
# time = np.arange(0, nframes) * (1.0 / framerate)  #采样频率 = 采样点数/时间
#
# # 绘制波形
# pl.subplot(211)
# pl.plot(time, wave_data[0])
# pl.subplot(212)
# pl.plot(time, wave_data[1], c="g")
# pl.xlabel("time (seconds)")
# pl.show()


# # 15.2 写wave
# # -*- coding: utf-8 -*-
# import wave
# import numpy as np
# import scipy.signal as signal
#
# framerate = 44100
# time = 10
#
# # 产生10秒44.1kHz的100Hz - 1kHz的频率扫描波
# t = np.arange(0, time, 1.0/framerate)
# wave_data = signal.chirp(t, 100, time, 1000, method='linear') * 10000
# wave_data = wave_data.astype(np.short)
#
# # 打开WAV文档
# f = wave.open(r"sweep.wav", "wb")
#
# # 配置声道数、量化位数和取样频率
# f.setnchannels(1)
# f.setsampwidth(2)
# f.setframerate(framerate)
# # 将wav_data转换为二进制数据写入文件
# f.writeframes(wave_data.tostring())
# f.close()


# 15.3 pyAudio/pyMedia 了解
# 16-21 信号处理

# 22 分形，混沌

# 22.1 Mandelbrot(曼德布洛特)集合 是在复平面上组成分形的点的集合。
# -*- coding: utf-8 -*-

import numpy as np
import pylab as pl
import time
from matplotlib import cm

def iter_point(c):
    z = c
    for i in range(1, 100): # 最多迭代100次
        if abs(z)>2: break # 半径大于2则认为逃逸
        z = z*z+c
    return i # 返回迭代次数

def draw_mandelbrot(cx, cy, d):
    """
    绘制点(cx, cy)附近正负d的范围的Mandelbrot
    """
    x0, x1, y0, y1 = cx-d, cx+d, cy-d, cy+d
    y, x = np.ogrid[y0:y1:200j, x0:x1:200j]
    c = x + y*1j
    start = time.clock()
    mandelbrot = np.frompyfunc(iter_point,1,1)(c).astype(np.float)
    print("time=",time.clock() - start)
    pl.imshow(mandelbrot, cmap=cm.Blues_r, extent=[x0,x1,y0,y1])
    pl.gca().set_axis_off()

x,y = 0.27322626, 0.595153338

pl.subplot(231)
draw_mandelbrot(-0.5,0,1.5)
for i in range(2,7):
    pl.subplot(230+i)
    draw_mandelbrot(x, y, 0.2**(i-1))
pl.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)
pl.show()
