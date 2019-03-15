from django.db import models
from authentication.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    url = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='pic_folder/%Y%m%d/', default='img/user.png')


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# 使用信号：当用户创建时自动创建profile
post_save.connect(create_user_profile, sender=User)

post_save.connect(save_user_profile, sender=User)
