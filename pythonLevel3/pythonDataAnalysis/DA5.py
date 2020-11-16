# pandas

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import pandas_datareader.data as web

# # 5.1pandas数据结构
# #
# # 1Series(可理解为带有序数的一维数组或一个定长的有序字典)
# obj = Series([4,7,-5,3])
# print(obj)
# print(obj.values)
# print(obj.index)
# obj2 = Series([4,7,-5,3],index=["d","b","a","c"])
# print(obj2)
# print(obj2["a"])
# print(obj2[["a","c"]])
# # NumPy数组运算一般会保留索引同值的关系
# obj2 = Series([4,7,-5,3],index=["d","b","a","c"])
# print(obj2[obj2 > 0])
# print(obj2 * 2)
# print(np.exp(obj2))
# print("b" in obj2)
# print("e" in obj2)
# # 字典 转 Series
# sdata = {"Ohio":35000,"Texas":71000,"Oregon":16000,"Utah":5000}
# obj3 = Series(sdata)
# print(obj3)
# newindex = ["California","Ohio","Oregon","Texas"]
# obj4 = Series(sdata,index=newindex)
# print(obj4)  #"California"不存在 ，显示NaN
# # print(pd.isnull(obj4))  #检验是否为null
# # print(pd.notnull(obj4))  #反上
# # 矢量化运算
# print(obj3+obj4)  #索引对应相加.
# 命名
# obj4.name = "population"
# obj4.index.name = "index"
# print(obj4)
# obj4.index = ["Bob","Steve","Jeff","Ryan"]
# print(obj4)
#
# # 2DataFrame(一个表格型的数据结构)
# # 创建DataFrame
# # 传入字典(可传入数据一览P134)
# data = {"state":["Ohio","Ohio","Ohio","Nevada","Nevada"],
#         "year":[2000,2001,2002,2001,2001],
#         "pop":[1.5,1.7,3.6,2.4,2.9]
#         }
# df = DataFrame(data)  #同Series,自动加索引
# print(df)
# df = DataFrame(data,columns=["year","state","pop","debt"],index=["one","two","three","four","five"])  #指定列索引,行索引
# print(df)
# # 查询
# print(df.columns)
# print(df["state"])
# print(df.year)
# print(df.ix["three"])
# # 更改
# df["debt"] = 16.5
# df["debt"] = np.arange(5.)
# print(df)
# val = Series([-1.2,-1.5,-1.7],index=["two","four","five"])  #对two,four,five 进行更改
# df["debt"] = val
# print(df)
# # 添加列，并赋值
# df["eastern"] = df.state == "Ohio"
# print(df)
# # 删除
# del df["eastern"]
# # 转置
# print(df.T)
#
# # 3索引对象(参看P136 index对象一览)
# obj = Series(range(3),index=["a","b","c"])
# index = obj.index
# print(index[1:])
# # index[1] = "d"  #index不可修改，故报错


# # 5.2 基本功能
#
# # 1 reindex() 重新索引(参考P140参数一览)
# # 对Series
# obj = Series([4.5,7.2,-5.3,3.6],index=["d","b","a","c"])
# print(obj)
# obj2 = obj.reindex(["a","b","c","d","e"],fill_value=0)  # fill_value填充索引处值为null的部分
# print(obj2)
# obj3 = Series(["blue","purple","yellow"],index=[0,2,4])
# obj3 = obj3.reindex(range(6),method="ffill")  #向前填充
# print(obj3)
# obj3 = obj3.reindex(range(6),method="bfill")  #向后填充
# print(obj3)
# # 对DataFrame
# df = DataFrame(np.arange(9).reshape((3,3)),index=["a","c","d"],columns=["Ohio","Texas","California"])
# print(df)
# df = df.reindex(["a","b","c","d"])  # 对行索引
# print(df)
# df = df.reindex(columns=["Texas","Utah","California"])  # 对列索引
# print(df)
# df = df.reindex(index=["a","b","c","d"],method="ffill",columns=["Texas","Utah","California"])  ## 对行,列索引
# df = df.ix[["a","b","c","d"],["Texas","Utah","California"]]  ## 对行,列索引
# print(df)
#
# # 2 丢弃指定轴上的项
# # 对Series
# obj = Series(np.arange(5.),index=["a","b","c","d","e"])
# new_del_obj = obj.drop("c")
# print(obj)
# print(new_del_obj)
# # 对DataFrame
# data = DataFrame(np.arange(16).reshape((4,4)),index=["Ohio","COLORADO","Utah","NewYouk"],columns=["one","two","three","four"])
# new_dropindex_obj = data.drop(["COLORADO","Ohio"])
# new_dropcolumns_obj = data.drop(["two","four"],axis=1)
# print(new_dropindex_obj)
# print(new_dropcolumns_obj)
#
# # 3索引，选取，过滤
# # Series查询
# obj = Series(np.arange(4.),index=["a","b","c","d"])
# print(obj["b"])
# print(obj[1])
# print(obj[2:4])
# print(obj["b":"c"])
# print(obj[obj<2])
# print(obj[[1,3]])
# # 更新
# obj["b":"d"] = 5
# print(obj)
# # DataFrame查询(参考P144 查询方法一览)
# data = DataFrame(np.arange(16).reshape((4,4)),index=["Ohio","Colorado","Utah","NewYork"],columns=["one","two","three","four"])
# print(data)
# print(data["two"])
# print(data[["three","one"]])
# print(data[:2])
# print(data[data["three"]>5])
# # ix[行，列]
# print(data.ix["Colorado",["two","three"]])
# print(data.ix[["Colorado","Utah"],[3,0,1]])
# print(data.ix[data.three>5,:3])
# print(data.ix[data["three"]>5,:3])
# # 更新
# data[data<5] = 0  #data<5会遍历该data所有数据进行判断
# print(data)


