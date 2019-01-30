"""
网络编程: socket
"""
# 模拟客户端访问新浪
import socket
# 创建连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 8000))
print(s.recv(1024).decode())
for data in [b'zhangsan', b'lisi', b'grace']:
    s.send(data)
    print(s.recv(1024).decode())
s.close()