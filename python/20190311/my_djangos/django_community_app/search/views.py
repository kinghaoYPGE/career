from django.db.models import Q
from django.shortcuts import render, redirect
from questions.models import Question


def search(request):
    query_words = request.GET.get('q').strip()
    if len(query_words) == 0:
        return redirect('home')

    results = Question.objects.filter(
        Q(title__icontains=query_words) |
        Q(description__icontains=query_words)
    )

    # todo

    context = {
        'results': results
    }

    return render(request, 'search/results.html', context=context)
