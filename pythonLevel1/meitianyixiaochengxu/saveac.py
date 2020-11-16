import pymysql

#1 确认数据连接成功
# 打开数据库连接
from base.meitianyixiaochengxu.activationcode import gene_activation_code

db = pymysql.connect("localhost","glexa","glexa","mybatis" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print ("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()

#2 新建表
# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS ACTIVITYCODE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE ACTIVITYCODE (
#          acid  INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#          activitycode  CHAR(20))"""
#
# cursor.execute(sql)
#
# # 关闭数据库连接
# db.close()

#3 存储数据

# SQL 插入语句
sql = """INSERT INTO activitycode(activitycode) VALUES(%s)"""
# sql = """INSERT INTO activitycode(activitycode) VALUES('WCHDVEDO6CWW45CD')"""

try:
   activitycodes = gene_activation_code(10, 18)
   # 执行sql语句
   cursor.executemany(sql, activitycodes)
   cursor.close()
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

# 关闭数据库连接
db.close()