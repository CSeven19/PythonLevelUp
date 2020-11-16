# 数据规整话(清理，转换，合并，重塑)


from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import json

# # 7.1 合并数据集
# # pandas.merge()(类似join)
# # pands.concat()(类似union)
# #
# # 1pandas.merge()
# (1)多对一
# df1 = DataFrame({"key":["b","b","a","c","a","a","b"],"data1":range(7)})
# df2 = DataFrame({"key":["a","b","d"],"data2":range(3)})
# print("*"*20)
# print(df1)
# print("*"*20)
# print(df2)
# print("*"*20)
# print(pd.merge(df1,df2))  #未指定连接点。以重叠列(key)为连接点
# print("*"*20)
# print(pd.merge(df1,df2,on="key"))  #未指定连接点。以重叠列为连接点
# print(pd.merge(df1,df2,how="outer"))  #outer外连接相当于求并,key未重复的项不会消失。how=[left,right,outer,inner]
#
# #(2)对象未有重复列名，指定
# df3 = DataFrame({"lkey":["b","b","a","c","a","a","b"],"data1":range(7)})
# df4 = DataFrame({"rkey":["a","b","d"],"data2":range(3)})
# print(pd.merge(df3,df4,left_on="lkey",right_on="rkey"))
#
# #(3)多对多
# df1 = DataFrame({"key":["b","b","a","c","a","b"],"data1":range(6)})
# df2 = DataFrame({"key":["a","b","a","b","d"],"data2":range(5)})
# print(pd.merge(df1,df2,on="key",how="left"))  #一共11行，多对多产生的笛卡尔积,left会保留c，但是d被删除。
# print(pd.merge(df1,df2,on="key",how="inner"))  #一共10行，多对多产生笛卡尔积,inner去非重复项(c,d项).
#
# # (4)多键连接(参考P201 连接相关方法一览)
# df1 = DataFrame({"key1":["foo","foo","bar"],"key2":["one","two","one"],"lval":[1,2,3]})
# df2 = DataFrame({"key1":["foo","foo","bar","bar"],"key2":["one","one","one","two"],"rval":[4,5,6,7]})
# print(pd.merge(df1,df2, on=["key1","key2"],how="outer"))
# print(pd.merge(df1,df2,on="key1",suffixes=("_left","_right")))  #重复列名(如:key2) 指定后缀用于区分
#
# # (5)列索引合并行索引(交叉合并).
# df1 = DataFrame({"key":["a","b","a","a","b","c"],"value":range(6)})
# df2 = DataFrame({"group_val":[3.5,7]},index=["a","b"])
# print("*"*20)
# print(df1)
# print("*"*20)
# print(df2)
# print("*"*20)
# print(pd.merge(df1,df2,left_on="key",right_index=True))  #以df1key 内连接df2行索引
# print(pd.merge(df1,df2,left_on="key",right_index=True,how="outer"))  #以df1key 外连接df2行索引
# # 层次化索引
# lefth = DataFrame({"key1":["Ohio","Ohio","Ohio","Nevada","Nevada"],
#                    "key2":[2000,2001,2002,2001,2002],
#                    "data":np.arange((5.))
#                    })
# righth = DataFrame(np.arange(12).reshape((6,2)),
#                    index=[["Nevada","Nevada","Ohio","Ohio","Ohio","Ohio"],
#                           [2001,2000,2000,2000,2001,2002]],
#                    columns=["event1","event2"])
# print("*"*20)
# print(lefth)
# print("*"*20)
# print(righth)
# print("*"*20)
# print(pd.merge(lefth,righth,left_on=["key1","key2"],right_index=True))  #以lefth["key1"],lefth["key2"] 内连接righth的2层结构行索引.
# print("*"*20)
# # join()合并
# print(lefth.join(righth,on=["key1","key2"],how="inner"))
# # (6)轴向连接
# # concatenate()
# arr = np.arange(12).reshape((3,4))
# print(arr)
# print(np.concatenate([arr,arr],axis=1))  #join型
# # concat() (参考P209 参数一览)
# s1 = Series([0,1],index=["a","b"])
# s2 = Series([2,3,4],index=["c","d","e"])
# s3 = Series([5,6],index=["f","g"])
# s4 = pd.concat([s1*5,s3])
# print(pd.concat([s1,s2,s3]))
# print("*"*20)
# print(pd.concat([s1,s2,s3],axis=1,join="inner"))
# print("*"*20)
# #指定行索引
# print(pd.concat([s1,s4],axis=1,join_axes=[["a","c","b","e"]]))
# #层次化索引，以区分
# print(pd.concat([s1,s1,s3],keys=["one","two","three"]))
# print("*"*20)
# print(pd.concat([s1,s1,s3],keys=["one","two","three"]).unstack())
# print("*"*20)
# # keys作为列索引
# print(pd.concat([s1,s2,s3],axis=1,keys=["one","two","three"]))
#
# # (7)合并重复数据
# #where
# a = Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],
#            index=["f","e","d","c","b","a"]
#            )
# b = Series(np.arange(len(a),dtype=np.float64),
#            index=["f","e","d","c","b","a"]
#            )
# b[-1] = np.nan
# print(a)
# print(b)
# print("*"*20)
# print(Series(np.where(pd.isnull(a),b,a),index=["f","e","d","c","b","a"]))  #三目运算
# print("*"*20)
# # combine_first
# print(b[:-2])
# print(a[2:])
# print(b[:-2].combine_first(a[2:]))  #类似where(),并自动排序
# # DataFrame
# df1 = DataFrame({"a":[1,np.nan,5.,np.nan],
#                  "b":[np.nan,2.,np.nan,6.],
#                  "c":range(2,18,4)})
# df2 = DataFrame({"a":[5.,4.,np.nan,3.,7.],
#                  "b":[np.nan,3.,4.,6.,8.]})
# print("*"*20)
# print(df1)
# print("*"*20)
# print(df2)
# print("*"*20)
# print(df1.combine_first(df2))

