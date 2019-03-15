from django.core.exceptions import ValidationError
from .models import User
from django import forms
from django.utils.translation import ugettext_lazy as _


def forbidden_username_validator(value):
    """
    用户注册禁用词
    :param value:
    :return:
    """
    forbidden_username = {
        'signup' 'user', 'community',
    }

    if value in forbidden_username:
        raise ValidationError(_('This is a forbidden word.'))


def invalid_username_validator(value):
    """
    校验用户名是否包含非法字符
    :param value:
    :return:
    """
    if '@' in value:
        raise ValidationError(_('Invalid username.'))


def unique_email_validator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError(_('Email have already registered.'))


def unique_username_validator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError(_('Username have already registered.'))


class SignUpForm(forms.ModelForm):
    """
    注册表单对象
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30, required=True, label=_('Username'),
        help_text=_('Username should contains number or word or _.')
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=_('Password'), required=True,
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=_('Confirm your password'), required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True, max_length=100, label=_('Email')
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        """
        验证表单数据合法性
        """
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators += [
            forbidden_username_validator, invalid_username_validator,
            unique_username_validator,
        ]
        self.fields['email'].validators += [
            unique_email_validator,
        ]

    def clean_password(self):
        """
        验证两次密码输入是否一致
        :return:
        """
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            msg = _("Password not match.")
            self.add_error('confirm_password', msg)

        return password

    def clean(self):
        self.clean_password()
        super(SignUpForm, self).clean()

    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
