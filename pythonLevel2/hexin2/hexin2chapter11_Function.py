# # 函数
# # 函数无法重载，因为是动态返回值。
# # 11.1实例
# #!/usr/bin/env python
# from operator import add, sub
# from random import randint, choice
#
# ops = {'+': add, '-': sub}
# MAXTRIES = 2
# def doprob():
#     op = choice('+-') # 随机返回其中的元素
#     nums = [randint(1,10) for i in range(2)] # 生成1-10之前的2个数的list
#     nums.sort(reverse=True)
#     ans = ops[op](*nums) # add(*nums) add()函数为BIF，*nums用于给函数传递元组，字典的可变参数.
#     pr = '%d %s %d = ' % (nums[0], op, nums[1])
#     oops = 0
#     while True:
#         try:
#             if int(input(pr)) == ans:
#                 print('correct')
#                 break
#             if oops == MAXTRIES:
#                 print('answer\n%s%d'%(pr, ans))
#             else:
#                 print('incorrect... try again')
#                 oops += 1
#         except KeyboardInterrupt:
#             print('invalid input... try again')
# def main():
#     while True:
#         doprob()
#         try:
#             opt = input('Again? [y]').lower()
#             if opt and opt[0] == 'n':
#                 break
#         except KeyboardInterrupt:
#             break
# if __name__ == '__main__':
#     main()
#
# # 11.2传参
# # 1形参不影响实参类型：整数、字符串、元组
# # !/usr/bin/python3
# def ChangeInt(a):
#     a = 10
# b = 2
# ChangeInt(b)
# print(b)  # 结果是 2
# # 2形参影响实参类型：列表，字典
# # !/usr/bin/python3
#
# # 可写函数说明
# def changeme(mylist):
#     # "修改传入的列表"
#     mylist.append([1, 2, 3, 4]);
#     print("函数内取值: ", mylist)
#     return
# # 调用changeme函数
# mylist = [10, 20, 30];
# changeme(mylist);
# print("函数外取值: ", mylist)
# # 函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
# # 函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
# # 可写函数说明
# def changeme(mylist):
#     #"修改传入的列表"
#     mylist = [1, 2, 3, 4] # 这里的形参没有改变实参。因为函数内的mylist完全变了。
#     print("函数内取值: ", mylist)
#     return
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值: ", mylist)
# # 函数内取值:  [1, 2, 3, 4]
# # 函数外取值:  [10, 20, 30]
# # 3参数类型:必需参数,关键字参数,默认参数,不定长参数
# # 必须参数:
# # 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
# # 调用printme()函数，你必须传入一个参数，不然会出现语法错误：
# # !/usr/bin/python3
# # 可写函数说明
# def printme(str):
#     #"打印任何传入的字符串"
#     print(str)
#     return
# # 调用printme函数
# printme()#报错
# # 关键字参数:
# # 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# # 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
# def printinfo(name, age):
#     #"打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
# # 调用printinfo函数
# printinfo(age=50, name="runoob")
# # 默认参数
# # 调用函数时，如果没有传递参数，则会使用默认参数。
# # !/usr/bin/python3
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
# # 调用printinfo函数
# printinfo(age=50, name="runoob")
# print("------------------------")
# printinfo(name="runoob")
# # 不定长参数
# # 变长参数，加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。
# # !/usr/bin/python3
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)
#
# # 11.3lambda匿名函数
# # 格式：lambda [arg1 [,arg2,.....argn]]:expression
# # !/usr/bin/python3
# sum = lambda arg1, arg2: arg1 + arg2;
# # 调用sum函数
# print("相加后的值为 : ", sum(10, 20))
# print("相加后的值为 : ", sum(20, 20))
# # 相加后的值为 :  30
# # 相加后的值为 :  40
# 实例:
# x = 10
# def foo():
#     y = 5
#     bar = lambda :x+y
#     print(bar())
# foo()
#
# # 11.4 return
# # return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
# #!/usr/bin/python3
# # 可写函数说明
# def sum( arg1, arg2 ):
#    # 返回2个参数的和."
#    total = arg1 + arg2
#    print ("函数内 : ", total)
#    return total
# # 调用sum函数
# total = sum( 10, 20 )
# print ("函数外 : ", total)
#
# 11.5 global 和 nonlocal关键字
# # 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字
# #!/usr/bin/python3
# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明,如果不使用的话，print(num)会报错,但是注意仅仅是num不行，num11就可以执行。
#     print(num)
#     num = 123
#     print(num)
# fun1()
# print(num)
# num1 = 1
# def ss(a):
#     c = a+num1
#     print(c)
# print(num1)
# ss(10)
# # 1
# # 123
#
# # 11.6注意点
# # 同c++,默认参数必须放在最后面，否则会报：
# def printinfo( age=35,name):   # 默认参数不在最后，会报错
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
# # lambda 匿名函数也是可以使用"关键字参数"进行参数传递,也可以设定默认值
# g = lambda x,y : x**2+y**2
# g(2, 3)
# g(y = 3, x = 2)
# g = lambda x = 0, y = 0 : x**2+y**2
# g(2, 3)
# g(2)
#
# # 11.7命名空间，独立的项目建立自己独立的命名空间体系。
#
# # 11.8 内嵌函数
# # 在函数体内创建另外一个函数（对象）是完全合法的。
# def outer():
#     print("outer")
#     def inner():
#         print("inner")
# # 闭包:
# def outer(x):
#     def inner():
#         print(x) #此处inner()中未发现x，然后获取了外部函数outer()中的x，闭包特性.
#     return inner
# print1 = outer(1)
# print2 = outer(2)
# print1()
# print2()
# # 可以多次调用x(不只2个作用域):定义在外部函数内的但由内部函数引用或者使用的变量被称为自由变量
# # 闭包和函数调用没多少相关，而是关于使用定义在其他作用域的变量。
# x = "glolal2"
# def fun1():
#     x = "2"
#     print("fun1"+x)
#     def fun2():
#         print("fun2"+x)
#         def fun3():
#             print("fun3"+x)
#         return fun3() #  不返回fun3()不执行fun3()
#     return fun2()  #  不返回fun2()不执行fun2() 都是调用的fun1()内的x
# fun1()
#
# # 装饰器
# # 装饰器其实就是一个以函数作为参数并返回一个替换函数的可执行函数
# def outer(some_func): # 装饰器(foo()函数加工者)
#     def inner():
#         print("before some_func")
#         ret = some_func() # 1
#         return ret + 1 #返回替换函数
#     return inner
# def foo(): # 作为参数的函数
#     return 1
# decorated = outer(foo) # 2
# decorated()
# # 格式:
# # @decorator(dec_opt_args)
# # def func2Bdecorated(func_opt_args):
# @outer
# def foo():
#     return 1
# # "foo"(函数对象的引用）和"foo()"（函数对象的调用）的区别
# def foo():
#     print('in foo()')
# bar = foo
# print(bar())
# # 实例
# from functools import wraps
# def sum_add(*args1):  # 我们要给我们的装饰器decorator，带上参数
#     print(*args1)  # 10 20
#
#     def decorator(func):  #第一个函数的参数接受被装饰函数.
#         print(func.__name__)  # sum
#
#         @wraps(func)  # 加上这句，原函数func被decorator作用后，函数性质不变,该函数可以使用被装饰函数参数args2
#         def my_sum(*args2):  # 注意，参数要和原函数保持一致，真正实行扩展功能的是外层的装饰器
#             print(*args2)  # 1 2 3 4 5
#             my_s = 0
#             for n in args1:
#                 my_s = my_s + n  # 这个是我们新加的求和结果
#             return func(*args2) + my_s  # 这个，我们在原求和函数的结果上再加上s，并返回这个值
#
#         return my_sum  # 返回my_sum函数，该函数扩展原函数的功能
#
#     return decorator  # 返回我们的装饰器
# @sum_add(10, 20)  # 启用装饰器 对sum函数进行功能扩展
# def sum(*args):
#     s = 0
#     for n in args:
#         s = s + n
#     return s
# print(sum(1, 2, 3, 4, 5))
# print(sum.__name__)
# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return "Coord: " + str(self.__dict__)
# def add(a, b):
#     return Coordinate(a.x + b.x, a.y + b.y)
# def sub(a, b):
#     return Coordinate(a.x - b.x, a.y - b.y)
# one = Coordinate(100, 200)
# two = Coordinate(300, 200)
# three = Coordinate(-100, -100)
# print(add(one, two))
# def wrapper(func):
#     def checker(a, b): # 1
#         if a.x < 0 or a.y < 0:
#             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
#         if b.x < 0 or b.y < 0:
#             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
#         ret = func(a, b)
#         if ret.x < 0 or ret.y < 0:
#             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
#         return ret
#     return checker
# add = wrapper(add)
# sub = wrapper(sub)
# sub(one, two)  # #Coord: {'y': 0, 'x': 0}
# add(one, three)  # #Coord: {'y': 200, 'x': 100}


