# 数据加载，存储，文件格式

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import csv

# # 6.1读写文本格式数据
# #
# # 1 read_*()族(参看P178参数一览)
#
# # DataFrame读取
# parsed = pd.read_csv("csv_mindex.csv",index_col=["key1","key2"])
# # parsed = pd.read_table("csv_mindex.csv",index_col=["key1","key2"],sep=",")  #等价于上
# print(parsed)
# result = pd.read_table("ex3.txt",sep="\s+")  #分隔符使用正则表达式
# print(result)
# result1= pd.read_table("ex3.txt",sep="\s+",skiprows=[0,2])  #skiprows 跳过文件行数.
# print(result1)
# sentinels = {"C":["-0.619500","NA"],"A":["-0.264438"]}
# result2 = pd.read_csv("ex3.txt",sep="\s+",na_values=sentinels)  #缺失的替换.将C列-0,619500，NA替换成NaN
# print(result2)
#
# # Series读取
# Series.from_csv("ex3.txt",parse_dates=True)
#
# # 非整体读取
# pd.read_csv("ex3.txt",nrows=2)  #指定读2行
# chunker = pd.read_csv("ex3.txt",chunksize=1024)  #分块读取
# print(chunker)
# # tot = Series([])
# for piece in chunker:
#     # tot = tot.add(piece["key"].value_counts(),fill_value=0)
#     print(piece)
# # print(tot[:10])
#
# # 写入
# data = pd.read_csv("ex3.txt")
# data.to_csv("ex4.txt" ,sep="|")  #w模式写入.
# data.to_csv("ex4.txt" ,sep="|",na_rep="NULL")  #替换NaN
# data.to_csv("ex4.txt" ,sep="|",na_rep="NULL",index=False,header=False)  #禁止写入行列索引.
# data.to_csv("ex4.txt" ,sep="|",na_rep="NULL",index=False,cols=["A","B"])  #写一部分列
#
# # 手工处理
# # 转字典
# lines = list(csv.reader(open("ex7.csv")))
# print(lines)
# print(lines[1:])
# header,values = lines[0],lines[1:]
# data2dict = {h:v for h,v in zip(header,zip(*values))}
# # data2dict = {h:v for h,v in zip(header,zip(values))}  #注意同上的区别
# print(data2dict)
# # 自定义csv格式(参考P183 设置属性一览)
# class my_dialect(csv.Dialect):
#     lineterminator = "\n"
#     delimiter = ";"
#     quotechar = '"'  #特殊字符(如分隔符)的引用符号
# reader = csv.reader(open("ex7.csv"),diaect=my_dialect)

