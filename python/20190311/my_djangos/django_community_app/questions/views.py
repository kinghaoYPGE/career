from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib import messages


@method_decorator([login_required], name='dispatch')
class CreateQuestionView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'questions/ask_question.html'

    def form_valid(self, form):
        question = form.save(commit=False)
        question.user = self.request.user
        question.save()
        form.save_m2m()
        messages.success(self.request, 'Question create successfully.')
        return redirect('questions:question_detail', question.pk)


class QuestionDetailView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'questions/question_detail.html'

    def get_context_data(self, **kwargs):
        """回显question"""
        question_id = self.kwargs.get('pk')
        question = Question.objects.get(pk=question_id)
        kwargs['question'] = question
        """回显question对应的answer列表"""
        kwargs['answers'] = question.answer_set.all()

        context = super().get_context_data(**kwargs)
        return context


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'questions/question_list.html'
    queryset = Question.objects.all()
    paginate_by = 1


@login_required
def create_answer(request, pk):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = Answer()
            answer.user = request.user
            answer.question = Question.objects.get(pk=pk)
            answer.description = form.cleaned_data.get('description')
            answer.save()
            messages.success(request, 'Answer publish successfully.')
    return redirect('questions:question_detail', pk)


