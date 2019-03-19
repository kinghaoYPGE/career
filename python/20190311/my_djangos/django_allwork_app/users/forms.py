from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction
from .models import User


class UserCreationForm(forms.ModelForm):
    """创建用户表单(注册和admin创建用户)"""
    username = forms.CharField(max_length=100, required=True, help_text='Required.')
    first_name = forms.CharField(max_length=100, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=100, required=True, help_text='Required.')
    email = forms.EmailField(max_length=200, required=True, help_text='Required')

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """用户修改表单"""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('password', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_admin')


class FreelancerSignUpForm(UserCreationForm):

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_freelancer = True
        if commit:
            user.save()
        return user


class OwnerSignUpForm(UserCreationForm):

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_owner = True
        if commit:
            user.save()
        return user
