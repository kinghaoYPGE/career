from django.db.models import Q
from django.utils import timezone

from .models import Message, ChatRoom
from .signals import message_sent


class MessageService(object):
    def send_message(self, sender, recipient, message):
        message = Message(sender=sender, recipient=recipient, content=str(message))
        message.save()
        message_sent.send(sender=message, from_user=message.sender, to=message.recipient)
        return message, 200

    def get_unread_messages(self, user):
        return Message.objects.filter(recipient=user, read_at=None)

    def read_message(self, message_id):
        message = Message.objects.get(id=message_id)
        message.read_at = timezone.now()
        return message.content

