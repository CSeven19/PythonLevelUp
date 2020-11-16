# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os
import codecs

# #1compile
# text = "JGood is a handsome boy, he is cool, clever, and so on…"
# regex = re.compile(r'\w*oo\w*') #regex = re.compile('\w*oo\w*')也是同样的输出结果
# print(regex.findall(text))#查找所有包含’oo’的单词

# #2match
# matchresult = re.match(r'\w*oo\w*',"JGood is a handsome boy, he is cool, clever, and so on…",re.I)
# if matchresult is not None: # show match if successful
#     matchresult.group()
#     print(matchresult.group())
#     for m in matchresult.group():
#         print(m)
# print(matchresult)

# #3search
# searchresult = re.search(r'\w*oo\w*',"JGood is a handsome boy, he is cool, clever, and so on…",re.I)
# if searchresult is not None: # show match if successful
#     searchresult.group()
#     print(searchresult.group())
#     for m in searchresult.group():
#         print(m)
# print(searchresult)

# #4findall
# findallresult = re.findall(r'\w*oo\w*',"JGood is a handsome boy, he is cool, clever, and so on…",re.I)
# if findallresult is not None: # show match if successful
#     # findallresult.group()
#     # print(findallresult.group())
#     for m in findallresult:
#         print(m)
# print(findallresult)

# #5finditer
# finditerresult = re.finditer(r'\w*oo\w*',"JGood is a handsome boy, he is cool, clever, and so on…",re.I)
# if finditerresult is not None: # show match if successful
#     for m in finditerresult:
#         print(m)
# print(finditerresult)

# #6split
# import re
# a='Beautiful, is; better*than\nugly'
# # 四个分隔符为：,  ;  *  \n
# x= re.split(',|; |\*|\n',a,2)
# print(x)

# #7sub
# x=re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',r'static PyObject*\npy_\1(void)\n{','def myfunc():')
# print(x)

# #8group
# a = "123abc456"
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))   #123abc456,返回整体
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))   #123
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))   #abc
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))   #456

# #9groups
# a = "123abc456"
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).groups())   #123abc456,返回整体

# #10groupdict()
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds").groupdict()
# print(m)

# #11match search 区别
# print(re.match('super','insuperable'))
# print(re.search('super','insuperable').group())

# #12 \B非单词边界 \b单词边界
# m = re.search(r'\bthe\b', 'bite the dog') # at a boundary
# if m is not None: print(m.group())

# #13处理文件的匹配相关
# # f = os.popen('flower.txt', 'r')
# f = codecs.open('flower.txt','r','utf-8')
# for eachLine in f:
#     # print(eachLine)
#     print(re.split(r'\s\s+|\t', eachLine.rstrip())) #eachLine.rstrip()字符串末尾的指定字符后生成的新字符串
# f.close()

# #14os.popen() 方法用于从一个命令打开一个管道。
# # 使用 mkdir 命令
# a = 'mkdir nwdir'
# b = os.popen(a,'r',1)
# print(b)
f = os.popen('who', 'r')
for eachLine in f:
    print(re.split(r'\s\s+|\t', eachLine.rstrip()))
f.close()
