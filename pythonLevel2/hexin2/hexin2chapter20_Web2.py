# web开发
#
# 20.1 url
# urllib是基于http的高层库，它有以下三个主要功能：
# （1）request处理客户端的请求
# （2）response处理服务端的响应
# （3）parse会解析url
# 参看菜鸟cgi图形
# urlparse功能 描述
# urlparse(urlstr,defProtSch=None,allowFrag=None) 将 urlstr 解析成各个部件，如果在 rulstr 中没有给定协议或者规划将使用 defProtSch；allowFrag决定是否允许有 URL零部件。
# urlunparse(urltup) 将 URL数据(urltup)的一个元组反解析成一个 URL字符串。
# urljoin(baseurl,newurl, allowFrag =None) 将 URL 的基部件 baseurl 和 newurl 拼合成一个完整的 URL；allowFrag 的作用和 urlpase()中相同。
#
# 20.2 urllib 模块
# # 1 urllib.request.urlopen()
# urlopen() 打开一个给定 URL 字符串与 Web 连接，并返回了文件类的对象
# f = urllib.request.urlopen() File-like Object Methods
# urlopen()对象方法 描述
# f.read([bytes]) 从 f 中读出所有或 bytes 个字节
# f.readline() 从 f 中读出一行
# f.readlines() 从 f 中读出所有行并返回一个列表
# f.close() 关闭 f 的 URL 的连接
# f.fileno() 返回 f 的文件句柄
# f.info() 获得 f 的 MIME 头文件
# f.geturl() 返回 f 所打开的真正的 URL
# # python文件写入也可以进行网站爬虫
# from urllib import request
# response = request.urlopen("http://www.baidu.com/") # 打开网站
# print(request.urlparse("http://www.baidu.com/"))
# fi = open("project.txt", 'w')                        # open一个txt文件
# line = response.readline()
# print("line",line)
# page = fi.write(str(response.read()))
# # 网站代码写入
# fi.close()                                           # 关闭txt文件
#
# # 2 urlretrieve(urlstr, localfile=None, downloadStatusHook=None)
# # urlretrieve()可以方便地将 urlstr 定位到的整个HTML 文件下载到你本地的硬盘上。urlretrieve()返回一个 2-元组，(filename, mime_hdrs)
# import urllib
# from urllib import request
# import os
# def reporthook(blocks_read, block_size, total_size):
#     """total_size is reported in bytes.
#     block_size is the amount read each time.
#     blocks_read is the number of blocks successfully read.
#     """
#     if not blocks_read:
#         print('Connection opened')
#         return
#     if total_size < 0:
#         # Unknown size
#         print('Read %d blocks (%d bytes)' % (blocks_read,blocks_read * block_size))
#     else:
#         amount_read = blocks_read * block_size
#         print('Read %d blocks, or %d/%d' % (blocks_read, amount_read, total_size))
#     return
# try:
#     filename, msg = urllib.request.urlretrieve(
#     'http://blog.csdn.net/xhw88398569/article/details/49179967',
#     reporthook=reporthook)  #html另存为磁盘上.
#     print()
#     print('File:', filename)
#     print('Headers:')
#     print(msg)
#     print('File exists before cleanup:', os.path.exists(filename))
# finally:
#     urllib.request.urlcleanup()  #清除由于urllib.urlretrieve()所产生的缓存
#     print('File still exists:', os.path.exists(filename))
#
# # 3 urllib.quote() and urllib.quote_plus() urllib.unquote() 和 urllib.unquote_plus()
# # quote*()函数获取 URL 数据，并将其编码,unquote()解码
# from urllib import parse
# name = 'joe mama'
# number = 6
# base = 'http://www/~foo/cgi-bin/s.py'
# final = '%s?name=%s&num=%d' % (base, name, number)
# print(final)
# final1 = parse.quote(final)
# final2 = parse.quote_plus(final)
# print(final1)
# print(final2)
# unfinal1 = parse.unquote(final1)
# unfinal2 = parse.unquote_plus(final2)
# print(unfinal1)
# print(unfinal2)
# # 4 urllib.urlencode()
# # 函数接收字典的键-值对，并将其编译成 CGI 请求的 URL 字符串的一部分
# from urllib import parse
# aDict = { 'name': 'Georgina Garcia', 'hmdir': '~ggarcia' }
# print(parse.urlencode(aDict))

# # 5 pathname2url, url2pathname
# import os
# from urllib.request import pathname2url, url2pathname
# print('== Default ==')
# path =('/a/b/c')
# print('Original:', path)
# print('URL :', pathname2url(path))
# print('Path :', url2pathname('/d/e/f'))
#
# # 6 urllib.request.Request() urlopen()提升版
# import urllib
# request = urllib.request.Request('http://localhost/')  #自定义发送请求详细
# request.add_header(
# 'User-agent',
# 'PyMOTW (http://www.doughellmann.com/PyMOTW/)',
# )
# response = urllib.request.urlopen(request)
# data = response.read()  #返回当前网页源码
# print(data)

