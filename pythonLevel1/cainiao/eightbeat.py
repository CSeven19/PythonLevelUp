# !/usr/bin/python
# -*- coding: UTF-8 -*-

#1 正则表达式
import re

# line = "Cats are smarter than dogs";
#
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if searchObj:
#     print "searchObj.group() : ", searchObj.group()
#     print "searchObj.group(1) : ", searchObj.group(1)
#     print "searchObj.group(2) : ", searchObj.group(2)
# else:
#     print "Nothing found!!"

#2 re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
# line = "Cats are smarter than dogs";
#
# matchObj = re.match(r'dogs', line, re.M | re.I)
# if matchObj:
#     print "match --> matchObj.group() : ", matchObj.group()
# else:
#     print "No match!!"
#
# matchObj = re.search(r'dogs', line, re.M | re.I)
# if matchObj:
#     print "search --> matchObj.group() : ", matchObj.group()
# else:
#     print "No match!!"

#3 Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
# phone = "2004-959-559 # 这是一个国外电话号码"
#
# # 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "", phone)
# print "电话号码是: ", num
#
# # 删除非数字(-)的字符串
# num = re.sub(r'\D', "", phone)
# print "电话号码是 : ", num


#4 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))