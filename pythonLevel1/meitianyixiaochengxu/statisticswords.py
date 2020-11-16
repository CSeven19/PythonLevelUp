#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os,sys

info = os.getcwd() #获取当前文件名称
print(info)
fin = open(u'flower.txt')
info = fin.read()
alist = info.split(' ') # 将文章按照空格划分开

# fout = open(u'count.txt', 'w')
# fout.write('\n'.join(alist)) # 可以通过文本文件的行号同样看到效果
# ##fout.write('%s' % alist)
# fout.close()

allen = len(alist) # 总的单词数
nulen = alist.count('') # 空格的数量
print("words' number is",allen)
print("null number is",nulen)
print ("poor words number is", allen-nulen) # 实际的单词数目

fin.close()