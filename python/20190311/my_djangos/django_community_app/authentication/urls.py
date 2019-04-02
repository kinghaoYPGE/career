from django.urls import path
from .views import UserSignUpView, LoginView, verify_code
from django.contrib.auth import views as auth_view

app_name = 'authentication'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('code/', verify_code, name='code'),
]
