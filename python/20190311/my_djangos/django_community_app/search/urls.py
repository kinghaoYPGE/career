from django.urls import path, include
from .views import search

app_name = 'search'

urlpatterns = [
    path('search/', search, name='search'),
]
