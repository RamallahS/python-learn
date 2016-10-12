from django.conf.urls import url

from . import views
from .services.auth import auth_views

urlpatterns = [
    url(r'^$', views.index2, name='index'),
    url(r'^auth/form', auth_views.page_auth, name='auth.page'),
    url(r'^auth/reminder', auth_views.page_reminder, name='auth.page.reminder'),
    url(r'^auth/registration', auth_views.page_registration, name='auth.page.registration'),
]
