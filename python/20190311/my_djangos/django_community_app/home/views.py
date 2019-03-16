from django.shortcuts import redirect, render


def home(request):
    return redirect('questions:question_list')
