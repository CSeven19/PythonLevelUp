# python对象
# # 4.1对象特性:身份，类型和值。
# # id用于返回对象身份,这个值可以被认为是该对象的内存地址。
# a_list = ["123", 1, 2]
# print(id(a_list))
#
# # 4.2类型
# # 标准类型:
# # z 数字（分为几个子类型，其中有三个是整型）
# # z 整型
# # z 布尔型
# # z 长整型
# # z 浮点型
# # z 复数型
# # z 字符串
# # z 列表
# # z 元组
# # z 字典
# # 其他类型：
# # z 类型
# # z Null 对象 (None)
# # z 文件
# # z 集合/固定集合
# # z 函数/方法
# # z 模块
# # z 类
# # type()
# print(type(42))
# print(type(type(42))) # 类型本身
# # isinstance()
# import string
# class objA:
#     pass
# A = objA()
# B = 'a', 'v'
# C = 'a string'
# print(isinstance(A, objA))
# print(isinstance(B, tuple))
# print(isinstance(C, string))
# # 内部类型：
# # z 代码
# # z 帧
# # z 跟踪记录
# # z 切片
# # z 省略
# # z Xrange
#
# # 4.3false:
# # z None
# # z False (布尔类型)
# # z 所有的值为零的数：
# # z 0 (整型)
# # z (浮点型)
# # z 0L (长整型)
# # z 0.0+0.0j (复数)
# # z "" (空字符串)
# # z [] (空列表)
# # z () (空元组)
# # z {} (空字典)
#
#


# 不支持方法或函数重载