from django.db import models
from django.conf import settings


class ChatRoom(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  related_name='chatroom_sender')

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  related_name='chatroon_recipient')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('sender', 'recipient', )


class Message(models.Model):
    content = models.TextField('Content')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='send_msg')

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='recipient_msg')

    sent_at = models.DateTimeField('send at', auto_now_add=True)
    read_at = models.DateTimeField('read at', blank=True, null=True)

    class Meta:
        ordering = ['-sent_at']

    @property
    def unread(self):
        if not self.read_at:
            return True
