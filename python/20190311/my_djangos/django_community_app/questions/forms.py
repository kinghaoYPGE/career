from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        label=_('Title'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        max_length=2000,
        label=_('Description'),
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        help_text=_('Write description here.')
    )

    class Meta:
        model = Question
        fields = ['title', 'description']


class AnswerForm(forms.ModelForm):
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        help_text=_('Write answer here.')
    )

    class Meta:
        model = Answer
        fields = ['description']
