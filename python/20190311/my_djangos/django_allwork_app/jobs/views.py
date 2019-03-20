from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, RedirectView
from .models import Job, JobProposal
from chats.models import ChatRoom
from users.models import User
from chats.services import MessageService

class JobListView(ListView):
    model = Job
    ordering = ('-date_modified', )
    context_object_name = 'jobs'
    template_name = 'jobs/job_list.html'
    queryset = Job.objects.all()


@method_decorator([login_required], name='dispatch')
class JobCreateView(CreateView):
    model = Job
    fields = ('job_title', 'job_description', 'price', 'tags', 'document')
    template_name = 'jobs/job_add_form.html'

    def form_valid(self, form):
        job = form.save(commit=False)
        job.owner = self.request.user
        job.save()
        form.save_m2m()
        return redirect('jobs:job_detail', job.pk)


@method_decorator([login_required], name='dispatch')
class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'

    def get_context_data(self, **kwargs):
        job_id = self.kwargs.get('pk')
        job = Job.objects.get(pk=job_id)
        if job.owner != self.request.user and self.request.user in job.freelancers:
            print(job)
            kwargs['current_proposal'] = JobProposal.objects.get(
                job__pk=job_id,
                freelancer=self.request.user
            )
        context = super().get_context_data(**kwargs)
        return context


@method_decorator([login_required], name='dispatch')
class JobApplyView(CreateView):
    model = JobProposal
    fields = ('proposal', )
    template_name = 'jobs/job_apply_form.html'

    def get_context_data(self, **kwargs):
        job_id = self.kwargs.get('pk')
        kwargs['job'] = Job.objects.get(pk=job_id)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        proposal = form.save(commit=False)
        proposal.job = Job.objects.get(pk=self.kwargs['pk'])
        proposal.freelancer = self.request.user
        proposal.save()
        return redirect('users:job_profile', self.request.user.username)


class ProposalAcceptView(RedirectView):
    pattern_name = 'jobs:job_detail'

    def get_redirect_url(self, *args, **kwargs):
        job = get_object_or_404(Job, pk=kwargs.get('pk'))
        job.freelancer = User.objects.get(username=kwargs.get('username'))
        job.status = 'working'
        job.save()
        chatroom = ChatRoom.objects.create(sender=self.request.user, recipient=job.freelancer)
        MessageService().send_message(
            sender=self.request.user,
            recipient=job.freelancer,
            message="""
            Hi {username}, your proposal have been accepted.
            Project details: <a href='{url}'>{job}</a>
            """.format(
                username=job.freelancer.username,
                url=reverse('jobs:job_detail', kwargs={'pk': job.pk}),
                job=job.job_title
            )
        )
        messages.success(self.request, 'User: {} is assiged to your project'.format(
            kwargs.get('username')
        ))
        return super().get_redirect_url(*args, pk=kwargs.get('pk'))


class JobCloseView(RedirectView):
    pattern_name = 'jobs:job_detail'

    def get_redirect_url(self, *args, **kwargs):
        job = get_object_or_404(Job, pk=kwargs.get('pk'))
        job.status = 'ended'
        job.save()
        messages.warning(self.request, 'Job have ended successfully.')
        return super().get_redirect_url(*args, pk=kwargs.get('pk'))
