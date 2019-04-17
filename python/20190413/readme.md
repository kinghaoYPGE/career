# Python Web项目生产部署方式

### 前言：

在讲生产部署前，有必要理解一些概念，不知大家想没想过一个问题。我使用python（Django、Flask等框架)开发好web项目后，都是直接可以在浏览器访问的，为什么不可以直接放到生产服务器上呢？

原因是因为Django、Flask等根本不是 http 服务器，而是 web 框架（就是简化开发的），你能直接访问你写的web app，只不过框架开发组体谅用户，自带一个简易的用于方便调试用的服务器，那是不能用于生产的，因为性能很差且不安全，违背了web服务的两大准则（一是性能，而是安全）！如果这些框架没有提供给你内置的调式服务器，你难道就不访问你的web应用了吗？

所以由此，一个成熟的站点提供服务，必须要搭配 **Web 服务器** [静态数据] 和 **App 服务器**[动态数据]。注意，这是针对所有编程语言而言！

**Web 服务器**目前属 Nginx 最流行。类似的还有apache、IIS等，请求过来后（假设是下载一个文件），这里就是请求一个静态数据，我们一般是通过Nginx返回给请求客户端，因为如果你静态文件都要走 Python 程序，不是浪费机器性能嘛。

**App服务器**是用来处理动态数据，这里我们指的是python生成的动态数据，如提交表单等请求。理解他们我们需要知道**WSGI协议**。WSGI 是一种协议，不是任何包不是任何服务器，就和 TCP 协议一样。它定义了 Web 服务器和 Web 应用程序之前如何通信的规范。至于这个协议为什么和 Python 扯在一起？因为这个协议是由 Python 开发组在 2003 年提出的。基于这个协议，python才有了很多优秀的App服务器，如：uWSGI, gunicorn等

Nginx 是一个 Web 服务器其中的 HTTP 服务器功能和 uWSGI 功能很类似，但是 Nginx 还可以用作更多用途，比如最常用的**反向代理**功能。这样一般 Nginx 不处理业务逻辑，就转发请求给后端的 App 服务器处理。Nginx一般做请求转发，反向代理，静态文件，负载均衡等

还有在需要性能的场合下（如电商、直播网站高并发时），通常单单 nginx 和 uWSGI/gunicorn 也是不够的。nginx 主要优化的是连接数和静态文件。uwsgi/gunicorn 主要优化的是 wsgi 服务。这些都只是手段。其它手段包括，优化数据库，增加缓存，加入负载均衡器，前端优化(vue.js，react.js...)，引入异步 IO 框架，计算密集型模块用 C 重写等。网站安全性也要很多考虑。

### Python网站部署

Python 网站有很多种生产部署方式，但是只是技术选型的不同。较为流行的有：

**Nginx/Apache + Gunicorn/uWSGI + Tornado/Django/Flask + supervisor**

下面我们以前面编写过的Django应用来部署到生产环境！

我们采用 **Nginx + uWSGI/Gunicorn + Django + supervisor**

### 1. 手动部署方式

1. 本地项目生成requirement.txt
2. 生成初始化数据库脚本
3. 将本地项目提交到master分支并打包
4. 将包发布到生产环境
5. 连接生产，初始化数据库
6. 创建virtual环境，初始化依赖包
7. 修改项目配置，执行migration使用django默认服务器测试是否发布成功
8. **搭建web服务器与后台进程管理**
9. 进行模块测试和压力测试

注意：mysql-client安装可能报错，执行sudo apt-get install libmysqlclient-dev python3-dev解决

针对上面第8步，我们来搭建

#### 1.1 Nginx+uWSGI+Django+supervisor

1. 下载uwsgi, pip install uwsgi（虚拟环境), 创建uwsgi初始化文件，有多种方式，创建uwsgi.ini

```
[uwsgi]
;ip:端口（直接做web服务器，使用http）
http=127.0.0.1:8000
;项目路径
chdir=/home/coding/workspace/my_django/django_allwork_app
;wsgi文件路径
module=allwork.wsgi
processes=4
threads=2
master=True
;socket
socket=/home/coding/workspace/my_django/django_allwork_app/allwork.sock
chmod-socket=666
vacuum=true
;记录uwsgi的进程号，用uwsgi命令读取文件可结束进程
pidfile=uwsgi.pid
;开启日志
daemonize=uwsgi.log

```

2. 使用uwsgi启动项目 uwsgi --ini uwsgi.ini --其他命令：uwsgi --stop/reload uwsgi.pid

注意如有端口占用情况：killall -9 uwsgi

3. 下载nginx sudo apt-get install nginx（全局) 

4. 收集静态文件

django settings.py文件加上STATIC_ROOT='/var/www/daily/'

创建文件目录:sudo mkdir /var/www/daily，sudo chmod 777 /var/www/daily，python manage.py collectstatic

