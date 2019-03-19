from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_view
from .views import (
    SignUpView, UserDetailView, UpdateProfileView,
    FreelancerSignUpView, ListFreelancersView, UserJobProfileView,
    OwnerSignUpView)

app_name = 'users'

urlpatterns = [
    # 认证路由
    path('accounts/', include([
        path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
        path('logout/', auth_view.LogoutView.as_view(), name='logout'),
        path('signup/', SignUpView.as_view(), name='signup'),
        path('signup/freelancer/', FreelancerSignUpView.as_view(), name='freelancer_signup'),
        path('signup/owner/', OwnerSignUpView.as_view(), name='owner_signup'),
    ])),
    # 自由竞争者列表路由
    path('freelancers/', ListFreelancersView.as_view(), name='list_freelancer'),
    # 个人信息路由
    path('user/', include([
        path('<int:pk>/edit', UpdateProfileView.as_view(), name='update_profile'),
        path('<str:username>/', UserDetailView.as_view(), name='user_profile'),
        path('<str:username>/jobs/', UserJobProfileView.as_view(), name='job_profile'),
    ])),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
