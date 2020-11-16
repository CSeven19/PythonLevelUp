# 网络编程
#
# 16.1socket()模块套接字
# s.bind() 绑定地址（主机，端口号对）到套接字
# s.listen() 开始 TCP 监听
# s.accept() 被动接受 TCP 客户的连接，（阻塞式）等待连接的到来
# 客户端套接字函数
# s.connect() 主动初始化 TCP 服务器连接
# s.connect_ex() connect()函数的扩展版本，出错时返回出错码，而不是抛异常
# 公共用途的套接字函数
# s.recv() 接收 TCP 数据
# s.send() 发送 TCP 数据
# s.sendall() 完整发送 TCP 数据
# s.recvfrom() 接收 UDP 数据
# s.sendto() 发送 UDP 数据
# s.getpeername() 连接到当前套接字的远端的地址
# s.getsockname() 当前套接字的地址
# s.getsockopt() 返回指定套接字的参数
# s.setsockopt() 设置指定套接字的参数
# s.close() 关闭套接字
# s.setblocking() 设置套接字的阻塞与非阻塞模式
# s.settimeout()a 设置阻塞套接字操作的超时时间
# s.gettimeout()a 得到阻塞套接字操作的超时时间
# 面向文件的套接字的函数
# s.fileno() 套接字的文件描述符
# s.makefile() 创建一个与该套接字关连的文件
# udp实例参考核心3
# tcp实例参考核心3
# 创建线程来处理客户的请求。
#
# 16.2 套接字属性
# 属性名字 描述
# 数据属性
# AF_UNIX, AF_INET, AF_INET6 Python 支持的套接字家族
# SO_STREAM, SO_DGRAM 套接字类型 (TCP = 流, UDP = 数据报)
# has_ipv6 表示是否支持 IPv6 的标志变量
# 异常
# error 套接字相关错误
# herror 主机和地址相关的错误
# gaierror 地址相关的错误
# timeout 超时
# 函数
# socket() 用指定的地址家族，套接字类型和协议类型（可选）创建一个套接字对象
# socketpair() 用指定的地址家族，套接字类型和协议类型（可选）创建一对套接字对象
# fromfd() 用一个已经打开的文件描述符创建一个套接字对象
# 数据属性
# ssl() 在套接字初始化一个安全套接字层(SSL)。不做证书验证。
# getaddrinfo() 得到地址信息
# getfqdn() 返回完整的域的名字
# gethostname() 得到当前主机名
# gethostbyname()由主机名得到对应的ip地址
# gethostbyname_ex()gethostbyname()的扩展版本，返回主机名，主机所有的别名和IP地址列表。
# gethostbyaddr() 由IP地址得到DNS信息，返回一个类似gethostbyname_ex()的3元组。
# getprotobyname()由协议名（如'tcp'）得到对应的号码。
# getservbyname() /getservbyport()  由服务名得到对应的端口号或相反,两个函数中，协议名都是可选的。
# ntohl() / ntohs()把一个整数由网络字节序转为主机字节序
# htonl() / htons()把一个整数由主机字节序转为网络字节序
# inet_aton() / inet_ntoa() 把IP地址转为32位整型，以及反向函数。（仅对IPv4地址有效）
# inet_pton() / inet_ntop() 把IP地址转为二进制格式以及反向函数。（仅对IPv4地址有效）
# getdefaulttimeout() /setdefaulttimeout() 得到／设置默认的套接字超时时间，单位秒（浮点数）
#
# 16.3  *SocketServer 模块
# SocketServer 是标准库中一个高级别的模块。用于简化网络客户与服务器的实现。
# SocketServer 模块的类
# 类 描述
# BaseServer 包含服务器的核心功能与混合(mix-in)类的钩子功能。这个类用于派生，不要直接生成这个类的类对象，可以考虑使用 TCPServer 和 UDPServer。
# TCPServer/ UDPServer基本的网络同步 TCP/UDP 服务器
# UnixStreamServer/ UnixDatagramServer 基本的基于文件同步 TCP/UDP 服务器
# ForkingMixIn/ 实现了核心的进程化或线程化的功能，用于与服务器类进行混合(mix-in)，以提供一些异步特性。
# ThreadingMixIn 不要直接生成这个类的对象
# ForkingTCPServer/ForkingUDPServer ForkingMixIn 和 TCPServer/UDPServer 的组合
# ThreadingTCPServer/ThreadingUDPServer ThreadingMixIn 和 TCPServer/UDPServer 的组合
# BaseRequestHandler 包含处理服务请求的核心功能。只用于派生新的类，不要直接生成这个类的对象，可以考虑使用 StreamRequestHandler 或 DatagramRequestHandler
# StreamRequestHandler/DatagramRequestHandler TCP/UDP服务器的请求处理类的一个实现
# # SocketServer服务器
# #!/usr/bin/env python
#
# from SocketServer import (TCPServer as TCP,StreamRequestHandler as SRH)
# from time import ctime
#
# HOST = ''
# PORT = 21567
# ADDR = (HOST, PORT)
#
# class MyRequestHandler(SRH):
#     def handle(self):
#         print('...connected from:', self.client_address)
#         self.wfile.write('[%s] %s' % (ctime(),
#         self.rfile.readline()))
# tcpServ = TCP(ADDR, MyRequestHandler)
# print('waiting for connection...')
# tcpServ.serve_forever()
# # SocketServer客服端
#
# #coding=UTF-8
# from socket import *
# import sys
# sys.setdefaultencoding('utf8')
#
# HOST = '192.168.1.27'
# PORT = 1234
# BUFSIZE = 1024
# ADDR = (HOST, PORT)
#
# while True:
#     tcpCliSock = socket(AF_INET, SOCK_STREAM)
#     tcpCliSock.connect(ADDR)
#     data = input('>')
#     if not data:
#         break
#     tcpCliSock.send('%s\r\n' % data.encode("UTF-8"))
#     data = tcpCliSock.recv(BUFSIZE).decode("UTF-8")
#     if not data:
#         break
#     print(data.strip())
#     tcpCliSock.close()
#
# 16.4 Twisted 框架
# 16.5 select模块 非阻塞式i/o编程 参考文档
# 16.6 socketserver模块(侧重服务端，客服端可继续使用socket),将socket模块和select模块进行了封装，从而创建了一些基类供人使用,可以提供多连接.
# 16.7 asyncore模块 提供了以异步的方式写入套接字服务的客户端和服务器的基础结构。
# 16.8 asynchat模块 建立在 asyncore 基础结构上，简化了异步客户端和服务器，使得处理带有以任意字符串终止或者可变长度的元素的协议更加容易。
