# 线程
#
# 18.1线程执行流程
# 1. 设置 GIL(全局解释器锁)
# 2. 切换到一个线程去运行
# 3. 运行：
#  a. 指定数量的字节码指令，或者
#  b. 线程主动让出控制（可以调用 time.sleep(0)）
# 4. 把线程设置为睡眠状态
# 5. 解锁 GIL
# 6. 再次重复以上所有步骤
#
# 18.2_thread
# # #!/usr/bin/python3
#
# import _thread
# import time
#
# # 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# # 创建两个线程
# try:
#    _thread.start_new_thread(print_time, ("Thread-1", 2,))
#    _thread.start_new_thread(print_time, ("Thread-2", 4,))
# except:
#    print("Error: 无法启动线程")
#
# while 1:
#    pass

# #18.3 threading
# # thread已经不推荐。并改为_thread,threading 相比 _thread要丰富的多.
# #推荐threading,另一个避免使用 thread 模块的原因是，它不支持守护线程(主程序退出后仍在执行的子线程)。
# 属性:
# threading模块对象 描述
# Thread 表示一个线程的执行的对象
# Lock 锁原语对象（跟 thread 模块里的锁对象相同）
# RLock 可重入锁对象。使单线程可以再次获得已经获得了的锁（递归锁定）。
# Condition 创建一个condition对象，支持从外界引用一个Lock对象（适用于多个condtion共用一个Lock的情况），默认是创建一个新的Lock对象。
# Event 通用的条件变量。多个线程可以等待某个事件的发生，在事件发生后，所有的线程都会被激活。
# Semaphore 为等待锁的线程提供一个类似“等候室”的结构
# BoundedSemaphore 与 Semaphore 类似，只是它不允许超过初始值
# Timer 与 Thread 相似，只是，它要等待一段时间后才开始运行。
# # #!/usr/bin/python3
# 方法:
# 函数 描述
# threading.Thread() 构造函数
# start() 开始线程的执行
# run() 定义线程的功能的函数（一般会被子类重写）
# join(timeout=None) 程序挂起，直到线程结束；如果给了 timeout，则最多阻塞 timeout 秒
# wait([timeout]):线程挂起，直到收到一个notify通知或者超时（可选的，浮点数，单位是秒s）才会被唤醒继续运行。wait()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。调用wait()会释放Lock，直至该线程被Notify()、NotifyAll()或者超时线程又重新获得Lock.
# notify(n=1):通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正等待该condition的线程,最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。notify()不会主动释放Lock。
# notifyAll(): 如果wait状态线程比较多，notifyAll的作用就是通知所有线程（这个一般用得少）
# getName() 返回线程的名字
# setName(name) 设置线程的名字
# isAlive() 布尔标志，表示这个线程是否还在运行中
# isDaemon() 返回线程的 daemon 标志
# setDaemon(daemonic) 把线程的 daemon 标志设为 daemonic（一定要在调用 start()函数前调用）
# activeCount() 当前活动的线程对象的数量
# currentThread() 返回当前线程对象
# enumerate() 返回当前活动线程的列表
# settrace(func) 为所有线程设置一个跟踪函数
# setprofile(func) 为所有线程设置一个 profile 函数
#
# # 实例1: 自定义线程(子线程)
# import threading
# import time
#
# exitFlag = 0
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, delay):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.delay = delay
#     def run(self):
#         print("开始线程：" + self.name)
#         print_time(self.name, self.delay, 5)
#         print("退出线程：" + self.name)
#
# # counter 5次，5次后结束。delay==休眠时间。
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)#(线程id，线程名，休眠时间)
#
# # 开启新线程
# thread1.start()
# # 获取当前线程
# print(threading.currentThread().getName())
# thread2.start()
# print("thread1.isAlive",thread1.isAlive())
# print("thread2.isAlive",thread2.isAlive())
# thread1.join() #join([time]):阻塞线程
# print("thread1.isAlive",thread1.isAlive())
# thread2.join()
# print("退出主线程")
#
# # 实例2: 含参threading构造
# import threading
# def worker(num):
#     """thread worker function"""
#     print('Worker: %s' % num)
#     return
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()
#
# # 实例3 Daemon(守护进程) vs. Non-Daemon Threads(默认)
# import threading
# import time
# import logging
# logging.basicConfig(level=logging.DEBUG,
# format='(%(threadName)-10s) %(message)s',
# )
# # 守护进程
# def daemon():
#     logging.debug('Starting')
#     time.sleep(2)
#     logging.debug('Exiting')
# d = threading.Thread(name='daemon', target=daemon)
# d.setDaemon(True)
# def non_daemon():
#     logging.debug('Starting')
#     logging.debug('Exiting')
# t = threading.Thread(name='non-daemon', target=non_daemon)
# d.start()
# t.start()
#
# # 实例4 enumerate() 枚举线程
# import random
# import threading
# import time
# import logging
# logging.basicConfig(level=logging.DEBUG,
# format='(%(threadName)-10s) %(message)s',
# )
# def worker():
#     """thread worker function"""
#     t = threading.currentThread()
#     pause = random.randint(1,5)
#     logging.debug('sleeping %s', pause)
#     time.sleep(pause)
#     logging.debug('ending')
#     return
# for i in range(3):
#     t = threading.Thread(target=worker)
#     t.setDaemon(True)
#     t.start()
# main_thread = threading.currentThread()
# for t in threading.enumerate():
#     if t is main_thread:
#         continue
#     logging.debug('joining %s', t.getName())
#     t.join()
#
# # 实例5: Timer Threads 定时器
# import threading
# import time
# import logging
# logging.basicConfig(level=logging.DEBUG,
# format='(%(threadName)-10s) %(message)s',
# )
# def delayed():
#     logging.debug('worker running')
#     return
# t1 = threading.Timer(3, delayed)
# t1.setName('t1')
# t2 = threading.Timer(3, delayed)
# t2.setName('t2')
# logging.debug('starting timers')
# t1.start()
# t2.start()
# logging.debug('waiting before canceling %s', t2.getName())
# time.sleep(2)
# logging.debug('canceling %s', t2.getName())
# t2.cancel()
# logging.debug('done')
#
# # 实例6: Event
# import logging
# import threading
# import time
# logging.basicConfig(level=logging.DEBUG,
# format='(%(threadName)-10s) %(message)s',
# )
# def wait_for_event(e):
#     """Wait for the event to be set before doing anything"""
#     logging.debug('wait_for_event starting')
#     event_is_set = e.wait()
#     logging.debug('event set: %s', event_is_set)
# def wait_for_event_timeout(e, t):
#     """Wait t seconds and then timeout"""
#     while not e.isSet():
#         logging.debug('wait_for_event_timeout starting')
#         event_is_set = e.wait(t)
#         logging.debug('event set: %s', event_is_set)
#         if event_is_set:
#             logging.debug('processing event')
#         else:
#             logging.debug('doing other work')
# e = threading.Event()  #1新建用于触发treading运行的事件。
# t1 = threading.Thread(name='block',target=wait_for_event,args=(e,))  #2配置事件.
# t1.start()
# t2 = threading.Thread(name='nonblock',target=wait_for_event_timeout,args=(e, 2))
# t2.start()
# logging.debug('Waiting before calling Event.set()')
# time.sleep(3)
# e.set()  #3set()设置Event,开始运行线程。类似运行的flag设置为true
# logging.debug('Event is set')
#
# # 实例7: Semaphore() 线程等候池
# import logging
# import random
# import threading
# import time
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s (%(threadName)-2s) %(message)s',
# )
# class ActivePool(object):
#     def __init__(self):
#         super(ActivePool, self).__init__()
#         self.active = []
#         self.lock = threading.Lock()  # 创建锁
#     def makeActive(self, name):
#         with self.lock:  # 获取并最后释放锁
#             self.active.append(name)
#             logging.debug('Running: %s', self.active)
#     def makeInactive(self, name):
#         with self.lock:
#             self.active.remove(name)
#             logging.debug('inactive Running: %s', self.active)
# def worker(s, pool):
#     logging.debug('Waiting to join the pool')
#     with s:  # 获取等候室并最后释放。
#         name = threading.currentThread().getName()
#         pool.makeActive(name)
#         time.sleep(5)
#         pool.makeInactive(name)
# pool = ActivePool()
# s = threading.Semaphore(2)  #创建可以存储2个线程的等候池
# for i in range(4):
#     t = threading.Thread(target=worker,name=str(i),args=(s, pool))
#     t.start()
#     time.sleep(1)
#
# # 实例8: threading.local
# # Python提供了threading.local模块，方便我们实现线程局部变量的传递,Threading.local最大的用处就是HTTP请求时绑定用户的信息，这样每个用户线程可以非常方便访问各自的资源而互不干扰。
# # /usr/bin/env python
# # coding:utf-8
# # 没什么太大意义，该例子不使用local也能正常输出.
# __author__ = 'kikay'
#
# import threading
#
# # Threading.local对象
# ThreadLocalHelper = threading.local()
# lock = threading.RLock()
#
# class MyTheadEx(threading.Thread):
#     def __init__(self, threadName, name, age, sex):
#         super(MyTheadEx, self).__init__(name=threadName)
#         self.__name = name
#         self.__age = age
#         self.__sex = sex
#
#     def run(self):
#         global ThreadLocalHelper
#         ThreadLocalHelper.ThreadName = self.name
#         ThreadLocalHelper.Name = self.__name
#         ThreadLocalHelper.Age = self.__age
#         ThreadLocalHelper.Sex = self.__sex
#         MyTheadEx.ThreadPoc()
#
#     # 线程处理函数
#     @staticmethod
#     def ThreadPoc():
#         lock.acquire()
#         try:
#             print('Thread={id}'.format(id=ThreadLocalHelper.ThreadName))
#             print('Name={name}'.format(name=ThreadLocalHelper.Name))
#             print('Age={age}'.format(age=ThreadLocalHelper.Age))
#             print('Sex={sex}'.format(sex=ThreadLocalHelper.Sex))
#             print('----------')
#         finally:
#             lock.release()
#
# if __name__ == '__main__':
#     Tom = {'Name': 'tom', 'Age': 20, 'Sex': 'man'}
#     xiaohua = {'Name': 'xiaohua', 'Age': 18, 'Sex': 'woman'}
#     Andy = {'Name': 'Andy', 'Age': 40, 'Sex': 'man'}
#     T = (Tom, xiaohua, Andy)
#     threads = []
#     for i in range(len(T)):
#         t = MyTheadEx(threadName='id_{0}'.format(i), name=T[i]['Name'], age=T[i]['Age'], sex=T[i]['Sex'])
#         threads.append(t)
#     for i in range(len(threads)):
#         threads[i].start()
#     for i in range(len(threads)):
#         threads[i].join()
#     print('All Done!!!')