# 5.3算数运算及数据对齐
# # 矢量化运算
# # Series
# s1 = Series([7.3,-2.5,3.4,1.5],index=["a","c","d","e"])
# s2 = Series([-2.1,3.6,-1.5,4,3.1],index=["a","c","e","f","g"])
# print(s1+s2)  #存在对应项的a,c,e相加，其余为NaN
#
# # DataFrame(行，列皆对应的运算)
# df1 = DataFrame(np.arange(9.).reshape((3,3)),columns=list("bcd"),index=["Ohio","Texas","Colorado"])
# df2 = DataFrame(np.arange(12.).reshape((4,3)),columns=list("bde"),index=["Utah","Ohio","Texas","Oregon"])
# print(df1+df2)
# print(df1.add(df2,fill_value=0))  #带填充NaN默认数据的加法.  类似的还有df1.reindex(columns=df2.columns,fill_value=0)
# print(df1.sub(df2,fill_value=0))  #df1,df2都为NaN的值是无法填充的.还是会保持NaN
# print(df1.div(df2,fill_value=0))
# print(df1.mul(df2,fill_value=0))
# df3 = DataFrame(np.arange(12.).reshape((3,4)),columns=list("abcd"))
# df4 = DataFrame(np.arange(20.).reshape((4,5)),columns=list("abcde"))
# print(df3.add(df4,fill_value=0))
#
# # DataFrame和Series运算
# # 广播(DataFrame和Series运算原理)
# arr = np.arange(12.).reshape((3,4))
# print(arr)
# print(arr[0])
# print(arr-arr[0])
# # dfとSeries
# df = DataFrame(np.arange(12.).reshape((4,3)),columns=list("bde"),index=["Utah","Ohio","Texas","Oregon"])
# series = df.ix[0]
# print(df)
# print(series)
# print(df - series)
# series2 = Series(range(3),index=["b","e","f"])
# print(series2)
# print(df+series2)  #series2的索引+df对应的列
# series3 = df["d"]
# print(series3)
# print(df.sub(series3,axis=0))  #df各列(非对应列)分别-series3的索引

# # 5.4函数应用和映射(numpy的ufuncs通用)
# # 1通用ufuncs
# df = DataFrame(np.random.randn(4,3), columns=list("bde"), index=["Utah","Ohio","Texas","Oregon"])
# print(np.abs(df))
# # 2自定义函数应用
# f = lambda x: x.max() - x.min()
# print(df.apply(f, axis=1))  #axis=0 代表index之间的处理. axis=1代表列之间处理
# def f2(x):
#     return Series([x.min(),x.max()],index=["min","max"])
# print(df.apply(f2))  #取列的最大，最小值
# # 3自定义格式化
# format = lambda x: "%.2f" % x
# print(df.applymap(format))
# print(df["e"].map(format))


# # # 5.5 排序，排名
# # # 1 排序
# # # Series
# obj = Series(range(4),index=["d","a","b","c"])
# print(obj.sort_index())
# print(obj.sort_values())
# #
# # DF
# df = DataFrame(np.arange(8).reshape((2,4)),index=["three","one"],columns=["d","a","b","c"])
# print("**"*10,df.sort_index())  #按行索引排序
# print("**"*10,df.sort_index(axis=1,ascending=False))  #按列索引降序排序
# print("**"*10,df.sort_values(by="a",ascending=False))  #按列a值进行降序排序
# df1 = DataFrame({"b":[4,7,-3,2],"a":[0,1,0,1]})
# print("**"*10,df1.sort_values(by=["a","b"],ascending=False))
#
# 2排名
# # rank() 数的大小排名，相同数取平均值
# # Series
# obj = Series([7,-5,7,4,2,0,4])
# print(obj.rank())
# print(obj.rank(method="first"))  #按大小，位置前后联合排名.method参数一览P152
# print(obj.rank(ascending=False,method="max"))
# # DataFrame
# df = DataFrame({"b":[4.3,7,-3,2],"a":[0,1,0,1],"c":[-2,5,8,-2.5]})
# print(df)
# print(df.rank(axis=1))  #对列之间进行排名.
#
# # 3重复索引
# obj = Series(range(5),index=["a","a","b","b","c"])
# print(obj)
# print(obj.index.is_unique)
# print(obj["a"])
# df = DataFrame(np.random.randn(4,3),index=["a","a","b","b"])
# # print(df["b"])  #报错，只能显示列索引
# # print(df[0])
# print(df.ix["b"])


