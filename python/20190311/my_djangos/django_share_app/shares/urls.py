from django.urls import path
from . import views

app_name = 'shares'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('my/', views.my_list, name='my_list'),
    path('search/', views.search, name='search'),
]
