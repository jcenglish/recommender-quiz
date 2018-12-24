from django.db import models


class Question(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content


class Role(models.Model):
    content = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content


class CompanyCulture(models.Model):
    kind = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.kind


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    size = models.IntegerField()
    culture = models.ForeignKey(CompanyCulture, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Job(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    salary = models.IntegerField()
    wage = models.IntegerField()
    date_published = models.DateTimeField('date published')

    def __str__(self):
        return self.title
