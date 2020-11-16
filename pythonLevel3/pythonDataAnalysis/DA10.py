# 时间序列

import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import json
import pylab
import os.path
from datetime import datetime
from pandas.tseries.offsets import Day, MonthEnd

# # 10.1 基础
# # 1 时间序列排序
# dates = [datetime(2011,1,2),datetime(2011,1,5),datetime(2011,1,7),
#          datetime(2011,1,8),datetime(2011,1,10),datetime(2011,1,12)]
# ts = Series(np.random.randn(6),index=dates)
# print(ts)
# print("*"*30)
# print(ts[::2])  #选取[0,2,4]序列的数据
# print("*"*30)
# print(ts + ts[::2])
# # 2 索引，切片，子集
# print("*"*30)
# print(ts["1/10/2011"])  # 索引
# longer_ts = Series(np.random.randn(1000),index=pd.date_range("1/1/2000",periods=1000))  #时间序列的Series创建.
# print("*"*30)
# print(longer_ts[datetime(2001, 1, 7):])  #切片
# print("*"*30)
# print(ts.truncate(after="1/9/2011"))  #切片
# # 3 聚合
# dates = pd.DatetimeIndex(["1/1/2000","1/2/2000","1/2/2000","1/2/2000","1/3/2000"])
# dup_ts = Series(np.arange(5),index=dates)
# print("*"*30)
# print(dup_ts.index.is_unique)
# grouped = dup_ts.groupby(level=0)
# print(grouped.mean())
# print(grouped.count())
# #
# # 4 日期范围，频率(参考P325 频率单位)，移动
# print("*"*30)
# print(pd.date_range("4/1/2012", "6/1/2012", freq="4h"))  #日期范围生成,freq=频率(时间间隔,4h=4个小时为间隔)
# # 移动
# ts = Series(np.random.randn(4),index=pd.date_range("1/1/2000",periods=4,freq="M"))
# print("*"*30)
# print(ts)
# print("*"*30)
# # 移动时间序列对应数据，时间序列不变
# print(ts.shift(2)) #前移2段时间
# print("*"*30)
# print(ts.shift(-2))  #后移2段时间
# print("*"*30)
# print(ts/ts.shift(1)-1)  #计算相邻时间的变化率.
# print("*"*30)
# # 移动时间序列,而非数据.
# print(ts.shift(2, freq="M"))
# # 偏移量移动时间
# now = datetime.now()
# print("*"*30)
# print(now + 3*Day())
# oneday = datetime(2011,11,30,0,0)
# print("*"*30)
# print(oneday+MonthEnd())  #滚动到月底
# print("*"*30)
# print(now + MonthEnd())
# print("*"*30)
# offset = MonthEnd()
# print(offset.rollforward(now))  #前滚到当月或下月月底.
# print(offset.rollback(now))  #回滚到上月月底
#
# # 5 时区
# stamp = pd.Timestamp("2011-03-12 04:00")
# stamp_utc = stamp.tz_localize("utc")
# print(stamp_utc.tz_convert("US/Eastern"))
# stamp_moscow = pd.Timestamp("2011-03-12 04:00", tz="Europe/Moscow")
#
# # 6 时期Period对象(参看P335 时期图)
# p = pd.Period("2007", freq="A-DEC")  #表示2007-01-01 到 2007-12-31整段时期.
# p.asfreq("M", how="start")  # 频率转化
#
# # 7 按季度计算的时期频率(参考P336 时期图)
# rng = pd.period_range("2011Q3","2012Q4",freq="Q-JAN")
# print("*"*30)
# print(Series(np.arange(len(rng)),index=rng))
# # Timestamp Period 互转
# ts = Series(np.random.randn(3),index=pd.date_range("1/1/2000", periods=3, freq="M"))
# print("*"*30)
# print(ts.to_period())  #转日期
# print("*"*30)
# print(ts.to_period().to_timestamp(how="end"))  #转timestamp
#
# # 8 重采样
# # print("*"*30)
# # print(ts.resample("D", how="sum"))  #重采样(参考P339 参数一览) 按天重新采样
# # 降采样(降低时间频率,聚合时间)
# ts = Series(np.arange(12),index=pd.date_range("1/1/2000",periods=12,freq="T"))
# print("*"*30)
# print(ts)
# print("*"*30)
# print(ts.resample("5min", closed="left", loffset="-1s").sum())  #数据聚合到5分钟间隔(closed="left" 左边界为闭合区间)计算总数. loffset="-1s"减1s的偏移量。
# # OHLC 重采样(按开盘，收盘，最高位，最低位统计数据)
# print("*"*30)
# print(ts.resample("5min").ohlc())
# # 利用groupby 重采样
# print("*"*30)
# print(ts.groupby(lambda x: x.month).mean())
# # 升采样
# frame = DataFrame(np.random.randn(2,4),
#                   index=pd.date_range("1/1/2000",periods=2,freq="W-WED"),
#                   columns=["Colorado","Texas","New York","Ohio"])
# df_daily = frame.resample("D").sum()  #升采样
# print("*"*30)
# print(df_daily)
# print("*"*30)
# print(frame.resample("D",fill_method="ffill",limit=2))  #升采样插值,limit=限制插值的次数


# 10.2 时间序列绘图
# close_px_all = pd.read_csv("stock_px.csv", parse_dates=True, index_col=0)
close_px_all = pd.read_csv("pythonLevel3/pythonDataAnalysis/stock_px.csv", parse_dates=True, index_col=0)  #parse_dates = True  ,变为datetimeindex 类型. index_col=
close_px = close_px_all[["AAPL", "MSFT", "XOM"]]
close_px = close_px.resample("B", fill_method="ffill")
# print(close_px)
# close_px["AAPL"].plot()  #苹果所有年数据
# close_px.ix["2009"].plot()  #2009年所有
# close_px["AAPL"].ix["01-2011":"03-2011"].plot()  #苹果2011-01到2011-03之间股价
# appl_q = close_px["AAPL"].resample("Q-DEC", fill_method="ffill")  # 苹果按季度
# appl_q.ix["2009":].plot()
# #  2 移动窗口函数(P线350 移动窗口函数一览)
# close_px.AAPL.plot()
# pd.rolling_mean(close_px.AAPL, 250).plot()  #苹果股价的250日均线
# pd.rolling_std(close_px.AAPL, 250,min_periods=10)  #250日每日回报标准差
#
# # 3 指数加权函数(时间越近权重越高,过去时间序列数据权重低)
# fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True, figsize=(12, 7))
# aapl_px = close_px.AAPL["2005":"2009"]
# ma60 = pd.rolling_mean(aapl_px, 60, min_periods=50)
# ewma60 = pd.ewma(aapl_px, span=60)  #指数加权函数
#
# aapl_px.plot(style="k-", ax=axes[0])
# ma60.plot(style="k--", ax=axes[0])
# aapl_px.plot(style="k-", ax=axes[1])
# ewma60.plot(style="k--", ax=axes[1])
# axes[0].set_title("Simple MA")
# axes[1].set_title("Exponentially weighted MA")
#
# 4 二元移动窗口函数
spx_px = close_px_all["SPX"]
spx_rets = spx_px/spx_px.shift(1) - 1
returns = close_px.pct_change()
corr = pd.rolling_corr(returns.AAPL, spx_rets, 125, min_periods=100)  #二元移动窗口函数, AAPL 6个月回报与标准普尔500(SPX)的相关系数
corr.plot()
corr = pd.rolling_corr(returns, spx_rets, 125, min_periods=100)
corr.plot()
#
# 5 自定义移动窗口函数
# rolling_apply()