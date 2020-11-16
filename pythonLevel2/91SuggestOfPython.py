# 1Pythonic
# 美胜丑，显胜隐，简胜杂，疏胜密
# 2函数原则
# 粒度均匀,健壮，可扩展
# 3常量
# 控制于一个文件中
# 4assert
# 断言用于捕获用户自定义的约束，而非捕获程序本身异常或是错误。python中对性能有影响。

# # 5非中间变量式交换
# x,y = 0,1
# # 老式交换
# temp = x
# x = y
# y = temp
# # 新式交换
# x,y = y,x

# # 6Lazy evaluation
# # 实例1:
# x,y = 1,2
# if x or y:  #因为如x为真，python就不会去判断y,故而会提高其效率。尽量提升效率，避免无必要运算
#     print("ok")
# # 实例2:
# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b
# from itertools import islice
# print(list(islice(fib(),7)))  #返回7项的迭代器.巧妙应用无穷循环，自由控制生成项。

# # 7 枚举(python自身不带枚举类型，只能自己制造)
# # 类属性制造
# class Seasons:
#     Spring = 0
#     Summer = 1
#     Autumn = 2
#     Winter = 3
#
#     def __init__(self):
#         self.__members__ = [self.Spring,self.Summer,self.Autumn,self.Winter]
# season1 = Seasons()
# for member in season1.__members__:
#     print(member)

# # 8 避免使用type类型判断(可能判断出错)
# # 使用类型转化(list(listing),str(name))
# # 或用isinstance(obj,classinfo)
# print(isinstance(2,float))

# # 9 除法前先转float型(该版本已经无用)
# gpa1 = ((4*96+3*85+5*98+2*70)*4)/((4+3+5+2)*100)
# print(gpa1)
# gpa2 = float(((4*96+3*85+5*98+2*70)*4))/float(((4+3+5+2)*100))
# print(gpa2)
# # 10 enumerate(sequence,start=0)
# li = ["a","b","c","d","e"]
# for i,e in enumerate(li):
#     print("index: ",i,"element: ",e)
# e = enumerate(li)
# print(e.__next__())
# print(e.__next__())
# # 11 ==区别is
# a1 = "I am using long string for test"
# b1 = "I am using long string for test"
# print(id(a1), id(b1))
# print(a1 is b1)  #比较id
# print(a1 == b1)  #比较value
# aa1 = ["1", '2']
# bb1 = ["1", '2']
# print(aa1 is bb1)
# print(aa1 == bb1)

# # 12 考虑兼容性使用Unicode
# unicodeString = u"i am a big ..."

# 13 节制使用from...import...  替换成import a.B亦可。

# 14 ++i != i+=1 勿用

# 15 with使用，自动关闭资源

# # 16 None
# # 为空 != None
# # 为空的情况:
# # 常量None
# # 常量False
# # 任意形式的数值类型零:0,0L,0.0,0j
# # 空序列:"",(),[]
# # 空字典:{}
# # nonzero(),len()等返回0或False时.
# print(None == False)
# # 错误(仅a==常量None时方通过)
# if a is not None:
#     ...
# # 正确(判断其为空)
# if a:
#     ...

# # 16 连接字符串优先使用join而不是+
# str1,str2,str3 = "testing","string","concatenation"
# str1+str2+str3
# "".join(str1,str2,str3)  #效率更高(连接量大时注意)

# # 17 格式化中，尽量使用format()而不是% (标准趋势)
# # 转化标记(参考:建议28)
# str = "The number {0:,} in hex is : {0:#x},the number {1} in oct is {1:#o}".format(4746,45)
# print(str)

# # 18 区别不可变，可变对象.
# # 字符串为不可变对象.
# teststr = "you are g"
# # teststr[2] = "h"
# # print(teststr)
# # 可借助array来修改
# import array
# a = array.array("u", teststr)
# a[8] = "h"
# newstr = ""
# for i,e in enumerate(a):
#     newstr = newstr + e
# print(newstr)

