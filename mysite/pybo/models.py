from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):

    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)   #blank=True : form.is_valid()를 통한 입력 폼 데이터 검사 시 값이 없어도 된다는 의미

    def __str__(self):
        return self.subject

class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content