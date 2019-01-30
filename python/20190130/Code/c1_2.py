"""
通过urllib模拟浏览器发送get请求
"""
from urllib import request, parse

# req = request.Request('http://www.douban.com')
# req.add_header('User-Agent', ' Mozilla/5.0 (Windows NT 10.0; WOW64)\
                                # AppleWebKit/537.36 (KHTML, like Gecko) \
                                # Chrome/71.0.3578.98 Safari/537.36')
# req.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1')                                
# with request.urlopen(req) as resp:
#     print(resp.read().decode())

"""
模拟浏览器发送post请求
"""
email = input('Email:')
pwd = input('Password:')
login_data = parse.urlencode([
    ('username', email),
    ('password', pwd),
    ('entry', 'mweibo'),     
    ('client_id', ''),     
    ('savestate', '1'),     
    ('ec', ''),     
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2 Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login') 
req.add_header('Origin', 'https://passport.weibo.cn') 
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25') 
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349& r=http%3A%2F%2Fm.weibo.cn%2F') 
 
with request.urlopen(req, data=login_data.encode('utf-8')) as f:     
    print('Status:', f.status, f.reason)     
    for k, v in f.getheaders():         
        print('%s: %s' % (k, v))     
        print('Data:', f.read().decode('utf-8')) 

# Handler: Proxy 代理IP
