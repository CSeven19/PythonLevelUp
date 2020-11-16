# file
# 9.1文件对象
# file_object = open(file_name, access_mode='r', code)
# file_name 可以是相对路径或者绝对路径.
# access_mode 文件使用模式 'r', 'w', 或是 'a' 分别代表读取, 写入和追加. 还有个 'U' 模式, 代表通用换行符支持
#  文件模式 操作
#  r 以读方式打开
#  rU 或 Ua 以读方式打开, 同时提供通用换行符支持 (PEP 278)
#  w 以写方式打开 (必要时清空)
#  a 以追加模式打开 (从 EOF 开始, 必要时创建新文件)
#  r+ 以读写模式打开
#  w+ 以读写模式打开 (参见 w )
#  a+ 以读写模式打开 (参见 a )
#  rb 以二进制读模式打开
#  wb 以二进制写模式打开 (参见 w )
#  ab 以二进制追加模式打开 (参见 a )
#  rb+ 以二进制读写模式打开 (参见 r+ )
#  wb+ 以二进制读写模式打开 (参见 w+ )
#  ab+ 以二进制读写模式打开 (参见 a+ )
#  a. Python 2.3 中新增
# code 编码
#
# # 9.2BIF
# # 文件方法可以分为四类: 输入, 输出, 文件内移动, 以及杂项操作.
# # 输入:
# # read() 方法用来直接读取字节到字符串中, 最多读取给定数目个字节. 如果没有给定 size
# # 参数(默认值为 -1)或者 size 值为负, 文件将被读取直至末尾. 未来的某个版本可能会删除此方
# # 法.
# # 打开一个文件
# f = open("/tmp/foo.txt", "r")
# str = f.read()
# print(str)
# # 关闭打开的文件
# f.close()
# # Python 是一个非常好的语言。是的，的确非常好!!
# # readline() 方法读取打开文件的一行(读取下个行结束符之前的所有字节). 然后整行，包括行
# # 结束符，作为字符串返回. 和 read() 相同, 它也有一个可选的 size 参数, 默认为 -1, 代表读至
# # 行结束符. 如果提供了该参数, 那么在超过 size 个字节后会返回不完整的行.
# #!/usr/bin/python3
# # 打开一个文件
# f = open("/tmp/foo.txt", "r")
# str = f.readline()
# print(str)
# # 关闭打开的文件
# f.close()
# # Python 是一个非常好的语言。
# # readlines() 方法并不像其它两个输入方法一样返回一个字符串. 它会读取所有(剩余的)行然
# # 后把它们作为一个字符串列表返回. 它的可选参数 sizhint 代表返回的最大字节大小. 如果它大
# # 于 0 , 那么返回的所有行应该大约有 sizhint 字节(可能稍微大于这个数字, 因为需要凑齐缓冲区
# # 大小).
# #!/usr/bin/python3
# # 打开一个文件
# f = open("/tmp/foo.txt", "r")
# str = f.readlines()
# print(str)
# # 关闭打开的文件
# f.close()
# # ['Python 是一个非常好的语言。\n', '是的，的确非常好!!\n']
# # 用迭代读取
# #!/usr/bin/python3
# # 打开一个文件
# f = open("example/two.txt", "r")
# print(f.__next__())
# for line in f:
#     print(line, end='')
# # 关闭打开的文件
# f.close()
# # Python 是一个非常好的语言。是的，的确非常好!!
# 输出:
# # write() 内建方法功能与 read() 和 readline() 相反. 它把含有文本数据或二进制数据块的
# # 字符串写入到文件中去.
# #!/usr/bin/python3
# # 打开一个文件
# f = open("/tmp/foo.txt", "w")
# num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# print(num)
# # 关闭打开的文件
# f.close()
# # 29
# writelines() 方法和 readlines() 一样，是针对列表的操作, 它接受一个字符串列表作为参
# 数 , 将它们写入文件 . 行结束符并不会被自动加入 , 所以如果需要的话 , 你必须在调用
# writelines()前给每行结尾加上行结束符.
# 文件内移动:
# seek() 方法(类似 C 中的 fseek() 函数)可以在文件中移动文件指针到不同的位置. offset
# 字节代表相对于某个位置偏移量. 位置的默认值为 0 , 代表从文件开头算起(即绝对偏移量), 1 代
# 表从当前位置算起, 2 代表从文件末尾算起.
# text() 方法是对 seek() 的补充; 它告诉你当前文件指针在文件中的位置 - 从文件起始算起,
# 单位为字节.
# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
# 杂项方法：
# file.close() 通过关闭文件来结束对它的访问.
# file.flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入
# file.isatty() 判断 file 是否是一个类 tty 设备
# file.fileno() 返回文件的描述符(file descriptor ,FD, 整数值)
# file.nexta() 返回文件的下一行(类似于 file.readline() ), 或在没有其它行时引发 StopIteration 异常
# file.truncate(size=file.tell()) 截取文件到最大 size 字节, 默认为当前文件位置
#
# 9.3文件属性
# 文件对象的属性 描述
# file.closed True 表示文件已经被关闭, 否则为 False
# file.encoding 文件所使用的编码 - 当 Unicode 字符串被写入数据时, 它们将自动使用 file.encoding 转换为字节字符串; 若 file.encoding 为 None 时使用系统默认编码
# file.mode 文件打开时使用的访问模式
# file.name 文件名
# file.newlines 未读取到行分隔符时为 None , 只有一种行分隔符时为一个字符串, 当文件有多种类型的行结束符时，则为一个包含所有当前所遇到的行结束符的列表
# file.softspace 为 0 表示在输出一数据后，要加上一个空格符，1 表示不加。这个属性一般程序员用不着，由程序内部使用。
#
# 9.4标准文件
# 一般说来, 只要你的程序一执行, 那么你就可以访问三个标准文件. 它们分别是标准输入(一
# 般是键盘), 标准输出(到显示器的缓冲输出)和标准错误(到屏幕的非缓冲输出). (这里所说的"缓冲
# "和"非缓冲"是指 open() 函数的第三个参数.) 这些文件沿用的是 C 语言中的命名, 分别为
# stdin , stdout 和 stderr . 我们说"只要你的程序一执行就可以访问这三个标准文件", 意思是这
# 些文件已经被预先打开了, 只要知道它们的文件句柄就可以随时访问这些文件.
# 可以用sys模块的sys.stdin , sys.stdout 和 sys.stderr 访问,
#
# # 9.5pickle 模块( marshal模块类似)
# # python的pickle模块实现了基本的数据序列和反序列化。
# # 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# # 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的python对象
# # pickle序列化写:
# #!/usr/bin/python3
# import pickle
# # 使用pickle模块将数据对象保存到文件
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
# output = open('data.pkl', 'wb')
# # Pickle dictionary using protocol 0. pickle.dump(obj, file, [,protocol])
# pickle.dump(data1, output)
# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)
# output.close()
# # pickle反序列化读：
# #!/usr/bin/python3
# import pprint, pickle
# #使用pickle模块从文件中重构python对象
# pkl_file = open('data.pkl', 'rb')
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
# pkl_file.close()
#
# 参考338页图形
# # 9.6dbm 在一些python小型应用程序中，不需要关系型数据库时，可以方便的用持久字典来存储名称/值对，它与python的字典非常类似，主要区别在于数据是在磁盘读取和写入的。另一个区别在于dbm的键和值必须是字符串类型。
# # 创建：
# import dbm
# db = dbm.open('Bookmark', 'c')
# #添加选项
# db['MyBlog'] = 'jonathanlife.sinaapp.com'
# print(db['MyBlog'])
# #保存，关闭
# db.close()
# # 访问:
# import dbm
# # open existing file
# db = dbm.open('websites', 'w')
# # add item
# db['first_data'] = 'Hello world'
# # verify the previous item remains
# if db['first_data'] != None:
#     print('the data exists')
# else:
#     print('Missing item')
# # iterate over the keys, may be slow
# for key in db.keys():
#     print("Key=", key, " value=", db[key])
# # delete item
# del db['first_data']
# # close and save to disk
# db.close()
# # 9.7 shelve
# import shelve
#
# s = shelve.open('test_shelf.db')
# try:
#     s['key1'] = {'int': 10, 'float':9.5, 'string':'Sample data'}
#     # print(s['key1'])
# finally:
#     s.close()
# import shelve
# s = shelve.open('test_shelf.db')
# print(s['key1'])
# s.close()
#
#
# 9.7os模块：文件系统
# os 和 os.path 模块提供了访问计算机文件系统的不同方法.
# 我们在本章学习的只是文件访问方面, 事实上 os 模块可以完成更多工作. 我们可以通过它管理进
# 程环境, 甚至可以让一个 Python 程序直接与另外一个执行中的程序"对话". 你很快就会发现自己
# 离不开这个模块了.
# 模块的文件 / 目录访问函数
# 函数 描述
# 文件处理
# mkfifo()/mknod() 创建命名管道/创建文件系统节点
# remove()/unlink() Delete file 删除文件
# rename()/renames() 重命名文件
# *stat() 返回文件信息
# symlink() 创建符号链接
# utime() 更新时间戳
# walk() 生成一个目录树下的所有文件名
# 目录/文件夹
# chdir()/fchdir() 改变当前工作目录/通过一个文件描述符改变当前工作目录
# chroot() 改变当前进程的根目录
# chflags 设置路径的标记为数字标记。
# listdir() 列出指定目录的文件
# getcwd()/getcwdu() 返回当前工作目录/功能相同, 但返回一个 Unicode 对象
# mkdir()/makedirs() 创建目录/创建多层目录
# rmdir()/removedirs() 删除目录/删除多层目录
# 访问/权限
# access() 检验权限模式
# chmod() 改变权限模式
# chown()/lchown() 改变 owner 和 group ID/功能相同, 但不会跟踪链接
# umask() 设置默认权限模式
# 文件描述符操作
# open() 底层的操作系统 open (对于文件, 使用标准的内建 open() 函数)
# read()/write() 根据文件描述符读取/写入数据
# dup()/dup2() 复制文件描述符号/功能相同, 但是是复制到另一个文件描述符设备号
# close(fd) 关闭文件描述符 fd
# closerange(fd_low, fd_high) 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
# makedev() 从 major 和 minor 设备号创建一个原始设备号
# major()/minor() 从原始设备号获得 major/minor 设备号
# os.path 模块中的路径名访问函数
# 函数 描述
# 分隔
# basename() 去掉目录路径, 返回文件名
# dirname() 去掉文件名, 返回目录路径
# join() 将分离的各部分组合成一个路径名
# split() 返回 (dirname(), basename()) 元组
# splitdrive() 返回 (drivename, pathname) 元组
# splitext() 返回 (filename, extension) 元组
# 信息
# getatime() 返回最近访问时间
# getctime() 返回文件创建时间
# getmtime() 返回最近文件修改时间
# getsize() 返回文件大小(以字节为单位)
# 查询
# exists() 指定路径(文件或目录)是否存在
# isabs() 指定路径是否为绝对路径
# isdir() 指定路径是否存在且为一个目录
# isfile() 指定路径是否存在且为一个文件
# islink() 指定路径是否存在且为一个符号链接
# ismount() 指定路径是否存在且为一个挂载点
# samefile() 两个路径名是否指向同个文件
#
# 9.8文件相关模块
# 模块 内容
# base64 提供二进制字符串和文本字符串间的编码/解码操作
# binascii 提供二进制和 ASCII 编码的二进制字符串间的编码/解码操作
# bz2a 访问 BZ2 格式的压缩文件
# csva 访问 csv 文件(逗号分隔文件)
# filecmpb 用于比较目录和文件
# # fileinput 提供多个文本文件的行迭代器,适合大文本.一次读取出来所有。
# import fileinput
# for line in fileinput.input('data.txt'):
#     print(line,)
# getopt/optparsea 提供了命令行参数的解析/处理
# glob/fnmatch 提供 Unix 样式的通配符匹配的功能
# gzip/zlib 读写 GNU zip( gzip) 文件(压缩需要 zlib 模块)
# shutil 提供高级文件访问功能
# c/StringIO 对字符串对象提供类文件接口
# tarfilea 读写 TAR 归档文件, 支持压缩文件
# tempfile 创建一个临时文件(名)
# uu 格式的编码和解码
# zipfilec 用于读取 ZIP 归档文件的工具
# mmap内存映射模块（大文本处理）
# codecs模块 编码解码
#
# # 9.9实例：
# # 1检索指定路径下后缀是 py 的所有文件
# #!/usr/bin/python3
# import os
# import os.path
# import sys
# #path = 'D:/UC/'
# ls = []
# name =3
# g = (1,2)
# print(sys.path)
# def getAppointFile(path,ls):
#     fileList = os.listdir(path)
#     # name + = 1 非引用型变量无法直接使用
#     # len(g) 元组可以使用
#     try:
#         for tmp in fileList:
#             pathTmp = os.path.join(path,tmp)
#             if True==os.path.isdir(pathTmp):
#                 getAppointFile(pathTmp,ls)
#             elif pathTmp[pathTmp.rfind('.')+1:].upper()=='PY':
#                 ls.append(pathTmp)
#     except PermissionError:
#         pass
# def main():
#     while True:
#         path = input('请输入路径:').strip()
#         if os.path.isdir(path) == True:
#             break
#     getAppointFile(path, ls)
#     print(ls)
#     print(len(ls))
# main()
# # 2显示所有视频格式文件，mp4，avi，rmvb
# import os
# def search_file(start_dir, target):
#     os.chdir(start_dir)
#
#     for each_file in os.listdir(os.curdir):
#         ext = os.path.splitext(each_file)[1]
#         if ext in target:
#             vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
# start_dir = input('请输入待查找的初始目录：')
# program_dir = os.getcwd()
# target = ['.mp4', '.avi', '.rmvb']
# vedio_list = []
# search_file(start_dir, target)
# f = open(program_dir + os.sep + 'vedioList.txt', 'w')
# f.writelines(vedio_list)
# f.close()
# # 3获取文件后缀
# def getfile_fix(filename):
#     return filename[filename.rfind('.') + 1:]
# print(getfile_fix('runoob.txt'))

