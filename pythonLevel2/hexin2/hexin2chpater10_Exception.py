# # 异常
# # 10.1 try except else finally
# try:
#  A
# except MyException: B
# else: C
# finally: D
#
# # 10.2with 用于替换try finally等的操作。高效。
# with open(r'somefileName') as somefile:
#     for line in somefile:
#         print(line)
#         # ...more code
# # 等价于
# somefile = open(r'somefileName')
# try:
#     for line in somefile:
#         print(line)
#         # ...more code
# finally:
#     somefile.close()
#
# # 10.3raise [SomeException [, args [, traceback]]] 抛出一个指定的异常，类似java throw
#
# # 10.4断言
# # Python的assert是用来检查一个条件，如果它为真，就不做任何事。如果它为假，则会抛出AssertError并且包含错误信息
# # 用于防御型的编程,运行时检查程序逻辑,检查约定,程序常量,检查文档
# try:
#     assert 1 == 0, 'One does not equal zero silly!'
# except AssertionError:
#     print("呀买已")
#
# # 10.5异常一览
# 异常名称 描述
# BaseExceptiona 所有异常的基类
# SystemExitb python 解释器请求退出
# KeyboardInterruptc 用户中断执行(通常是输入^C)
# Exceptiond 常规错误的基类
# StopIteratione 迭代器没有更多的值
# GeneratorExita 生成器(generator)发生异常来通知退出
# SystemExith Python 解释器请求退出
# StandardErrorg 所有的内建标准异常的基类
# ArithmeticErrord 所有数值计算错误的基类
# FloatingPointErrord 浮点计算错误
# OverflowError 数值运算超出最大限制
# ZeroDivisionError 除(或取模)零 (所有数据类型)
# AssertionErrord 断言语句失败
# AttributeError 对象没有这个属性
# EOFError 没有内建输入,到达 EOF 标记
# EnvironmentErrord 操作系统错误的基类
# IOError 输入/输出操作失败
# OSErrord 操作系统错误
# WindowsErrorh
#  Windows 系统调用失败
# ImportError 导入模块/对象失败
# KeyboardInterruptf 用户中断执行(通常是输入^C)
# LookupErrord 无效数据查询的基类
# IndexError 序列中没有没有此索引(index)
# KeyError 映射中没有这个键
# MemoryError 内存溢出错误(对于 Python 解释器不是致命的)
# NameError 未声明/初始化对象 (没有属性)
# UnboundLocalErrorh 访问未初始化的本地变量
# ReferenceErrore 弱引用(Weak reference)试图访问已经垃圾回收了的对象
# RuntimeError 一般的运行时错误
# NotImplementedErrord 尚未实现的方法
# SyntaxError Python 语法错误
# IndentationErrorg 缩进错误
# TabErrorg
#  Tab 和空格混用
# SystemError 一般的解释器系统错误
# TypeError 对类型无效的操作
# ValueError 传入无效的参数
# UnicodeErrorh
#  Unicode 相关的错误
# UnicodeDecodeErrori
#  Unicode 解码时的错误
# UnicodeEncodeErrori
#  Unicode 编码时错误
# UnicodeTranslateErrorf Unicode 转换时错误
# Warningj 警告的基类
# DeprecationWarningj 关于被弃用的特征的警告
# FutureWarningi 关于构造将来语义会有改变的警告
# OverflowWarningk 旧的关于自动提升为长整型(long)的警告
# PendingDeprecationWarningi 关于特性将会被废弃的警告
# RuntimeWarningj 可疑的运行时行为(runtime behavior)的警告
# SyntaxWarningj 可疑的语法的警告
# UserWarningj 用户代码生成的警告
#
# 10.6关联模块
# exceptions 内建异常(永远不用导入这个模块)
# contextliba 为使用 with 语句的上下文对象工具
# sys 包含各种异常相关的对象和函数(见 sys.ex*)