5. 在`/etc/nginx/conf.d`目录下，新建一个文件，叫做`allwork.conf`

```
upstream allwork{
    server unix:///home/coding/workspace/my_django/django_allwork_app/allwork.sock; 
}

# 配置服务器
server {
    # 监听的端口号
    listen      80;
    # 域名
    server_name 127.0.0.1; 
    charset     utf-8;

    # 最大的文件上传尺寸
    client_max_body_size 75M;  

    # 静态文件访问的url
    location /static {
        # 静态文件地址
        alias /var/www/daily/; 
    }
# 最后，发送所有非静态文件请求到django服务器
    location / {
        uwsgi_pass  allwork;
        # uwsgi_params文件地址
        include     /etc/nginx/uwsgi_params; 
    }
}

```

6. 启动nginx， sudo service start nginx，测试配置 service nginx configtest，改动配置后要重启nginx， service nginx restart
7. supervisor可以在uwsgi发生意外的情况下，会自动的重启。安装supervisor，pip install supervisor(全局安装)或sudo apt-get install supervisor
8. 项目根目录创建supervisor.conf

```
#supervisor的程序名字
[program:allwork]
#supervisor执行的命令
command=/home/coding/workspace/my_django/django_allwork_app/venv/bin/uwsgi --ini uwsgi.ini
#项目的目录
directory = /home/coding/workspace/my_django/django_allwork_app
#开始的时候等待多少秒
startsecs=0
#停止的时候等待多少秒
stopwaitsecs=0
#自动开始
autostart=true
#程序挂了后自动重启
autorestart=true
#输出的log文件
stdout_logfile=/home/coding/workspace/my_django/django_allwork_app/supervisord.log
#输出的错误文件
stderr_logfile=/home/coding/workspace/my_django/django_allwork_app/supervisord.err

[supervisord]
#log的级别
loglevel=info
#使用supervisorctl的配置
[inet_http_server]
supervisor的服务器
port = :9001
#用户名和密码
username = admin 
password = admin

[supervisorctl]
#使用supervisorctl登录的地址和端口号
serverurl = http://127.0.0.1:9001

username = admin 
password = admin

[rpcinterface:supervisor] 
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface 
```

supervisord -c supervisor.conf 使用supervisor启动uwsgi（记得先关闭uwsgi服务 killall -9 uwsgi)

supervisorctl -c supervisor.conf 进入supervisor客户端

* status # 查看状态 
* start program_name #启动程序 
* restart program_name #重新启动程序 
* stop program_name # 关闭程序 
* reload # 重新加载配置文件 
* quit # 退出控制台

#### 1.2 Nginx+gunicorn+Django+supervisor

1. 将安装uwsgi的步骤换成安装gunicorn，其他步骤一致
2. pip install gunicorn（虚拟环境）在django的setting文件添加'gunicorn'
3. 项目中创建gunicorn.conf.py

```
bind = "127.0.0.1:8088"
user = "root" 
```

4. 修改supervisor配置文件

```
...
#uwsgi
#command=/home/coding/workspace/my_django/django_allwork_app/venv/bin/uwsgi --ini uwsgi.ini
#gunicorn
command=/home/coding/workspace/my_django/django_allwork_app/venv/bin/gunicorn -c gunicorn.conf.py allwork.wsgi:application
...
```

5. 配置nginx，在`/etc/nginx/conf.d`目录下，新建一个文件，叫做`allwork2.conf`，重启nginx

```
# 配置服务器
server {
    # 监听的端口号
    listen      80;
    # 域名
    server_name 127.0.0.1; 
    charset     utf-8;

    # 最大的文件上传尺寸
    client_max_body_size 75M;  

    # 静态文件访问的url
    location /static {
        # 静态文件地址
        alias /var/www/daily/; 
    }
# 最后，发送所有非静态文件请求到django服务器
    location / {
      proxy_pass http://127.0.0.1:8088;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```



### 2. 自动化远程部署

可以看到手动部署方式步骤较多，想象下，如果时真正的生产项目，可能有几十到几百个模块，甚至是多个系统。这时候会采用分模块部署，这步骤是非常繁琐的，而且不能出错。所以有了现在的自动化部署技术。

python自动化部署工具我们推荐[fabric](https://blog.csdn.net/tichimi3375/article/details/82378807#fabric)

自动化测试、自动化运维、自动化部署、自动化监控等

自动化其实说白了就是写程序代替人类重复频繁的操作

### 3. Docker+Kubernetes(K8S)容器化

Linux容器虚拟技术(LXC)

虚拟机技术，如VMWare, OpenStack

容器技术：轻量级的虚拟化，占用空间小，可以同时运行几千个在主机上

Docker技术三大核心：

仓库-》镜像-》容器

仓库里有很多公共镜像，需要进行管理, Docker Registry服务，常用的就是Docker Hub

K8S: 基于容器的集群管理平台

