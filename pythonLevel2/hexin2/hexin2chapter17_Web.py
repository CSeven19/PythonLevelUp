 #!/usr/bin/env python

# #17.1 ftp 客户程序
# 1ftplib.FTP 类方法
# 方法 描述
# login(user='anonymous',passwd='', acct='') 登录到 FTP 服务器，所有的参数都是可选的
# pwd() 得到当前工作目录
# cwd(path) 把当前工作目录设置为 path
# dir([path[,...[,cb]]) 显示 path 目录里的内容，可选的参数 cb 是一个回调函数，它会被传给 retrlines()方法
# nlst([path[,...]) 与 dir()类似，但返回一个文件名的列表，而不是显示这些文件名
# retrlines(cmd [, cb]) 给定 FTP 命令（如“RETR filename”），用于下载文本文件。可选的回调函数 cb 用于处理文件的每一行
# retrbinary(cmd, cb[,bs=8192[, ra]]) 与 retrlines()类似，只是这个指令处理二进制文件。回调函数 cb 用于处理每一块（块大小默认为 8K）下载的数据。
# storlines(cmd, f) 给定 FTP 命令（如“STOR filename”），以上传文本文件。要给定一个文件对象 f
# storbinary(cmd, f[,bs=8192]) 与 storlines()类似，只是这个指令处理二进制文件。要给定一个文件对象 f，上传块大小 bs 默认为 8Kbs=8192])
# rename(old, new) 把远程文件 old 改名为 new
# delete(path) 删除位于 path 的远程文件
# mkd(directory) 创建远程目录
# rmd(directory) 删除远程目录
# quit() 关闭连接并退出
# 2实例
# import ftplib
# import os
# import socket
#
# HOST = 'ftrans.chieru.co.jp'
# DIRN = 'CaLaboLanguage/v1.1/20170605'
# FILE = 'languagelib.zip'
#
# def main():
#     try:
#      f = ftplib.FTP(HOST)
#     except (socket.error, socket.gaierror) as e:
#         print('ERROR: cannot reach "%s"'% HOST)
#         return
#     print('*** Connected to host "%s"'% HOST)
#
#     try:
#         f.login('adtis_dev','gG5Wxfdc')
#     except ftplib.error_perm:
#         print('ERROR: cannot login anonymously')
#         f.quit()
#         return
#     print('*** Logged in as "anonymous"')
#
#     try:
#         f.cwd(DIRN)
#     except ftplib.error_perm:
#         print('ERROR: cannot CD to "%s"' % DIRN)
#         f.quit()
#         return
#     print('*** Changed to "%s" folder' % DIRN)
#
#     try:
#         f.retrbinary('RETR %s' % FILE,open(FILE, 'wb').write)
#     except ftplib.error_perm:
#         print('ERROR: cannot read file "%s"' % FILE)
#         os.unlink(FILE)
#     else:
#         print('*** Downloaded "%s" to CWD' % FILE)
#         f.quit()
#         return
#
# if __name__ == '__main__':
#     main()

