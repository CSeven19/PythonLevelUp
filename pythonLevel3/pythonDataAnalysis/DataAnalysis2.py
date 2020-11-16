# 基础

from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import json
from matplotlib import pyplot as plt
import pylab
import os.path

# 2.1
# # 1获取records
# path = "usagov_bitly_data2012-03-16-1331923249.txt"
# # with open(path) as tf:
# #     firstline = tf.readline()
# # fldict = json.loads(firstline)
# # print(fldict)
# records = [json.loads(line) for line in open(path)]
# # print(records[0]['tz'])
#
# # 2时区计数
# # # 纯python标准库获取时区计数(省略)
# # time_zones = [rec['tz'] for rec in records if 'tz' in rec]
# # print(time_zones[:10])
# # 使用pandas进行时区技术统计
# frame = DataFrame(records)
# tz_counts = frame['tz'].value_counts()  #对出现次数进行分组统计
# # print(tz_counts[:10])
# # 为记录中未知和缺失时区填上替代值
# clean_tz = frame["tz"].fillna("Missing")  # 替换缺失值(NA)
# clean_tz[clean_tz == ""] = "Unknown"  #未知替换Unknown
# tz_counts = clean_tz.value_counts()
# # print(tz_counts[:10])
# # 要使用pylab打开显示图形
# tz_counts[:10].plot(kind="barh",rot=0)
# # plt.plot(tz_counts[:10])  #利用matplotlib绘制
# # plt.show()
#
# # 3对时区进行一些常规操作
# results = Series([x.split()[0] for x in frame.a.dropna()])  #pandas删除缺失数据(pd.dropna()方法)
# # print(results[:5])
# # print(results.value_counts()[:8])
# operating_system = np.where(frame["a"].str.contains("Windows"),"Windows","Not Windows")  #返回包含Windows，Not Windows的list
# # print(operating_system[:15])
# by_tz_os = frame.groupby(["tz",operating_system])  #按时区及Windows/Not Windows分组
# agg_counts = by_tz_os.size().unstack().fillna(0)  #对计数结果进行2次美化
# # print(agg_counts[:10])
# # 选取常出现时区
# # indexer1 = agg_counts.sum(0)  #DataFrame.sum(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
# # indexer2 = agg_counts.sum(1)  #axis : {index (0), columns (1)}
# # print(indexer1[:10])
# # print(indexer2[:10])
# indexer = agg_counts.sum(1).argsort()  #argsort()将原始组中的元素从小到大排列，提取并返回其对应的index(索引)
# # print(indexer[:10])
#
# # import numpy as np
# # x=np.array([1,4,3,-1,6,9])
# # print(x.argsort())
# # print(x.argmax())
# # print(x.argmin())  #返回最小值的所在index
#
# count_subset = agg_counts.take(indexer)[-10:]  #截取按indexer排序的后10个
# print(count_subset)
# print(agg_counts[-10:])
# count_subset.plot(kind='barh',stacked=True)
# normed_subset = count_subset.div(count_subset.sum(1),axis=0)
# normed_subset.plot(kind="barh",stacked=True)


