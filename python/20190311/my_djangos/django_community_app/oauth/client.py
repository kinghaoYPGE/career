import json
import urllib
from urllib import parse, request


class OAuthBase(object):
    def __init__(self, client_id, client_key, redirect_url):
        self.client_id = client_id
        self.client_key = client_key
        self.redirect_url = redirect_url

    def _get(self, url, data):
        request_url = '%s?%s' % (url, parse.urlencode(data))
        print('request url: ', request_url)
        response = request.urlopen(request_url)
        return response.read()

    def _post(self, url, data):
        req = request.Request(url, data=parse.urlencode(data).encode('utf-8'))
        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e)
            raise
        return response.read()

    def get_auth_url(self):
        pass

    def get_access_token(self, code):
        pass

    def get_open_id(self):
        pass

    def get_user_info(self):
        pass

    def get_email(self):
        pass


class OAuthGitHub(OAuthBase):
    """github授权登陆"""
    def get_auth_url(self):
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_url,
            'scope': 'user:email',
            'state': 1,
        }
        url = 'https://github.com/login/oauth/authorize?%s' % parse.urlencode(params)
        return url

    def get_access_token(self, code):
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_key,
            'code': code,
            'redirect_uri': self.redirect_url,
            'scope': 'user:email',
        }
        url = 'https://github.com/login/oauth/access_token'
        response = self._post(url, params)
        result = parse.parse_qs(response)
        self.access_token = result[b'access_token'][0]
        return self.access_token

    def get_user_info(self):
        params = {'access_token': self.access_token}
        response = self._get('https://api.github.com/user', params)
        result = json.loads(response.decode('utf-8'))
        print('get_user_info: ', result)
        self.openid = result.get('id', '')
        return result

    def get_email(self):
        params = {'access_token': self.access_token}
        response = self._get('https://api.github.com/user/emails', params)
        result = json.loads(response.decode('utf-8'))
        print('get_email: ', result)
        return result[0]['email']



