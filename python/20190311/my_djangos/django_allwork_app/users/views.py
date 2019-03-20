from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import (
    TemplateView, UpdateView, CreateView, ListView
)
from .models import User
from .forms import FreelancerSignUpForm, OwnerSignUpForm


class SignUpView(TemplateView):
    template_name = 'users/signup.html'


class UserDetailView(TemplateView):
    model = User
    template_name = 'users/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username')
        context['profile'] = User.objects.get(username=username)
        return context


class UpdateProfileView(UpdateView):
    model = User
    fields = ['profile_photo', 'first_name', 'last_name', 'profile', ]
    template_name = 'users/user_profile_update.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        # 自定义字段
        user.save()
        form.save_m2m()
        messages.success(self.request, 'Profile update successfully.')
        return redirect('users:user_profile', self.object.username)


class ListFreelancersView(ListView):
    model = User
    context_object_name = 'freelancers'
    template_name = 'users/freelancer_list.html'

    def get_queryset(self):
        return User.objects.filter(is_freelancer=True)


class FreelancerSignUpView(CreateView):
    model = User
    form_class = FreelancerSignUpForm
    template_name = 'users/signup_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'freelancer'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = 'users/signup_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'project owner'
        return context

    def form_valid(self, form):
        print(form.__dict__)
        user = form.save()
        login(self.request, user)
        return redirect('home')


class UserJobProfileView(TemplateView):
    model = User
    template_name = 'users/user_job_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username')
        context['user'] = User.objects.get(username=username)
        return context

