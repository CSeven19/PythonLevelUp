# # 12.1sys相关
# import sys
# # 系统默认的搜索路径
# print(sys.path)
# # 文件未在搜索路径中，但自己知道路径地址的时候
# sys.path.append('F:\\Python27\\workspace\\pythonLevelB\\hexin2chapter14_Command.py')
# # 当前已有模板
# print(sys.modules)
# # 模板中BIF
# # dir():
# print(dir(sys))

# 12.2名称空间
# Python 解释器首先加载内建名称空间。 它由 __builtins__ 模块中的名字构成。 随后加载执
# 行模块的全局名称空间, 它会在模块开始执行后变为活动名称空间。 这样我们就有了两个活动的名称空间。
# 如果在执行期间调用了一个函数, 那么将创建出第三个名称空间, 即局部名称空间。 我们可以
# 通过 globals() 和 locals() 内建函数判断出某一名字属于哪个名称空间。
# 参看454图
# 查找过程：
# 那么确定作用域的规则是如何联系到名称空间的呢? 它所要做的就是名称查询. 访问一个属性
# 时, 解释器必须在三个名称空间中的一个找到它。 首先从局部名称空间开始, 如果没有找到, 解释
# 器将继续查找全局名称空间. 如果这也失败了, 它将在内建名称空间里查找。 如果最后的尝试也失
# 败了, 你会得到这样的错误:
# >>> foo
# Traceback (innermost last): File "<stdin>", line 1, in ?
# NameError: foo
# #  你可以在任何时候给函数添加属性(使用熟悉的句点属性标识):
# def foo():
#     pass
# foo.__doc__ = 'Oops, forgot to add doc str above!'
# foo.version = 0.2
#
# 12.3导入模板
# from module import name1[, name2[,... nameN]]
# from Tkinter import Tk, Frame, Button, Entry, Canvas, Text, LEFT, DISABLED, NORMAL, RIDGE, END
# import module1[, module2[,... moduleN]]
# from fibo import *
# from sound.effects import * 从一个包中导入
# 导入自定义模块:
# 1包必须是带__init__.py的python-package
# 2import 包名.py文件名
# # 变更导入模板名
# import longmodulename
# short = longmodulename
# del longmodulename
# 或者使用as： from cgi import FieldStorage as form
#
# # 12.4__name__属性
# # 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，
# # 模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行
# # 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
# #!/usr/bin/python3
# # Filename: using_name.py
# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')
#
# 12.6杂项
# from __future__ import new_feature 导入python可能有的新特性
# 从 ZIP 文件中导入模块
# 导入模块函数：__import__(module_name[, globals[, locals[, fromlist]]])
# reload()重新加载模块
#
# # 12.5 globals() 和 locals()
# # globals() 和 locals() 内建函数分别返回调用者全局和局部名称空间的字典。
# def foo():
#     print('\ncalling foo()...')
#     aString = 'bar'
#     anInt = 42
#     print("foo()'s globals:", globals().keys())
#     print("foo()'s locals:", locals().keys())
# print("__main__'s globals:", globals().keys())
# print("__main__'s locals:", locals().keys())
# foo()



# std19.1 importlib 模板
