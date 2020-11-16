# !/usr/bin/python
# -*- coding: UTF-8 -*-
# tcp
# #python2
# from socket import *
# from time import ctime
#
# HOST = ''
# PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)
#
# while True:
#     print('waiting for connection...')
#     tcpCliSock, addr = tcpSerSock.accept()
#     print('...connected from:', addr)
#
#     while True:
#         data = tcpCliSock.recv(BUFSIZ)
#         if not data:
#             break
#         tcpCliSock.send('[%s] %s' % (ctime(), data))
#
#     tcpCliSock.close()
# tcpSerSock.close()

# #2python3 tcp_server
# from socket import *
# from time import ctime
#
# HOST = '127.0.0.1'
# PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)
#
# while True:
#     print('waiting for connection...')
#     tcpCliSock, addr = tcpSerSock.accept()
#     print('...connected from:', addr)
#
#     while True:
#         data = tcpCliSock.recv(BUFSIZ)
#         if not data:
#             break
#         tcpCliSock.send('[%s] 客户发送 %s'.encode("utf-8") % (ctime().encode("utf-8"), data))
#
#     tcpCliSock.close()
# tcpSerSock.close()

# #3 UDP_server
#
# from socket import *
# from time import ctime
#
# HOST = ''
# PORT = 21568
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# # SOCK_DGRAM 一般用于广播
# udpSerSock = socket(AF_INET, SOCK_DGRAM)
# udpSerSock.bind(ADDR)
# while True:
#     print('waiting for message...')
#     data, addr = udpSerSock.recvfrom(BUFSIZ)
#     udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
#     print('...received from and returned to:', addr)
#
# udpSerSock.close()