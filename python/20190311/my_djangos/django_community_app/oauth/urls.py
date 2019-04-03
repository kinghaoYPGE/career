from django.urls import path
from . import views

app_name = 'oauth'

urlpatterns = [
    path('oauth/github_login', views.git_login, name='github_login'),
    path('oauth/github_check', views.git_check, name='github_check'),
]
