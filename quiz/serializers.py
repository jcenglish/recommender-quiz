# from django.contrib.auth.models import User, Group
# from quiz.models import Question, Choice, Quiz
# from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


# class QuizSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Quiz
#         fields = ('url', 'title', 'description')

# # class QuestionSerializer(serializers.HyperlinkedModelSerializer):
# #     class Meta:
# #         model = Question
# #         fields = ('url', 'content')


# # class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
# #     class Meta:
# #         model = Choice
# #         fields = ('url', 'content')
