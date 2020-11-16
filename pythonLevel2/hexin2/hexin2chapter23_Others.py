# 杂项
#
# # 23.1 xml
# # 1sax解析
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# import xml.sax
#
#
# class MovieHandler(xml.sax.ContentHandler):
#     def __init__(self):
#         self.CurrentData = ""
#         self.type = ""
#         self.format = ""
#         self.year = ""
#         self.rating = ""
#         self.stars = ""
#         self.description = ""
#
#     # 元素开始事件处理
#     def startElement(self, tag, attributes):
#         self.CurrentData = tag
#         if tag == "movie":
#             print("*****Movie*****")
#             title = attributes["title"]
#             print("Title:", title)
#
#     # 元素结束事件处理
#     def endElement(self, tag):
#         if self.CurrentData == "type":
#             print("Type:", self.type)
#         elif self.CurrentData == "format":
#             print("Format:", self.format)
#         elif self.CurrentData == "year":
#             print("Year:", self.year)
#         elif self.CurrentData == "rating":
#             print("Rating:", self.rating)
#         elif self.CurrentData == "stars":
#             print("Stars:", self.stars)
#         elif self.CurrentData == "description":
#             print("Description:", self.description)
#         self.CurrentData = ""
#
#     # 内容事件处理
#     def characters(self, content):
#         if self.CurrentData == "type":
#             self.type = content
#         elif self.CurrentData == "format":
#             self.format = content
#         elif self.CurrentData == "year":
#             self.year = content
#         elif self.CurrentData == "rating":
#             self.rating = content
#         elif self.CurrentData == "stars":
#             self.stars = content
#         elif self.CurrentData == "description":
#             self.description = content
#
#
# if __name__ == "__main__":
#     # 创建一个 XMLReader
#     parser = xml.sax.make_parser()
#     # turn off namepsaces
#     parser.setFeature(xml.sax.handler.feature_namespaces, 0)
#
#     # 重写 ContextHandler
#     Handler = MovieHandler()
#     parser.setContentHandler(Handler)
#
#     parser.parse("movies.xml")
#
# # 2xml.dom解析(有点类似java反射)
# from xml.dom.minidom import parse
# import xml.dom.minidom
#
# # 使用minidom解析器打开 XML 文档
# DOMTree = xml.dom.minidom.parse("movies.xml")
# collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print("Root element : %s" % collection.getAttribute("shelf"))
#
# # 在集合中获取所有电影
# movies = collection.getElementsByTagName("movie")
#
# # 打印每部电影的详细信息
# for movie in movies:
#    print("*****Movie*****")
#    if movie.hasAttribute("title"):
#       print("Title: %s" % movie.getAttribute("title"))
#
#    type = movie.getElementsByTagName('type')[0]
#    print("Type: %s" % type.childNodes[0].data)
#    format = movie.getElementsByTagName('format')[0]
#    print("Format: %s" % format.childNodes[0].data)
#    rating = movie.getElementsByTagName('rating')[0]
#    print("Rating: %s" % rating.childNodes[0].data)
#    description = movie.getElementsByTagName('description')[0]
#    print("Description: %s" % description.childNodes[0].data)
#


# # 23.2 json
# # 1 encode 对数据进行编码。
# import json
#
# # Python 字典类型转换为 JSON 对象
# data = {
#     'no': 1,
#     'name': 'Runoob',
#     'url': 'http://www.runoob.com'
# }
#
# json_str = json.dumps(data)
# print ("Python 原始数据：", repr(data))  #   函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式
# print ("JSON 对象：", json_str)
#
# # 2 decode
# import json
#
# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
#
# text = json.loads(jsonData)
# print(text["a"])
#
# # 3 json文件的读取写入
# # 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(json_str, f)
#
# # 读取数据
# with open('data.json', 'r') as f:
#     data = json.load(f)
#     print(data)
#