# # 7 post
# import urllib
# from urllib import request
# from urllib import parse
# query_args = { 'q':'query string', 'foo':'bar' }
# # request = urllib.request.Request('http://localhost:8080/')
# request = urllib.request.Request(url='http://localhost',
#                      data=parse.urlencode(query_args).encode(encoding="utf-8"))  #post请求
# print('Request method before data:', request.get_method())
# # request.data(parse.urlencode(query_args))
# print('Request method after data :', request.get_method())
# 'User-agent',
# 'PyMOTW (http://www.doughellmann.com/PyMOTW/)',
# )
# print()
# print('OUTGOING DATA:')
# print(request.data)
# print()
# print('SERVER RESPONSE:')
# print(urllib.request.urlopen(request).read())

# # 8 上传文件
# import requests
#
# url = 'http://www.test.com/doFile.php'
# # url = 'http://www.test.com/doPost.php'
# # files = {'file': open('D:/tmp/1.jpg', 'rb')}
#
# # 要上传的文件
# files = {'file123': ('1.jpg', open('D:/tmp/1.jpg', 'rb'))
#          }  # 显式的设置文件名
#
# # post携带的数据
# data = {'a': '杨', 'b': 'hello'}
#
# r = requests.post(url, files=files, data=data)
# print(r.text)
#


# # 20.3 urllib2 模块(已合并入urllib)
# # urllib2 可以处理更复杂 URL 的打开问题。
# # 一个例子就是有基本认证（登录名和密码）需求的 Web 站点。
# # 实例:
# #!/usr/bin/env python
#
# import urllib.request
#
# LOGIN = 'AB_demo007_t01'.encode(encoding="utf-8")
# PASSWD = "test".encode(encoding="utf-8")
# URL = 'http://localhost'
#
# def handler_version(url):
#     from urllib import parse
#     hdlr = urllib.request.HTTPBasicAuthHandler()
#     hdlr.add_password('Archives', parse.unquote_plus(url)[1], LOGIN, PASSWD)
#     opener = urllib.request.build_opener(hdlr)
#     urllib.request.install_opener(opener)
#     return url
#
# def request_version(url):
#     import base64
#     req = urllib.request.Request(url)
#     b64str = base64.b64encode('%s:%s'.encode(encoding="utf-8") % (LOGIN, PASSWD))[:-1]
#     req.add_header("Authorization", "Basic %s" % b64str)
#     return req
#
# for funcType in ('handler', 'request'):
#     print('*** Using %s:' % funcType.upper())
#     # url = handler_version(URL)
#     # request_version(URL)
#     url = eval('%s_version' % funcType)(URL)
#     f = urllib.request.urlopen(url)
#     print(f.readline())
#     f.close()
#
# 20.4 cgi
#
# 20.5 相关模块
# 模块/包 描述
# Web 应用程序
# cgi 从标准网关接口（CGI）获取数据
# cgitbc 处理 CGI 返回数据
# htmllib 解析 HTML 文件时用的旧 HTML 解析器；HTMLParser 类扩展自 sgmllib.SGMLParser
# HTMLparser 新的非基于 SGML 的 HTML、XHTML 解析器
# htmlentitydefs HTML 普通实体定义
# Cookie 用于 HTTP 状态管理的服务器端 cookie
# cookielib HTTP 客户端的 cookie 处理类
# webbrowser 控制器：向浏览器加载 Web 文档
# sgmllib 解析简单的 SGML 文件
# robotparser 解析 robots.txt 文件作 URL 的“可获得性”分析
# httplib 用来创建 HTTP 客户端
# XML 解析
# xmllib 原始的简单 XML 解析器（已过时/不推荐使用）
# xml 包含许多不同 XML 特点的解析器（见下文）
# xml.sax 简单的适用于 SAX2 的 XML(SAX)解析器
# xml.dom 文本对象模型（DOM）的 XML 解析器
# xml.etree 树型的 XML 解析器，基于 Elemnt flexible container 对象
# xml.parsers.expat 非验证型 Expat XML 解析器的接口
# xmlrpclib 通过 HTTP 提供 XML 远程过程调用（RPC）客户端
# SimpleXMLRPCServer Python XML-RPC 服务器的基本框架
# DocXMLRPCServer 自描述 XML-RPC 服务器的框架
# Web 服务器
# BaseHTTPServer 用来开发 Web 服务器的抽象类
# SimpleHTTPServer 处理最简单的 HTTP 请求（HEAD 和 GET）
# CGIHTTPServer 不但能像 SimpleHTTPServers 一样处理 Web 文件，还能处理 CGI 请求（HTTP POST）
# wsgiref Web 服务器和 Python Web 应用程序间的标准接口
# 第三方开发包（非标准库）
# HTMLgen 协助 CGI 把 Python 对象转换成可用的 HTML http://starship.python.net/crew/friedrich/HTMLgen/ html/main.html
# BeautifulSoup HTML、XML 解析器及转换器 http://crummy.com/software/BeautifulSoup
# 邮件客户端协议
# poplib 用来创建 POP3 客户端
# imaplib 用来创建 IMAP4 客户端邮件、MIME 处理及数据编码格式
# emailc 管理 e-mail 消息的工具包，包括 MIME 和其它基于 RFC2822 的消息
# mailbox e-mail 消息的信箱类
# mailcap 解析 mailcap 文件，从中获得 MIME 应用授权
# 邮件、MIME 处理及数据编码格式
# mimetools 提供封装 MIME 编码信息的功能
# mimetypes 提供和 MIME 类型相关的功能
# MimeWriter 生成 MIME 编码的多种文件
# multipart 可以解析多种 MIME 编码文件
# quopri 编解码使用 quoted-printable 规范的数据
# rfc822 解析符合 RFC822 标准的 e-mail 头信息
# smtplib 用来创建 SMTP（简单邮件传输协议）客户端
# base64 编解码使用 base64 标准的数据
# binascii 编解码使用 base64、binhex、uu（模块）格式的数据
# binhex 编解码使用 binhex4 标准的数据
# uu 编解码使用 uuencode 格式的数据
# 因特网协议
# httpliba 用来创建 HTTP 客户端
# ftplib 用来创建 FTP(File Transfer Protocol)客户端
# gopherlib 用来创建 Gopher 客户端
# telnetlib 用来创建 Telnet 客户端
# nntplib 用来创建 NNTP（网络新闻传输协议[Usenet]）客户端

