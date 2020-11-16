# 金融，经济数据应用


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

# # 11.1 数据规整化
# #
# # 1 数据对齐
# df1 = DataFrame(np.random.randn(7,4), index=pd.date_range("2011-09-06","2011-09-12",freq="D"), columns=["AAPL","JNJ","SPX","XOM"])
# df2 = DataFrame(np.random.randn(5,3), index=["2011-09-06","2011-09-07","2011-09-08","2011-09-09","2011-09-12"], columns=["AAPL","JNJ","XOM"])
# print(df1)
# print("*"*20)
# print(df2)
# print("*"*20)
# print(df1 * df2)  #数据自动对齐，矢量化计算
# vwap = (df1 * df2).sum()/df2.sum()
# print("*"*20)
# print(vwap.dropna())
# print("*"*20)
# print(df1.align(df2, join="inner"))  #手动对齐
# # 使用字典自构建DataFrame
# s1 = Series(range(3),index=["a","b","c"])
# s2 = Series(range(4),index=["d","b","c","e"])
# s3 = Series(range(3),index=["f","a","c"])
# print("*"*20)
# print(DataFrame({"one":s1,"two":s2,"three":s3}))
# print("*"*20)
# print(DataFrame({"one":s1,"two":s2,"three":s3},index=list("face")))
#
# # 2 频率不同时间序列运算
# # 方法1:升频填充 匹配 更高频运算.
# ts1 = Series(np.random.randn(3),index=pd.date_range("2012-6-13", periods=3, freq="W-WED"))
# ts1.resample("B", fill_method="ffill")
# # 方法2:
# dates = pd.DatetimeIndex(["2012-6-12", "2012-6-17", "2012-6-18", "2012-6-21", "2012-6-22", "2012-6-29"])
# ts2 = Series(np.random.randn(6), index=dates)
# print(ts2)
# print("*"*20)
# print(ts2 + ts1.reindex(ts2.index, method="ffill"))  #按ts2的index 重新index ts1 再运算
#
# # 3 时间选取
# rng = pd.date_range("2012-06-01 09:30", "2012-06-01 15:59", freq="T")
# rng = rng.append([rng + pd.offsets.BDay(i) for i in range(1, 4)])
# ts = Series(np.arange(len(rng), dtype=float), index=rng)
# print(ts)
# print("*"*20)
# print(ts[time(10, 0)])  #选取10点整的各数据.
# print("*"*20)
# print(ts.at_time(time(10, 0)))  #同上
# print("*"*20)
# print(ts.between_time(time(10, 0), time(10, 1)))  #选取时间区间数据
# # asof(指定时间) 选取指定时间的最近有效时间的数据(非NaN数据)。
#
# # 4 拼接数据
# # concat()
# data1 = DataFrame(np.ones((6, 3),dtype=float),
#                   columns=["a", "b", "c"],
#                   index=pd.date_range("6/12/2012", periods=6))
# data2 = DataFrame(np.ones((6, 3), dtype=float)*2,
#                   columns=["a", "b", "c"],
#                   index=pd.date_range("6/13/2012", periods=6))
# spliced = pd.concat([data1.ix[:"2012-06-14"], data2.ix["2012-06-15":]])
# print(spliced)
# data2 = DataFrame(np.ones((6, 4), dtype=float)*2,
#                   columns=["a", "b", "c", "d"],
#                   index=pd.date_range("6/13/2012", periods=6))
# spliced = pd.concat([data1.ix[:"2012-06-14"], data2.ix["2012-06-15":]])
# print("*"*20)
# print(spliced)
# print("*"*20)
# # combine_first(data2)
# print(spliced.combine_first(data2))  #当spliced中NaN处为空，且data2对应位置右值的话。data2的值替换NaN。如果data2对应处也为NaN，则保持NaN
# print(spliced.update(data2, overwrite=False))  #同上 update(data2, overwrite=False)  #overwrite=覆盖否.
# # 利用索引替换数据


# 11.2 相关计算
# 1 收益指数及累计收益
# 2 分组变换，分析
# 3 分组因子暴露
# 4 十分位，四分位分析
