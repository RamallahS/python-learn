from django.shortcuts import render
from django.http import HttpResponse

from polls.services.auth.auth_forms import RegistrationForm

from .auth_service import AuthService


def page_auth(request):
    return render(request, 'auth.form.html')


def page_reminder(request):
    return render(request, 'auth.form.reminder.html')


def page_registration(request):
    if request.method == 'GET':
        return render(request, 'auth.form.registration.html')
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            AuthService.register_user(form);
            return HttpResponse("Is valid form")
        else:
            return render(request, 'auth.form.registration.html', {"form": form})
