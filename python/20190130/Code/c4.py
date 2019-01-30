"""
服务端
服务器进程要先绑定一个端口监听其他客户端的请求连接
如果请求过来了，服务器与其建立连接，进行通信
服务器一般使用固定端口(80)监听
为了区分socket连接是和哪个客户端进程般的，所以需要4个参数去区分：
1. 服务器地址 2. 客户端地址 3. 服务端端口 4 客户端端口
"""
import socket
import threading
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址
s.bind(('127.0.0.1', 8000))
# 进行监听
s.listen(5) # 等待连接的最大数量
print('connecting...')
# 接受客户端的连接

def process_tcp(sock, addr):
    print('new connection from %s:%s' % (addr))
    sock.send(b'welcome my home')
    while True:
        # 处理请求
        data = sock.recv(1024)
        time.sleep(1)
        if not data:
            break
        sock.send(b'hello %s' % data)
    sock.close()
    print('conection from %s:%s closed' % addr)
while True:
    # 接受新连接
    sock, addr = s.accept()
    # 创建新的线程来处理TCP连接
    t = threading.Thread(target=process_tcp, args=(sock, addr))
    t.start()

