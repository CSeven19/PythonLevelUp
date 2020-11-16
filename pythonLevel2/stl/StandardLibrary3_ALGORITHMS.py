# 算法
#
# # 3.1 functools
#
# # 1 cmp_to_key，将一个比较函数转换关键字函数；
# from functools import cmp_to_key
#
# def compare(ele1,ele2):
#     return ele2 - ele1
#
# a = [2, 3, 1]
# b = ['abc', 'bac', 'cba']
# print(sorted(a, key=cmp_to_key(compare)))
# print(sorted(b, key=cmp_to_key(compare)))  #字符串报错不能这么简单相减
#
# # 2 偏函数
# import functools
#
# def add(a,b):
#     return a + b
#
# add3 = functools.partial(add,3)
# add5 = functools.partial(add,5)
#
# print(add3(4))
# print(add5(10))
#
# # # 3 total_ordering
# # # 这是一个类装饰器，给定一个类，这个类定义了一个或者多个比较排序方法，这个类装饰器将会补充其余的比较方法，减少了自己定义所有比较方法时的工作量；
# # # 被修饰的类必须至少定义 __lt__()， __le__()，__gt__()，__ge__()中的一个，同时，被修饰的类还应该提供 __eq__()方法。
# from functools import total_ordering
#
# class Person:
#     # 定义相等的比较函数
#     def __eq__(self,other):
#         return ((self.lastname.lower(), self.firstname.lower()) ==
#                 (other.lastname.lower(), other.firstname.lower()))
#
#     # 定义小于的比较函数
#     def __lt__(self,other):
#         return ((self.lastname.lower(), self.firstname.lower()) <
#                 (other.lastname.lower(), other.firstname.lower()))
#
# p1 = Person()
# p2 = Person()
#
# p1.lastname = "123"
# p1.firstname = "000"
#
# p2.lastname = "1231"
# p2.firstname = "000"
#
# print(p1 < p2)
# # print(p1 <= p2)  #无法执行，不能被自动填充。
# print(p1 == p2)
# print(p1 > p2)
# # print(p1 >= p2)
#
# # 4装饰器
# # update_wrapper 更新一个包裹（wrapper）函数，使其看起来更像被包裹（wrapped）的函数。
# # 这个函数的主要用途是在一个装饰器中，原函数会被装饰（包裹），装饰器函数会返回一个wrapper函数，如果装饰器返回的这个wrapper函数没有被更新，那么它的一些元数据更多的是反映wrapper函数定义的特征，无法反映wrapped函数的特性。
# # wraps这个函数可用作一个装饰器，简化调用update_wrapper的过程，调用这个函数等价于调用partial(update_wrapper, wrapped = wrapped, assigned = assigned,updated = updated)。
#
# from functools import wraps
#
# def my_decorator(f):
#     @wraps(f)
#     def wrapper(*args,**kwds):
#         print("Calling decorated function")
#         return f(*args,**kwds)
#     return wrapper
#
# @my_decorator
# def example():
#     """DocString"""
#     print("Called example function")
#
# @my_decorator
# def example2():
#     """DocString"""
#     print("Called example function2")
#
# example()
# example2()
# print(example.__name__)
# print(example.__doc__)
#

# 3.2  itertools—Iterator Functions 循环器
#
# # 3.2.1 迭代器
# # 1 iter() 迭代器
# for i in iter([2, 4, 5, 6]):
#     print(i)
# # 2 无穷循环器
# # count(5, 2)  # 从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...
# # cycle('abc')  # 重复序列的元素，既a, b, c, a, b, c ...
# # repeat(1.2)  # 重复1.2，构成无穷循环器，即1.2, 1.2, 1.2, ...  repeat也可以有一个次数限制:repeat(10, 5)  # 重复10，共重复5次
# # 3 accumulate() 累计迭代器
# from itertools import *
# print(list(accumulate((1,2,3,4,5))))
# # 4chain级联迭代器(用于返回级联元素)
# from itertools import *
# print(list(chain((1,2,3),"abc",range(5))))
# # 5 compress(data，selectors) 选择压缩迭代器  根据选择器selectors的元素（True/False），返回元素为True对应的data系列中的元素，当data或selectors终止时，停止判断
# addresses = [
#             '5412 N CLARK',
#             '5148 N CLARK',
#             '5800 E 58TH',
#             '2122 N CLARK',
#             '5645 N RAVENSWOOD',
#             '1060 W ADDISON',
#             '4801 N BROADWAY',
#             '1039 W GRANVILLE',
#         ]
# counts = [0, 3, 10, 4, 1, 7, 6, 1]
# from itertools import compress
# more5 = [n > 5 for n in counts]
# print(more5)
# print(list(compress(addresses, more5)))
# # 6 islice(iterable,stop)切片迭代器
# import itertools
# print(list(itertools.islice("ABCDFEG", 2, 4)))
# print(list(itertools.islice("ABCDEF", 2)))
# print(list(itertools.islice("ABCDFEG", 0, None, 2)))  # islice(iterable,start,stop,step)
# # 7 permutations(iterable,r=None) 排列迭代器 返回可迭代对象iterable的元素排列，组合长度为r（默认为系列的长度）
# import itertools
# print(list(itertools.permutations([1,2,3],2)))
# print(list(itertools.permutations([1,2,3])))
# # 8 product(*itertools,repeat=1)  product('ABCD', repeat=2) 笛卡尔积迭代器 返回可迭代对象itertools1，itertools2...的元素的笛卡尔积，repeat为可迭代对象的重复次数
# import itertools
# print(list(itertools.permutations([1,2,3],2)))
# print(list(itertools.permutations([1,2,3])))
# print(list(itertools.product([1,2],"abc")))
# print(list(itertools.product(range(2),repeat=3)))
# print(list(itertools.product(range(2),repeat=2)))

