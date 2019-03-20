from django.db.models import Q
from django.utils import timezone

from .models import Message, ChatRoom
from .signals import message_sent, message_read


class MessageService(object):

    @staticmethod
    def send_message(sender, recipient, message):
        message = Message(sender=sender, recipient=recipient, content=str(message))
        message.save()
        message_sent.send(sender=message, from_user=message.sender, to=message.recipient)
        return message, 200

    @staticmethod
    def get_unread_messages(user):
        return Message.objects.filter(recipient=user, read_at=None)

    @staticmethod
    def read_message(message_id):
        message = Message.objects.get(id=message_id)
        MessageService.__mark_as_read(message)
        return message.content

    def __mark_as_read(message):
        if message.read_at is None:
            message.read_at = timezone.now()
            message_read.send(sender=message, from_user=message.sender, to=message.recipient)
            message.save()

    @staticmethod
    def read_message_formatted(message_id):
        message = Message.objects.get(id=message_id)
        MessageService.__mark_as_read(message)
        return message.sender.username + ": " + message.content

    @staticmethod
    def get_active_conversations(sender, recipient):
        active_conversations = Message.objects.filter(
            (Q(sender=sender) & Q(recipient=recipient)) |
            (Q(sender=recipient) & Q(recipient=sender))
        ).order_by('sent_at')
        return active_conversations

    @staticmethod
    def get_conversations(user):
        chatrooms = ChatRoom.objects.filter(Q(sender=user) | Q(recipient=user))
        chatroom_mapper = []
        for chatroom in chatrooms:
            chatroom_dict = {}
            chatroom_dict['pk'] = chatroom.pk
            if user == chatroom.sender:
                recipient = chatroom.recipient
            else:
                recipient = chatroom.sender
            chatroom_dict['recipient'] = recipient
            chatroom_mapper.append(chatroom_dict)
        return chatroom_mapper

