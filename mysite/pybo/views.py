from django.shortcuts import get_object_or_404, render, get_list_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request) :

  """
  pybo 목록 출력
  """

  question_list = Question.objects.order_by('-create_date')
  context = {'question_list': question_list}

  return render(request, 'pybo/question_list.html', context)


def detail(reqeust, question_id) :
  """
  pybo 내용 출력
  """

  question = get_object_or_404(Question, pk=question_id)
  context = {'question': question}
  return render(reqeust, 'pybo/question_detail.html', context)