# 19 列表解析
# # a语法:
# [expr for iter_item in iterable if coud_expr] 条件表达式非必须，迭代执行并最终返回list
# 语法等价于:
# NewList = []
# for iter_item in iterable:
#     if cond_expr:
#         NewList.append(expr)
# # b支持多重嵌套:
# nested_list = [[s.upper() for s in xs] for xs in nested_list]
# # c支持多重迭代
# [(a,b) for a in ["1","2","3","a"] for b in ["3","4","5","b"] if a!=b]
# # d expr可以是简单，复杂表达式，甚至是函数:
# def func(ccc):
#     print(ccc)
# [func(v) for v in [1,2,3,-1] if v>0]
# # e iterable可以是任意迭代对象，包括文件句柄.
# import codecs
# with codecs.open("test.txt", "r" ,"utf-8") as fh:
#     result = [i for i in fh if "abc" in i]
#     print(result)

# # 20 函数传参既不是传参也不是传引用
# # 区别c，python中赋值语句:b=a 实际是a,b共用同一引用。但是a=5,b=a,b=7之后b就重新分配了空间了.
# def change_me(org_list):
#     print("org_list:",id(org_list))
#     new_list = org_list
#     print("new_list:",id(new_list))
#     if len(new_list)>5:
#         new_list = ["a","b","c"]  #类似：a=5,b=a,b=7 id(b)已生改变.
#     for i,e in enumerate(new_list):
#         if isinstance(e,list):
#             new_list[i] = "****"
#     print("newlist:",new_list)
#     print("new_list:",id(new_list))
#     print("org_list:",id(org_list))
# test1 = [1,["a",1,3],[2,3],6]
# change_me(test1)
# print(test1)
# test2 = [1,["a",1,3],[2,3],6,2,4]
# change_me(test2)
# print(test2)

# # 21 可变长传参
# # 非字典型
# def SumFun(*args):
#     result = 0
#     for x in args[0:]:
#         result += x
#     return result
# print(SumFun(2,4))
# print(SumFun(2,4,45,32))
# print(SumFun())
# # 字典型
# def category_table(**kwargs):
#     for name,value in kwargs.items():
#         print("{0} is a kind of {1}".format(name,value))
# category_table(apple="fruit",carro="vegatable",python="python")
# category_table(BMW="car")

# 22 staticmethod/classmethod使用场合
# 相同点：访问方式相同(都可使用：class.method/object.method来访问)
# 不同点：静态方法类似类外部的函数，类方法则会匹配各自的类,所以apple.classmethod不用于banana.classmethod.

# # 23 字符串
# # a 长句子排序
# s = "select * " \
#     "from atable " \
#     "where afield = 'value'"
# print(s)
# # b 字符串处理方法
# # 判定(is类)/查找替换/分切连接/变形/填空/删除
# # 判定(isalnum()/isalpha()/islower()/startswith()/...)
# # 查找替换(count()/find(sub[,start[,end]])/index()/sub()/rfind()/.../replace(old,new[,count]))
# str = "Test if a string contains some spe.."
# print(str.count("a"))
# print(str.endswith(".."))
# if str.find("some",0,-1) != -1:
#     print("some have")
# # 方法2
# if "some" in str:
#     print("some have")
# # 分切连接(split([sep[,maxsplit]])/partition(sep)/splitlines([keepends])/.../)
# # 变形(lower()/upper()/capitalize()/swapcase()/title())
# strt = str.title()
# print(strt)
# print(str.center(40, '*'))
# # 删除(strip([chars])/lstrip()/rstrip())
# # 填充(fillchar()/zfill()/...)

