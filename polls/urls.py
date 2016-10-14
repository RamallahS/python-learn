from django.conf.urls import url
from django.views.generic import TemplateView

from polls.modules.dashboard.DashboardIndex import DashboardIndex, DashboardAnimalForm
from polls.services.auth.auth_views import PageAuthReminderView
from . import views
from .services.auth import auth_views

from .modules.dashboard.animal_views import AnimalDelete, AnimalCreate, AnimalList, AnimalUpdate

urlpatterns = [
    url(r'^$', views.index2, name='index'),
    url(r'^auth/form', auth_views.page_auth, name='auth.page'),
    url(r'^auth/registration', auth_views.page_registration, name='auth.page.registration'),
    url(r'^auth/reminder$', PageAuthReminderView.as_view(), name='auth.page.reminder'),
    url(r'^auth/logout$', auth_views.auth_logout_action, name='auth.logout'),

    # Users Dashboard
    url(r'^dashboard$', AnimalList.as_view(), name='animals.list'),
    url(r'^dashboard/animals/new$', AnimalCreate.as_view(), name='animals.new'),
    url(r'^dashboard/animals/edit/(?P<pk>\d+)$', AnimalUpdate.as_view(), name='animal.edit'),
    url(r'^dashboard/animals/delete/(?P<pk>\d+)$', AnimalDelete.as_view(), name='animal.delete'),
]
