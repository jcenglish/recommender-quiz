from django.contrib.auth.models import User
from .models import Quiz, User, Question
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    quizzes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Quiz.objects.all())

    class Meta:
        model = User
        fields = ('url', 'username', 'quizzes')


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Question.objects.all())
    author = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Quiz
        fields = ('url', 'name', 'description', 'owner')
