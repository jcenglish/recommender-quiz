from django.contrib.auth.models import User
from .models import Quiz, Question, Choice
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    quizzes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Quiz.objects.all())

    class Meta:
        model = User
        fields = ('url', 'username', 'quizzes')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choices = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Choice.objects.all())

    class Meta:
        model = User
        fields = ('url', 'content', 'quiz', 'choices')


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Question.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Quiz
        fields = ('url', 'title', 'description', 'owner', 'questions')
