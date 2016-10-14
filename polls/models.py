from django.db import models
from django.core.urlresolvers import reverse


class Question(models.Model):
    question_test = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_test


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class AnimalKind(models.Model):
    name = models.CharField(max_length=100)


class Animal(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('animal.edit', kwargs={'pk': self.pk})
