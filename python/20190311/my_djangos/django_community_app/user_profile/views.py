from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator

from .models import Profile
from authentication.models import User

from django.views.generic import TemplateView, UpdateView


@method_decorator([login_required], name='dispatch')
class ProfileDetailView(TemplateView):
    model = Profile
    template_name = 'user_profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id')
        context['user'] = User.objects.get(id=user_id)
        context['profile'] = Profile.objects.get(id=user_id)
        return context


@method_decorator([login_required], name='dispatch')
class UpdateProfileView(UpdateView):
    model = Profile
    fields = ['avatar', 'url', 'location', 'job_title']
    template_name = 'user_profile/profile_update.html'

    def get_object(self, queryset=None):
        return Profile.objects.get(user_id=self.kwargs.get('user_id'))

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.save()
        form.save_m2m()
        # 重定向到用户详情页
        return redirect('user_profile:profile', self.kwargs.get('user_id'))

    def get_success_url(self):
        return reverse('user_profile:profile', self.kwargs.get('user_id'))

