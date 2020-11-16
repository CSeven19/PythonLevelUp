# #
# # 17.1 site模块 处理特定站点的配置，尤其是导入路径。
# import sys
# import os
# import platform  #获取操作系统平台、版本及架构
# import site
# if 'Windows' in platform.platform():
#     SUFFIXES = [
#     '',
#     'lib/site-packages',
#     ]
# else:
#     SUFFIXES = [
#     'lib/python%s/site-packages' % sys.version[:3],
#     'lib/site-python',
#     ]
# print('Path prefixes:')
# for p in site.PREFIXES:
#     print(' ', p)
# for prefix in sorted(set(site.PREFIXES)):
#     print()
#     print(prefix)
# for suffix in SUFFIXES:
#     print()
#     print(' ', suffix)
#     path = os.path.join(prefix, suffix).rstrip(os.sep)
#     print(' exists :', os.path.exists(path))
#     print(' in path:', path in sys.path)
#
# # 实例2: 自定义site
# print('Loading sitecustomize.py')
# import site
# import platform
# import os
# import sys
# path = os.path.join('/opt',
# 'python',
# sys.version[:3],
# platform.platform(),
# )
# print('Adding new path', path)
# site.addsitedir(path)


# # 17.2 sys模块
# # sys模块提供了一系列有关Python运行环境的变量和函数
# # 1 sys.argv 可以用sys.argv获取当前正在执行的命令行参数的参数列表(list)。
# # sys.argv[0]	当前程序名
# # sys.argv[1]	第一个参数
# # sys.argv[2]	第二个参数
# # encoding: utf-8
# # filename: argv_test.py
# import sys
#
# # 获取脚本名字
# print('The name of this program is: %s' %(sys.argv[0]))
# # 获取参数列表
# print('The command line arguments are:')
# for i in sys.argv:
#     print(i)
# # 统计参数个数
# print('There are %s arguments.'%(len(sys.argv)-1))  # sys.argv(0)不是参数.
#
# # 2 sys.platform
# # 获取当前执行环境的平台，如win32表示是Windows 32bit操作系统，linux2表示是linux平台；
# import sys
# print(sys.platform)
#
# # 3 sys.path
# # path是一个目录列表，供Python从中查找第三方扩展模块
# import sys
# print(sys.path)
# # 开始位置插入一个路径
# sys.path.insert(0,'F:\\Python27\\test')
#
# # 4 sys.builtin_module_names
# # 返回一个列表，包含内建模块的名字。
# import sys
# print(sys.builtin_module_names)
#
# # 5 sys.exit(n)
# # 调用sys.exit(n)可以中途退出程序，当参数非0时，会引发一个SystemExit异常，从而可以在主程序中捕获该异常
#
# # 6 version()
# import sys
# print('sys.version =', repr(sys.version))
# print('sys.version_info =', sys.version_info)
# print('sys.hexversion =', hex(sys.hexversion))
# print('sys.api_version =', sys.api_version)
#
# # 7 flags
# import sys
# if sys.flags.debug:
#     print('Debuging')
# # if sys.flags.py3k_warning:
# #     print('Warning about Python 3.x incompatibilities')
# # if sys.flags.division_warning:
# #     print('Warning about division change')
# # if sys.flags.division_new:
# #     print('New division behavior enabled')
# if sys.flags.inspect:
#     print('Will enter interactive mode after running')
# if sys.flags.optimize:
#     print('Optimizing byte-code')
# if sys.flags.dont_write_bytecode:
#     print('Not writing byte-code files')
# if sys.flags.no_site:
#     print('Not importing "site"')
# if sys.flags.ignore_environment:
#     print('Ignoring environment')
# # if sys.flags.tabcheck:
# #     print('Checking for mixed tabs and spaces')
# if sys.flags.verbose:
#     print('Verbose mode')
# # if sys.flags.unicode:
# #     print('Unicode')
#
# # 8 编码
# import sys
# print('Default encoding :', sys.getdefaultencoding())
# print('File system encoding :', sys.getfilesystemencoding())  #MBCS(Multi-Byte Chactacter System，即多字节字符系统)它是编码的一种类型，而不是某个特定编码的名称。 Unicode与MBCS的区别是：MBCS字符可以使用不同长度的字节编码。
#
# # 9 python执行器和路径
# import sys
# print('Interpreter executable:', sys.executable)
# print('Installation prefix :', sys.prefix)
#
# # 10 sys.getrefcount() 引用计数
# import sys
# one = []
# print('At start :', sys.getrefcount(one))
# two = one
# print('Second reference :', sys.getrefcount(one))
# del two
# print('After del :', sys.getrefcount(one))
#
# # 11 sys.getsizeof() 占位长度
# import sys
# class OldStyle:
#     pass
# class NewStyle(object):
#     pass
# for obj in [ [], (), {}, 'c', 'string', 1, 2.3,
# OldStyle, OldStyle(), NewStyle, NewStyle(),
# ]:
#     print('%10s : %s' % (type(obj).__name__, sys.getsizeof(obj)))
#
# # 12 递归设置
# import sys
# num = sys.getrecursionlimit()  # 最大递归数(堆栈最大深度), 详见 函数 文章(http://blog.csdn.net/rozol/article/details/69242050)
# print(num)
# sys.setrecursionlimit(5000)  # 修改最大递归数
# num2 = sys.getrecursionlimit()
# print(num2)
#
# 其他 参考Python3 sys(解释器 模块)文档.


