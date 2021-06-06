from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request) :

  """
  pybo 목록 출력
  """

  # 입력 파라미터
  page = request.GET.get('page', '1') # 페이지

  question_list = Question.objects.order_by('-create_date')

  paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
  page_obj = paginator.get_page(page)

  context = {'question_list': page_obj}

  return render(request, 'pybo/question_list.html', context)


def detail(reqeust, question_id) :
  """
  pybo 내용 출력
  """

  question = get_object_or_404(Question, pk=question_id)
  context = {'question': question}
  return render(reqeust, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_create(request, question_id) :
  """
  pybo 답변등록
  """

  question = get_object_or_404(Question, pk=question_id)

  if request.method == "POST" :
    form = AnswerForm(request.POST)

    if form.is_valid() :
      answer = form.save(commit=False)
      answer.create_date = timezone.now()
      answer.question = question
      answer.author = request.user  # 추가한 속성 author 적용
      answer.save()
      return redirect('pybo:detail', question_id=question.id)

  else :
    form = AnswerForm()
  context = {'question': question, 'form': form}

  return render(request, 'pybo/question_detail.html', context)



@login_required(login_url='common:login')
def question_create(request) :
  """
  pybo 질문등록
  """


  if request.method == "POST" :
    form = QuestionForm(request.POST)

    if form.is_valid() :
      question = form.save(commit=False)
      question.create_date = timezone.now()
      question.author = request.user  # 추가한 속성 author 적용
      question.save()
      return redirect('pybo:index')

  else :
    form = QuestionForm()
  
  context = {'form': form}
  return render(request, 'pybo/question_form.html', {'form': form})