# # 23 sorted/sort
# # a 区别
# # sorted(iterable,key,reverse)  #任意迭代对象
# # s.sort(key,reversed)  #list对象
# a = (1,2,3,7,5)
# a1 = sorted(a)
# print(a1)
# # a.sort()  #报错
# b = [1,2,2,4,5,3]
# b.sort()
# print(b)
# # b 字典排序
# phonebook = {"Linda":750,"Bob":9345,"Carol":5834}
# from operator import itemgetter
# # 按值排序
# sorted_pd = sorted(phonebook.items(),key=itemgetter(1))  #itemgetter(1)使phonebook.items()的各1位元素得到排序.
# print(sorted_pd)
# # 按键排序
# sorted_pd2 = sorted(phonebook.items(),key=itemgetter(0))  #itemgetter(0)使phonebook.items()的各0位元素得到排序.
# print(sorted_pd2)
# # c 多维list排序
# from operator import itemgetter
# gameresult = [["Bob",95.00,"A"],["Alan",86.0,"C"],["Mandy",82.5,"A"],["Bob",86,"E"]]
# sorted_pd = sorted(gameresult,key=itemgetter(2,1))  #先按2排，如果2相等再按1排
# print(sorted_pd)
# # d 字典中混合list
# mydict = {
#     "li":["M",7],
#     "zhang":["E",2],
#     "wang":["P",3],
#     "du":["C",2],
#     "ma":["C",9],
#     "zhe":["H",7],
# }
# from operator import itemgetter
# # sorted_pd = sorted(mydict.items(),key=lambda k_v:itemgetter(1)(k_v[1]))  #按a:[m,n]中n排序,k_v为元组(k,v),k_v[1]代表value也就是[m,n]
# # sorted_pd = sorted(mydict.items(),key=lambda k_v:itemgetter(0)(k_v[1]))  #按a:[m,n]中m排序
# sorted_pd = sorted(mydict.items(),key=lambda k_v:itemgetter(0)(k_v[0]))  #按a:[m,n]中a排序
# print(sorted_pd)
# # e list中含字典
# gameresult = [{"name":"Bob","wins":10,"losses":3,"rating":75.00},
#                 {"name":"David","wins":3,"losses":5,"rating":57.00},
#                 {"name":"Carol","wins":4,"losses":5,"rating":57.00},
#                 {"name":"Patty","wins":9,"losses":3,"rating":71.48},
#               ]
# from operator import itemgetter
# sorted_pd = sorted(gameresult,key=itemgetter("rating","name"))  #先按rating排再按name排.
# print(sorted_pd)

# 24 浅拷贝深拷贝
# 浅拷贝(shallow copy):引用(工厂，切片，copy())
# 深拷贝(deep copy):复制(递归复制deepcopy())
# 实例1
# import copy
# import sys
# class A():
#     # time = 0
#     def __init__(self,time):
#         self.time = time
#     def changetime(self,time):
#         self.time = time
#     def gettime(self):
#         return self.time
# a = A(1)
# print("referenccounts:",sys.getrefcount(a))
# b = copy.copy(a)
# c = copy.deepcopy(a)
# print("a:",id(a))
# print("b:",id(b))
# print("c:",id(c))
# print("referenccounts:",sys.getrefcount(a))
# d = a
# print("d:",id(d))
# print("referenccounts:",sys.getrefcount(a))
# b.changetime(2)
# print("a time:",a.time)
# print("b time:",b.time)
# c.changetime(3)
# print("a time:",a.time)
# print("c time:",c.time)
# # 实例2(参考107图形)
# import copy
# class Pizza(object):
#     def __init__(self,name,size,price):
#         self.name = name
#         self.size=size
#         self.price=price
#     def getPizzaInfo(self):
#         return self.name,self.size,self.price
#     def showPizzaInfo(self):
#         print("Pizza name:"+self.name)
#         print("Pizza size:"+str(self.size))
#         print("Pizza price:"+str(self.price))
#     def changeSize(self,size):
#         self.size=size
#     def changePrice(self,price):
#         self.price=price
# class Order(object):
#     def __init__(self,name):
#         self.customername=name
#         self.pizzaList=[]
#         self.pizzaList.append(Pizza("Mushroom",12,30))
#     def ordermore(self,pizza):
#         self.pizzaList.append(pizza)
#     def changeName(self,name):
#         self.customername=name
#     def getorderdetail(self):
#         print("customer name:"+self.customername)
#         for i in self.pizzaList:
#             i.showPizzaInfo()
#     def getPizza(self,number):
#         return self.pizzaList[number]
# customer1=Order("zhang")
# customer1.ordermore(Pizza("seafood",9,40))
# customer1.ordermore(Pizza("fruit",12,35))
# print("customer1 order info:")
# customer1.getorderdetail()
# print("-"*30)
# customer2=copy.copy(customer1)
# print("order 2 customer name:",customer2.customername)
# customer2.changeName("li")
# customer2.getPizza(2).changeSize(9)
# customer2.getPizza(2).changePrice(30)
# print("customer2 order info:")
# customer2.getorderdetail()
# print("-"*30)
# print("customer1 order info:")  #浅拷贝不具备递归复制，所以只是customer1的名字没变，订单都跟customer2一致了。因为Pizza并没有被递归复制上。
# customer1.getorderdetail()
# # id一致，说明Pizza并没有递归被复制上.
# print("customer1 Pizza2 id",id(customer1.getPizza(2)))
# print("customer2 Pizza2 id",id(customer2.getPizza(2)))

