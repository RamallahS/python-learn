from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question


def auth_page(request):
    return render(request, 'auth.form.html')


# render variant 1
def index(request):
    questions_list = Question.objects.all()
    template = loader.get_template('index.html')
    context = {"questions_list": questions_list}
    return HttpResponse(template.render(context, request))


# render variant 2
def index2(request):
    questions_list = Question.objects.all()
    context = {"questions_list": questions_list}
    return render(request, 'index.html', context)
