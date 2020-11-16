# 数据聚合，分组


import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import json
import pylab
import os.path
from datetime import datetime
# import statsmodels.api as sm


# # 9.1分组(P275 分组原理图)
# df = DataFrame({"key1":["a","a","b","b","a"],
#                 "key2":["one","two","one","two","one"],
#                 "data1":np.random.randn(5),
#                 "data2":np.random.randn(5)})
# print(df)
# grouped = df["data1"].groupby(df["key1"])
# groupedall = df.groupby("key1").mean()  #直接使用列名分组,结果中未有key2,因为不是数据列.
# size = df.groupby(["key1", "key2"]).size()  #分组size
# print(type(grouped))  #根据groupby分组生成了新的Series
# print("*"*20)
# print(grouped.mean())
# means = df["data1"].groupby([df["key1"],df["key2"]]).mean()  #按2个关键字分组
# print(means)
# print(means.unstack())
# # 2新添加列的分组
# states = np.array(["Ohio","California","California","Ohio","Ohio"])
# years = np.array([2005,2005,2006,2005,2006])
# print(df["data1"].groupby([states,years]).mean())
# # 3对所有列分组
# print(dict(list(df.groupby(df.dtypes,axis=1))))
# # 4选取一个列，或一组列 分组.
# print(df.groupby("key1")["data1"])  # 等价于 df["data1"].groupby(df["key1"])
# print("*"*20)
# print(df.groupby(["key1","key2"])[["data2"]].mean())
#
# # 5通过字典，Series分组(自定义分组)
# people = DataFrame(np.random.randn(5,5),
#                    columns=["a","b","c","d","e"],
#                    index=["Joe","Steve","Wes","Jim","Travis"])
# people.ix[2:3,["b","c"]] = np.nan
# print(people)
# mapping = {"a":"red","b":"red","c":"blue","d":"blue","e":"red","f":"orange"}
# by_column = people.groupby(mapping,axis=1)  #按字典分组
# print("*"*20)
# print(by_column.sum())
# map_series = Series(mapping)
# print("*"*20)
# print(people.groupby(map_series,axis=1).count())  #按Series分组
#
# # 6 通过函数分组
# print("*"*20)
# print(people.groupby(len).sum())  #以人名长度分组
# print("*"*20)
# key_list = ["one","one","one","two","two"]
# print(people.groupby([len,key_list]).min())
#
# # 7 根据索引级别分组
# columns = pd.MultiIndex.from_arrays([["US","US","US","JP","JP"],[1,3,5,1,3]],
#                                     names=["cty","tenor"])
# hier_df = DataFrame(np.random.randn(4,5),columns=columns)
# print(hier_df)
# print("*"*20)
# print(hier_df.groupby(level="cty",axis=1).count())
# print("*"*20)
# print(hier_df.groupby(level="tenor",axis=1).count())


# # 9.2 聚合(P284 聚合方法一览)
# # 1
# print("*"*20)
# print(df.groupby("key1")["data1"].quantile(0.9))  #取以[min(data1[a]),max(data1[a])]为区间的正太分布的分位数.
# # 2自定义聚合函数 agg()
# def peak_to_peak(arr):
#     return arr.max() - arr.min()
# print(df.groupby("key1").agg(peak_to_peak))
#



