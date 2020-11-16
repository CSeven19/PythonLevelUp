# import os
# from hashlib import sha256
# from hmac import HMAC
#
# def encrypt_password(password, salt=None):
#     """Hash password on the fly."""
#     if salt is None:
#         salt = os.urandom(8) # 64 bits.
#
#     assert 8 == len(salt)
#     assert isinstance(salt, str)
#
#     if isinstance(password, unicode):
#         password = password.encode('UTF-8')
#
#     assert isinstance(password, str)
#
#     result = password
#     for i in xrange(10):
#         result = HMAC(result, salt, sha256).digest()
#
#     return salt + result


# -------------------------------------------
# Python简单密码加密程序
# 随机生成4位salt，与原始密码组合，通过md5加密
# Author : Lrg
# -------------------------------------------
# encoding = utf-8
from random import Random
from hashlib import md5


# 获取由4位随机大小写字母、数字组成的salt值
def create_salt(length=4):
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars) - 1
    random = Random()
    for i in range(length):
        # 每次从chars中随机取一位
        salt += chars[random.randint(0, len_chars)]
    return salt


# 获取原始密码+salt的md5值
def create_md5(pwd, salt):
    md5_obj = md5()
    md5_obj.update((pwd + salt).encode(encoding='UTF-8',errors='strict'))
    return md5_obj.hexdigest()


# 原始密码
pwd = '20141124'
# 随机生成4位salt
salt = create_salt()

# salt = "eVkm"
# 7807dff56efe82a25445caa432784bfd
# 经测试，只要pwd，salt相同生成的md5是一样的。

# 加密后的密码
md5 = create_md5(pwd, salt)
print('[pwd]\n', pwd)
print('[salt]\n', salt)
print('[md5]\n', md5)