# # std12.1 http.server模块
# # http.server模块:
# #     主要包含两个类HTTPServer和BaseHTTPRequestHandler
# # HTTPServer:
# #     继承SocketServer.TCPServer，用于获取请求，并将请求分配给应答程序处理
# # BaseHTTPRequestHandler:
# #     继承SocketServer.StreamRequestHandler，对http连接的请求作出应答（response）
# #
# # 1实例1:
# # coding=utf-8
# '''
# @explain: 实现GET方法和POST方法请求
# '''
# from http.server import HTTPServer, BaseHTTPRequestHandler
# import io,shutil
#
# class ServerHTTP(BaseHTTPRequestHandler):
#     def setheader(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.send_header("test", "This is test!")
#         self.end_headers()
#     def post(self):
#         # path = self.path
#         # print(path)
#         # # 拆分url(也可根据拆分的url获取Get提交才数据),可以将不同的path和参数加载不同的html页面，或调用不同的方法返回不同的数据，来实现简单的网站或接口
#         # query = urllib.request.splitquery(path)
#         # print(query)
#         self.setheader()
#         buf = '''<!DOCTYPE HTML>
#                 <html>
#                 <head><title>Get page</title></head>
#                 <body>
#
#                 <form action="post_page" method="post">
#                   username: <input type="text" name="username" /><br />
#                   password: <input type="text" name="password" /><br />
#                   <input type="submit" value="POST" />
#                 </form>
#
#                 </body>
#                 </html>'''
#         # self.wfile.write(buf)
#         # 3.0版本修正
#         # enc = "UTF-8"
#         # encoded = ''.join(buf).encode(enc)
#         # f = io.BytesIO()
#         # f.write(encoded)
#         # f.seek(0)
#         # shutil.copyfileobj(f, self.wfile)
#
#     def recieve(self):  # 2创建新线程以连接对象(开始理解成请求对象)为参数实例化应答类:ServerHTTP()应答类根据请求方式调用ServerHTTP.do_XXX处理方法
#         # path = self.path
#         # print(path)
#         self.setheader()
#         # 获取post提交的数据
#         datas = self.rfile.read(int(self.headers['content-length']))
#         # datas = urllib.parse.unquote(datas).decode("utf-8", 'ignore')
#         buf = '''<!DOCTYPE HTML>
#         <html>
#             <head><title>Post page</title></head>
#             <body>Post Data:%s  <br />Path:%s</body>
#         </html>''' % (datas, self.path)
#         # self.wfile.write(buf)
#         # 3.0版本修正
#         # enc = "UTF-8"
#         # encoded = ''.join(buf).encode(enc)
#         # f = io.BytesIO()
#         # f.write(encoded)
#         # f.seek(0)
#         # shutil.copyfileobj(f, self.wfile)
#
# if __name__ == "__main__":
#     http_server = HTTPServer(('', 8001), ServerHTTP)
#     http_server.serve_forever()  # 1serve_forever()方法使用select.select()循环监听请求，当接收到请求后调用 当监听到请求时，取出请求对象


