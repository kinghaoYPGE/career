from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    content = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput()
    )

    class Meta:
        model = Message
        fields = ['content']
