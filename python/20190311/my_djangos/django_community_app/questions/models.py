from django.db import models
from authentication.models import User
from markdown import markdown


class Question(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-update_date', ]

    def __str__(self):
        return self.title

    def get_description_as_markdown(self):
        desc = markdown(self.description)
        return desc


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date', ]

    def __str__(self):
        return self.description

    def get_description_as_markdown(self):
        desc = markdown(self.description)
        return desc
