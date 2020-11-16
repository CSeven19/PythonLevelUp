# !/usr/bin/python
# -*- coding: UTF-8 -*-

#1
# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     # self == java中this
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print "Total Employee %d" % Employee.empCount
#
#     def displayEmployee(self):
#         print "Name : ", self.name, ", Salary: ", self.salary
#
# "创建 Employee 类的第一个对象"
# emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount
#
# print "Employee.__doc__:", Employee.__doc__
# print "Employee.__name__:", Employee.__name__
# print "Employee.__module__:", Employee.__module__
# print "Employee.__bases__:", Employee.__bases__
# print "Employee.__dict__:", Employee.__dict__

#2 销毁

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print class_name, "销毁"
#
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print id(pt1), id(pt2), id(pt3)  # 打印对象的id
# del pt1
# del pt2
# del pt3

#3 继承

# class Parent:  # 定义父类
#     parentAttr = 100
#
#     def __init__(self):
#         print "调用父类构造函数"
#
#     def parentMethod(self):
#         print '调用父类方法'
#
#     def setAttr(self, attr):
#         Parent.parentAttr = attr
#
#     def getAttr(self):
#         print "父类属性 :", Parent.parentAttr
#
#
# class Child(Parent):  # 定义子类
#     def __init__(self):
#         print "调用子类构造方法"
#
#     def childMethod(self):
#         print '调用子类方法 child method'
#
#
# c = Child()  # 实例化子类
# c.childMethod()  # 调用子类的方法
# c.parentMethod()  # 调用父类方法
# c.setAttr(200)  # 再次调用父类的方法
# c.getAttr()  # 再次调用父类的方法

#4 方法重写

# class Parent:  # 定义父类
#     def myMethod(self):
#         print '调用父类方法'
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print '调用子类方法'
#
#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法

#5 运算符重载

# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print v1 + v2

#6 私有变量，公有变量

"""
__foo__: 定义的是特列方法，类似
__init__()
之类的。

_foo: 以单下划线开头的表示的是
protected
类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于
from module import *

__foo: 双下划线的表示的是私有类型(private)
的变量, 只能是允许这个类本身进行访问了。
"""


# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print self.__secretCount
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print counter.publicCount
# print counter.__secretCount  # 报错，实例不能访问私有变量