# 7.2重塑层次化索引
#
# 1 旋转操作stack()/unstack()  stack默认会滤除缺失数据，因此可逆.
# stack() 列索引旋转为行索引
# unstack() 行索引旋转为列索引
# pivot() 行列转换


# # 7.3数据转换(过滤，清理，转换)
# #
# # 1移除重复数据
# data = DataFrame({"k1":["one"]*3+["two"]*4,"k2":[1,1,2,3,3,4,4]})
# print("*"*20)
# print(data)
# print("*"*20)
# print(data.duplicated())  #判断是否为重复行
# print("*"*20)
# print(data.drop_duplicates())
# print("*"*20)
# data["point"] = range(7)
# print(data.drop_duplicates(["k1"]))  #删除k1列重复的行。保留最初的行.
# print("*"*20)
# print(data.drop_duplicates(["k1","k2"],keep="last"))  #删除k1,k2重复的前面的行，保留位置最后的行.
#
# # 2 数据转换
# data =DataFrame({"food":["bacon","pulled pork","bacon","Pastrami","corned beef","Bacon",
#                          "pastrami","honey ham","nova lox"],
#                  "ounces":[4,3,12,6,7.5,8,3,5,6]})
# print(data)
# # (1)添加一列食物来源列
# meat_from_whoanimal = {
#     "bacon":"pig",
#     "pulled pork":"pig",
#     "pastrami":"cow",
#     "corned beef":"cow",
#     "honey ham":"pig",
#     "nova lox":"salmon"
# }
# # data["animal"] = data["food"].map(str.lower).map(meat_from_whoanimal)
# # data["animal"] = data["food"].map(lambda x:meat_from_whoanimal[x.lower()])
# data["animal"] = [meat_from_whoanimal[x.lower()] for x in data["food"]]
# print("*"*20)
# print(data)
# # (2)替换
# data = Series([1.,-999.,2.,-999.,-1000.,3.])
# print(data)
# print("*"*20)
# print(data.replace(-999,np.nan))  #fillna()属于replace的特例.
# print("*"*20)
# print(data.replace([-999,-1000],np.nan))
# print("*"*20)
# print(data.replace([-999,-1000],[np.nan,0]))
# print("*"*20)
# print(data.replace({-999:np.nan,-1000:0}))
#
# #(3)重命名轴索引
# data = DataFrame(np.arange(12).reshape((3,4)),
#                  index=["Ohio","Colorado","New York"],
#                  columns=["one","two","three","four"])
# data.index = [x.upper() for x in data.index]
# print(data)
# # rename(index=,columns=)
# data1 = data.rename(index=str.title,columns=str.upper)
# print("*"*20)
# print(data1)
# data2 = data.rename(index={"OHIO":"INDIANA"},
#             columns={"three":"peekaboo"})
# print("*"*20)
# print(data2)
# data.rename(index={"OHIO":"INDIANA"},
#             columns={"three":"peekaboo"},inplace=True)  #不新生成data对象，而是就地对原对象作修改.
# print("*"*20)
# print(data)
#
# # (4)划分(面元划分)
# ages = [20,22,25,27,21,23,37,31,61,45,41,32]
# bins = [18,25,35,60,100]
# cats = pd.cut(ages,bins)
# # print(cats)
# # print(cats.codes)
# # # print(cats.levels)
# # print(pd.value_counts(cats))
# print([cat for cat in ages if 18<cat<26])
# # (5) 数据显示
# np.random.seed(12345)
# data = DataFrame(np.random.randn(1000,4))  #randn(行数,列数)
# print("*"*20)
# print(data.describe())
# print("*"*20)
# print(data[3][np.abs(data[3])>3])
# print("*"*20)
# print(data[(np.abs(data)>3).any(1)])  #选出存在绝对值超过3的所有行
# print("*"*20)
# data[(np.abs(data)>3)] = np.sign(data) * 3  #将超过3的部分范围控制在[-3,3],np.sign()返回[-1,1]之间的数组
# print(data.describe())

