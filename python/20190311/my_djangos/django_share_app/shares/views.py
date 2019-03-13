import json

from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
import os
from .models import Upload


class IndexView(ListView):
    template_name = 'base.html'
    context_object_name = 'upload_list'

    def get_queryset(self):
        return Upload.objects.order_by('-upload_time')

    def post(self, request):
        if request.FILES:
            file = request.FILES.get('file')
            # check_file
            file_name = file.name
            # rename_file
            file_size = int(file.size)
            # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            path = os.path.join('shares/static/file', file_name)
            with open(path, 'wb') as f:
                f.write(file.read())

            Upload(
                file_name=file_name,
                file_size=file_size,
                file_path='static/file/'+file_name,
                ip_addr=str(request.META['REMOTE_ADDR'])
            ).save()
            return HttpResponseRedirect(reverse('shares:index'))


def my_list(request):
    ip_addr = request.META['REMOTE_ADDR']
    context = Upload.objects.filter(ip_addr=ip_addr).order_by('-upload_time')
    return render(request, 'base.html', {'upload_list': context})


def search(request):
    kwords = request.GET.get('kw')
    results = Upload.objects.filter(Q(file_name__icontains=kwords))
    if results:
        return HttpResponse(json.dumps([result.to_dict() for result in results]), content_type='application/json')
    else:
        raise Http404()
