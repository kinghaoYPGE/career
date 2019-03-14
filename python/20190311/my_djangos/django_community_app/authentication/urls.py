from django.urls import path
from .views import UserSignUpView
from django.contrib.auth import views as auth_view

app_name = 'authentication'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
]
