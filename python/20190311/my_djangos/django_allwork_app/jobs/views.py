from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, RedirectView
from .models import Job, JobProposal


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
        proposal.job = self.kwargs['job']
        proposal.freelancer = self.request.user
        proposal.save()
        return redirect('users:job_profile', self.request.user.username)


class ProposalAcceptView(RedirectView):
    pattern_name = 'jobs:job_detail'

    def get_redirect_url(self, *args, **kwargs):
        job = get_object_or_404(Job, pk=kwargs.get('pk'))
        job.status = 'working'
        job.save()
        return super().get_redirect_url(*args, **kwargs)