# # 7.4 排列及随机采样
# #
# # 1permutation() 随机重排序
# df = DataFrame(np.arange(5*4).reshape(5,4))
# sampler = np.random.permutation(5)  #生成5个整数的随机序列
# print(df)
# print("*"*20)
# # print(df.take(sampler))  #按sampler对df重排序--方法1
# print(df.ix[sampler,[0,1,2,3]])  #按sampler对df重排序--方法2
# # 2randint()
# bag = np.array([5,7,-1,6,4])
# sampler2 = np.random.randint(0,len(bag),size=10)
# print(sampler2)
# print(bag.take(sampler2))  #bag 按照sampler2的指定顺序排序，

# # 7.5指标矩阵(哑变量矩阵)
# df = DataFrame({"key":["b","b","a","c","a","b"],
#                 "data1":range(6)
#                 })
# print(df)
# print("*"*20)
# print(pd.get_dummies(df["key"],prefix="key"))  #df["key"]的非重复项作为指标，生成0,1(0,1根据原矩阵中关系判断所得)的指标矩阵
# # 结合cut()
# values = np.random.rand(10)
# print(values)
# bins = [0,0.2,0.4,0.6,0.8,1]
# print(pd.get_dummies(pd.cut(values,bins)))

# 7.6实例
# 基本查看
db = json.load(open("foods-2011-10-03.json"))
# db = json.load(open("pythonLevel3/pythonDataAnalysis/foods-2011-10-03.json"))
print(len(db))
print("*"*20)
print(db[:5])
print("*"*20)
print(db[0].keys())
print("*"*20)
print(db[0]["nutrients"][0])
print("*"*20)
nutrients = DataFrame(db[0]["nutrients"])
print(nutrients[:7])
print("*"*20)
info_keys = ["description","group","id","manufacturer"]
info = DataFrame(db,columns=info_keys)
print(info[:5])
print("*"*20)
print(pd.value_counts(info["group"])[:10])  #查看食物类别分布情况
print("*"*20)
# 分析营养成分
nutrients = []
for rec in db:
    fnuts = DataFrame(rec["nutrients"])
    fnuts["id"] = rec["id"]
    nutrients.append(fnuts)
nutrients = pd.concat(nutrients,ignore_index=True)  #将所有nutrients合并为一张大表格.
print(nutrients)
print("*"*20)
print(nutrients.duplicated().sum())  #判断重复项数
nutrients = nutrients.drop_duplicates()  #删除重复项
print(nutrients)
col_mapping = {"description":"food",
               "group":"fgroup"
               }
info = info.rename(columns=col_mapping,copy=False)  #重命名
col_mapping = {"description":"nutrient",
               "group":"nutgroup"
               }
nutrients = nutrients.rename(columns=col_mapping,copy=False)  #重命名
print("*"*20)
print(nutrients)
ndata = pd.merge(nutrients,info,on="id",how="outer")  #合并
print("*"*20)
print(ndata)
print("*"*20)
print(ndata.ix[30000])
# 发现锌含量排位图
result = ndata.groupby(["nutrient","fgroup"])["value"].quantile(0.5)  #quantile(0.5) 50%分位数(中分维数)
# result = ndata.groupby(["nutrient","fgroup"])["value"].quantile(0.25)  #相比quantile(0.5)x轴更短
# result = ndata.groupby(["nutrient","fgroup"])["value"].sum()  # 跟上面不同的在于x轴不一样。
# result = ndata.groupby(["nutrient","fgroup"])["value"].mean()  # 跟quatile(0.5)差不多
result["Zinc, Zn"].sort_values().plot(kind="barh")
# 发现营养最丰富食物
by_nutrient = ndata.groupby(["nutgroup","nutrient"])
print("*"*20,"by_nutrient")
print(by_nutrient)
get_maximum = lambda x: x.xs(x.value.idxmax())  #idxmax() 最大值的索引值.  获取value最大的索引
get_minimum = lambda x: x.xs(x.value.idxmin())
max_foods = by_nutrient.apply(get_maximum)[["value","food"]]  #返回value最大的列索引为["value","food"]的表
print(max_foods)
max_foods.food = max_foods.food.str[:50]  #截取最大食物串的前50.
print("*"*20)
print(max_foods.ix["Amino Acids"]["food"])