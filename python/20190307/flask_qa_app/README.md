1.首先创建一个qa_db数据库（utf-8格式）
    CREATE DATABASE `qa_db` CHARACTER SET 'utf8';
    grant all privileges on qa_db.* to qa@localhost identified by 'qa';
2.初始化数据库：python manage.py db init
3.生成数据库语句：python manage.py db migrate
4.创建数据库：python manage.py upgrade