#
#
# # std6.1 os.path
# import os.path
# FILENAMES = [ __file__,
# os.path.dirname(__file__),
# '/',
# './broken_link',
# ]
# for file in FILENAMES:
#     print('File :', file)
#     print('Absolute :', os.path.isabs(file))
#     print('Is File? :', os.path.isfile(file))
#     print('Is Dir? :', os.path.isdir(file))
#     print('Is Link? :', os.path.islink(file))
#     print('Mountpoint? :', os.path.ismount(file))
#     print('Exists? :', os.path.exists(file))
#     print('Link Exists?:', os.path.lexists(file))
#     print()
#
# # std6.2 遍历文件夹
# import os
# import os.path
# import pprint
# def visit(arg, dirname, names):
#     print(dirname, arg)
#     for name in names:
#         subname = os.path.join(dirname, name)
#         if os.path.isdir(subname):
#             print(' % s /' % name)
#         else:
#             print(' % s' % name)
#     print()
# if not os.path.exists('example'):
#     os.mkdir('example')
# if not os.path.exists('example/one'):
#     os.mkdir('example/one')
# with open('example/one/file.txt', 'wt') as f:
#     f.write('contents')
# with open('example/two.txt', 'wt') as f:
#     f.write('contents')
# for root, dirs, files in os.walk('example', visit, '(User data)'):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))
# # glob()文件路径搜索返回路径list
# import glob
# for name in glob.glob('example/*'):
#     print('example/* ',name)
# # ?通配符
# for name in glob.glob('example/one/fil?.txt'):
#     print('example/one/fil?.txt ',name)
# # 正则表达式
# for name in glob.glob('example/one/*[0-9].*'):
#     print('example/one/*[0-9].* ',name)
#
# # std6.3 linecache模块 —Read Text Files Efficiently
# import os
# import tempfile
# lorem = '''Lorem ipsum dolor sit amet, consectetuer
# adipiscing elit. Vivamus eget elit. In posuere mi non
# risus. Mauris id quam posuere lectus sollicitudin
# varius. Praesent at mi. Nunc eu velit. Sed augue massa,
# fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur
# eros pede, egestas at, ultricies ac, apellentesque eu,
# tellus.
# Sed sed odio sed mi luctus mollis. Integer et nulla ac augue
# convallis accumsan. Ut felis. Donec lectus sapien, elementum
# nec, condimentum ac, interdum non, tellus. Aenean viverra,
# mauris vehicula semper porttitor, ipsum odio consectetuer
# lorem, ac imperdiet eros odio a sapien. Nulla mauris tellus,
# aliquam non, egestas a, nonummy et, erat. Vivamus sagittis
# porttitor eros.'''
# def make_tempfile():
#     fd, temp_file_name = tempfile.mkstemp()  #新建临时文件
#     os.close(fd)
#     f = open(temp_file_name, 'wt')
#     try:
#         f.write(lorem)
#     finally:
#         f.close()
#     return temp_file_name
# def cleanup(filename):
#     os.unlink(filename)  #用于删除文件,如果文件是一个目录则返回一个错误。
# import linecache
# filename = make_tempfile()
# # Pick out the same line from source and cache.
# # (Notice that linecache counts from 1)
# print('SOURCE:')
# print('%r' % lorem.split('\n')[4])
# print()
# print('CACHE:')
# print('%r' % linecache.getline(filename, 5))  # 获取该文件第五行.
# cleanup(filename)
#
# # std6.4 tempfile—Temporary File System Objects
# import os
# import tempfile
# print('Building a filename with PID:')
# filename = 'guess_my_name.%s.txt' % os.getpid()
# temp = open(filename, 'w+b')
# try:
#     print('temp:')
#     print(' ', temp)
#     print('temp.name:')
#     print(' ', temp.name)  #guess_my_name.8304.txt
# finally:
#     temp.close()
#     # Clean up the temporary file yourself
#     os.remove(filename)
# print()
# print('TemporaryFile:')
# temp = tempfile.TemporaryFile()
# try:
#     print('temp:')
#     print(' ', temp)
#     print('temp.name:')
#     print(' ', temp.name)  #C:\Users\ADMINI~1\AppData\Local\Temp\tmpjbsqeenr
# finally:
#     # Automatically cleans up the file
#     temp.close()
# # NamedTemporaryFile
# import tempfile
# with tempfile.NamedTemporaryFile(
# suffix='_suffix', prefix='prefix_', dir='example',
# ) as temp:
#     print('temp:')
#     print(' ', temp)
#     print('temp.name:')
#     print(' ', temp.name)
# # tempFile location
# import tempfile
# print('gettempdir():', tempfile.gettempdir())
# print('gettempprefix():', tempfile.gettempprefix())
#

