# !/usr/bin/python
# -*- coding: UTF-8 -*-

#变量转换
# x="123"
# s=[1,2,3]
# y=1
# gushi="gushi"
# z='z'
# print int(x );         #将x转换为一个整数
# print long(x );        #将x转换为一个长整数
# print float(x );               #将x转换到一个浮点数
# # print complex(real [,imag ]);  #创建一个复数
# print str(x );                 #对象 x 转换为字符串
# print repr(x );                #将对象 x 转换为表达式字符串
# print eval(gushi );              #用来计算在字符串中的有效Python表达式,并返回一个对象
# print tuple(s );               #将序列 s 转换为一个元组
# print list(s );                #将序列 s 转换为一个列表
# print chr(y );                 #将一个整数转换为一个字符
# print unichr(y );              #将一个整数转换为Unicode字符
# print ord(z );                 #将一个字符转换为它的整数值
# print hex(y );                 #将一个整数转换为一个十六进制字符串
# print oct(y );                 #将一个整数转换为一个八进制字符串

#字符串操作
a = "Hello"
b = "Python"

print "a + b 输出结果：", a + b
print "a * 2 输出结果：", a * 2
print "a[1] 输出结果：", a[1]
print "a[1:4] 输出结果：", a[1:4]

if( "H" in a) :
    print "H 在变量 a 中"
else :
	print "H 不在变量 a 中"

if( "M" not in a) :
    print "M 不在变量 a 中"
else :
	print "M 在变量 a 中"

print r'\n'
print R'\n'
#格式化输出
print "My name is %s and weight is %d kg!" % ('Zara', 21)
#unicode定义
print u'Hello World !'