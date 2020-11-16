#!/usr/bin/env python

# #1 python3 tcp_client
# from socket import *
#
# HOST = '127.0.0.1' # or 'localhost'
# PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)
#
# while True:
#     data = input('> ')
#     if not data:
#         break
#     tcpCliSock.send(data.encode(encoding="utf-8"))
#     data = tcpCliSock.recv(BUFSIZ)
#     if not data:
#         break
#     print(data.decode('utf-8'))
#
# tcpCliSock.close()

# #2 ipv6的tcp_client
#
# from socket import *
#
# HOST = '::1'
# PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# tcpCliSock = socket(AF_INET6, SOCK_STREAM)
# tcpCliSock.connect(ADDR)
#
# while True:
#     data = input('> ')
#     if not data:
#         break
#     tcpCliSock.send(data)
#     data = tcpCliSock.recv(BUFSIZ)
#     if not data:
#         break
#     print(data)
#
# tcpCliSock.close()

#
# #3 UDP_client
#
# from socket import *
#
# HOST = 'localhost'
# PORT = 21568
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# udpCliSock = socket(AF_INET, SOCK_DGRAM)
#
# while True:
#     data = input('> ')
#     if not data:
#         break
#     udpCliSock.sendto(data.encode(), ADDR)
#     data, ADDR = udpCliSock.recvfrom(BUFSIZ)
#     if not data:
#         break
#     print(data)
#
# udpCliSock.close()