# #17.2 NNTP
# 1nntplib.NNTP类方法
# 方法 描述
# group(name) 选择一个组的名字，返回一个元组(rsp,ct,fst,lst,group):服务器的返回信息，文章的数量，第一个和最后一个文章的号码以及组名，所有数据都是字符串。（返回的 group 与我们传进去的 name 应该是相同的）
# xhdr(hdr, artrg,[ofile]) 返回文章范围 artrg('头-尾'的格式)内文章 hdr 头的列表，或输出到文件 ofile 中
# body(id[,ofile]) 给定文章的 id，id 可以是消息的 ID（放在尖括号里），或一个文章号（是一个字符串），返回一个元组(rsp, anum, mid,data): 服务器的返回信息，文章号（是一个字符串），消息的 ID（放在尖括号里），和文章所有行的列表或把数据输出到文件 ofile 中。
# head(id) 与 body()相似，只是返回的元组中那个行的列表中只包含了文章的标题。
# article(id) 也跟 body()一样，只是返回的元组中那个行的列表中包含了文章的标题和内容。
# stat(id) 让文章的“指针”指向 id（同上，是一个消息的 ID 或是文章的号码）。返回一个跟 body 一样的元组(rsp, anum, mid)，但不包含文章的数据。
# next() 用法和 stat()类似，把文章指针移到下一篇文章，返回与stat()相似的元组
# last() 用法和 stat()类似，把文章指针移到最后一篇文章，返回与stat()相似的元组
# post(ufile) 上传 ufile 文件对象里的内容（使用 ufile.readline()），并在当前新闻组发表。
# quit() 关闭连接，然后退出
# 2实例
# import nntplib
# import socket
#
# HOST = 'your.nntp.server'
# GRNM = 'comp.lang.python'
# USER = 'wesley'
# PASS = 'youllNeverGuess'
#
# def main():
#
#     try:
#         n = nntplib.NNTP(HOST)
#         #, user=USER, password=PASS)
#     except socket.gaierror as e:
#         print('ERROR: cannot reach host "%s"' % HOST)
#         print(' ("%s")' % eval(str(e))[1])
#         return
#     except nntplib.NNTPPermanentError as e:
#         print('ERROR: access denied on "%s"' % HOST)
#         print(' ("%s")' % str(e))
#         return
#     print('*** Connected to host "%s"' % HOST)
#
#     try:
#         rsp, ct, fst, lst, grp = n.group(GRNM)
#     except nntplib.NNTPTemporaryError as e2:
#         print('ERROR: cannot load group "%s"' % GRNM)
#         print(' ("%s")' % str(e2))
#         print(' Server may require authentication')
#         print(' Uncomment/edit login line above')
#         n.quit()
#         return
#     except nntplib.NNTPTemporaryError as e3:
#         print('ERROR: group "%s" unavailable' % GRNM)
#         print(' ("%s")' % str(e3))
#         n.quit()
#         return
#     print('*** Found newsgroup "%s"' % GRNM)
#
#     rng = '%s-%s' % (lst, lst)
#     rsp, frm = n.xhdr('from', rng)
#     rsp, sub = n.xhdr('subject', rng)
#     rsp, dat = n.xhdr('date', rng)
#     print ('''*** Found last article (#%s):
#     From: %s
#     Subject: %s
#     Date: %s
# '''% (lst, frm[0][1], sub[0][1], dat[0][1]))
#
#     rsp, anum, mid, data = n.body(lst)
#     displayFirst20(data)
#     n.quit()
#
# def displayFirst20(data):
#     print('*** First (<= 20) meaningful lines:\n')
#     count = 0
#     lines = (line.rstrip() for line in data)
#     lastBlank = True
#     for line in lines:
#         if line:
#             lower = line.lower()
#             if (lower.startswith('>') and not \
#                 lower.startswith('>>>')) or \
#                 lower.startswith('|') or \
#                 lower.startswith('in article') or \
#                 lower.endswith('writes:') or \
#                 lower.endswith('wrote:'):
#                     continue
#             if not lastBlank or (lastBlank and line):
#                 print(' %s' % line)
#                 if line:
#                     count += 1
#                     lastBlank = False
#                 else:
#                     lastBlank = True
#             if count == 20:
#              break
#
# if __name__ == '__main__':
#     main()