# # 23.3 time
# # 1 时间戳
# #!/usr/bin/python3
#
# import time  # 引入time模块
#
# ticks = time.time()
# print ("当前时间戳为:", ticks)
# # 2 时间元祖
# # 0	tm_year	2008
# # 1	tm_mon	1 到 12
# # 2	tm_mday	1 到 31
# # 3	tm_hour	0 到 23
# # 4	tm_min	0 到 59
# # 5	tm_sec	0 到 61 (60或61 是闰秒)
# # 6	tm_wday	0到6 (0是周一)
# # 7	tm_yday	一年中的第几天，1 到 366
# # 8	tm_isdst	是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1
# #!/usr/bin/python3
#
# import time
#
# localtime = time.localtime(time.time())
# print ("本地时间为 :", localtime)
# # 3 格式化时间
# #!/usr/bin/python3
#
# import time
#
# localtime = time.asctime( time.localtime(time.time()) )
# print ("本地时间为 :", localtime)
# # # 4 time 模块的 strftime 方法来格式化日期
# # !/usr/bin/python3
#
# import time
#
# # 格式化成2016-03-20 11:45:39形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
#
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
# # 5 日历
# #!/usr/bin/python3
#
# import calendar
#
# cal = calendar.month(2016, 1)
# print ("以下输出2016年1月份的日历:")
# print (cal)
# # 6 time模块
# 1	time.altzone 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。以下实例展示了 altzone()函数的使用方法：
# import time
# print ("time.altzone %d " % time.altzone)
# # time.altzone -28800
# 2	time.asctime([tupletime]) 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。以下实例展示了 asctime()函数的使用方法：
# import time
# t = time.localtime()
# print ("time.asctime(t): %s " % time.asctime(t))
# # time.asctime(t): Thu Apr  7 10:36:20 2016
# 3	time.clock() 用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。	实例
# 4	time.ctime([secs]) 作用相当于asctime(localtime(secs))，未给参数相当于asctime() 以下实例展示了 ctime()函数的使用方法：
# import time
# print ("time.ctime() : %s" % time.ctime())
# # time.ctime() : Thu Apr  7 10:51:58 2016
# 5	time.gmtime([secs])接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0以下实例展示了 gmtime()函数的使用方法：
# import time
# print ("gmtime :", time.gmtime(1455508609.34375))
# # gmtime : time.struct_time(tm_year=2016, tm_mon=2, tm_mday=15, tm_hour=3, tm_min=56, tm_sec=49, tm_wday=0, tm_yday=46, tm_isdst=0)
# 6	time.localtime([secs]接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。以下实例展示了 localtime()函数的使用方法：
# import time
# print ("localtime(): ", time.localtime(1455508609.34375))
# # localtime():  time.struct_time(tm_year=2016, tm_mon=2, tm_mday=15, tm_hour=11, tm_min=56, tm_sec=49, tm_wday=0, tm_yday=46, tm_isdst=0)
# 7	time.mktime(tupletime)接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。	实例
# 8	time.sleep(secs)推迟调用线程的运行，secs指秒数。以下实例展示了 sleep()函数的使用方法：
# #!/usr/bin/python3
# import time
#
# print ("Start : %s" % time.ctime())
# time.sleep( 5 )
# print ("End : %s" % time.ctime())
# 9	time.strftime(fmt[,tupletime])接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。以下实例展示了 strftime()函数的使用方法：
# import time
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# # 2016-04-07 11:18:05
# 10	time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')根据fmt的格式把一个时间字符串解析为时间元组。以下实例展示了 strftime()函数的使用方法：
# import time
# struct_time = time.strptime("30 Nov 00", "%d %b %y")
# print ("返回元组: ", struct_time)
# # 返回元组:  time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
# 11	time.time( )返回当前时间的时间戳（1970纪元后经过的浮点秒数）。以下实例展示了 time()函数的使用方法：
# import time
# print(time.time())
# # 1459999336.1963577
# 12	time.tzset()
# 根据环境变量TZ重新初始化时间相关设置。
# time属性
# 1   time.timezone
# 属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。
# 2	time.tzname
# 属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。
# import time
# print(time.tzname)
#
# # 7 calendar模块
# 1	calendar.calendar(year,w=2,l=1,c=6)返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
# 2	calendar.firstweekday( )返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
# 3	calendar.isleap(year)是闰年返回True，否则为false。
# 4	calendar.leapdays(y1,y2)返回在Y1，Y2两年之间的闰年总数。
# 5	calendar.month(year,month,w=2,l=1)返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
# 6	calendar.monthcalendar(year,month)返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
# 7	calendar.monthrange(year,month)返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
# 8	calendar.prcal(year,w=2,l=1,c=6)相当于 print calendar.calendar(year,w,l,c).
# 9	calendar.prmonth(year,month,w=2,l=1)相当于 print calendar.calendar（year，w，l，c）。
# 10	calendar.setfirstweekday(weekday)设置每周的起始日期码。0（星期一）到6（星期日）。
# 11	calendar.timegm(tupletime)和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
# 12	calendar.weekday(year,month,day)返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）
# 8 datetime模块
#


# # 23.4 web扩展
# from urllib import request
# u = request.urlopen('http://quote.yahoo.com/d/quotes.csv?s=YHOO&f=sl1d1t1c1ohgv')
# for row in u:
#     print(row)
# import csv
# for row in csv.reader(u):  #设想u返回的是个csv
#     print(row)
#


# # 23.5 com接口(暂时弃用)
# #!/usr/bin/env python
#
# from tkinter import Tk
# from time import sleep
# import tkinter.messagebox
# import win32com.client as win32
#
# warn = lambda app: tkinter.messagebox.showwarning(app, 'Exit?')
# RANGE = range(3, 8)
#
# def excel():
#     app = 'Excel'
#     xl = win32.gencache.EnsureDispatch('%s.Application' % app)
#     ss = xl.Workbooks.Add()
#     sh = ss.ActiveSheet
#     xl.Visible = True
#     sleep(1)
#
# sh.Cells(1,1).Value = 'Python-to-%s Demo' % app
# sleep(1)
# for i in RANGE:
#     sh.Cells(i,1).Value = 'Line %d' % i
#     sleep(1)
#     sh.Cells(i+2,1).Value = "Th-th-th-that's all folks!"
#
#     warn(app)
#     ss.Close(False)
#     xl.Application.Quit()
#
# if __name__=='__main__':
#     Tk().withdraw()
#     excel()
#
# 实例2 excel操作
# 参看db2connector.py
#


# 23.6 Jython
# Jython的作用在于将Python方便的整合进那些以JVM为基础的项目里。