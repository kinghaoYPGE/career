from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import RedirectView, CreateView
from .models import ChatRoom, Message
from .forms import MessageForm
from .services import MessageService


class MessageView(RedirectView):
    pattern_name = 'chats:user_message'

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        chatroom = ChatRoom.objects.filter(Q(sender=user) | Q(recipient=user)).first()

        if chatroom:
            return super().get_redirect_url(*args, pk=chatroom.pk)
        return reverse('jobs:job_list')


class MessageDetailView(CreateView):
    model = ChatRoom
    form_class = MessageForm
    template_name = 'chats/direct_messages.html'

    def get_context_data(self, **kwargs):
        chat_id = self.kwargs.get('pk')
        chatroom = ChatRoom.objects.get(pk=chat_id)
        message = Message.objects.filter(
            sender=chatroom.sender,
            recipient=chatroom.recipient
        ).first()
        kwargs['active_conversation'] = message
        user = self.request.user
        current_conversations = MessageService.get_conversations(user=user)
        kwargs['conversations'] = current_conversations

        if user == message.sender:
            active_recipient = message.recipient
        else:
            active_recipient = message.sender
        running_conversations = MessageService.get_active_conversations(user, active_recipient)
        kwargs['running_conversations'] = running_conversations
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        obj = self.get_object()
        if self.request.user == obj.sender:
            recipient = obj.recipient
        else:
            recipient = obj.sender

        message = form.save(commit=False)
        message.sender = self.request.user
        message.recipient = recipient

        message.save()
        return redirect('chats:user_message', obj.pk)
