# # 执行环境
# # Python 有 4 种可调用对象：函数(内建函数（BIFs),用户定义的函数（UDF）,)，方法，类，以及一些类的实例。(属于类的叫方法，类外的叫函数(包括类中的静态方法))
# #
# # 14.1代码对象
# # 可执行对象和内建函数
# # 内建函数和语句 描述
# # callable(obj) 如果 obj 可调用，返回 True，否则返回 FALSE
# # compile(string,file, type) 从 type 类型中创建代码对象(包括:eval可求值的表达式（和eval()一起用）,single单一可执行语句（和exec一起用）,exec可执行语句组（和exec一起用）)； file 是代码存放的地方（通常设为"")
# # eval(obj, glo- bals=globals(), 对 obj 进行求值，obj 是已编译为代码对象的表达式，或是一个字符串表达式；可以给出全局或者/和局部的名字空间
# # locals=locals()) 对 obj 进行求值，obj 是已编译为代码对象的表达式，或是一个字符串表达式；可以给出全局或者/和局部的名字空间
# # exec obj 执行 obj、单一的 python 语句或者语句的集合，也就是说格式是代码对象或者字符串；obj 也可以是一个文件对象（已经打开的有效 python 脚本中）
# # input(prompt='') 等同于 eval(raw_input(prompt=”))
# # 以下可在命令行中执行
# print(callable(dir))  # built-in function # 内建函数
# print(callable(1))  # integer #整数
# def foo(): pass
# print(callable(foo))  # user-defined function # 用户自定义函数
# print(callable('bar'))  # string #字符串
# class C(object): pass
# print(callable(C)) # class #类
# eval_code = compile('100 + 200', '', 'eval')
# print(eval(eval_code))
# single_code = compile('print("Hello world!")', '', 'single')
# print(single_code)  #<code object ? at 120998, file "", line 0>
# exec(single_code)  #Hello world!
# exec_code = compile("""
# req = input('Count how many numbers? ')
# for eachNum in range(int(req)):
#     print(eachNum)""", '', 'exec')
# exec(exec_code)
#
# # 14.2 执行其他的Python或其他语言程序
# # 1 exec()
# import codecs
# f = codecs.open("F:\Python35\workspace\pythonLevelB\getjpg.py", 'r',"utf-8")
# exec(f.read())
# f.close()
# # 2执行其他（非 Python）程序
# Table 14.6 执行外部程序的 os 模块函数
#  (u 只对 unix 有效， w 只对 windows 有效）
# os 模块函数 描述
# system(cmd) 执行程序 cmd（字符串），等待程序结束，返回退出代码（windows 下，始终为 0）执行任何的命令和程序显示输出都会传到标准输出上。
# fork() 创建一个和父进程并行的子进程[通常来说和 exec*()一起使用]；返回两次....一次给父进程一次给子进程
# execl(file, arg0,arg1,...) 用参数列表 arg0, arg1 等等执行文件
# execv(file, arglist) 除了使用参数向量列表，其他的和 execl()相同
# execle(file, arg0,arg1,... env) 和 execl 相同，但提供了环境变量字典 env
# execve(file,arglist, env) 除了带有参数向量列表，其他的和 execle()相同
# execlp(cmd, arg0,arg1,...) 于 execl()相同，但是在用户的搜索路径下搜索完全的文件路径名
# execvp(cmd, arglist) 除了带有参数向量列表，与 execlp()相同
# execlpe(cmd, arg0, arg1,... env) 和 execlp 相同，但提供了环境变量字典 env
# execvpe(cmd,arglist, env) 和 execvp 相同，但提供了环境变量字典 env
# spawn*(mode, file, args[, env]) spawn*()家族在一个新的进程中执行路径，args 作为参数，也许还有环境变量的字典 env;模式（mode）是个显示不同操作模式的魔术。
# wait() 等待子进程完成[通常和 fock 和 exec*()一起使用] ○U
# waitpid(pid,options) 等待指定的子进程完成[通常和 fock和 exec*()一起使用] ○U
# popen(cmd, mode='r',buffering=-1)是文件对象和 system()函数的结合 执行字符串 cmd，返回一个类文件对象作为运行程序通信句柄，默认为读取模式和默认系统缓冲
# startfile(path) 用关联的应用程序执行路径 W
# # system():
# import os
# result = os.system('dir')
# print(result)
# # popen():
# import os
# f = os.popen('uname -a')  #linux
# data = f.readline()
# f.close()
# print(data)
# # fork():
# ret = os.fork() # spawn 2 processes, both return #产生两个进程，都返回
# if ret == 0: # child returns with PID of 0 #子进程返回的 PID 是 0
#     pass  #child_suite # child code #子进程的代码
# else: # parent returns with child's PID #父进程返回是子进程的 PID
#     pass  #parent_suite # parent code #父进程的代码
# # exec*：
# # 模拟子进程执行一个xbill的小游戏，而父进程继续运行 Python解释器。
# ret = os.fork()
# if ret == 0: # child code #子进程代码
#     os.execvp('xbill', ['xbill'])
# else:
#     # parent code #父进程代码
# os.wait()
# 当子进程执行完毕，需要它们的父进程进行扫尾工作。这个任务，称为”收获孩子”（reaping a child），可以用 wati*()函数完成。
# 当子进程完成执行，还没有被收获的时候，它进入了闲置状态，变成了著名的僵尸进程。
# 在系统中，应该尽量把僵尸进程的数目降到最少，因为在这种状态下的子进程仍保留着在存活时期分配给它们的系统资源，而这些资源只能在父进程收获它们之后才能释放掉。
# # 3subprocess 模块
# # 替换system()
# from subprocess import call
# res = call(('dir',r'D:'),shell=True)
# # res = call(('cat', '/etc/motd'))  #linux
# print(res)
# # 替换popen()
# from subprocess import Popen, PIPE
# f = Popen("notepad.exe test.txt", shell=True, stdout=PIPE)
# # 4相关函数
# os/popen2.popen2a() 执行文件，打开文件，从新创建的运行程序读取(stdout)，或者向该程序写(stdin)
# os/popen2.popen3a() 执行文件，打开文件，从新创建的运行程序读取(stdout 和 stder) ，或者向该程序写(stdin)
# os/popen2.popen4b() 执行文件，打开文件，从新创建的运行程序读取(结合 stdout，stdout)，或者向该程序写(stdin)
# commands.getoutput() 在子进程中执行文件，以字符串返回所有的输出○U
# subprocess.callc() 创建 subprocess 的便捷函数。 Popen 等待命令完成，然后返回状态代码;与 os.system()类似，但是是较灵活的替代方案
# # 5结束执行sys.exit() and SystemExit
# # sys.exit() 立即退出程序并返回调用程序,调用 sys.exit()时，就会引发 systemExit()异常
# #!/usr/bin/env python/args.py
# import sys
#
# def usage():
#     print('At least 2 arguments (incl. cmd name).')
#     print('usage: args.py arg1 arg2 [arg3... ]')
#     sys.exit(1)
# argc = len(sys.argv)
# if argc < 3:
#     usage()
# print("number of args entered:", argc)
# print("args (incl. cmd name) were:", sys.argv)
#
# # 调用
# # $ args.py
# # At least 2 arguments required (incl. cmd name). usage: args.py arg1 arg2
# # [arg3... ]
# # $ args.py XXX
# # At least 2 arguments required (incl. cmd name). usage: args.py arg1 arg2 [arg3... ]
# # $ args.py 123 abc
# # number of args entered: 3
# # args (incl. cmd name) were: ['args.py', '123', 'abc']
# # $ args.py -x -2 foo
# # number of args entered: 4
# # args (incl. cmd name) were: ['args.py', '-x', '-2',
# # 'foo']
#
# 14.3各种操作系统接口
# os 模块属性 描述
# uname() 获得系统信息（主机名，操作系统版本，补丁级别， 系统构架等等）
# getuid()/setuid(uid) 获取/设置现在进程的真正的用户 ID
# getpid()/getppid() 获取真正的现在/父进程 ID（PID) ○W
# getgid()/setgid(gid) 获取/设置现在进程的群组 ID
# getsid()/setsid() 获取会话 ID(SID)或创建和返回新的 SID。
# umask(mask) 设置现在的数字 unmask，同时返回先前的那个（mask 用于文件许可）○W
# getenv(ev)/putenv(ev, value),environ 获取和设置 环境变量 ev 的值；os.envion 属性是描述当前所有环境变量的字典○
# geteuid()/setegid() 获取/设置当前进程的有效用户 ID（GID）
# getegid()/setegid() 获取/设置当前进程的有效组 ID（GID）
# getpgid(pid)/setpgid(pid, pgrp) 获取和设置进程 GID 进程 PID;对于 get,如果 pid 为 0，便返回现在进程的进程 GID
# getlogin() 返回运行现在进程的用户登录
# times() 返回各种进程时期的元组 ○W
# strerror(code) 返回和错误代码对应的错误信息
# getloadavg() 返回代表在过去 1，5，15 分钟内的系统平均负载值的元组。
#
# 14.4相关模块
# 模块 描述
# atexita 注册当 python 解释器退出时候的执行句柄,只定义了一个register函数用于注册程序退出时的回调函数，我们可以在这个回调函数中做一些资源清理的操作。
# popen2 提供额外的在 os.popen 之上的功能：（提供通过标准文件和其他的进程交互的能力；对于 python2.4 和更新的版本，使用 subpross）
# commands 提供额外的在 os.system 之上的功能：把所有的程序输出保存在返回的字符串中（与输出到屏幕的相反）；对于 python2.4 和更新的版本，使用 subpross○U
# getopt 在这样的应用程序中的处理选项和命令行参数
# argparse 命令行解析工具
# site 处理 site-specific 模块或包
# platformb 底层平台和架构的属性
# subprocessc 管理（计划替代旧的函数和模块，比如 os.system()， os.spawn*()，os.popen*()， popen2.*, command.*)
# readline 模块定义了一系列函数用来读写Python解释器中历史命令，并提供自动补全命令功能。这个模块可以通过relcompleter模块直接调用，模块中的设置会影响解释器中的交互提示，以及内置函数raw_input()和input()提供的提示。
# getpass模块提供了可移植的密码输入，一共包括下面两个函数：1. getpass.getpass() 2. getpass.getuser()
# shlex 使用类似shell的语法分割字符串s，相当于特殊的tokenizer。经常用在subprocess.Popen的第一个参数中。
# sched 模块功能类似Timer，不同的原理。


