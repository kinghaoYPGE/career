from django.urls import path
from .views import QuestionDetailView, QuestionListView, CreateQuestionView, create_answer

app_name = 'questions'

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='question_list'),
    path('questions/add/', CreateQuestionView.as_view(), name='question_add'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('questions/<int:pk>/add', create_answer, name='answer_add'),
]