# # 2.2 MovieLens 1M数据集
# # 1 读取dat文件
# unames = ["user_id","gender","age","occupation","zip"]
# users = pd.read_table("users.dat",sep="::",header=None,names=unames,engine='python')
# rnames = ["user_id","movie_id","rating","timestamp"]
# ratings = pd.read_table("ratings.dat",sep="::",header=None,names=rnames,engine='python')
# mnames = ["movie_id","title","genres"]
# movies = pd.read_table("movies.dat",sep="::",header=None,names=mnames,engine='python')
# # # 2切片
# # print(users[:5])
# # print(ratings[:5])
# # print(movies[:5])
# # # 3合并
# data = pd.merge(pd.merge(ratings,users),movies)
# print(data[:5])
# # # 4聚合
# # # mean_ratings = data.pivot_table("rating",rows="title",cols="gender",aggfunc="mean")
# mean_ratings = data.pivot_table("rating",index=["title"],columns=["gender"],aggfunc="mean")  #rating=要聚合的列，但不显示，index=行，columns=列，aggfunc=处理函数
# print(mean_ratings[:5])
# # 5过滤掉评分数小于250的
# # 获取size
# ratings_by_title = data.groupby("title").size()
# # print(ratings_by_title[:10])
# active_titles = ratings_by_title.index[ratings_by_title >= 250]
# # print(active_titles[:10])
# # 根据active_titles进行过滤
# mean_ratings = mean_ratings.ix[active_titles]
# # print(mean_ratings[:10])
# # 女性评分最高10部电影(按F的评分降序)
# # top_female_ratings = mean_ratings.sort_index(by="F",ascending=False) 过时
# top_female_ratings = mean_ratings.sort_values(by=["F"],ascending=False)  #ascending=False 降序
# # print(top_female_ratings[:10])
# # 6计算男女评分分歧
# mean_ratings["diff"] = mean_ratings["M"] - mean_ratings["F"]
# sorted_by_diff = mean_ratings.sort_values(by=["diff"],ascending=False)
# # print(sorted_by_diff[:10])
# # 反序
# # print(sorted_by_diff[::-1][:10])
# # 7计算标准差
# rating_std_by_title = data.groupby("title")["rating"].std()  #std=sqrt(mean(abs(x-x.mean())**2))
# rating_std_by_title = rating_std_by_title.ix[active_titles]
# # print(rating_std_by_title.order(ascending=False)[:10])  #order()已废除
# print(rating_std_by_title.sort_values(ascending=False)[:10])

# # 2.3 读取excel文件
# df = pd.read_excel("../in/sales-funnel.xlsx")
# df.head()
# # 为方便起见，我们将上表中“Status”列定义为category，并按我们想要的查看方式设置顺序。
# df["Status"] = df["Status"].astype("category")  #使用astype实现dataframe字段类型转换
# df["Status"].cat.set_categories(["won","pending","presented","declined"],inplace=True)
# # 处理数据
# pd.pivot_table(df,index=["Name"])