# # 3.2.2 函数式工具
# # 函数式编程是将函数本身作为处理对象的编程范式。在Python中，函数也是对象，因此可以轻松的进行一些函数式的处理，比如map(), filter(), reduce()函数。
# # itertools包含类似的工具。这些函数接收函数作为参数，并将结果返回为一个循环器。
# from itertools import *
# print('Doubles:')
# for i in imap(lambda x:2*x, range(5)):
#     print(i)
# print('Multiples:')
# for i in imap(lambda x,y:(x, y, x*y), range(5), range(5,10)):
#     print('%d * %d = %d' % i)
# # 3.2.3 组合工具groupby() 用于返回可迭代对象的分组
# from itertools import groupby
# def height_class(h):
#     if h > 180:
#         return "tall"
#     elif h < 160:
#         return "short"
#     else:
#         return "middle"
#
# friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
#
# friends = sorted(friends, key=height_class)
# for m, n in groupby(friends, key=height_class):
#     print(m)
#     print(list(n))
#

# # 3.3  operator—Functional Interface to Built-in Operators
# # 逻辑操作
# from operator import *
# a = -1
# b = 5
# print('a =', a)
# print('b =', b)
# print()
# print('not_(a) :', not_(a))
# print('truth(a) :', truth(a))  # not_相反函数
# print('is_(a, b) :', is_(a,b))
# print('is_not(a, b):', is_not(a,b))
# # 比较运算
# a = 3
# b = 5
# print('a =', a)
# print('b =', b)
# print()
#
# for func in (lt, le, eq, ne, ge, gt):
#     print('{0}(a, b):'.format(func.__name__), func(a, b))
# # 算术操作符
# a, b, c, d = -1, 2, -3, 4
#
# print('a =', a)
# print('b =', b)
# print('c =', c)
# print('d =', d)
#
# print('\nPositive/Negative:')
# print('abs(a):', abs(a))
# print('neg(a):', neg(a))
# print('neg(b):', neg(b))
# print('pos(a):', pos(a))
# print('pos(b):', pos(b))
# # 原地操作符
# # 即in-place操作， x += y 等同于 x = iadd(x, y), 如果复制给其他变量比如z = iadd(x, y)等同与z = x; z += y。
# a = 3
# b = 4
# c = [1, 2]
# d = ['a', 'b']
#
# print('a =', a)
# print('b =', b)
# print('c =', c)
# print('d =', d)
# print()
#
# a = iadd(a, b)
# print('a = iadd(a, b) =>', a)
# print()
#
# c = iconcat(c, d)
# print('c = iconcat(c, d) =>', c)
#

# # 3.4 contextlib—Context Manager Utilities  它的作用就是把任意对象变为上下文对象，并支持 with语句。
# # 1定制with可用的上下文类
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s...' % self.name)
# with Query('Bob') as q:
#     q.query()
#
# # 2使用@contextmanager替换上例
# from contextlib import contextmanager
#
#
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
#
# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')
# with create_query('Bob') as q:
#     q.query()
#
# # 3实例3 有点类似装饰器用法了。
# from contextlib import contextmanager
# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)
#
#
# with tag("h1"):
#     print("hello")
#     print("world")
# #
# # 4closing() 如果一个对象没有实现上下文，就不能使用 with 语句，但是可以用 closing() 来把对象变为上下文对象。
# from contextlib import closing
# from urllib.request import urlopen
#
# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)
#