# # 11.9 BIF
# 函数式编程的内建函数(基本可被列表解析替换)
# 内建函数 描述
# apply(func[, nkw][, kw])  用可选的参数来调用 func，nkw 为非关键字参数，kw 关
#                           键字参数；返回值是函数调用的返回值。
# filter(func, seq) 调用一个布尔函数 func 来迭代遍历每个 seq 中的元素； 返回一个
#                   使 func 返回值为 ture 的元素的序列。
# map(func, seq1[,seq2...]) 将函数 func 作用于给定序列（s)的每个元素，并用一个列表来提
#                           供返回值；如果 func 为 None， func 表现为一个身份函数，返回
#                           一个含有每个序列中元素集合的 n 个元组的列表。
# reduce(func, seq[, init]) 将二元函数作用于 seq 序列的元素，每次携带一对（先前的结果
#                           以及下一个序列元素），连续的将现有的结果和下雨给值作用在获
#                           得的随后的结果上，最后减少我们的序列为一个单一的返回值；如
#                           果初始值 init 给定，第一个比较会是 init 和第一个序列元素而不
#                           是序列的头两个元素。
#
# # 11.10偏函数PFA
# # 正常函数
# def add(a, b):
#     return a + b;
# add(3, 5)
# add(4, 7)
# # 如果已知其中一个参数为100,只需给出另一个值的时候(有点类似c++ 二元函数转一元的意思)
# from  functools import partial
# puls = partial(add, 100)
# result = puls(9)
# print(result)
# # 实例2:
# # 关键字参数模式的PFA
# # /usr/bin/env Python3
# # -*- encoding:UTF-8 -*-
# import  functools
# def mod(m,*,key=2):
#     return m % key == 0
# mod_to_2 = functools.partial(mod, key=2)
# print('A__3___使用原函数的默认关键字参数对2进行求余：')
# print(mod(3))                           #对2进行求余-- 原函数 使用默认参数
# print('B__3___使用偏函数对2进行求余：')
# print(mod_to_2(3))                      #对2进行求余-- 新函数 --偏函数产生
# mod_to_5 = functools.partial(mod,key=5)
# print('C__25___使用原函数的关键字参数对5进行求余：')
# print(mod(25,key=5))                    #对5进行求余 -- 原函数
# print('D__25___使用偏函数对5进行求余：')
# print(mod_to_5(25))                     #对5进行求余 -- 新函数--偏函数产生
#
# # 11.11 递归
# # 如果函数包含了对其自身的调用，该函数就是递归的。
# def factorial(n):
#     if n == 0 or n == 1: # 0! = 1! = 1
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(100))
#
#