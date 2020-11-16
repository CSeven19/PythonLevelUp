# 数据结构
#
# # 2.1 counter 统计用
# import collections
# c = collections.Counter('abcdaab')
# for letter in 'abcde':
#     print('%s : %d' % (letter, c[letter]))
#

# # 2.2 namedtuple tuple子类
# Person = collections.namedtuple('Person', 'name age gender')
# print('Type of Person:', type(Person))
# bob = Person(name='Bob', age=30, gender='male')
# print('\nRepresentation:', bob)
# jane = Person(name='Jane', age=29, gender='female')
# print('\nField by name:', jane.name)
# print('\nFields by index:')
# for p in [bob, jane]:
#     print('%s is a %d year old %s' % p)
#

# # 2.3 OrderedDict 有序字典(按值排序)
# import collections
# print('Regular dictionary:')
# d = {}
# d['f'] = 'A'
# d['b'] = 'B'
# d['c'] = 'C'
# for k, v in d.items():
#     print(k, v)
# print('\nOrderedDict:')
# d = collections.OrderedDict()
# d['f'] = 'A'
# d['b'] = 'B'
# d['c'] = 'C'
# kd = collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))
# print(kd)
# print(d.items())
# for k, v in d.items():
#     print(k, v)
#

# # 2.4 heapq 堆
# from heapq import *
# def heapsort(iterable):
#     h = []
#     for value in iterable:
#         heappush(h, value)  #往堆中插入一条新的值
#     print(h)
#     return [heappop(h) for i in range(len(h))]  #heappop(h)从堆中弹出最小值
#
# print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
#

# # 2.5 bisect
# import bisect
# import random
# # Use a constant seed to ensure that
# # the same pseudo-random numbers
# # are used each time the loop is run.
# random.seed(1)
# print('New Pos Contents')
# print('--- --- --------')
# # Generate random numbers and
# # insert them into a list in sorted
# # order.
# m = []
# for i in range(1, 15):
#     r = random.randint(1, 100)
#     position = bisect.bisect(m, r)
#     bisect.insort(m, r)
#     print('%3d %3d' % (r, position), m)
#

# # 2.6 Queue—Thread-Safe FIFO Implementation
# import queue
# q = queue.Queue()
# for i in range(5):
#     q.put(i)
# while not q.empty():
#     print(q.get(),)
# print()
# # LIFO Queue
# import queue
# q = queue.LifoQueue()
# for i in range(5):
#     q.put(i)
# while not q.empty():
#     print(q.get(),)
# print()
#

# # 2.7 Building a Threaded Podcast Client
# from queue import Queue
# from threading import Thread
# import time
# import urllib
# from urllib import parse
# import feedparser  #用于解析RSS
# # Set up some global variables
# num_fetch_threads = 2
# enclosure_queue = Queue()
# # A real app wouldn’t use hard-coded data...
# feed_urls = ['http://www.zhihu.com/rss',]
# def downloadEnclosures(i, q):
#     """This is the worker thread function.
#     It processes items in the queue one after
#     another. These daemon threads go into an
#     infinite loop, and only exit when
#     the main thread ends.
#     """
#     while True:
#         print('%s: Looking for the next enclosure' % i)
#         url = q.get()
#         parsed_url = urllib.parse(url)
#         print('%s: Downloading:' % i, parsed_url.path)
#         response = urllib.urlopen(url)
#         data = response.read()
#         # Save the downloaded file to the current directory
#         outfile_name = url.rpartition('/')[-1]
#         with open(outfile_name, 'wb') as outfile:
#             outfile.write(data)
#         q.task_done()
# for i in range(num_fetch_threads):
#     worker = Thread(target=downloadEnclosures,
#     args=(i, enclosure_queue,))
#     worker.setDaemon(True)
#     worker.start()
# for url in feed_urls:
#     response = feedparser.parse(url)  #解析rss
#     for entry in response['entries'][-5:]:
#         for enclosure in entry.get('enclosures', []):
#             parsed_url = urllib.parse(enclosure['url'])
#             print('Queuing:', parsed_url.path)
#             enclosure_queue.put(enclosure['url'])
#

