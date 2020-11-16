# 1
# distutilsed打包工具(参考foobar包为标准).
# pbr打包工具.
# python setup.py sdist生成tarball然后发布到http:///pypi.python.org生成可以pip的包.
# 2
# 框架与外部库的区别：框架更像是我们用代码去扩充它(框架就是更丰富强大的外部库)
# 事件驱动框架Twisted(参考文档)
# web框架dijango
# 3
# Sphinx文档工具(类似doku文档工具,参考文档)
# 4
# virtualenv(参考文档) virtualenv通过创建独立Python开发环境的工具, 来解决依赖、版本以及间接权限
# 问题. 比如一个项目依赖Django1.3 而当前全局开发环境为Django1.7, 版本跨度过大, 导致不兼容使项目无法正在运行, 使用virtualenv可以解决这些问题.
# 5 测试
# nose(参考文档)
# mock模块
# 6 ast 抽象语法树
# 7 性能
# # 实例1:集合的应用
# fields = ["foo","32","12","bar","bar"]
# def find_field():
#     for field in fields:
#         if field not in ["foo","bar"]:
#             return True
#         return False
# # 替换find_field()
# def find_field2():
#     return  set(fields) - set(["foo","bar"])
# if __name__ == '__main__':
#     r = find_field()
#     print(r)
#     print(find_field2())
#
# # 实例2:bisect 2分查找法及性能分析  参考:Python 二分查找与 bisect 模块
# import math
# def binary_search_recursion(lst, value, low, high):
#     if high < low:
#         return None
#     mid = math.ceil((low + high) / 2)
#     if lst[mid] > value:
#         return binary_search_recursion(lst, value, low, mid - 1)
#     elif lst[mid] < value:
#         return binary_search_recursion(lst, value, mid + 1, high)
#     else:
#         return mid
#
#
# def binary_search_loop(lst, value):
#     low, high = 0, len(lst) - 1
#     while low <= high:
#         mid = math.ceil((low + high) / 2)
#         if lst[mid] < value:
#             low = mid + 1
#         elif lst[mid] > value:
#             high = mid - 1
#         else:
#             return mid
#     return None
#
# # 2分查找法
# def binary_search_bisect(lst, x):
#     from bisect import bisect_left
#     i = bisect_left(lst, x)
#     if i != len(lst) and lst[i] == x:
#         return i
#     return None
#
# if __name__ == "__main__":
#     import random
#
#     lst = [random.randint(0, 10000) for _ in range(100000)]
#     lst.sort()
#
#
#     def test_recursion():
#         binary_search_recursion(lst, 999, 0, len(lst) - 1)
#
#
#     def test_loop():
#         binary_search_loop(lst, 999)
#
#
#     def test_bisect():
#         binary_search_bisect(lst, 999)
#
#
#     import timeit
#
#     t1 = timeit.Timer("test_recursion()", setup="from __main__ import test_recursion")
#     t2 = timeit.Timer("test_loop()", setup="from __main__ import test_loop")
#     t3 = timeit.Timer("test_bisect()", setup="from __main__ import test_bisect")
#
#     print("Recursion:", t1.timeit())
#     print("Loop:", t2.timeit())
#     print("Bisect:", t3.timeit())
#
# 实例3: 避免大块复制
#
# 8 postgresql触发器 参考:PostgreSQL触发器
# 创建监听message表成功插入后的触发事件notify_on_message_insert,触发函数为notify_on_insert()
# create trigger notify_on_message_insert after insert on message for each row execute procedure notify_on_insert()