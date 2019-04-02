from django.db import models

type = (
    ('1', 'github'),
    # qq..
)


class OAuth(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    openid = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=1, choices=type)

