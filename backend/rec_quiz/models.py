import datetime
from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.utils import timezone


class Quiz(models.Model):
    class Meta:
        verbose_name_plural = "quizzes"
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(
        'auth.User', related_name='quizzes',
        on_delete=models.CASCADE,
    )
    date_published = models.DateTimeField('date published', null=True)
    date_modified = models.DateTimeField('date modified', null=True)
    date_created = models.DateTimeField('date created')

    def published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title


class Question(models.Model):
    content = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Association(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name='choices', on_delete=models.CASCADE)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    date_published = models.DateTimeField('date published', null=True)
    date_modified = models.DateTimeField('date modified', null=True)
    date_created = models.DateTimeField('date created')

    def __str__(self):
        return self.title


class QuizResult(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, default=1)
    date_created = models.DateTimeField('date created')
    # get quiz through choice through question
    # get question through choice
    # get association through choice
