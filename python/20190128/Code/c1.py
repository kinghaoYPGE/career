"""
python常用内建模块
"""
# base64: 用64个字符表示任意二进制数据, 二进制编码
# 网络上传输二进制文件可以通过base64转换成字符
import base64
r = base64.b64encode(b'hello python')
print(r.decode())
r = base64.b64decode(r)
print(r)

# struct: 把数字转换成字节数据
n = 101010301
import struct
n = struct.pack('>I', n)
print(n)
n = struct.unpack('>I', n)
print(n)

# hashlib 哈希算法:摘要算法 如MD5, SHA1
# 把任意长度数据转换成固定长度的字符串(用16进制字符串表示)
import hashlib
md5 = hashlib.md5()
target_str = 'life is short, i use python'
md5.update(target_str.encode('utf-8'))
print(md5.hexdigest())

my_str = 'life is short, i use Python'
md5.update(my_str.encode('utf-8'))
print(md5.hexdigest())
# md5算法应用:网站登录密码

# hmac: 防止黑客通过哈希值返回原始口令
# 在计算哈希值时， 增加一个salt（加盐) 使相同输入得到不同哈希值
import hmac
msg = b'abc'
key = b'secret'
h_value = hmac.new(key, msg, digestmod='MD5')
print(h_value.hexdigest())
