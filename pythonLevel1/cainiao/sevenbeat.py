# !/usr/bin/python
# -*- coding: UTF-8 -*-

#1
# 定义函数
# def printme( str ):
#    "打印传入的字符串到标准显示设备上"
#    print str
#    return
#
# # 调用函数
# printme("我要调用用户自定义函数!");
# printme("再次调用同一函数");

#2 传不可变参数

# def ChangeInt( a ):
#     a = 10
#
# b = 2
# ChangeInt(b)
# print b # 结果是 2

#3 传可变参数 类c++引用类型，可以改变外面的值。
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4]);
#     print "函数内取值: ", mylist
#     return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30];
# changeme(mylist);
# print "函数外取值: ", mylist

#4 必须参数
# #可写函数说明
# def printme( str ):
#    "打印任何传入的字符串"
#    print str;
#    return;
#
# #调用printme函数，没有传入参数报错
# printme();

#5 关键字参数，可不在意顺序，程序以关键字查找参数

# # 可写函数说明
# def printinfo(name, age):
#     "打印任何传入的字符串"
#     print "Name: ", name;
#     print "Age ", age;
#     return;
#
#
# # 调用printinfo函数
# printinfo(age=50, name="miki");

#6 缺省参数

# # 可写函数说明
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print "Name: ", name;
#     print "Age ", age;
#     return;
#
#
# # 调用printinfo函数
# printinfo(age=50, name="miki");
# printinfo(name="miki");

#7 不定长参数

# 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print "输出: "
#     print arg1
#     for var in vartuple:
#         print var
#     return;
#
#
# # 调用printinfo 函数
# printinfo(10);
# printinfo(70, 60, 50);

#8 匿名函数

# # 可写函数说明
# sum = lambda arg1, arg2: arg1 + arg2;
#
# # 调用sum函数
# print "相加后的值为 : ", sum(10, 20)
# print "相加后的值为 : ", sum(20, 20)

#9 return

# # 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2
#     print "函数内 : ", total
#     return total;
#
#
# # 调用sum函数
# total = sum(10, 20);
# print total

#10 变量作用域

total = 0;  # 这是一个全局变量

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total;


# 调用sum函数
sum(10, 20);
print("函数外是全局变量 : ", total)

#11 列表反转函数

def reverse(li):
    for i in range(0, len(li)/2):
        temp = li[i]
        li[i] = li[-i-1]
        li[-i-1] = temp

l = [1, 2, 3, 4, 5]
reverse(l)
print(l)