# # 5.6 统计(参考P155 统计方法一览)
# # 1 ufuncs()
# df = DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=["a","b","c","d"],columns=["one","two"])
# print(df.sum())
# print(df.sum(axis=1))
# print(df.mean(axis=1,skipna=False))  #默认skipna=True,但是所有值都为NaN的场合还是得NaN;skipna=False不自动将其后加入的NaN化为0,
# print(df.describe())  #汇总显示各类统计量
#
# # 2相关系数，协方差
# # all_data ={}
# # for ticker in ["AAPL","IBM","MSFT","GOOG"]:
# #     all_data[ticker] = web.get_data_yahoo(ticker,"1/1/2010","1/1/2015")
# # price = DataFrame({tic:data["Adj Close"] for tic,data in all_data.items()})
# # volume = DataFrame({tic:data["Volume"] for tic,data in all_data.items()})
# # returns = price.pct_change()
# # print(returns.tail())
# #
# df = DataFrame([[0.034339,0.011117,0.004420,0.002747],[0.012294,0.007098,0.013282,0.005479],[-0.011861,-0.005571,-0.003474,0.006812],
#                 [0.012147,0.005376,0.005468,-0.013532],[-0.004300,-0.004416,-0.012609,-0.015432]],
#                index=["2009-12-24","2009-12-28","2009-12-29","2009-12-30","2009-12-31"],
#                columns=["AAPL","IBM","MSFT","GOOG"])
# # print(df)
# # 两随机变量的相关系数及协方差
# print(df.MSFT.corr(df.IBM))  # corr() 计算相关系数
# print(df["MSFT"].corr(df["IBM"]))
# print(df["MSFT"].cov(df["IBM"]))
# # 所有变量相互相关系数及协方差
# print(df.corr())
# print(df.cov())
# # 多对一相互相关系数
# print(df.corrwith(df["IBM"]))
#
# # 3 唯一值，值计数，成员资格
# # Series
# # 唯一值
# obj = Series(["c","a","d","a","a","b","b","c","c"])
# uniques = obj.unique()
# print(uniques)
# # 值计数
# print(obj.value_counts())  #计算各数据出现频数
# print(pd.value_counts(obj.values,sort=False))
# # 成员资格判断
# mask = obj.isin(["b","c"])
# print(mask)
# print(obj[mask])
# DataFrame
# # 计数
# data = DataFrame({"Qu1":[1,3,4,3,4],
#                   "Qu2":[2,3,1,2,3],
#                   "Qu3":[1,5,2,4,4]})
# print(data)
# print(data.apply(pd.value_counts).fillna(0))
#
# # 4 处理缺失数据(P160 处理方法一览)
# # dropna()删除NaN
# data = Series([1,np.nan,3.5,np.nan,7])
# print(data[data.notnull()])
# print(data.dropna())
# df = DataFrame([[1.,6.5,3.],[1.,np.nan,np.nan],[np.nan,np.nan,np.nan],[np.nan,6.5,3.]])
# print(df.dropna())  #默认删除所有至少存在一个NaN的行
# print(df.dropna(how="all"))  #删除全为NaN的行.
# print(df.dropna(axis=1,how="all"))  #删除全为NaN的列
# print(df.dropna(thresh=3))  #保留至少3个非空值
# # fillna(0)填充NaN (参考P164,参数一览)
# # print(df.fillna(0))
# print(df.fillna({1:0.5,2:-1}))  #填充对应的列
# print(df.fillna(method="ffill"))  #填充对应的列
# print(df.fillna(method="ffill",limit=2))  #填充对应的列
#
# 5 层次化索引
# # Series
# data = Series(np.random.randn(10),index=[["a","a","a",'b',"b","b","c","c","d","d"],
#                                          [1,2,3,1,2,3,1,2,2,3]])
# print(data)
# print(data.index)
# print(data["b"])
# print(data[:,2])  #选取所有为2子索引的行.
# # 使用unstack()转化成非堆叠显示. Series->DataFrame
# print(data.unstack())
# print(type(data.unstack()))
# # stack()堆叠显示，DataFrame -> Series
# print(data.unstack().stack())
# print(type(data.unstack().stack()))
#
# # DataFrame
# df = DataFrame(np.arange(12).reshape((4,3)),index=[["a","a","b","b"],[1,2,1,2]],
#                 columns=[["Ohio","Ohio","Colorado"],["Green","Red","Green"]])
# print(df)
# df.index.names = ["key1","key2"]
# df.columns.names = ["state","color"]
# print(df)
# print(df["Ohio"])
# # swaplevel(name1,name2) 互换2序列，值不变
# print(df.swaplevel("key1","key2"))
# print(df.sortlevel(1))  #按行索引1排序.过时。
# print(df.sort_index(level=1))
# print(df.swaplevel(0,1).sortlevel(0))  #交换索引1，索引0，并对交换后的索引0排序。
#
# # 6 根据层次来ufuncs
# print(df.sum(level="color",axis=1))
#
# set_index() 列索引转行索引
# reset_index() 行索引转列索引

# 5.7 Panel数据结构(三维版DataFrame)