# # std12.2 base64
# # 处理一些如SMTP之类只能进行纯文本传输的情况，避免特殊符号。
# import base64
# import textwrap
# # Load this source file and strip the header.
# with open(__file__, 'rt',encoding='utf-8') as input:
#     raw = input.read()
#     initial_data = raw.split('#end_pymotw_header')[1]
# # encoded_data = base64.b64encode(initial_data)
# encoded_data = base64.b64encode(initial_data.encode(encoding="utf-8"))  #类似这种都需要转bytes
# num_initial = len(initial_data)
# # There will never be more than 2 padding bytes.
# padding = 3 - (num_initial % 3)
# print('%d bytes before encoding' % num_initial)
# print('Expect %d padding bytes' % padding)
# print('%d bytes after encoding' % len(encoded_data))
# print()
# print(encoded_data)
# decoded_string = base64.b64decode(encoded_data)
# print('Decoded :', decoded_string)

# # std12.3 robotparser
# # robotparser是一个专门用来解析网站的robots.txt文本文件的Python模块。
# # Robots协议（也称为爬虫协议、机器人协议等）的全称是“网络爬虫排除标准”（Robots Exclusion Protocol），网站通过Robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取。存于根目录上。
# import urllib.robotparser
# rp = urllib.robotparser.RobotFileParser()
# rp.set_url("http://baidu.com/robots.txt")  # Sets the URL referring to a robots.txt file.
# lines = rp.read()  # Reads the robots.txt URL and feeds it to the parser.
# rp.parse(lines)  # Parses the lines argument.
# # rrate = rp.request_rate("*")
# # rrate.requests
# # rrate.seconds
# # rp.crawl_delay("*")
# print(rp.can_fetch("*", "http://baidu.com/robots.txt"))  #Returns True if the useragent is allowed to fetch the url according to the rules contained in the parsed robots.txt file.
# print(rp.can_fetch("*", "http://www.musi-cal.com/"))


# # std12.4 cookie
# #coding:utf-8
# import urllib
# import http.cookiejar
#
# url = "http://c.highpin.cn/Users/CLogin"
# postdata =urllib.parse.urlencode({
#     "Logon_Password":"sunmin",
#     "Logon_PostCode":"fghc",
#     "Logon_RememberMe":"false",
#     "Logon_UserEmail":"sun121@qq.com"
# }).encode('utf-8')
# header = {
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Encoding":"utf-8",
#     "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
#     "Connection":"keep-alive",
#     "Host":"c.highpin.cn",
#     "Referer":"http://c.highpin.cn/",
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
# }
# req = urllib.request.Request(url,postdata,header)
# ##print(urllib.request.urlopen(req).read().decode('utf-8'))
#
# #自定义封装cookie设置的opener
# cj = http.cookiejar.CookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  #用来自定义 opener, 这种方法的好处是可以方便的拓展功能, 例如下面的代码就拓展了自动处理 Cookies 的功能
# r = opener.open(req)
# print(r.read().decode('utf-8'))


# # std12.5 uuid
# import uuid
# u = uuid.uuid1()
# print(u)
# print(type(u))
# print('bytes :', repr(u.bytes))
# print('hex :', u.hex)
# print('int :', u.int)
# print('urn :', u.urn)
# print('variant :', u.variant)
# print('version :', u.version)
# print('fields :', u.fields)
# print('\ttime_low : ', u.time_low)
# print('\ttime_mid : ', u.time_mid)
# print('\ttime_hi_version : ', u.time_hi_version)
# print('\tclock_seq_hi_variant: ', u.clock_seq_hi_variant)
# print('\tclock_seq_low : ', u.clock_seq_low)
# print('\tnode : ', u.node)
# print('\ttime : ', u.time)
# print('\tclock_seq : ', u.clock_seq)


# # std12.6 XML-RPC 参考例子(XMLRPC包中)，注意区分socket,select,socketserver等技术.
# # 服务端
# from xmlrpc.server import SimpleXMLRPCServer
# s = SimpleXMLRPCServer(("localhost",4242))
# def twice(x):
#     return x*2
# s.register_function(twice)
# s.serve_forever()
# # 客服端
# import xmlrpc.client
# s = xmlrpc.client.ServerProxy('http://localhost:4242')
# print(s.twice(2))