# #18.4 同步
#
# #!/usr/bin/python3
#
# import threading
# import time
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开启线程： " + self.name)
#         # 获取锁，用于线程同步
#         # threadLock.acquire()
#         with threadLock:
#             myThread.print_time(self.name, self.counter, 3)
#         # 释放锁，开启下一个线程
#         # threadLock.release()
#     @staticmethod
#     def print_time(threadName, delay, counter):
#         while counter:
#             time.sleep(delay)
#             print ("%s: %s" % (threadName, time.ctime(time.time())))
#             counter -= 1
#
# threadLock = threading.Lock()
# threads = []
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
#
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")

# #18.5 Queue模块
# # Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
# # 函数
# # Queue 模块函数
# # queue(size) 创建一个大小为 size 的 Queue 对象
# # Queue 对象函数
# # qsize() 返回队列的大小（由于在返回的时候，队列可能会被其它线程修改，所以这个值是近似值）
# # empty() 如果队列为空返回 True，否则返回 False
# # full() 如果队列已满返回 True，否则返回 False
# # put(item,block=0) 把 item 放到队列中，如果给了 block（不为 0），函数会一直阻塞到队列中有空间为止
# # get(block=0) 从队列中取一个对象，如果给了 block（不为 0），函数会一直阻塞到队列中有对象为止
#
# #!/usr/bin/python3
#
# import queue
# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print("开启线程：" + self.name)
#         process_data(self.name, self.q)
#         print("退出线程：" + self.name)
#
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print("%s processing %s" % (threadName, data))
#             # q.task_done()
#         else:
#             queueLock.release()
#         time.sleep(1)
#
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1
#
# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
#
# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
# # workQueue.join()
#
# # 等待队列清空
# while not workQueue.empty():
#     pass
#
# # 通知线程是时候退出
# exitFlag = 1
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print("退出主线程")
#
# 18.6相关模块
# thread 基本的，底级别的线程模块
# threading 高级别的线程和同步对象
# Queue 供多线程使用的同步先进先出（FIFO）队列
# mutex 互斥对象
# SocketServer 具有线程控制的 TCP 和 UDP 管理器


