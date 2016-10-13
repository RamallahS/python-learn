from django.conf.urls import url
from django.views.generic import TemplateView

from polls.services.auth.auth_views import PageAuthReminderView
from . import views
from .services.auth import auth_views

urlpatterns = [
    url(r'^$', views.index2, name='index'),
    url(r'^auth/form', auth_views.page_auth, name='auth.page'),
    url(r'^auth/registration', auth_views.page_registration, name='auth.page.registration'),
    url(r'^auth/reminder$', PageAuthReminderView.as_view(), name='auth.page.reminder'),
    url(r'auth/logout$', auth_views.auth_logout_action, name='auth.logout')

]