# # 9.3 面向列的多函数应用
tips = pd.read_csv("tips.csv")
tips["tip_pct"] = tips["tip"]/tips["total_bill"]
# grouped = tips.groupby(["sex","smoker"])
# print(grouped["tip_pct"].agg(["mean","std",peak_to_peak]))
# print("*"*20)
# print(grouped["tip_pct"].agg([("foo","mean"),("bar",np.std)]))  #各列分别进行对应的聚合运算
# print("*"*20)
# print(grouped["tip_pct","total_bill"].agg(["count","mean","max"]))
# print("*"*20)
# print(grouped.agg({"tip_pct":["min","max","mean","std"],
#                    "size":"sum"}))
#
# # 2 transform()
# key = ["one","two","one","two","one"]
# print(people.groupby(key).mean())
# print("*"*20)
# print(people.groupby(key).transform(np.mean))  #注意区别上式，主要是行索引分别都按one,two分组算平均后赋值了。
# print("*"*20)
# def demean(arr):
#     return arr-arr.mean()
# demeaned = people.groupby(key).transform(demean)
# print(demeaned)
# print("*"*20)
# print(demeaned.groupby(key).mean())
#
# # 3 apply()
# def top(df,n=5,column="tip_pct"):
#     return df.sort_values(by=column, ascending=True)[-n:]  #升序
# print(top(tips,n=6))
# print("*"*20)
# print(tips.groupby("smoker").apply(top))  # apply() = top(smoker)进行排序 + pandas.concat组装
# print("*"*20)
# print(tips.groupby(["smoker","day"]).apply(top,n=4,column="total_bill"))
# print("*"*20)
# print(tips.groupby("smoker",group_keys=False).apply(top))  # 禁用分组，将不会按“smoker”分组
# print("*"*20)
# print(tips.groupby("smoker").apply(top))
#
# # 4 桶分析
# frame = DataFrame({"data1":np.random.randn(1000),
#                    "data2":np.random.randn(1000)})
# factor = pd.cut(frame.data1, 4)
# def get_stats(group):
#     return {"min":group.min(), "max":group.max(), "count":group.count(), "mean":group.mean()}
# grouped = frame.data2.groupby(factor)
# print(grouped.apply(get_stats).unstack())
# # 5 分位数分析
# grouping = pd.qcut(frame.data1, 10)  #cut()函数每个划分数量可以不同(每个划分间隔基本一致)。而qcut()可以保证每个划分数量相同(但一般每个划分间隔不等)
# print("*"*30)
# print(grouping)
# grouped = frame.data2.groupby(grouping)
# print("*"*30)
# print(grouped.apply(get_stats).unstack())


# # 9.4 示例
# #
# # 1 实例1:分组加权平均数及相关系数
# df = DataFrame({"category":["a","a","a","a","b","b","b","b"],
#                 "data":np.random.randn(8),
#                 "weights":np.random.rand(8)})
# print(df)
# grouped = df.groupby("category")
# get_wavg = lambda g: np.average(g["data"],weights=g["weights"])  # 分组加权平均函数.
# print("*"*30)
# print(grouped.apply(get_wavg))
#
# # # 2 实例2:计算日收益率与SPX之间年度相关系数.
# close_px = pd.read_csv("stock_px.csv", parse_dates=True, index_col=0)
# print("*"*30)
# print(close_px[-4:])
# rets = close_px.pct_change().dropna()  #pct_change 这个函数用来计算同colnums两个相邻的数字之间的变化率。
# print("*"*30)
# print(rets[-4:])
# spx_corr = lambda x: x.corrwith(x["SPX"])  #各变量对"SPX"的相关系数
# by_year = rets.groupby(lambda x: x.year)  #groupby(函数) 按行索引的年度分组.
# print("*"*30)
# print(by_year.apply(spx_corr))
# print("*"*30)
# print(by_year.apply(lambda g: g["AAPL"].corr(g["MSFT"])))  #苹果，微软的年度相关系数
#
# # 3 面向分组的线性回归
# def regress(data,yvar,xvars):  # 普通最小二乘回归
#     Y = data[yvar]
#     X = data[xvars]
#     X["intercept"] = 1
#     result = sm.OLS(Y,X).fit()
#     return result.params
# print(by_year.apply(regress, "AAPL", ["SPX"]))


# # 9.5 透视表，交叉表
# # 1 透视表(pivot_table) = 分组 + 聚合
# print(tips.pivot_table(["tip_pct", "size"], index=["sex", "day"], columns="smoker", margins=True))  # ["tip_pct","size"]=待聚合列,rows=分组行索引,cols=列索引，margins=分项小计(横排，竖排均值All)
# print("*"*30)
# print(tips.pivot_table("size", index=["time", "sex", "smoker"], columns="day", aggfunc="sum", fill_value=0))  #aggfunc=聚合函数,fill_value=填充缺失值.
#
# # 2 交叉表(crosstab) 计算分组频率(频数)的特殊透视表
# data = pd.read_csv("crosstabdata.txt")
# print(data)
# # 根据性别和用手习惯进行统计汇总
# print("*" * 30)
# print(pd.crosstab(data["Gender"], data["Handedness"], margins=True))
# # 对小费进行统计
# print("*" * 30)
# print(pd.crosstab([tips.time, tips.day], tips.smoker, margins=True))


