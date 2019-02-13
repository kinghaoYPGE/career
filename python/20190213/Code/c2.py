"""
python操作mysql
"""
>>> import mysql
>>> dir(mysql)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
>>> mysql
<module 'mysql' from 'C:\\develop\\python3.6\\lib\\site-packages\\mysql\\__init__.py'>
>>> from mysql import connector
>>> conn = connector.connect(user='root', password='123456', database='mysql_test')
>>> cur = conn.cursor()
>>> cur.execute('create table user (id varchar(20) primary key, name varchar(20))')
>>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
NameError: name 'cursor' is not defined
>>> cur.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
>>> cur.rowcount
1
>>> conn.commit()
>>> cur.execute('insert into user (id, name) values (?, ?)', ('1', 'Michael'))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    cur.execute('insert into user (id, name) values (?, ?)', ('1', 'Michael'))
  File "C:\develop\python3.6\lib\site-packages\mysql\connector\cursor.py", line 561, in execute
    "Not all parameters were used in the SQL statement")
mysql.connector.errors.ProgrammingError: Not all parameters were used in the SQL statement
>>> cur.close()
True
>>> cur = conn.cursor()
>>> cursor.execute('select * from user where id = %s', ('1',))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    cursor.execute('select * from user where id = %s', ('1',))
NameError: name 'cursor' is not defined
>>> cur.execute('select * from user where id = %s', ('1',))
>>> values = cur.fetchall()
>>> values
[('1', 'Michael')]
>>> cur.close()
True
>>> conn.close()
>>> cur.execute('select * from user where id = ?', ('1',))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    cur.execute('select * from user where id = ?', ('1',))
  File "C:\develop\python3.6\lib\site-packages\mysql\connector\cursor.py", line 537, in execute
    raise errors.ProgrammingError("Cursor is not connected")
mysql.connector.errors.ProgrammingError: Cursor is not connected
>>> 
