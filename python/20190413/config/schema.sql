CREATE USER 'django_mysql'@'127.0.0.1' IDENTIFIED BY '123';
grant all privileges on allwork_db.* to django_mysql@127.0.0.1 identified by '123';
CREATE DATABASE allwork_db CHARACTER SET 'utf8';