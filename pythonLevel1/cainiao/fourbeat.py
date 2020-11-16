# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 例2：elif用法

# num = 5
# if num == 3:  # 判断num的值
#     print 'boss'
# elif num == 2:
#     print 'user'
# elif num == 1:
#     print 'worker'
# elif num < 0:  # 值小于零时输出
#     print 'error'
# else:
#     print 'roadman'  # 条件均不成立时输出

#简单语句组
# var = 100
#
# if (var == 100): print "变量 var 的值为100"
#
# print "Good bye!"

#循环
# i = 2
# while (i < 100):
#     j = 2
#     while (j <= (i / j)):
#         if not (i % j): break
#         j = j + 1
#     if (j > i / j): print i, " 是素数"
#     i = i + 1
#
# print "Good bye!"



num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)