# # 加密
# #
# # 9.1 hashlib—Cryptographic Hashing参考文档
# import hashlib
# import os
# def md5sum(filename):
#         """
#         用于获取文件的md5值
#         :param filename: 文件名
#         :return: MD5码
#         """
#         if not os.path.isfile(filename):  # 如果校验md5的文件不是文件，返回空
#             return
#         myhash = hashlib.md5()
#         f = open(filename, 'rb')
#         while True:
#             b = f.read(8096)
#             if not b:
#                 break
#             myhash.update(b)
#         f.close()
#         return myhash.hexdigest()
# def md5Simple(str):
#     md5obj = hashlib.md5()
#     md5obj.update(str)
#     return md5obj.hexdigest()
# print(md5sum('todo.db'))
# print(md5Simple("admin".encode("utf-8")))
# print(len(md5Simple("admin".encode("utf-8"))))
#

# 9.2 hmac—Cryptographic Message Signing and Verification
#!/usr/bin/env python
# coding=utf-8
# __author__ = 'Luzhuo'
# __date__ = '2017/5/19'
# hmac_demo.py HMAC算法
# 与hashlib不同之处在于多了key

import hmac


def hmac_demo():
    # 加密
    h = hmac.new(b"net")
    h.update(b"Li")
    h_str = h.hexdigest()
    print(h_str)

    # 比较密码
    boolean = hmac.compare_digest(h_str, hmac.new(b"net", b"luzhuo.me").hexdigest())
    print(boolean)



def hmac_func():
    # 创建key和内容,再都进行加密
    # hmac.new(key, msg=None, digestmod=None) // 创建新的hmac对象, key:键, msg:update(msg), digestmod:hash名称(同hashlib.new())(默认md5)
    hc = hmac.new(b"key")

    # hmac对象
    hc.update(b"msg")  # 字节缓冲区  hc.update(a) hc.update(b) == hc.update(a+b)
    hash_bytes = hc.digest()  # 字节hash
    hash_str = hc.hexdigest()  # 16进制hash字符串
    hc = hc.copy()  # 拷贝hmac副本
    num = hc.digest_size  # hash大小
    num = hc.block_size  # hash算法内部块大小
    strs = hc.name  # hash名称
    # hmac.compare_digest(a, b) // 比较两个hash密钥是否相同, 参数可为: str / bytes-like object, (注:建议使用,不建议使用a==b)
    boolean = hmac.compare_digest(hmac.new(b"net", b"luzhuo.me").digest(), hmac.new(b"net", b"luzhuo.me").digest())




if __name__ == "__main__":
    hmac_demo()

    # hmac_func()