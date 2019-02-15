"""
python操作数据库(原始方式)
"""
# sqlite(嵌入式数据库, python自带)

import sqlite3

# 创建与sqlite数据库的连接
conn = sqlite3.connect('test.db')

# 得到游标
cur = conn.cursor()

cur.execute(r'create table user (id varchar(20) primary key, name varchar(20))')

cur.execute("insert into user (id, name) values ('1', 'Michael')")
print(cur.rowcount)
# 提交数据
conn.commit()

# 查询操作
cur.execute(r'select * from user where id = ?', ('1', ))
results = cur.fetchall()
print(type(results))
print(results)

# 关闭游标
cur.close()

# 关闭连接
conn.close()

