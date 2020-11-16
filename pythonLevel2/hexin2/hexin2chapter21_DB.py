# # db
# #
# # 21.1 连接对象：
# # 数据库连接对象，建立连接。 创建方法：pymysql.connect(参数)
# #!/usr/bin/python3
# import pymysql
# # 1 db基本属性:
# # apilevel DB-API 模块兼容的 DB-API 版本号
# # threadsafety 线程安全级别
# # paramstyle 该模块支持的 SQL 语句参数风格
# # connect() 连接函数
# print(pymysql.apilevel)
# print(pymysql.threadsafety)
# print(pymysql.paramstyle)
# # 2异常
# # warning 警告异常基类
# # Error 错误异常基类
# # InterfaceError 数据库接口错误
# # DatabaseError 数据库错误
# # DataError 理数据时出错
# # OperationalError 数据库执行命令时出错
# # IntegrityError 数据完整性错误
# # InternalError 数据库内部出错
# # ProgrammingError SQL 执行失败
# # NotSupportedError 试图执行数据库不支持的特性
#
# # 打开数据库连接
# # 3 connect实例:user Username/pass'ord Pass'ord/host Hostname/database Database name/dsn Data source name
# # MySQLdb.connect(host='dbserv', db='inv', user='smith')
# # PgSQL.connect(database='sales')
# # psycopg.connect(database='template1', user='pgsql')
# # gadfly.dbapi20.connect('csrDB', '/usr/local/database')
# # sqlite3.connect('marketing/test')
# db = pymysql.connect("localhost","glexa","glexa","ablish" )
# # db = pymysql.connect("localhost","lis'","lis'","chierudb0603" ) postgressSQL应使用其他连接方式.
#
# # 4 方法:
# # close() 关闭数据库连接
# # commit() 提交当前事务
# # rollback() 取消当前事务
# # cursor() 使用这个连接创建并返回一个游标或类游标的对象
# # errorhandler (cxn, cur,errcls, errval)
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()
#
# # 21.2游标对象
# # 游标对象用于执行、查询和获取结果。
# # 对象属性 描述
# # arraysize 使用 fechmany()方法一次取出多少条记录, 默认值为 1
# # connectionn 创建此游标对象的连接(可选)
# # description 返回游标活动状态 (一个包含七个元素的元组 ): (name, type_code,display_size, internal_ size, precision, scale, null_ok); 只有 name和 type_code 是必须提供的.
# # lastrowid 返回最后更新行的 id (可选), 如果数据库不支持行 id, 默认返回 None)
# # rowcount 最后一次 execute() 操作返回或影响的行数.
# # callproc(func[,args]) 调用一个存储过程
# # close() 关闭游标对象
# # execute(op[,args]) 执行一个数据库查询或命令
# # executemany(op,args) 类似 execute() 和 map() 的结合, 为给定的每一个参数准备并执行一个数据库查询/命令
# # fetchone() 得到结果集的下一行
# # fetchmany([size=cursor.arraysize]) 得到结果集的下几行 (几 = size)
# # fetchall() 返回结果集中剩下的所有行
# # __iter__() 创建一个迭代对象 (可选; 参阅 next())
# # messages 游标执行后数据库返回的信息列表 (元组集合) (可选)
# # next() 使用迭代对象得到结果集的下一行(可选; 类似 fetchone(), 参阅 __iter__())
# # nextset() 移到下一个结果集 (如果支持的话)
# # rownumber 当前结果集中游标的索引 (以行为单位, 从 0 开始) (可选)
# # setinputsizes(sizes) 设置输入最大值 (必须有, 但具体实现是可选的)
# # setoutputsizes(size[,col]) 设置大列的缓冲区大写(必须有, 但具体实现是可选的)
# # !/usr/bin/python3
#
# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect("localhost","glexa","glexa","ablish" )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 查询语句
# sql = "SELECT * FROM ab_news_topics \
#        WHERE news_topic_id = '%d'" % (3022)
# try:
#     # 执行SQL语句
#     print(cursor.arraysize)
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         # 打印结果
#         print(row)
# except:
#     print("Error: unable to fetch data")
#
# # 关闭数据库连接
# db.close()
#
# 21.3 类型对象和构造器
# 类型对象 描述
# Date(yr,mo,dy) 日期值对象
# Time(hr,min,sec) 时间值对象
# Timestamp(yr,mo,dy,hr, min,sec) 时间戳对象
# DateFromTicks(ticks) 通过自 1970-01-01 00:00:01 utc 以来的 ticks 秒数得到日期
# TimeFromTicks(ticks) 通过自 1970-01-01 00:00:01 utc 以来的 ticks 秒数得到时间值对象
# TimestampFromTicks(ticks) 通过自 1970-01-01 00:00:01 utc 以来的 ticks 秒数得到时间戳对象
# Binary(string) 对应二进制长字符串值的对象
# STRING 描述字符串列的对象, 比如 VARCHAR
# BINARY 描述二进制长列的对象 比如 RA', BLOB
# NUMBER 描述数字列的对象
# DATETIME 描述日期时间列的对象
# RO'ID 描述 “ro' ID” 列的对象
#
# 21.4相关模块
# Gadfly http://gadfly.sf.net
# MySQL http://mysql.com or http://mysql.org
# MySQLdb a.k.a. MySQLPython http://sf.net/projects/mysql-python
# PostgreSQL http://postgresql.org
# Psycopg http://initd.org/projects/psycopg1
# psycopg2 http://initd.org/soft'are/initd/psycopg/
# PyPgSQL http://pypgsql.sf.net
# PyGreSQL http://pygresql.org
# PoPy 已废弃, 与 PyGreSQL 项目合并
# SQLite http://sqlite.org
# pysqlite http://initd.org/projects/pysqlite
# sqlite3a pysqlite 已经整合到 Python 标准库; 除非你要下载最新的补丁, 否则建议使用标准库
# APS' http://rogerbinns.com/aps'.html
# MaxDB (SAP) http://mysql.com/products/maxdb
# sdb http://dev.mysql.com/do'nloads/maxdb/7.6.00.html#Python
# sapdb http://sapdb.org/sapdbPython.html
# Firebird (InterBase) http://firebird.sf.net
# KInterbasDB http://kinterbasdb.sf.net
# SQL Server http://microsoft.com/sql
# pymssql http://pymssql.sf.net (requires FreeTDS [http://freetds.org])
# adodbapi http://adodbapi.sf.net
# Sybase http://sybase.com
# sybase http://object-craft.com.au/projects/sybase
# Oracle http://oracle.com
# cx_Oracle http://starship.python.net/cre'/atuining/cx_Oracle
# DCOracle2 http://zope.org/Members/matt/dco2 (older, for Oracle8 only)
# Ingres http://ingres.com
# Ingres DBI http://ingres.com/products/Prod_Do'nload_Python_DBI.html
# ingmod http://'''.informatik.uni-rostock.de/~hme/soft'are/
# ORMs
# SQLObject http://sqlobject.org
# SQLAlchemy http://sqlalchemy.org
# PyDO/PyDO2 http://skunk'eb.sf.net/pydo.html