# # 2.4 1880-2010年间全美婴儿姓名
# # 1
# names1880 = pd.read_csv("name/yob1880.txt",names=["names","sex","births"])
# print(names1880[:100])
# print(names1880.groupby("sex").births.sum())
#
# # 2获得1880-2010全部超过5次出现的名字
# years = range(1880,2011)
# pieces = []
# columns = ["names","sex","births"]
# for year in years:
#     # path = "name/yob%d.txt" % year
#     path = "pythonLevel3/pythonDataAnalysis/name/yob%d.txt" % year
#     frame = pd.read_csv(path,names=columns)
#     frame["year"] = year
#     pieces.append(frame)
# names = pd.concat(pieces,ignore_index=True)
# # 显示按年、sex分组的序列
# total_births = names.pivot_table("births",index="year",columns="sex",aggfunc=sum)
# # print(total_births)
# # print(total_births.tail())  #显示最后5行
# total_births.plot(title="Total births by sex and year")
# #
# # 3 增加名字出现比率列(基本样本点出现次数/样本空间)
# def add_prop(group):
#     births = group.births.astype(float)
#     group["prop"] = births/births.sum()
#     return group
# names = names.groupby(["year","sex"]).apply(add_prop)
# # print(names[:100])
# # 统计检查(检查比率和是否为1)
# # print(np.allclose(names.groupby(["year","sex"]).prop.sum(),1))  # True
# # 3获取前sex/year组合的前1000
# def get_top1000(group):
#     return group.sort_values(by="births",ascending=False)[:1000]
# grouped = names.groupby(["year","sex"])
# top1000 = grouped.apply(get_top1000)
# # print(top1000)
# # 获得前1000方法2
# # pieces = []
# # for year,group in names.groupby(["year","sex"]):
# #     pieces.append(group.sort_values(by="births",ascending=False)[:1000])
# # toop1000 = pd.concat(pieces,ignore_index=True)
# #
# # 4分析命名趋势
# # 分男女
# boys = top1000[top1000.sex == "M"]
# girls = top1000[top1000.sex == "F"]
# total_births = top1000.pivot_table("births",index="year",columns="names",aggfunc=sum)
# # print(total_births)
# subset = total_births[["John","Harry","Mary","Andy"]]
# # 显示趋势图
# subset.plot(subplots=True,figsize=(12,10),grid=False,title="Number of Births per year")
# # 评估命名多样性的增长
# # 方法1:(显示最流行1000名字所占比例变化趋势)
# table = top1000.pivot_table("prop",index="year",columns="sex",aggfunc=sum)
# table.plot(title="Sum of table1000.prop by year and sex",yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10))
# # 方法2:统计占出生人数前50%不同名字数量
# # 计算2010前50%所处位置
# df = boys[boys.year == 2010]
# # print(df)
# # 计算prop累积和
# prop_cumsum = df.sort_values(by="prop",ascending=False).prop.cumsum()
# # print(prop_cumsum[:10])
# # 找出prop累积和为0.5的index
# # print(prop_cumsum.searchsorted(0.5)+1)
# # 计算1900前50%所处位置
# df = boys[boys.year ==1900]
# in1900 = df.sort_values(by="prop",ascending=False).prop.cumsum()
# # print(in1900.searchsorted(0.5)+1)
# def get_quantile_count(group,q=0.5):
#     group = group.sort_values(by="prop",ascending=False)
#     return int(group.prop.cumsum().searchsorted(q))+1
# diversity = top1000.groupby(["year","sex"]).apply(get_quantile_count)
# diversity = diversity.unstack("sex")
# # print(diversity)
# # diversity.head()  #显示前5条
# diversity.plot(title="Number of popular names in top 50%")
# # # stack()(会将列索引转换成行的子索引)/unstack()
# # import numpy as np
# # import pandas as pd
# # from pandas import Series,DataFrame
# # data=DataFrame(np.arange(6).reshape((2,3)),index=pd.Index(['street1','street2']),columns=pd.Index(['one','two','three']))
# # print(data)
# # print('-----------------------------------------\n')
# # data2=data.stack()
# # data3=data2.unstack()
# # print(data2)
# # print('-----------------------------------------\n')
# # print(data3)
# #
# # 5"最后一个字母"的变革
# # 聚合全部出生数据的年度，性别，末尾字母
# get_last_letter = lambda x:x[-1]
# last_letters = names.names.map(get_last_letter)
# # print(last_letters)
# # # 列表解析表示
# # last_letters = [x[-1] for x in names.names]
# # print(last_letters)
# last_letters.name = 'last_letter'
# table = names.pivot_table("births",index=last_letters,columns=["sex","year"],aggfunc=sum)
# subtable = table.reindex(columns=[1910,1960,2010],level="year")
# # print(subtable.head())
# letter_prop = subtable/subtable.sum().astype(float)
# flg,axes = plt.subplots(2,1,figsize=(10,8))
# letter_prop["M"].plot(kind="bar",rot=0,ax=axes[0],title="Male")
# letter_prop["F"].plot(kind="bar",rot=0,ax=axes[1],title="Female",legend=False)
# letter_prop = table/table.sum().astype(float)
# dny_ts = letter_prop.ix[["d","n","y"],"M"].T
# # print(dny_ts.head())
# dny_ts.plot()
# #
# # 6变成女孩名字的男孩名字
# # 获取所有lesl开头的姓名列表
# all_names = top1000.names.unique()  #去重复
# mask = np.array(["lesl" in x.lower() for x in all_names])
# lesley_like = all_names[mask]
# # print(lesley_like)
# # print(type(top1000.names))
# filtered = top1000[top1000.names.isin(lesley_like)]
# # print(filtered.groupby("names").births.sum())
# table = filtered.pivot_table("births",index="year",columns="sex",aggfunc="sum")
# table = table.div(table.sum(1),axis=0)
# print(table.tail())
# table.plot(style={"M":"k-","F":"k--"})