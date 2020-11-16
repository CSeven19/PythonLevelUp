# !/usr/bin/python
# -*- coding: UTF-8 -*-

#variable

#数字，字符串
# counter = 100  # 赋值整型变量
# miles = 1000.0  # 浮点型
# name = "John"  # 字符串
#
# print counter
# print miles
# print name

#list
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

# print list  # 输出完整列表
# print list[0]  # 输出列表的第一个元素
# print list[1:3]  # 输出第二个至第三个的元素
# print list[2:]  # 输出从第三个开始至列表末尾的所有元素
# print tinylist * 2  # 输出列表两次
# print list + tinylist  # 打印组合的列表

#元组 类似于list，不能2次赋值，相当于只读list
# tuple = ('runoob', 786, 2.23, 'john', 70.2)
# tinytuple = (123, 'john')
#
# print tuple  # 输出完整元组
# print tuple[0]  # 输出元组的第一个元素
# print tuple[1:3]  # 输出第二个至第三个的元素
# print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
# print tinytuple * 2  # 输出元组两次
# print tuple + tinytuple  # 打印组合的元组

#字典 类似java Hashmap
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值
print type(tinydict)
print isinstance(tinydict, int)
