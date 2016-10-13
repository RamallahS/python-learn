from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST, require_GET
from django.views.generic import TemplateView

from polls.services.auth.auth_forms import RegistrationForm

from .auth_service import AuthService


class WithAuthMixin(object):
    def __init__(self, request):
        self.request = request

    def is_auth(self):
        return self.request.user.is_authenticated


class PageAuthReminderView(TemplateView, WithAuthMixin):
    template_name = 'auth.form.reminder.html'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        print('GET', self.is_auth())
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        print('POST', request)
        return render(request, self.template_name)


@require_GET
def page_auth(request):
    # if request.user.is_authenticated:
    #   return redirect('/pools')
    if request.method == 'GET':
        return render(request, 'auth.form.html')
    else:
        user = authenticate(username="root", password="pingpong22")
        print(user)


def auth_logout_action(request):
    logout(request)
    return redirect('/pools')


def page_reminder(request):
    return render(request, 'auth.form.reminder.html')


def page_registration(request):
    if request.method == 'GET':
        return render(request, 'auth.form.registration.html')
    else:
        form = RegistrationForm(request.POST)
        try:
            if form.is_valid():
                AuthService.register_user(form)
                return HttpResponse("Is valid form")
            else:
                return render(request, 'auth.form.registration.html', {"form": form})
        except Exception as e:
            return render(request, 'auth.form.registration.html', {"form": form, "exception": str(e)})
