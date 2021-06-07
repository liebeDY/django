from datetime import time
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from ..models import Answer, Question, Comment

from django.utils import timezone

from ..forms import QuestionForm, AnswerForm, CommentForm

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

from django.contrib import messages


@login_required(login_url='common:login')
def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    pybo 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)
    
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')  # messages 모듈 : 오류를 임의로 발생시키고 싶은 경우 (넌필드 오류)
        return redirect('pybo:detail', question_id=question.id)
    
    if request.method == "POST":    # POST 방식으로 호출되어 데이터 수정이 이뤄짐
        form = QuestionForm(request.POST, instance=question)    # instance 매개변수에 question을 저장하면 기존 값을 폼에 채울 수 있다.
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question_id)
    else:   # GET 방식으로 호출되어 질문 수정 화면이 나타남
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id = question_id)
    
    question.delete()
    return redirect('pybo:index')