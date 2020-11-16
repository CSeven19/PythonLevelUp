# GUI
#
# 19.1GUI开发基本流程
# 1. 导入 Tkinter 模块（import Tkinter，或者，from Tkinter import *)。
# 2. 创建一个顶层窗口对象，来容纳您的整个 GUI 程序,并设置好top属性。
# 3. 在您的顶层窗口对象上（或者说在“其中”）创建所有的 GUI 模块（以及功能）。
# 4. 把这些 GUI 模块与底层程序代码相连接。
# 5. 进入主事件循环。
#
# 19.2Tk 组件
# 组件 描述
# Button 按钮。类似标签，但提供额外的功能，例如鼠标掠过、按下、释放以及键盘操作/事件
# Canvas 画布。提供绘图功能（直线、椭圆、多边形、矩形）；可以包含图形或位图
# Checkbutton 选择按钮。一组方框，可以选择其中的任意个（类似 HTML 中的 checkbox）
# Entry 文本框。单行文字域，用来收集键盘输入（类似 HTML 中的 text）
# Frame 框架。包含其他组件的纯容器
# Label 标签。用来显示文字或图片
# Listbox 列表框。一个选项列表，用户可以从中选择
# Menu 菜单。点下菜单按钮后弹出的一个选项列表，用户可以从中选择
# Menubutton 菜单按钮。用来包含菜单的组件（有下拉式、层叠式等等）
# Message 消息框。类似于标签，但可以显示多行文本
# Radiobutton 单选按钮。一组按钮，其中只有一个可被“按下”（类似 HTML 中的 radio）
# Scale 进度条。线性“滑块”组件，可设定起始值和结束值，会显示当前位置的精确值
# Scrollbar 滚动条。对其支持的组件（文本域、画布、列表框、文本框）提供滚动功能
# Text 文本域。多行文字区域，可用来收集（或显示）用户输入的文字（类似 HTML中的 textarea）
# Toplevel 顶级。类似框架，但提供一个独立的窗口容器。
# # 实例1:
# #!/usr/bin/env python
#
# import tkinter
#
# # 顶层窗口
# top = tkinter.Tk()
# top.geometry('250x150')
# # label
# label = tkinter.Label(top, text='Hello World!')
# label.pack()
# # button
# quit = tkinter.Button(top, text='Hello World!',command=top.quit)
# quit.pack()
# # button2
# quit = tkinter.Button(top, text='QUIT',command=top.quit, bg='red', fg='white')
# quit.pack(fill=tkinter.X, expand=1)
# # 进入消息循环
# tkinter.mainloop()
#
# # 19.3布局grid
# import tkinter as tk
#
# root = tk.Tk()
#
# label1 = tk.Label(root, text = "Height:")
# label1.grid(row = 0, column = 0)
# label2 = tk.Label(root, text = "Width:")
# label2.grid(row = 1, column = 0)
#
# entry1 = tk.Entry(root)
# entry1.grid(row = 0, column = 1)
# entry2 = tk.Entry(root)
# entry2.grid(row = 1, column = 1)
#
# checkbutton = tk.Checkbutton(root, text = "Preserve aspect")
# checkbutton.grid(row = 2, column = 0, rowspan = 1, columnspan = 2, sticky=tk.W)#sticky设置控件的对其方位，这里设置为靠西(左西右东)
#
# img = tk.PhotoImage(file = "image_test.png")
# imageview = tk.Label(root, image= img)
# imageview.grid(row = 0, column = 2, rowspan = 2, columnspan = 2)
#
# button1 = tk.Button(root, text = "Zoom in")
# button1.grid(row = 2, column = 2)
# button1 = tk.Button(root, text = "Zoom out")
# button1.grid(row = 2, column = 3)
#
# root.mainloop()
#
# # 19.4gui+PFA
# #!/usr/bin/env python
#
# from functools import partial as pto
# import tkinter
# import tkinter.messagebox
#
# # 1准备
# WARN = 'warn'
# CRIT = 'crit'
# REGU = 'regu'
#
# SIGNS = {
#     'do not enter': CRIT,
#     'railroad crossing': WARN,
#     '55\nspeed limit': REGU,
#     'wrong way': CRIT,
#     'merging traffic': WARN,
#     'one way': REGU,
# }
#
# critCB = lambda: tkinter.messagebox.askokcancel('Error', 'Error Button Pressed!')
# warnCB = lambda: tkinter.messagebox.askokcancel('Warning','Warning Button Pressed!')
# infoCB = lambda: tkinter.messagebox.askokcancel('Info', 'Info Button Pressed!')
#
# # 2设置top
# top = tkinter.Tk()
# top.geometry('250x350')
# top.title('Road Signs')
# tkinter.Button(top, text='QUIT', command=top.quit,bg='red', fg='white').pack()
#
# # 3设置几种button类型,pto()偏函数
# MyButton = pto(tkinter.Button, top)  # 等价于tkinter.Button(top,...)
# CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
# WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
# ReguButton = pto(MyButton, command=infoCB, bg='white')
#
# # 4放入top
# for eachSign in SIGNS:
#     signType = SIGNS[eachSign]
#     cmd = '%sButton(text=%r%s).pack(fill=tkinter.X, expand=True)' % (signType.title(), eachSign,'.upper()' if signType == CRIT else '.title()')
#     eval(cmd)
#
# # 5执行
# top.mainloop()
#
# # 19.5复杂案例:文件选择器
# #!/usr/bin/env python
#
# import os
# from time import sleep
# from tkinter import *
#
# # 1类定义完整的gui结构
# class DirList(object):
#     def __init__(self, initdir=None):
#         self.top = Tk()
#         self.label = Label(self.top,text = 'Directory Lister v1.1')
#         self.label.pack()
#         self.cwd = StringVar(self.top)
#         self.dirl = Label(self.top, fg='blue',
#         font = ('Helvetica', 12, 'bold'))
#         self.dirl.pack()
#         self.dirfm = Frame(self.top)
#         self.dirsb = Scrollbar(self.dirfm)
#         self.dirsb.pack(side=RIGHT, fill=Y)
#         self.dirs = Listbox(self.dirfm, height=15,width = 50, yscrollcommand = self.dirsb.set)
#         self.dirs.bind('<Double-1>', self.setDirAndGo)
#         self.dirsb.config(command=self.dirs.yview)
#         self.dirs.pack(side=LEFT, fill=BOTH)
#         self.dirfm.pack()
#         self.dirn = Entry(self.top, width=50,textvariable = self.cwd)
#         self.dirn.bind('<Return>', self.doLS)
#         self.dirn.pack()
#         self.bfm = Frame(self.top)
#         self.clr = Button(self.bfm, text='Clear',command = self.clrDir,activeforeground = 'white',activebackground = 'blue')
#         self.ls = Button(self.bfm,text = 'List Directory',command = self.doLS,activeforeground = 'white',activebackground = 'green')
#         self.quit = Button(self.bfm, text='Quit',command = self.top.quit,activeforeground='white',activebackground='red')
#         self.clr.pack(side=LEFT)
#         self.ls.pack(side=LEFT)
#         self.quit.pack(side=LEFT)
#         self.bfm.pack()
#
#         if initdir:
#             self.cwd.set(os.curdir)
#             self.doLS()
# # 2定义相关响应方法
#     def clrDir(self, ev=None):
#         self.cwd.set('')
#
#     def setDirAndGo(self, ev=None):
#         self.last = self.cwd.get()
#         self.dirs.config(selectbackground='red')
#         check = self.dirs.get(self.dirs.curselection())
#         if not check:
#             check = os.curdir
#         self.cwd.set(check)
#         self.doLS()
#
#     def doLS(self, ev=None):
#         error = ''
#         tdir = self.cwd.get()
#         if not tdir: tdir = os.curdir
#         if not os.path.exists(tdir):
#             error = tdir + ': no such file'
#         elif not os.path.isdir(tdir):
#             error = tdir + ': not a directory'
#         if error:
#             self.cwd.set(error)
#             self.top.update()
#             sleep(2)
#             if not (hasattr(self, 'last') and self.last):
#                 self.last = os.curdir
#                 self.cwd.set(self.last)
#                 self.dirs.config(\
#                 selectbackground='LightSkyBlue')
#                 self.top.update()
#                 return
#
#         self.cwd.set('FETCHING DIRECTORY CONTENTS...')
#         self.top.update()
#         dirlist = os.listdir(tdir)
#         dirlist.sort()
#         os.chdir(tdir)
#         self.dirl.config(text=os.getcwd())
#         self.dirs.delete(0, END)
#         self.dirs.insert(END, os.curdir)
#         self.dirs.insert(END, os.pardir)
#         for eachFile in dirlist:
#             self.dirs.insert(END, eachFile)
#             self.cwd.set(os.curdir)
#             self.dirs.config(selectbackground='LightSkyBlue')
# # 3执行
# def main():
#     d = DirList(os.curdir)
#     mainloop()
#
# if __name__ == '__main__':
#     main()
#
# 19.6相关模块
# GUI 模块或系统 描述
# Tk 相关模块
# Tkinter TK INTERface: Python 的默认 GUI 工具集http://wiki.python.org/moin/TkInter
# Pmw Python MegaWidgets （Tkinter 扩展）http://pmw.sf.net
# Tix Tk Interface eXtension （Tk 扩展）http://tix.sf.net
# TkZinc (Zinc) Extended Tk canvas type （Tk 扩展）http://www.tkzinc.org
# EasyGUI (easygui) 非常简单的非事件驱动 GUI （Tkinter 扩展）http://ferg.org/easygui
# TIDE + (IDE Studio) Tix 集成开发环境（包括 IDE Studio, 一个 Tix 加强版的标准 IDLE IDE)http://starship.python.net/crew/mike
# wxWidgets 相关模块
# wxPython Python对 wxWidgets的绑定，一个跨平台的 GUI框架库（早期称为 wxWindows）http://wxpython.org
# Boa Constructor Python 集成开发环境兼 wxPython GUI 构造工具http://boa-constructor.sf.net
# PythonCard 基于 wxPython 的 GUI 桌面应用程序工具集（从 HyperCard 获得灵感）http://pythoncard.sf.net
# wxGlade 另一个 wxPython GUI 设计工具 （从 Glade（GTK+/GNOME 的 GUI 构建工具）受到启发）http://wxglade.sf.net
# GTK+/GNOME 相关模块
# PyGTK Python 对 GIMP 工具集(GTK+)的封装库 http://pygtk.org
# GNOME-Python Python 对 GNOME 桌面开发库的绑定http://gnome.org/start/unstable/bindings http://download.gnome.org/sources/gnome-python
# Glade 一个针对 GTK+和 GNOME 的 GUI 构建工具http://glade.gnome.org
# PyGUI (GUI) “Pythonic”式的跨平台 GUI 程序编程接口（MacOS X 中基于 Cocoa，POSIX/X11 和 Win32 中 基 于 GTK+ ）
# http://www.cosc.canterbury.ac.nz/~greg/python_gui
# Qt/KDE 相关模块
# PyQt Trolltech 开发的 Python 对 Qt GUI/XML/SQL 工具集的绑定(双协议，部分开源) http://riverbankcomputing.co.uk/pyqt
# PyKDE Python 对 KDE 桌面环境的绑定http://riverbankcomputing.co.uk/pykde
# eric Python 使用 QScintilla editor 组件编写的 PyQt 集成开发环境http://die-offenbachs.de/detlev/eric3 http://ericide.python-hosting.com/
# PyQtGPL 包括 Qt（Win32 Cygwin 移植版）、Sip、QScintilla 和 PyQt 的工具包http://pythonqt.vanrietpaap.nl
# 其他开源 GUI 工具集
# FXPy Python 对 FOX 工具集的绑定 （http://fox-toolkit.org）http://fxpy.sf.net
# pyFLTK (fltk) Python 对 FLTK 工具集的绑定 （http://fltk.org）http://pyfltk.sf.net
# PyOpenGL (OpenGL) Python 对 OpenGL 的绑定 （http://opengl.org）http://pyopengl.sf.net
# GUI 模块或系统 描述
# 商业软件
# win32ui Python 版的 Microsoft MFC (基于 Python 的 Windows 扩展)http://starship.python.net/crew/mhammond/win32
# swing Python 版的 Sun Microsystems Java/Swing (基于 Jython)http://jython.org
