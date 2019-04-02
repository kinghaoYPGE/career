# 一、OAuth2.0

## 1 OAuth原理

OAuth（开放授权 Open Authorization）是一个开放标准，允许用户授权第三方网站访问他们存储在另外的服务提供者上的信息，而不需要将用户名和密码提供给第三方网站或分享他们数据的所有内容。 

注意: OAuth是一种认证协议，有自己的规则，详细的协议、格式定义等，他是一个技术标准。所以OAuth也分客户端实现(如：第三方登陆)和服务端实现(如：实现认证服务器、SSO-单点登陆)。

**OAuth 2.0 有四种授权类型：**

- **授权码授权（适用于 Web 应用, 推荐）**
- 隐式授权 （适用于移动应用）
- 用户密码授权 （不推荐使用）
- 客户端授权 (适用于后端应用)

**认证流程包括（授权码模式)：**

1. 获取授权Code
2. 利用Code请求Access Token (令牌)
3. 利用令牌请求用户的Openid及其用户信息 （每个用户拥有唯一的Openid，因此可以通过Openid标识用户） 

![](https://img-blog.csdn.net/20180125183255263?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvemp3X3B5dGhvbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

回调地址就是你接受code的url，要在第三方登录平台上填写，这样才能把code传递给你的网站。

举个例子：豆瓣的qq登陆功能

![img](https://images2017.cnblogs.com/blog/1096103/201708/1096103-20170824142737402-1297004164.png)



## 2 OAuth第三方登陆

这里我们以先前的django项目(QA)为例，新加github登陆功能

代码如下：

base.html

```html
...
<li></li>
                            <li>
                                <div id="oauth_button">
                                    <div class="pull-right">
                                        <a href="{% url 'oauth:github_login' %}"><img width="15px" height="15px" class="type" src="{% static 'img/github.png' %}" alt="GITHUB"/></a>&nbsp;
                                        <a href="#"><img width="15px" height="15px" class="type" src="{% static 'img/QQ.png' %}" alt="QQ"/></a>&nbsp;
                                        <a href="#"><img width="15px" height="15px" class="type" src="{% static 'img/weibo.png' %}" alt="WEIBO"/></a>
                                    </div>
                                </div>
                            </li>
```

settings.py

```python
#Oauth
#github
GITHUB_APP_ID = '************'
GITHUB_KEY = '************'
GITHUB_CALLBACK_URL = 'http://127.0.0.1:8000/oauth/github_check'  #填写你的回调地址

```

models.py

```python
from django.db import models

type = (
    ('1', 'github'),
)


class OAuth(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    openid = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=1, choices=type)
```

urls.py

```python
from django.urls import path
from . import views

app_name = 'oauth'

urlpatterns = [
    path('github_login', views.git_login, name='github_login'),
    path('github_check', views.git_check, name='github_check'),
]
```

client.py

```python
import json
import urllib
import re


class OAuthBase(object):  # 基类，将相同的方法写入到此类中
    def __init__(self, client_id, client_key, redirect_url):  # 初始化，载入对应的应用id、秘钥和回调地址
        self.client_id = client_id
        self.client_key = client_key
        self.redirect_url = redirect_url

    def _get(self, url, data):  # get方法
        request_url = '%s?%s' % (url, urllib.parse.urlencode(data))
        response = urllib.request.urlopen(request_url)
        return response.read()

    def _post(self, url, data):  # post方法
        request = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(encoding='utf-8'))  # 1
        response = urllib.request.urlopen(request)
        return response.read()

    # 下面的方法，不同的登录平台会有细微差别，需要继承基类后重写方法

    def get_auth_url(self):  # 获取code
        pass

    def get_access_token(self, code):  # 获取access token
        pass

    def get_open_id(self):  # 获取openid
        pass

    def get_user_info(self):  # 获取用户信息
        pass

    def get_email(self):  # 获取用户邮箱
        pass


# Github类
class OAuthGitHub(OAuthBase):
    def get_auth_url(self):
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_url,
            'scope': 'user:email',
            'state': 1
        }
        url = 'https://github.com/login/oauth/authorize?%s' % urllib.parse.urlencode(params)
        return url

    def get_access_token(self, code):
        params = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_key,
            'code': code,
            'redirect_url': self.redirect_url
        }
        response = self._post('https://github.com/login/oauth/access_token', params)  # 此处为post方法
        result = urllib.parse.parse_qs(response, True)
        self.access_token = result[b'access_token'][0]
        return self.access_token

    # github不需要获取openid，因此不需要get_open_id()方法

    def get_user_info(self):
        params = {'access_token': self.access_token}
        response = self._get('https://api.github.com/user', params)
        result = json.loads(response.decode('utf-8'))
        self.openid = result.get('id', '')
        return result

    def get_email(self):
        params = {'access_token': self.access_token}
        response = self._get('https://api.github.com/user/emails', params)
        result = json.loads(response.decode('utf-8'))
        return result[0]['email']
```

views.py

```python
from django.shortcuts import redirect
from django.conf import settings
from authentication.models import User
from .client import OAuthGitHub
from .models import OAuth
from django.contrib.auth import login as auth_login
import time
import uuid


def git_login(request):  # 获取code
    oauth_git = OAuthGitHub(settings.GITHUB_APP_ID, settings.GITHUB_KEY, settings.GITHUB_CALLBACK_URL)
    url = oauth_git.get_auth_url()
    return redirect(url)


def git_check(request):
    request_code = request.GET.get('code')
    oauth_git = OAuthGitHub(settings.GITHUB_APP_ID, settings.GITHUB_KEY, settings.GITHUB_CALLBACK_URL)
    try:
        access_token = oauth_git.get_access_token(request_code)  # 获取access token
        time.sleep(0.1)  # 此处需要休息一下，避免发送urlopen的10060错误
    except:  # 获取令牌失败，反馈失败信息
        return redirect('home')
    infos = oauth_git.get_user_info()  # 获取用户信息
    nickname = infos.get('login', '')
    image_url = infos.get('avatar_url', '')
    open_id = str(oauth_git.openid)
    signature = infos.get('bio', '')
    if not signature:
        signature = "无个性签名"
    githubs = OAuth.objects.filter(openid=open_id, type='1')  # 查询是否该第三方账户已绑定本网站账号
    if githubs:  # 若已绑定，直接登录
        auth_login(request, githubs[0].user)
        return redirect('home')
    else:  # 否则尝试获取用户邮箱用于绑定账号
        try:
            email = oauth_git.get_email()
        except:  # 若获取失败，则跳转到绑定用户界面，让用户手动输入邮箱
            return redirect('home')
    users = User.objects.filter(email=email)  # 若获取到邮箱，则查询是否存在本站用户
    if users:  # 若存在，则直接绑定
        user = users[0]
    else:  # 若不存在，则新建本站用户
        while User.objects.filter(username=nickname):  # 防止用户名重复
            nickname = nickname + '*'
        user = User(username=nickname, email=email)
        pwd = str(uuid.uuid1())  # 随机设置用户密码
        user.set_password(pwd)
        user.save()
    oauth = OAuth(user=user, openid=open_id, type=type)
    oauth.save()  # 保存后登陆
    auth_login(request, user)
    return redirect('home')
```

# 二、Python图像处理

## 1 图像基本属性

位图与矢量图

图像主要分为两类：一类是位图，一类是矢量图。

位图是由多个像素组成的，当放大位图时，可以看见图像被分成了很多色块（锯齿效果），而且放大的位图属于失真状态。我们平时拍的照片、扫描的图片等都属于位图。

矢量图是通过数学公式计算获得的图像，它最大的特点是无论放大多少倍都不失真，而且文件小、分辨率高，缺点是难以表现色彩层次丰富的逼真图像效果。

像素(px)：像素是构成位图图像最基本的单元，每个像素都有自己的颜色（RGB)，像素越多，颜色信息就越丰富，图像效果就越好

分辨率(dpi)：是单位长度内包含像素点的数量，通常以像素每英寸ppi(pixels per inch)为单位来表示图像分辨率的大小，例如分辨率为72ppi表示每英寸包含72个像素点，分辨率越高，包含的像素点就越多，图像就越清晰，但占用的存储空间就越大。分辨率分为屏幕分辨率和图像分辨率，例如：屏幕分辨率是1280×720，就是屏幕的水平方向上有1280个像素点，垂直方向上有720个像素点；一张图片分辨率是800×500，就是说图片在没有缩放的前提下，水平方向有800个像素点，垂直方向有500个像素点。

像素与分辨率的关系：二者关系密不可分，它们的组合决定了图像的质量。分辨率=图像水平方向的像素点数×图像垂直方向的像素点数。例如1英寸×1英寸，分辨率为100dpi的图像包含10000个像素（100像素×100像素）。

灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像。

RGB色彩模式是工业界的一种颜色标准，是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色的，RGB即是代表红、绿、蓝三个通道的颜色，这个标准几乎包括了人类视力所能感知的所有颜色，是目前运用最广的颜色系统之一。

灰度值与RGB转换公式（简化版本):

gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b

## 2 Pillow库操作图像

PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。

由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫[Pillow](https://github.com/python-pillow/Pillow)，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。

官方文档：<https://pillow.readthedocs.org/>

```python
from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

from PIL import Image, ImageFilter
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

#PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
```

## 3 Pillow实战

### 3.1 验证码登陆

login.html

```html
...
<img src="{% url 'authentication:code' %}" onclick="this.src=this.src+'?'+Math.random()" /><br><br>
```

utils.py

```python
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def create_lines(draw):
    '''绘制干扰线'''

    for i in range(4):
        # 起始点
        begin = (random.randint(0, 320), random.randint(0, 30))
        # 结束点
        end = (random.randint(0, 320), random.randint(0, 30))
        draw.line([begin, end], fill=(0, 0, 0))


def create_verify_code():
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('./static/fonts/seguiemj.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    create_lines(draw)
    # 输出文字:
    codes = ''
    for t in range(4):
        random_char = rndChar()
        draw.text((60 * t + 10, 10), random_char, font=font, fill=rndColor2())
        codes += random_char
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    # image.save('code.jpg', 'jpeg')
    return image, codes
```

urls.py

```python
from django.urls import path
from .views import UserSignUpView, verify_code, LoginView
from django.contrib.auth import views as auth_view

app_name = 'authentication'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('code/', verify_code, name='code'),
]
```

views.py

```python
from .forms import SignUpForm, LoginForm
from .utils import create_verify_code
from django.contrib.auth import views as auth_view
from io import BytesIO

class LoginView(auth_view.LoginView):
    """
    用户登陆
    """
    authentication_form = LoginForm
    template_name = 'authentication/login.html'

    def form_valid(self, form):
        if self.request.session['verify_code'] != form.cleaned_data['verify_code']:
            form.add_error('verify_code', ValidationError('Invalid Verify Code.'))
            return super().form_invalid(form)
        return super().form_valid(form)


def verify_code(request):
    image, code = create_verify_code()
    buf = BytesIO()
    image.save(buf, 'jpeg')
    response = HttpResponse(content=buf.getvalue(), content_type='image/gif')
    request.session['verify_code'] = code
    return response
```

forms.py

```python
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    verify_code = forms.CharField(
        widget=forms.TextInput(),
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'verify_code']
```



### 3.2 图片转字符

```python
from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
```

