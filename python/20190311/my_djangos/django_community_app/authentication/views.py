from io import BytesIO

from django.contrib.auth import login
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView
from .models import User
from .forms import SignUpForm, LoginForm
from .utils import create_verify_code
from django.contrib.auth import views as auth_view


class UserSignUpView(CreateView):
    """
    用户注册
    """
    model = User
    form_class = SignUpForm
    template_name = 'authentication/signup.html'

    def form_valid(self, form):
        """
        保存用户并登陆, 重定向到主页
        :param form:
        :return:
        """
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginView(auth_view.LoginView):
    authentication_form = LoginForm
    template_name = 'authentication/login.html'

    def form_valid(self, form):
        if self.request.session['verify_code'] != form.cleaned_data['verify_code']:
            form.add_error('verify_code', ValidationError('Invalid verify code.'))
            return super().form_invalid(form)
        return super().form_valid(form)


def verify_code(request):
    image, code = create_verify_code()
    buf = BytesIO()  # 缓冲流
    image.save(buf, 'jpeg')
    response = HttpResponse(content=buf.getvalue(), content_type='image/gif')
    request.session['verify_code'] = code
    return response