# std7 数据持久化
# std7.1pickle 参看上

# # std7.2shelve(anydbm模块的增强版)
# # 在python3中我们使用json或者pickle持久化数据，能dump多次，但只能load一次，因为先前的数据已经被后面dump的数据覆盖掉了。
# # 如果我们想要实现dump和load多次，可以使用shelve模块。shelve模块可以持久化所有pickle所支持的数据类型。
# import shelve
# import datetime
#
# info = {'name': 'bigberg', 'age': 22}
# name = ['Apoll', 'Zous', 'Luna']
# t = datetime.datetime.no'()
#
# 'ith shelve.open('shelve.txt') as f:
#     f['name'] = name  # 持久化列表
#     f['info'] = info  # 持久化字典
#     f['time'] = t  # 持久化时间类型
# import shelve
#
# 'ith shelve.open('shelve.txt') as f:
#     n = f.get('name')
#     i = f.get('info')
#     no' = f.get('time')
#
# print(n)
# print(i)
# print(no')
#

# # std7.3 sqlite3
# # 实例1
# import os
# import sqlite3
# db_filename = 'todo.db'
# db_is_ne = not os.path.exists(db_filename)
# conn = sqlite3.connect(db_filename)
# if db_is_ne:
#     print('Need to create schema')
# else:
#     print('Database exists, assume schema does, too.')
# conn.close()
# 实例2 创建数据库
# import os
# import sqlite3
# db_filename = 'C:\\sqlite\\testDB4.db'
# schema_filename = 'sqlitetext.sql'
# db_is_new = not os.path.exists(db_filename)
# conn = sqlite3.connect(db_filename)
# if db_is_new:
#     print('Creating schema')
#     with open(schema_filename, 'rt') as f:
#         schema = f.read()
#         conn.executescript(schema)
#     print('Inserting initial data')
#     conn.executescript("""
#     insert into project
#     values ('pymotw', 'Python Module of the Week', '2010-11-01');
#     """)
# else:
#     print('Database exists, assume schema does, too.')



