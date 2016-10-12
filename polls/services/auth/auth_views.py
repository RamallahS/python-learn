from django.shortcuts import render


def page_auth(request):
    return render(request, 'auth.form.html')


def page_reminder(request):
    return render(request, 'auth.form.reminder.html')


def page_registration(request):
    return render(request, 'auth.form.registration.html')