# # 25 count
# from collections import Counter
# some_data = ["a","2",2,4,5,"2","b",4,7,"a",5,"d","a","z"]
# print(Counter(some_data))
# print(some_data.count("a"))

# # 26 ConfigParser
# # -* - coding: UTF-8 -* -
# import configparser
#
# conf = configparser.ConfigParser()
# conf.read("example.conf")
#
# # 获取指定的section， 指定的option的值
# name = conf.get("section1", "name")
# print(name)
# age = conf.get("section1", "age")
# print(age)
#
# #获取所有的section
# sections = conf.sections()
# print(sections)
#
# #写配置文件
# # 更新指定section, option的值
# conf.set("section2", "port", "8081")
# # 写入指定section, 增加新option的值
# conf.set("section2", "IEPort", "80")
# # 添加新的 section
# conf.add_section("new_section")
# conf.set("new_section", "new_option", "http://www.cnblogs.com/tankxiao")
# # 写回配置文件
# conf.write(open("example.conf","w"))

# 27 argparse 处理命令行参数
# # getopt(初期)
# import getopt
# import sys
# def cmdtest():
#     try:
#         # sys.argv获取命令行参数,sys.argv[1:]过滤掉python get.py 命令行输入python get.py -o t --help cmd file1 file2 获取['get.py', '-o', 't', '--help', 'cmd', 'file1', 'file2']
#         #短格式分析串"ho:" "h"是一个开关选项；"o:"则表示后面应该带一个参数
#         #长格式分析串列表：["help", "output="] "help"是一个开关选项；"output="则表示后面应该带一个参数。
#         #调用getopt函数。函数返回两个列表：opts和args。opts为分析出的格式信息。args为不属于格式信息的剩余的命令行参数。
#         # 命令行:-a -b -c foo -d bar a1 a2 经getopt转化 opts配置项:[("-a",""),("-b",""),("-c","foo"),("-d","bar")]+args参数列表:["a1","a2"]
#         opts,args = getopt.getopt(sys.argv[1:],"ho:v",["help","output="])
#     except getopt.GetoptError as err:
#         print(str(err))
#         sys.exit(2)
#     output = None
#     verbose = False
#     print(opts,args)
#     for o,a in opts:
#         if o == "-v":
#             verbose = True
#         elif o in ["-h","--help"]:
#             sys.exit()
#         elif o in ("-o","--output"):
#             output = a
#         else:
#             assert False,"unhandled option"
# if __name__ == "__main__":
#     cmdtest()
# # optparse(中期)
# # optparse.add_option区别getopt，
# # 1同时支持长短配置
# # 命令行:-f outfile --quiet之类都是可行的.
# # 2并有默认值.
# # 3帮助文档(默认支持-h/--help)
# # -h
# # -f  #write report to FILE
# from optparse import OptionParser
# import ast
# parser = OptionParser()
# parser.add_option("-f","--file",dest="filename",help="write report to FILE",metavar="FILE")
# parser.add_option("-q","--quiet",action="store_false",dest="verbose",default=True,help="don't print status messages to stdout")
# (options,args) = parser.parse_args()
# print(options)
# if options.filename == "test.txt":
#     req = input("are you really want to write to file?")
#     if req == "Y":
#         print("writing...")
#     else:
#         print("not write")
# # argparse(现在)
# # 类似optparse,提升optparse功能
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-o","--output")
# parser.add_argument("-v",dest="verbose",action="store_true")
# # 支持类型更多
# # parser.add_argument("bar",type="argparse.FileType('w')")
# # 可扩展函数为type
# parser.add_argument("door",type=int,choices=range(1,4))
# args = parser.parse_args()
# args = parser.parse_args(["out.txt"])
# # 适合复杂CLI,可提供分组如输入命令:python setup.py help,可支持子命令
# # docopt(最新)

