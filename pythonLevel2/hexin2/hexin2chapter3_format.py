# # 3.1编写风格基础语法
# # z 井号(#)表示之后的字符为 Python 注释
# # z 换行 (\n) 是标准的行分隔符（通常一个语句一行）
# # z 反斜线 ( \ ) 继续上一行
# # 在含有小括号、中括号、花括号时可以多行书写。另外就是三引号包括下的字符串也可以跨行书写。
# if (weather_is_hot == 1) and \
# (shark_warnings == 0):
# send_goto_beach_mesg_to_pager()
# # z 分号 ( ; )将两个语句连接在一行中
# # 同一行写多个语句
# import sys; x = 'foo'; sys.stdout.write(x + '\n')
# # z 冒号 ( : ) 将代码块的头和体分开
# # z 语句（代码块）用缩进块的方式体现
# # z 不同的缩进深度分隔不同的代码块
# # z Python 文件以模块的形式组织,每一个 Python 脚本文件都可以被当成是一个模块。
#
# # 3.2风格
# # (1) 起始行(Unix)
# # (2) 模块文档
# # (3) 模块导入
# # (4) 变量定义
# # (5) 类定义
# # (6) 函数定义
# # (7) 主程序
# (1)#/usr/bin/env python 仅Unix中用
# (2)"this is a test module"
# (3)import sys;import os
# (4)debug = ture
# (5)class FooClass(Object):
#         FooClass
#         pass
# (6)def test():
#     print("test function")
# # 如果模块是被导入， __name__ 的值为模块名字
# # 如果模块是被直接执行， __name__ 的值为 '__main__'
# (7)if __name__ == '__main__':
#         test()
#
# 3.3有价值模块
# # pdb:Debugger工具，pycharm因为自带有调试所以可以忽略
# import pdb
# a = "aaa"
# pdb.set_trace()
# b = "bbb"
# c = "ccc"
# final = a + b + c
# print(final)

# # logging:日志工具
# import logging
# # 默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
# # 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。
# # 通过logging.basicConfig函数对日志的输出格式及方式做相关配置
# logging.basicConfig(level=logging.DEBUG,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='myapp.log',
#                 filemode='w')
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')
# # 将日志同时输出到文件和屏幕
# logging.basicConfig(level=logging.DEBUG,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='myapp.log',
#                 filemode='w')
# #################################################################################################
# #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
# console = logging.StreamHandler()
# 设置日志等级：包含DEBUG,INFO,WARNING,ERROR,CRITICAL等级
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# 设置日志格式
# console.setFormatter(formatter)
# 处理信息输出,此处将logging输出到控制台，亦可输出到文件。
# logging.getLogger('').addHandler(console)
# #################################################################################################
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')

# # cProfile:程序性能测试工具
# # 命令模式
# # # 直接把分析结果打印到控制台
# # python -m cProfile test.py
# # # 把分析结果保存到文件中
# # python -m cProfile -o result.out test.py
# # # 增加排序方式
# # python -m cProfile -o result.out -s cumulative test.py
# def test():
#     x = 1
#     while x < 1000000:
#         print("123")
#         x += 1
# if __name__ == "__main__":
#     import cProfile
#     # 直接把分析结果打印到控制台
#     cProfile.run("test()")
#     # 把分析结果保存到文件中
#     cProfile.run("test()", filename="result.out")
#     # 增加排序方式
#     cProfile.run("test()", filename="result.out", sort="cumulative")
# # # 使用cProfile分析的结果可以输出到指定的文件中，但是文件内容是以二进制的方式保存的，用文本编辑器打开时乱码。
# # # 所以，Python提供了一个pstats模块，用来分析cProfile输出的文件内容。
# import pstats
# # 创建Stats对象
# p = pstats.Stats("result.out")
# # strip_dirs(): 去掉无关的路径信息
# # sort_stats(): 排序，支持的方式和上述的一致
# # print_stats(): 打印分析结果，可以指定打印前几行
# # 和直接运行cProfile.run("test()")的结果是一样的
# p.strip_dirs().sort_stats(-1).print_stats()
# # 按照函数名排序，只打印前3行函数的信息, 参数还可为小数,表示前百分之几的函数信息
# p.strip_dirs().sort_stats("name").print_stats(3)
# # 按照运行时间和函数名进行排序
# p.strip_dirs().sort_stats("cumulative", "name").print_stats(0.5)
# # 如果想知道有哪些函数调用了sum_num
# p.print_callers(0.5, "sum_num")
# # 查看test()函数中调用了哪些函数
# p.print_callees("test")
#