# std6.5 shutil 是高级的文件，文件夹，压缩包处理模块。
# # 1 将文件内容拷贝到另一个文件中
# import shutil
# shutil.copyfileobj(open('old.xml', 'r'), open('new.xml', 'w'))
#
# shutil.make_archive(base_name, format,...) 创建压缩包并返回文件路径
# shutil.copyfile(src, dst)拷贝文件
# shutil.copymode(src, dst)仅拷贝权限。内容、组、用户均不变
# shutil.copystat(src, dst)仅拷贝状态的信息，包括：mode bits, atime, mtime, flags
# shutil.copy(src, dst)拷贝文件和权限
# shutil.copy2(src, dst)拷贝文件和状态信息
# shutil.ignore_patterns(*patterns)
# shutil.copytree(src, dst, symlinks=False, ignore=None)递归的去拷贝文件夹
# shutil.rmtree(path[, ignore_errors[, onerror]])递归的去删除文件
# shutil.move(src, dst)递归的去移动文件，它类似mv命令，其实就是重命名。
#


# pdf
# 1
# from PyPDF2.pdf import PdfFileReader
# from PyPDF2.pdf import PdfFileWriter
# import pymysql
# import os
# import os.path
# from time import strftime,strptime
#
# def sqlupdate(sql):
#         conn = pymysql.connect(host="xxx.xxx.xx.xxx",port=3306,user="***",password="***",database="db_name")
#         cur=conn.cursor()
#         cur.execute(sql)
#         conn.commit()
#         conn.close()
#
# def getDataUsingPyPdf2(filename):
#     pdf = PdfFileReader(open(filename, "rb"))
#     # out = PdfFileWriter(open(filename, "w"))
#     content = ""
#     for i in range(0, pdf.getNumPages()):
#         extractedText = pdf.getPage(i).extractText()
#         content +=  extractedText + "\n"
#     #return content.encode("ascii", "ignore")
#     return content
#
#
# def removeBlankFromList(list_old):
#     list_new = []
#     for i in list_old:
#         if i != '':
#             list_new.append(i)
#     return list_new
#
#
# if __name__ == '__main__':
#     rootdir = '/root/'
#     for dirpath,dirnames,filenames in os.walk(rootdir):
#         filedir = dirpath.split('/')[-1]
#         for filename in filenames:
#             filename = filename
#             filename_long = dirpath+'/'+filename
#             outputString = getDataUsingPyPdf2(filename_long)
#             #outputString = getDataUsingPyPdf2("/root/a.pdf")
#             outputString = outputString.split('\n')
#             outputString_new = removeBlankFromList(outputString)
#             outputString = outputString_new
#             try:
#                 rectime = strftime('%Y-%m-%d %H:%M:%S',strptime(outputString[1].rstrip(' '), "%a %b %d %Y %H:%M:%S"))
#             except:
#                 rectime = strftime('%Y-%m-%d %H:%M:%S',strptime(outputString[-1].rstrip(' '), "%a %b %d %Y %H:%M:%S"))
#             pn = outputString[0].split()
#             if len(pn) > 1:
#                 sn = pn[1]
#             else:
#                 sn = ''
#             pn = pn[0].strip()
#             #print('[%s],[%s],[%s]' % (pn,topbut,rectime))
#             sql = "insert into tb_1(pn,sn,rectime,dir,filename) values ('%s','%s','%s','%s','%s')" % (pn,sn,rectime,filedir,filename)
#             print('sql=[%s]' % sql)
#             sqlupdate(sql)
#             print('done')
#     #print(getDataUsingPyPdf2("/root/a.pdf"))
#
# # 2 pdf读fn)写
# from PyPDF2 import PdfFileReader, PdfFileWriter
# readFile = 'read.pdf'
# writeFile = 'write.pdf'
# # 获取一个 PdfFileReader 对象
# pdfReader = PdfFileReader(open(readFile, 'rb'))
# # 获取 PDF 的页数
# pageCount = pdfReader.getNumPages()
# print(pageCount)
# # 返回一个 PageObject
# page = pdfReader.getPage(1)
# # 获取一个 PdfFileWriter 对象
# pdfWriter = PdfFileWriter()
# # 将一个 PageObject 加入到 PdfFileWriter 中
# pdfWriter.addPage(page)
# # 输出到文件中
# pdfWriter.write(open(writeFile, 'wb'))
# # 3 pdf合并分割
# from PyPDF2 import PdfFileReader, PdfFileWriter
# def split_pdf(infn, outfn):
#     pdf_output = PdfFileWriter()
#     pdf_input = PdfFileReader(open(infn, 'rb'))
#     # 获取 pdf 共用多少页
#     page_count = pdf_input.getNumPages()
#     print(page_count)
#     # 将 pdf 第五页之后的页面，输出到一个新的文件
#     for i in range(5, page_count):
#         pdf_output.addPage(pdf_input.getPage(i))
#     pdf_output.write(open(outfn, 'wb'))
# def merge_pdf(infnList, outfn):
#     pdf_output = PdfFileWriter()
#     for infn in infnList:
#         pdf_input = PdfFileReader(open(infn, 'rb'))
#         # 获取 pdf 共用多少页
#         page_count = pdf_input.getNumPages()
#         print(page_count)
#         for i in range(page_count):
#             pdf_output.addPage(pdf_input.getPage(i))
#     pdf_output.write(open(outfn, 'wb'))
# if __name__ == '__main__':
#     infn = 'infn.pdf'
#     outfn = 'outfn.pdf'
#     split_pdf(infn, out


# # std7.4 csv
# import csv
# import sys
# with open(sys.argv[1], 'rt') as f:  #Sys.argv[]是用来获取命令行参数的 参考文档
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#
# # 2写入
# import csv
# import sys
# with open(sys.argv[1], 'wt') as f:
#     writer = csv.writer(f)
#     writer.writerow( ('Title 1', 'Title 2', 'Title 3') )
#     for i in range(3):
#         writer.writerow( (i+1,
#         chr(ord('a') + i),
#         '08/%02d/07' % (i+1),
#         )
#         )
# print(open(sys.argv[1], 'rt').read())
#
#