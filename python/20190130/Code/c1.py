"""
python内置模块请求网络模块: urllib
用于操作url
"""
from urllib import request
with request.urlopen(r'http://www.douban.com') as response:
    data = response.read().decode()
    """
    http 请求头:
    Request URL: https://www.douban.com/
    Request Method: GET-POST-PUT-DELETE(REST)
    Status Code: 200 OK 404, 500
    Remote Address: 154.8.131.171:443
    Referrer Policy: no-referrer-when-downgrade
    """
    print('Status:',response.status, response.reason)
    print(response.getheaders())
    print(data)


    



