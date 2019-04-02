from django.shortcuts import render

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
    except Exception as e:  # 获取令牌失败，反馈失败信息
        print(e)
        return redirect('home')
    print('access_token: ', access_token)
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
        except Exception as e:  # 若获取失败，则跳转到绑定用户界面，让用户手动输入邮箱
            print(e)
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
    oauth = OAuth(user=user, openid=open_id, type='1')
    oauth.save()  # 保存后登陆
    auth_login(request, user)
    return redirect('home')