# # 28 pandas(处理大型csv文件)
# # 1 render(csv读取)
# # 参考hexin2chapter23_others
# from urllib import request
# import csv
# u = request.urlopen('http://quote.yahoo.com/d/quotes.csv?s=YHOO&f=sl1d1t1c1ohgv')
# for row in csv.reader(u):  #设想u返回的是个csv
#     print(row)
# # 2 csv.writer(写入)
# import csv
# with open("XXX.csv","w",newline="") as datacsv:
#     #dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
#     csvwriter = csv.writer(datacsv,dialect = ("excel"))
#     #csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
#     csvwriter.writerow(["A","B","C","D"])
# # 3 DictReader()/DictWriter映射到字典中去.
# # 4 pandas
# # 4.1两种基本数据结构:Series/DataFrame
# # Series
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# s = pd.Series([1,3,5,np.nan,6,8])
# print(s)
# # DataFrame
# import pandas as pd
# import numpy as np
# data = {
#     "OrderDate":["1-6-10","23","9","26","15"],
#     "Region":["East","Central","Central","West","East"],
#     "Rep":["Jones","Kivell","Jardine","Gill","Sorvino"]
# }
# dataframe = pd.DataFrame(data,columns=["OrderDate","Region","Rep"])
# print(dataframe)
# # 4.2read_csv()(读取csv并返回DataFrame)
# import pandas as pd
# import numpy as np
# import contextlib
# # with contextlib.closing(pd.read_csv("course.csv")) as rc:  #虽然可以读出来，但是会报错。似乎不能try,catch
# #     print(rc)
# df = pd.read_csv("course.csv",nrows=5,usecols=["OrderDate","Region","Rep"])
# print(df)
# # 4.3to_csv()(用DataFrame写入到csv)
# df.to_csv("course.csv")
# # 4.4 csv,excel兼容
# import pandas as pd
# import csv
# dia = csv.excel()
# dia.delimiter="|"  #分隔符设置为"|"
# pd1 = pd.read_csv("course.csv")
# print(pd1)
# pd2 = pd.read_csv("course.csv",dialect=dia,error_bad_lines=False)
# print("-"*30)
# print(pd2)
# # 4.5 分块并返回可迭代对象
# import pandas as pd
# import csv
# pd1 = pd.read_csv("course.csv",chunksize=10,iterator=True)
# print(type(pd1))
# if iter(pd1).__next__:
#     print(iter(pd1).__next__)
# # 4.6 合并相似文件
# import os
# import pandas as pd
# filelist = os.listdir("exmaple")
# os.chdir("exmaple")
# dfs = [pd.read_csv(f) for f in filelist]
# total_df = pd.concat(dfs)
# print(total_df)

