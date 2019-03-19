from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, username, email, password, **kwargs):
        """创建普通用户"""
        if not email:
            raise ValueError('User must have a valid email address.')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name'),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **kwargs):
        """创建超级用户"""
        user = self.create_user(
            username, email, password, **kwargs
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    # 用户简介
    profile_photo = models.ImageField(upload_to='pic_folder/%Y%m%d', default='pic_folder/default.jpg')
    profile = models.TextField(null=True, blank=True)

    # 用户角色
    is_owner = models.BooleanField('project_owner status', default=False)
    is_freelancer = models.BooleanField('freelancer status', default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # admin
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']  # createsuperuser 创建admin时的字段
