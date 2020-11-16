#!/usr/bin/python
# -*- coding: UTF-8 -*-

# str = raw_input("请输入：");
# print "你输入的内容是: ", str
# str = input("请输入：");
# print "你输入的内容是: ", str


#exception

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print("Error: 没有找到文件或读取文件失败")