# # 29 pickle/json序列反序列(参考128图) (效率:pickle略高json)
# # 1 json对datatime的可序列化扩展
# import datetime
# from time import mktime
# try:import simplejson as json
# except ImportError:import json
#
# class DateTimeEncoder(json.JSONEncoder):
#     def default(self,obj):
#         if isinstance(obj,datetime.datetime):
#             return obj.strftime("%Y-%m-%d %H:%M:%S")  # 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
#         elif isinstance(obj,datetime.date):
#             return obj.strftime("%Y-%m-%d")
#         return json.JSONEncoder.default(self,obj)
#
# d = datetime.datetime.now()
# print(json.dumps(d,cls=DateTimeEncoder))
# # 如不使用扩展类，会报错。因为json本身不能序列化datetime
# print(json.dumps(d))
# # 2 pickle(cPickle已在3.0后移除)
# import pickle
#
# #!/usr/bin/python
# # Filename: pickling.py
#
# import pickle as p
#
# shoplistfile = 'shoplist.data'  #因为存储的是对象，必须使用二进制形式写进文件
# shoplist = ['apple', 'mango', 'carrot']
#
# # Write to the file
# f = open(shoplistfile, 'wb') #二进制打开
# p.dump(shoplist, f)
# f.close()
#
# del shoplist # remove the shoplist
# # Read back from the storage
# f = open(shoplistfile, 'rb')
# storedlist = p.load(f)
# print(storedlist)

# # 30 Queue(线程安全的)
# # 包含三种队列:Queue先进先出/LifoQueue/PriorityQueue(maxsize)
# # 方法：
# # qsize():返回近似的队列大小
# # empty():队列为空返回True
# # full():队列满返回True
# # put(item[,block[,timeout]]):往队列中加item,block=true且timeout= not None当队列满时会一直等到队列为空插入
# # put_nowait(itme):等价于put
# # get():删除并返回该被删除元素
# # get_nowait():等价于get(False)
# # join():阻塞直到队列所有元素处理完毕.
# import os
# import queue
# import threading
# import urllib
# import urllib.request
# class DownloadThread(threading.Thread):
#     def __init__(self,queue):
#         threading.Thread.__init__(self)
#         self.queue=queue
#     def run(self):
#         while True:
#             url=self.queue.get()
#             print(self.name,"begin download",url,"...")
#             self.download_file(url)
#             self.queue.task_done()  #task_done()，每次从queue中get一个数据之后，当处理好相关问题，最后调用该方法，以提示q.join()是否停止阻塞，让线程向前执行或者退出；
#             print(self.name,"download completed!!")
#     def download_file(self,url):
#         urlhandler = urllib.request.urlopen(url)
#         fname = os.path.basename(url).join(".html")
#         with open(fname,"wb") as f:
#             while True:
#                 chunk = urlhandler.read(1024)
#                 if not chunk:break
#                 f.write(chunk)
#
# if __name__=="__main__":
#     urls = ["http://wiki.python.org/moin/WebProgramming",
#             "https://www.createspace.com/3611970",
#             "http://wiki.python.org/moin/Documentation"
#             ]
#     queue = queue.Queue()
#     # 执行5个线程.
#     for i in range(5):
#         t = DownloadThread(queue)
#         t.setDaemon(True)  #将父线程设置为守护线程.
#         t.start()
#     # 先启动线程，再往queue里放url(同先往queue里放url,再启动线程是无所谓的)
#     for url in urls:
#         queue.put(url)
#     queue.join()  #join ()方法：主线程A中，创建了子线程B，并且在主线程A中调用了B.join()，那么，主线程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行，那么在调用这个线程时可以使用被调用线程的join方法。

# # 31 单例模式
# # python中import模板是天然的单例模式。
# # World.py
# import Sun
# def run():
#     while True:
#         Sun.rise()
#         sun.set()
# # main.py
# import World
# World.run()  #就实现了单例