# # std10.1 subprocess
# # 用来生成子进程，并可以通过管道连接他们的输入/输出/错误，以及获得他们的返回值。
# # call() 执行命令，返回状态码，shell = True允许shell命令时字符串形式
# # check_call 执行命令，如果执行状态码是0，则返回0，否则抛出异常
# # check_output 执行命令，如果状态码是0，则返回执行结果，否则抛出异常
# # subprocess.Popen(...)　用于执行复杂的系统命令
# import subprocess
#
# obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                        universal_newlines=True)
# obj.stdin.write("print(1)\n")
# obj.stdin.write("print(2)")
# obj.stdin.close()
#
# cmd_out = obj.stdout.read()
# obj.stdout.close()
# cmd_error = obj.stderr.read()
# obj.stderr.close()
#
# # print(cmd_out)
# print(cmd_error)
#

# # std10.2 multiprocessing 多进程
# # 实例1: 基本多线程方式
# import multiprocessing
# def worker():
#     """worker function"""
#     print('Worker:',multiprocessing.current_process().name)    # 获取当前进程
#     print(multiprocessing.Process.authkey)
#     print(multiprocessing.Process.exitcode)
#     print(multiprocessing.Process.sentinel)
#     return
# if __name__ == '__main__':
#     jobs = []
#     for i in range(5):
#         p = multiprocessing.Process(target=worker)
#         jobs.append(p)
#         p.start()
#
# # 实例2: 线程池
# # -*- coding:utf-8 -*-
# from multiprocessing import Pool
# import os,time
#
# def run_proc(name):        ##定义一个函数用于进程调用
#     for i in range(5):
#         time.sleep(0.2)
#         print('Run child process %s (%s)' % (name, os.getpid()))
# #执行一次该函数共需1秒的时间
#
# if __name__ =='__main__': #执行主进程
#     print('Run the main process (%s).' % (os.getpid()))
#     mainStart = time.time() #记录主进程开始的时间
#     p = Pool(8)           #开辟进程池
#     for i in range(16):                                 #开辟15个进程
#         p.apply_async(run_proc,args=('Process'+str(i),))#异步执行，每个进程都调用run_proc函数， #args表示给该函数传递的参数。
#
#     print('Waiting for all subprocesses done ...')
#     p.close() #关闭进程池
#     p.join()  #等待开辟的所有进程执行完后，主进程才继续往下执行
#     print('All subprocesses done')
#     mainEnd = time.time()  #记录主进程结束时间
#     print('All process ran %0.2f seconds.' % (mainEnd-mainStart)) #主进程执行时间
#
# # 实例3: 守护进程
# import multiprocessing
# import time
# import sys
# def daemon():
#     p = multiprocessing.current_process()
#     print('Starting:', p.name, p.pid)
#     # sys.stdout.flush()
#     time.sleep(2)
#     print('Exiting :', p.name, p.pid)
#     # sys.stdout.flush()
# def non_daemon():
#     p = multiprocessing.current_process()
#     print('Starting:', p.name, p.pid)
#     # sys.stdout.flush()
#     print('Exiting :', p.name, p.pid)
#     # sys.stdout.flush()
# if __name__ == '__main__':
#     d = multiprocessing.Process(name='daemon', target=daemon, daemon=True)
#     n = multiprocessing.Process(name='non-daemon', target=non_daemon, daemon=False)
#     d.start()
#     # d.terminate()
#     time.sleep(1)
#     n.start()
#
# # 实例4: 退出状态
# import multiprocessing
# import sys
# import time
# def exit_error():
#     sys.exit(1)
# def exit_ok():
#     return
# def return_value():
#     return 1
# def raises():
#     raise RuntimeError('There was an error!')
# def terminated():
#     time.sleep(3)
# if __name__ == '__main__':
#     jobs = []
#     for f in [exit_error, exit_ok, return_value, raises, terminated]:
#         print('Starting process for', f.__name__)
#         j = multiprocessing.Process(target=f, name=f.__name__)
#         jobs.append(j)
#         j.start()
#     jobs[-1].terminate()
#     for j in jobs:
#         j.join()
#         print('%15s.exitcode = %s' % (j.name, j.exitcode))
#
# # 实例5: 传递消息给线程
# import multiprocessing
# class MyFancyClass(object):
#     def __init__(self, name):
#         self.name = name
#     def do_something(self):
#         proc_name = multiprocessing.current_process().name
#         print('Doing something fancy in %s for %s!' % (proc_name, self.name))
# def worker(q):
#     obj = q.get()
#     obj.do_something()
# if __name__ == '__main__':
#     queue = multiprocessing.Queue()
#     p = multiprocessing.Process(target=worker, args=(queue,))  #传入queue
#     p.start()
#     queue.put(MyFancyClass('Fancy Dan'))  #给queue传值，相当于传递消息给已启动的进程p
#     queue.put(MyFancyClass('Fancy Dan2'))
#     # Wait for the worker to finish
#     queue.close()
#     queue.join_thread()
#     p.join()
# from multiprocessing import Process, Queue
#
# def f(q):
#     q.put([42, None, 'hello'])
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())    # prints "[42, None, 'hello']"
#     p.join()
# # pipe
# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     p.join()
#
# # 实例6: event(类似event的)
# import multiprocessing
# import time
# def wait_for_event(e):
#     """Wait for the event to be set before doing anything"""
#     print('wait_for_event: starting')
#     e.wait()
#     print('wait_for_event: e.is_set()->', e.is_set())
# def wait_for_event_timeout(e, t):
#     """Wait t seconds and then timeout"""
#     print('wait_for_event_timeout: starting')
#     e.wait(t)
#     print('wait_for_event_timeout: e.is_set()->', e.is_set())
# if __name__ == '__main__':
#     e = multiprocessing.Event()
#     w1 = multiprocessing.Process(name='block',
#     target=wait_for_event,
#     args=(e,))
#     w1.start()
#     w2 = multiprocessing.Process(name='nonblock',
#     target=wait_for_event_timeout,
#     args=(e, 2))
#     w2.start()
#     print('main: waiting before calling Event.set()')
#     time.sleep(3)
#     e.set()
#     print('main: event is set')
#
# # 实例7: 同步
# import multiprocessing
# import time
# def stage_1(cond):
#     """perform first stage of work,
#     then notify stage_2 to continue
#     """
#     name = multiprocessing.current_process().name
#     print('Starting', name)
#     with cond:
#         print('%s done and ready for stage 2' % name)
#         cond.notify_all()
# def stage_2(cond):
#     """wait for the condition telling us stage_1 is done"""
#     name = multiprocessing.current_process().name
#     print('Starting', name)
#     with cond:
#         cond.wait()  #挂起当前线程
#         print('%s running' % name)
# if __name__ == '__main__':
#     condition = multiprocessing.Condition()
#     s1 = multiprocessing.Process(name='s1',
#     target=stage_1,
#     args=(condition,))
#     s2_clients = [
#     multiprocessing.Process(name='s2[%d]' % i,
#     target=stage_2,
#     args=(condition,))
#     for i in range(1, 3)
#     ]
#     for c in s2_clients:
#         c.start()
#     time.sleep(1)
#     s1.start()
#     s1.join()
#     for c in s2_clients:
#         c.join()
#
# # Manager() 进程间通信
# from multiprocessing import Process, Manager
#
# def f(d, l):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None
#     l.reverse()
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         # d = manager.dict()
#         # l = manager.list(range(10))
#         d = {}
#         l = list(range(10))
#
#         p = Process(target=f, args=(d, l))
#         p.start()
#         p.join()
#
#         print(d)
#         print(l)