from django.contrib import admin
from .models import Quiz, Choice, Question, Association


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


class QuizAdmin(admin.ModelAdmin):
    fields = ['date_published', 'title', 'description']
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    fields = ['content', 'quiz']
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    fields = ['content', 'question', 'association']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Association)