# # 32 mixin(混入)模式(对c++模板的反应)
# def simple_tea_people():
#     people = People()
#     people.__bases__ += (UseSimpleTeapot,)  #增加基类,python支持动态增加基类
#     return people
# def coffee_people():
#     people = People()
#     people.__bases__ += (UseCoffeepot,)
#     return people
# def tea_and_coffee_people():
#     people = People()
#     people.__bases__ += (UseSimpleTeapot,UseCoffeepot,)
#     return people
# def boss():
#     people = People()
#     people.__bases__ += (kungfuteapot,UseCoffeepot,)
#     return people
# # 利用反射简化动态插入基类代码
# import mixins
# def staff():
#     people = People()
#     bases = []
#     for i in config.checked():
#         bases.append(getattr(mixins,i))  #getattr(object, name, default=None)
#     people.__bases__ += tuple(bases)
#     return people

# # 33 __new__()才是真正创建实例，__init__()更多只是初始化.
# # 1 使用__new__情况1：当类继承不可变类型且默认__new__无法满足需求# # 2 工厂，单例模式，元类编程
# import string
# class UserSet(frozenset):
#     def __init__(self,arg=None):
#         # if isinstance(arg,str):
#         #     arg = arg.split()
#         print()
#
#     def __new__(cls, *args, **kwargs):
#         if args and isinstance(args[0],str):
#             args = (args[0].split(),)
#         return super(UserSet,cls).__new__(cls,*args,**kwargs)
#
# print(UserSet("I am testing"))
# print(frozenset("I am testing"))


# 34 多继承的MRO搜索顺序
# 新式类中采用C3 MRO(参考169图)

# 35 描述符
# python描述符是一个“绑定行为”的对象属性，在描述符协议中，它可以通过方法重写属性的访问。这些方法有 __get__(), __set__(), 和__delete__()。
# 如果这些方法中的任何一个被定义在一个对象中，这个对象就是一个描述符。

# # 36 __getattr__/__getattribute__
# class A(object):
#     def __init__(self,name):
#         self.name = name
# a = A("attribute")
# print(a.name)
# print(a.test)  #__getattribute__ 无论属性是否存在只要执行都会调用.
# __getattr__
# class A(object):
#     def __init__(self,name):
#         self.name = name
#     def __getattr__(self, name):
#         print("calling __getattr__:",name)
# a = A("attribute")
# print(a.name)
# print(a.test)  #__getattr__ 仅当属性不在基类及自己的__dict__,抛出AttributeError时;

# # 37 property(原理参考179图,类似java的bean类)
# # 是特殊的数据描述符.
# # 数据描述符:同时定义了__get__/__set__
# # 非数据描述符:仅定义了__get__
# class Some_Class(object):
#     _x=None
#     def __init__(self):
#         self._x = None
#     @property  #创建一个property实际就是让其属性的访问与特定函数关联起来。如下
#     def x(self):
#         print("calling get method to return value")
#         return self._x
#     @x.setter
#     def x(self,value):
#         print("calling set method to set value")
#         self._x = value
#     @x.deleter
#     def x(self):
#         print("calling delete method to delete value")
#         del self._x
# A = Some_Class()
# A.x = "ok"
# A.x
# del A.x

# # 38 python对象协议
# # 1转换协议:__str__()(类似java中toString()),__repr__(),__int__,__nonzero__()...
# # 2比较协议:__eq__(),__ne__(),__it__()...
# # 3数值协议:__add__(),__sub__()...
# # 4容器类协议:__getitem__(),__setitem__(),__delitem__(),__len__(),__iter__()...
# # 5可调对象协议:__call__()
# class Functor(object):
#     def __init__(self,context):
#         self._context = context
#     def __call__(self):
#         print("do someting in call {0}".format(self._context))
# lai_functor = Functor("lai")
# yong_functor = Functor("yong")
# lai_functor()
# yong_functor()
# print(dir(Functor))
# # 6可哈希协议:__hash__()
# # 7描述符和属性交互协议:__getattr__(),__setattr__(),__delattr__(),__enter__(),__exit__()
# class Closer:
#     """通过with语句和一个close方法来关闭一个对象"""
#     def __init__(self,obj):
#         self.obj = obj
#     def __enter__(self):
#         return self.obj  #绑定到对象
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         try:
#             self.obj.close()
#         except AttributeError:  #obj isn't closable
#             print("Not closable.")
#             return True
# from ftplib import FTP
# with Closer(FTP("ftp.somesite.com")) as conn:  #with就是用__enter__,__exit__实现的。
#     conn.__dict__
# conn.__dict__

