# numpy 高级


import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import json
import pylab
import os.path
from datetime import datetime
from pandas.tseries.offsets import Day, MonthEnd
from datetime import time


# # 12.1ndarray(参考P379 组成图)
# # 1 数据类型
# intsrei = np.ones(10, dtype=np.uint16)
# print(np.issubdtype(intsrei.dtype, np.integer))  # issubdtype() 判断类型
# print(np.float64.mro())  #返回所有父类list
# # 2 数据重塑
# # 1维 => 多维
# # reshape((3, -1)) # -1 代表该维度由数据及reshape()联合自动决定.
# # 多维 => 1维
# # ravel()(不返回数据副本)/flatten()(返回数据副本)
# # 3 数据合并，拆分(P385 方法一览)
# # concatenate() #join()
# # vstack((arr1,arr2))/hstack()  #垂直，水平堆叠
# # split #拆分
# # r_/c_
# arr = np.arange(6)
# arr1 = arr.reshape((3, 2))
# arr2 = np.random.randn(3, 2)
# print(arr1)
# print(arr2)
# print("*"*30)
# print(np.r_[arr1,arr2])  #行堆叠,类union
# print("*"*30)
# print(np.c_[arr1,arr2])  #列堆叠,类join
# # 3 元素重复
# # repeat()
# arr = np.arange(3)
# print(arr)
# print(arr.repeat(3))  #重复3次
# print(arr.repeat([2, 3, 4]))  #各元素依次重复2,3,4次
# arr1 = np.random.randn(2, 2)
# print("*"*30)
# print(arr1)
# print("*"*30)
# print(arr1.repeat([2,3], axis=0))
# print("*"*30)
# print(arr1.repeat([2,3], axis=1))
# # tile()
# print("*"*30)
# print(np.tile(arr1, 2))
# print("*"*30)
# print(np.tile(arr1, (2, 1)))  #(y轴重复倍数，x轴重复倍数)
# print("*"*30)
# print(np.tile(arr1, (3, 2)))


# # 12.2 广播(矢量化计算. 更兼容的矩阵运算)
# # 1简单示例1:
# arr = np.arange(5)
# print(arr * 4)  #标量4广播到所有元素上
# # 2示例2:(区别矩阵的加减法运算)
# arr = np.random.randn(4, 3)
# print(arr)
# print(arr-arr.mean(0))  # arr - 各列平均值 = arr - [mean_y1,mean_y2,mean_y3].repeat(4, axis=0)(可以理解为)
# print((arr-arr.mean(0)).mean(0))
# # 3三维
# arr = np.random.randn(3, 4, 5)
# z_means = arr.mean(2)
# print(arr - z_means[:, :, np.newaxis])  # 由于z轴被平均消除了，np.newaxis 新建长度为1的新轴填补z轴
# print((arr - z_means[:, :, np.newaxis]).mean(2))
# # 4广播方式添加值
# arr = np.zeros((4,3))
# arr[:] = 5
# print(arr)
# col = np.array([1.28, -0.42, 0.44, 1.6])
# arr[:] = col[:, np.newaxis]  #添加y轴
# print("*"*30)
# print(arr)
# print("*"*30)
# arr[:2] = [[-1.37], [0.509]]  #0,1行被修改
# print(arr)


# 12.3 ufunc高级(参考P396 高级方法一览)
# 自定义ufunc(frompyfunc()/vectorize())


# # 12.4 结构化数组
# dtype = [("x", np.int64, 3), ("y", np.int32)]  #自定义dtype[(索引名，类型，长度),(索引名，类型)]
# arr = np.zeros(4, dtype=dtype)
# print(arr)
# print("*"*30)
# print(arr[0]["x"])

# # 12.5 间接排序
# # 1argsort()
# values = np.array([5, 0, 1, 3, 2])
# indexer = values.argsort()  #返回重新排序后的索引list
# print(indexer)
# print(values[indexer])
# # 2lexsort() 类似argsort() 可同时对多array间接排序
# first_name = np.array(["Bob", "Jane", "Steve", "Bill", "Barbara"])
# last_name = np.array(["Jones", "Arnold", "Arnold", "Jones", "Walters"])
# sorter = np.lexsort((first_name, last_name))
# print(first_name[sorter])
# print(last_name[sorter])
# # 3有序数组中查找元素位置 searchsorted()
# arr = np.array([0, 7, 12, 15, 234])
# print(arr.searchsorted([0,8], side="left"))
# # searchsorted() 应用
# data = np.floor(np.random.uniform(0, 10000, size=50))
# bins = np.array([0, 100, 1000, 5000, 10000])
# print(data)
# labels = bins.searchsorted(data)  #等价于np.digitize(data,bins)
# print(Series(data).groupby(labels).mean())


# # 12.6 matrix类
# X = np.array([[8.82, 3.82, -1.14, 2.04],
#               [3.82, 6.75, 0.83, 2.08],
#               [-1.14, 0.84, 5.02, 0.79],
#               [2.04, 2.08, 0.79, 6.24]])
# Xm = np.matrix(X)
# ym = Xm[:, 0]
# print(Xm)
# print("*"*30)
# print(ym)  #选取ai1列
# # 矩阵乘法
# print("*"*30)
# print(ym.T * Xm)
# print("*"*30)
# print(ym.T * Xm * ym)
# # 矩阵的逆
# print(Xm.I)
# print("*"*30)
# print((Xm.I * X).astype("float16"))


# # 12.7 其他
# # 内存映像文件
# # 内存无法存储数据切块读取
# # 1 memmap()对象
# mmap = np.memmap("mymmap", dtype="float64", mode="w+", shape=(10000, 10000))
# mmap.flush()
# del mmap
# 2 h5py/pytables模块  hdf(层次化数据格式)
# 3 性能
# # （1）行优先顺序
# # 将数组元素按行向量排列，第i+1个行向量紧接在第i个行向量后面。
# # [例]二维数组Amn的按行优先存储的线性序列为：
# # a11,a12,…,a1n,a21,a22,…,a2n,……，am1,am2,…，amn
# arr_c = np.ones((1000, 1000), order="C")  #内存布局:行优先顺序，一般行优先的是连续存储的。速度要快.
# arr_f = np.ones((1000, 1000), order="F")  #内存布局:列优先顺序
# print(arr_c.flags)  #查看其属性标志
# print("*"*30)
# print(arr_f.flags)
# print("*"*30)
# print(arr_f.copy("C").flags)  #列优先 转 行优先