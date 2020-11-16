# # 时间日期
# #
# # -*- coding: UTF-8 -*-
# # # 4.1 ctime()/time()/clock()
# import hashlib  #提供加密
# import time
# import codecs
# # Data to use to calculate md5 checksums
# data = codecs.open(__file__, 'r', 'utf-8').read()  #获取当前执行主脚本的方法有两个：sys.argv[0]和__file__。
# for i in range(5):
#     h = hashlib.sha1()
#     print(time.ctime(), ': %0.3f %0.3f' % (time.time(), time.clock()))
#     for j in range(300000):
#         h.update(data.encode('utf-8'))
#     cksum = h.hexdigest()
#     print(cksum)