# # 39 迭代器
# # 其协议本质是实现了：1返回自身2next()
# class Next(object):
#     def __init__(self, data=1):
#         self.data = data
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         print("__next__ called")
#         if self.data > 5:
#             raise StopIteration
#         else:
#             self.data += 1
#             return self.data
# for i in Next(3):
#     print(i)

# # 40 生成器(生成器不是迭代器，仅其结果是迭代器)
# def fib(n):
#     a,b = 1,1
#     while a<n:
#         yield a  #条件内存储a到迭代器的堆中
#         a,b = b,a + b
# for i,f in enumerate(fib(10)):
#     print(f)
# f = fib(10)
# print(type(f))
# print(dir(f))  #注意观察其中的__iter__(),next(),send(),throw(),close()为其生成器实现的内部封装方法.

# # 41 协程(协作式协议，非抢占(需要加锁，谦让),不能利用多核,适合结合异步I/O来编写I/O密集型应用)
# # 实例1:通过yield实现协程(区别传统的线程)
# import time
#
# def A():
#     while 1:
#         print('------A-----')
#         time.sleep(0.1)  #测试目的
#         yield()
#
# def B():
#     while 1:
#         print('-------B-----')
#         time.sleep(0.1)
#         next(a)
#
# a = A()
# B()
# # 实例2:greenlet实现协程
# from greenlet import greenlet
# import time
# count = 0
# def A():
#     while 1:
#         print('-------A-------')
#         time.sleep(0.1)
#         global count
#         count += 1
#         g2.switch()  #2跳转至g2
#         while count > 10:  #4超过10次执行后终止协程
#             g1.dead
#             g2.dead
# def B():
#     while 1:
#         print('-------B-------')
#         time.sleep(0.1)
#         time.sleep(0.1)
#         g1.switch()  #3又跳转至g1
#
# g1 = greenlet(A)  #创建协程g1
# g2 = greenlet(B)
#
# g1.switch()  #1开始执行，并跳转至协程g1
# # 实例3:gevent
# import gevent
#
# def A():
#     while 1:
#         print('-------A-------')
#         gevent.sleep(1) #用来模拟一个耗时操作，注意不是time模块中的sleep
#
# def B():
#     while 1:
#         print('-------B-------')
#         gevent.sleep(0.5)  #每当碰到耗时操作，会自动跳转至其他协程
#
# g1 = gevent.spawn(A) # 创建一个协程
# g2 = gevent.spawn(B)
# g1.join()  #等待协程执行结束
# g2.join()

# 42 GIL(参考206图)
# 采用multiprocessing/C来改善多核多线程的需求.

# 43 常用工具
# PyPI(类似pip的工具,http://pypi.douban.com可参看各种包)
# pip
# yolk
# paster(参考215步骤及foorbar例子,生成标准包)(pastescript自动生成setup.py等功能)
# setuptools

# cython
import math
def great_circle(lon1, lat1, lon2, lat2):
    radius = 3956  # miles
    x = math.pi / 180.0

    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    c = math.acos((math.cos(a) * math.cos(b)) +
                  (math.sin(a) * math.sin(b) * math.cos(theta)))
    return radius * c
import timeit
lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
num = 500000
# python执行时间
t = timeit.Timer("great_circle(%f,%f,%f,%f)" % (lon1, lat1, lon2, lat2),setup="from __main__ import great_circle")
print("Pure python function", t.timeit(num), "sec")
# cython执行时间
t1 = timeit.Timer("Simulate.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2),"import pythonLevel2.Simulate.py")
print("Cython function (using trig function from math.h)", t1.timeit(num), "sec")
