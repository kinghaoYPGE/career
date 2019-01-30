"""
requests请求url:
使用更加方便,封装了很多高级功能
"""
import requests
# r = requests.get('http://www.douban.com')
# print(r.status_code)
# print(r.text)

# 带参数的请求
r = requests.get('https://www.douban.com/search', params={'cat': '1002', 'q': 'python'})
print(r.url)
print(r.encoding)

# 访问api(得到json字符串转换成字典)
r = requests.get('https://api.douban.com/v2/book/2129650')
print(type(r.json()))
print(r.json())

# add header
r = requests.get('http://www.douban.com', headers={'Use-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'})
# print(r.text)

# 模拟post请求
r = requests.post('https://accounts.douban.com/passport/login', data={'form_email':'abc', 'form_password':'asdf'})
print(r.text)