# # 2.8 Binary Data Structures 二进制字符串互相转化
# import struct
# import binascii
# values = (1, b'ab', 2.7)
# s = struct.Struct(b'I 2s f')
# packed_data = s.pack(*values)
# print('Original values:', values)
# print('Format string :', s.format)
# print('Uses :', s.size, 'bytes')
# print('packed_data :', packed_data)
# print('Packed Value :', binascii.hexlify(packed_data))  #转二进制
# packed_data = binascii.unhexlify(binascii.hexlify(packed_data))  #解二进制
# s = struct.Struct('I 2s f')
# unpacked_data = s.unpack(packed_data)
# print('Unpacked Values:', unpacked_data)
#
# # 实例2 endianness
# # @ Native order
# # = Native standard
# # < Little-endian
# # > Big-endian
# # ! Network order
# import struct
# import binascii
# values = (1, b'ab', 2.7)
# print('Original values:', values)
# endianness = [
#     (b'@', b'native, native'),
#     (b'=', b'native, standard'),
#     (b'<', b'little-endian'),
#     (b'>', b'big-endian'),
#     (b'!', b'network'),
# ]
# for code, name in endianness:
#     s = struct.Struct(code + b' I 2s f')
#     packed_data = s.pack(*values)
#     print()
#     print('Format string :', s.format, 'for', name)
#     print('Uses :', s.size, 'bytes')
#     print('Packed Value :', binascii.hexlify(packed_data))
#     print('Unpacked Value :', s.unpack(packed_data))
#
# # 实例3 buffer(缓冲区) pack_into/unpack_from buffer式放入取出
# import struct
# import binascii
#
# s = struct.Struct(b' I 2s f')
# values = (1, b'ab', 2.7)
# print('Original:', values)
# print()
# print('ctypes string buffer')
# import ctypes
# b = ctypes.create_string_buffer(s.size)  #创建 buffer(缓冲区), 返回一个 Python 对象
# print('Before :', binascii.hexlify(b.raw))
# s.pack_into(b, 0, *values)
# print('After :', binascii.hexlify(b.raw))
# print('Unpacked:', s.unpack_from(b, 0))
#

# # 2.9 weakref模块
# # 弱引用。相对于通常的引用来说，如果一个对象有一个常规的引用，它是不会被垃圾收集器销毁的，但是如果一个对象只剩下一个弱引用，那么它可能被垃圾收集器收回。
# # 并非所有的对象都支持weakref，例如list和dict就不支持，但是文档中介绍了可以通过继承dict来支持weakref。
# # -*- coding: cp936 -*-
# import weakref
# class TestObj:
#     pass
# a = TestObj()
# # 建立一个a的弱引用
# x = weakref.ref(a)
# print(x)
# print(x())
# print(a)
#
# # 实例2 建立弱引用的时候指定一个回调函数，一旦自己引用的对象被销毁，将会调用这个回调函数。
# # -*- coding: cp936 -*-
# import weakref
# class TestObj:
#     pass
# def test_func(reference):
#     print('Hello from Callback function!')
#     print(reference, 'This weak reference is no longer valid')
# a = TestObj()
# # 建立一个a的弱引用
# x = weakref.ref(a, test_func)
# del a
#

# # 2.10 copy
# # 自定义copy
# import copy
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#     # def __cmp__(self, other):
#     #     return cmp(self.name, other.name)
#     #     120 Data Structures
#     def __copy__(self):
#         print('__copy__()')
#         return MyClass(self.name)
#     def __deepcopy__(self, memo):
#         print('__deepcopy__(%s)' % str(memo))
#         return MyClass(copy.deepcopy(self.name, memo))
# a = MyClass('a')
# sc = copy.copy(a)
# dc = copy.deepcopy(a)