# # std14.1 getopt模块
# getopt(args, shortopts, longopts = [])
# 在运行程序时，可能需要根据不同的条件，输入不同的命令行选项来实现不同的功能。目前有短选项和长选项两种格式。短选项格式为"-"加上单个字母选项；长选项为"--"加上一个单词。
# 长格式是在Linux下引入的。许多Linux程序都支持这两种格式。在Python中提供了getopt模块很好的实现了对这两种用法的支持，而且使用简单。
# # 实例1:
# import getopt
# opts, args = getopt.getopt([ '--noarg',  #识别--XXX的，并返回一个(key,val)元组.
#     '--witharg', 'val',
#     '--witharg2=another',
#     ],
#     '',
#     [ 'noarg', 'witharg=', 'witharg2=' ]
# )
# for opt in opts:
#     print(opt)
#
# # 实例2:
# import getopt
# import sys
# version = '1.0'
# verbose = False
# output_filename = 'default.out'
# print(sys.argv[1:])
# try:
#     options, remainder = getopt.getopt(
#     sys.argv[1:],
#     'o:v',
#     ['output',
#     'verbose',
#     'version',
#     ])
# except getopt.GetoptError as err:
#     print('ERROR:', err)
#     sys.exit(1)
# print('OPTIONS :', options)
# for opt, arg in options:
#     if opt in ('-o', '--output'):
#         output_filename = arg
#     elif opt in ('-v', '--verbose'):
#         verbose = True
#     elif opt == '--version':
#         version = arg
# print('VERSION :', version)
# print('VERBOSE :', verbose)
# print('OUTPUT :', output_filename)
# print('REMAINING :', remainder)
#