# #17.3  SMTP POP3 EXAMPLE
# 1smtplib.SMTP 类方法
# 方法 描述
# Sendmail(from, to, msg[,mopts, ropts]) 把 msg 从 from 发送给 to（列表或元组）。ESMTP 设置（mopts）和收件人设置（ropts）为可选。
# quit() 关闭连接，然后退出
# login(user, passwd) 使用 user 用户和 passwd 密码登录到 SMTP 服务器
# 2smtp实例:
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = '***'
# receiver = '***'
# subject = 'python email test'
# smtpserver = 'smtp.163.com'
# username = '***'
# password = '***'
#
# msg = MIMEText('你好', 'text', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
# msg['Subject'] = Header(subject, 'utf-8')
#
# smtp = smtplib.SMTP()
# smtp.connect('smtp.163.com')
# smtp.login(username, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()
# 3poplib.POP3 类方法
# POP3 对象的常用方法
# 方法 描述
# user(login) 发送用户名 login 到服务器，并等候服务器的正在等待用户密码的返回信息
# pass_(passwd) 发送密码 passwd（在使用 user()登录之后使用）。如果登录失败，引发一个异常
# stat() 返回邮件的状态，一个长度为 2 的元组（msg_ct, mbox_siz）：消息的数量和消息的总大小也即字节数
# list([msgnum]) stat()的扩展，从服务器返回长度为 3 的元组的消息列表（rsp, msg_list,rsp_siz）：服务器的返回信息，消息的列表，返回信息的大小。如果给了 msgnum 的话，只返回指定消息的数据。
# retr(msgnum) 从服务器中得到消息 msgnum，并设置其“已读”标志。返回一个长度为3 的元组（rsp, msglines, msgsiz）：服务器的返回信息，消息 msgnum的所有行，消息的字节数
# dele(msgnum) 把消息 msgnum 标记为删除，大多数服务器在调用 quit()后执行删除操作。
# quit() 登出，保存修改（如，执行“已读”和“删除”标记等），解锁邮箱，结束连接，然后退出
# # 4pop3实例:
# from poplib import POP3
# p = POP3('pop.python.is.cool')
# p.user('techNstuff4U')
# p.pass_('notMyPasswd')
# p.user('techNstuff4U')
# p.pass_('youllNeverGuess')
# p.stat()
# rsp, msg, siz = p.retr(102)
# rsp, siz('+OK', 480)
# for eachLine in msg:
#     print(eachLine)
# p.quit()
# 5smtp及pop3客服端
# from smtplib import SMTP
# from poplib import POP3
# from time import sleep
# SMTPSVR = 'smtp.python.is.cool'
# POP3SVR = 'pop.python.is.cool'
# origHdrs = ['From: wesley@python.is.cool', 'To: wesley@python.is.cool','Subject: test msg']
# origBody = ['xxx', 'yyy', 'zzz']
# origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),'\r\n'.join(origBody)])
# sendSvr = SMTP(SMTPSVR)
# errs = sendSvr.sendmail('101091912@python.is.cool','24423234@python.is.cool', origMsg)
# sendSvr.quit()
# assert len(errs) == 0, errs
# sleep(10) # wait for mail to be delivered
# recvSvr = POP3(POP3SVR)
# recvSvr.user('wesley')
# recvSvr.pass_('youllNeverGuess')
# rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])  # 下载第一条消息
# sep = msg.index('')
# recvBody = msg[sep+1:]
# assert origBody == recvBody # 判断发送的邮件和接受的邮件时一致的
# # 6实例
# # !/usr/bin/python3
#
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = 'from@runoob.com'
# receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")
#
#17.4email其他模块
# 模块/包 描述
# email e-mail 处理的包 （也支持 MIME）
# rfc822 RFC2822 邮件头解析器
# smtpd SMTP 服务器
# base64 Base 16，32，和 64 数据编码(RFC 3548)
# mhlib 处理 MH 文件夹和信息的类
# mailbox 支持 mailbox 文件格式解析的类
# mailcap “mailcap” 文件的处理模块
# mimetools （不建议使用）MIME 信息解析工具（使用上面的 email）
# mimetypes 在文件名或 URL 到相关的 MIME 类型之间转换的模块
# MimeWriter （不建议使用）MIME 信息处理模块（使用上面的 email）
# mimify （不建议使用）信息的 MIME 处理工具（使用上面的 email）
# binascii 二进制和 ASCII 转换
# binhex Binhex4 编码和解码支持
#
# 17.5其他网络协议模块
# 模块 描述
# ftplib FTP 协议客户端
# gopherlib Gopher 协议客户端
# httplib HTTP 和 HTTPS 协议客户端
# imaplib IMAP4 协议客户端
# nntplib NNTP protocol client
# nntplib NNTP 协议客户端
# poplib POP3 协议客户端
# smtplib SMTP 协议客户端
# telnetlib Telnet 协议客户端类