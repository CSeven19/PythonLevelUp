#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os,sys

fin = open(u'minganci.txt')
info = fin.read()
alist = info.split('\n')

str = input("请输入：")
if str in alist:
    print("freedom")
else:
    print("human")