# # std14.2 optparse
# # Python 有两个内建的模块用于处理命令行参数：
# # 一个是 getopt，《Deep in python》一书中也有提到，只能简单处理 命令行参数；
# # 另一个是 optparse，它功能强大，而且易于使用，可以方便地生成标准的、符合Unix/Posix 规范的命令行说明。
# from optparse import OptionParser
#
# parser = OptionParser()
# parser.add_option("-f", "--file", dest="filename",
#                   help="write report to FILE", metavar="FILE")
# parser.add_option("-q", "--quiet",
#                   action="store_false", dest="verbose", default=True,
#                   help="don't print status messages to stdout")
# (options, args) = parser.parse_args()
#
# 现在，妳就可以在命令行下输入：
# <yourscript> --file=outfile -q
# <yourscript> -f outfile --quiet
# <yourscript> --quiet --file outfile
# <yourscript> -q -foutfile
# <yourscript> -qfoutfile
# 上面这些命令是相同效果的。除此之外， optparse 还为我们自动生成命令行的帮助信息：
# <yourscript> -h
# <yourscript> --help
# 输出:
# usage: < yourscript > [options]
#
# options:
# -h, --help show this help message and exit
# -f FILE, --file = FILE write report to FILE
# -q, --quiet don't print status messages to stdout
