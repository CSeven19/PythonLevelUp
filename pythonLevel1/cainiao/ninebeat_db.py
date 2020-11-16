# !/usr/bin/python
# -*- coding: UTF-8 -*-

#1 建立连接
# import MySQLdb
#
# # 打开数据库连接
# db = MySQLdb.connect("localhost","glexa","glexa","ablish" )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取一条数据库。
# data = cursor.fetchone()
#
# print "Database version : %s " % data
#
# # 关闭数据库连接
# db.close()

# #2 查询
#
# import MySQLdb
#
#
# # 打开数据库连接
# db = MySQLdb.connect("localhost","glexa","glexa","ablish" )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 查询语句
# sql = "SELECT * FROM ab_categories"
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#       # 打印结果
#       print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#              (fname, lname, age, sex, income )
# except:
#    print "Error: unable to fecth data"
#
# # 关闭数据库连接
# db.close()