# 17.3 os 参考核心2


# # 17.4 platform
# import platform
# print('Version :', platform.python_version())
# print('Version tuple:', platform.python_version_tuple())
# print('Compiler :', platform.python_compiler())
# print('Build :', platform.python_build())
# print('Normal :', platform.platform())
# print('Aliased:', platform.platform(aliased=True))
# print('Terse :', platform.platform(terse=True))
# print('uname:', platform.uname())  # 该平台基本信息。
# print()
# print('system :', platform.system())
# print('node :', platform.node())
# print('release :', platform.release())
# print('version :', platform.version())
# print('machine :', platform.machine())
# print('processor:', platform.processor())
# print('interpreter:', platform.architecture())
# print('/bin/ls :', platform.architecture('/bin/ls'))


# # 17.5 gc 垃圾回收
# # 实例1：不存在内存泄漏情况.
# import gc
# import sys
#
# class CGcLeak(object):
#     def __init__(self):
#         self._text = '#' * 10
#
#     def __del__(self):
#         pass
#
# def make_circle_ref():
#     _gcleak = CGcLeak()
#     print("_gcleak ref count0 对象_gcleak的引用计数为: %d" %(sys.getrefcount(_gcleak)))
#     del _gcleak
#     try:
#         print("_gcleak ref count1:%d" %(sys.getrefcount(_gcleak)))
#     except UnboundLocalError:           # 本地变量xxx引用前没定义
#         print("_gcleak is invalid!因为执行了del函数，_gcleak变为了不可达的对象")
# def test_gcleak():
#     gc.enable()                         #设置垃圾回收器调试标志
#     # gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_INSTANCES | gc.DEBUG_OBJECTS)
#     gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
#
#     print("begin leak test...")
#     make_circle_ref()
#
#     print("\nbegin collect...")
#     _unreachable = gc.collect()
#     print("unreachable object num 本次回收不可达的对象个数为:%d" %(_unreachable))
# # gc.garbage是一个list对象，列表项是垃圾收集器发现的不可达（即垃圾对象）、但又不能释放(不可回收)的对象，通常gc.garbage中的对象是引用对象还中的对象。
# # 因Python不知用什么顺序来调用对象的__del__函数，导致对象始终存活在gc.garbage中，造成内存泄露 if __name__ == "__main__": test_gcleak()。如果知道一个安全次序，
# # 那么就可以打破引用焕，再执行del gc.garbage[:]从而清空垃圾对象列表
#     print("garbage object num 整个解释器中垃圾个数为:%d" %(len(gc.garbage)))
# if __name__ == "__main__":
#     test_gcleak()
#
# # 当字典，列表等存在A,B互相利用而无法实现回收时可以使用.
# # 实例2：存在对自己的循环引用造成内存泄露
# import gc
# import sys
#
# class CGcLeak(object):
#     def __init__(self):
#         self._text = '#' * 10
#
#     def __del__(self):
#         pass
#
# def make_circle_ref():
#     _gcleak = CGcLeak()
#     _gcleak._self = _gcleak     #自己循环引用自己
#     print("_gcleak ref count0: %d" %(sys.getrefcount(_gcleak)))
#     del _gcleak
#     try:
#         print("_gcleak ref count1 :%d" %(sys.getrefcount(_gcleak)))
#     except UnboundLocalError:
#         print("_gcleak is invalid!")
#
# def test_gcleak():
#     gc.enable()
# #   gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_INSTANCES | gc.DEBUG_OBJECTS)
#     gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
#
#     print("begin leak test...")
#     make_circle_ref()
#
#     print("\nbegin collect...")
#     _unreachable = gc.collect()
#     print("unreachable object num:%d" %(_unreachable))
#     print("garbage object num:%d" %(len(gc.garbage)))
#
# if __name__ == "__main__":
#     test_gcleak()
# 实例3:利用threshold阀值，超出阀值的自动回收(默认：(700,10,10))

# # 17.6 sysconfig 提供python配置信息的入口
# import sysconfig
# config_values = sysconfig.get_config_vars()
# print('Found %d configuration settings' % len(config_values.keys()))
# print()
# print('Some highlights:')
# print()
# print(' Installation prefixes:')
# print(' prefix={prefix}'.format(**config_values))
# print(' exec_prefix={exec_prefix}'.format(**config_values))
# print()
# print(' Version info:')
# print(' py_version={py_version}'.format(**config_values))
# print(' py_version_short={py_version_short}'.format(**config_values))
# print(' py_version_nodot={py_version_nodot}'.format(**config_values))
# print()
# print(' Base directories:')
# print(' base={base}'.format(**config_values))
# print(' platbase={platbase}'.format(**config_values))
# print(' userbase={userbase}'.format(**config_values))
# print(' srcdir={srcdir}'.format(**config_values))




