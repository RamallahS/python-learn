from django.conf.urls import url
from django.views.generic import TemplateView

from polls.modules.dashboard.DashboardIndex import DashboardIndex, DashboardAnimalForm
from polls.services.auth.auth_views import PageAuthReminderView
from . import views
from .services.auth import auth_views

from .modules.dashboard.animal_views import AnimalDelete

urlpatterns = [
    url(r'^$', views.index2, name='index'),
    url(r'^auth/form', auth_views.page_auth, name='auth.page'),
    url(r'^auth/registration', auth_views.page_registration, name='auth.page.registration'),
    url(r'^auth/reminder$', PageAuthReminderView.as_view(), name='auth.page.reminder'),
    url(r'^auth/logout$', auth_views.auth_logout_action, name='auth.logout'),

    # Users Dashboard
    url(r'^dashboard$', DashboardIndex.as_view(), name='dashboard.index'),
    url(r'^dashboard/animals/new$', DashboardAnimalForm.as_view(), name='dashboard.animals.new'),
    url(r'^dashboard/animals/save$', DashboardAnimalForm.as_view(), name='dashboard.animals.save'),
    url(r'^dashboard/animals/remove/(?P<pk>[0-9+])$', AnimalDelete.as_view(), name='dashboard.animals.remove'),
]
