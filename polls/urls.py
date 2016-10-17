from django.conf.urls import url
from django.views.generic import TemplateView

from polls.modules.dashboard.DashboardIndex import DashboardIndex, DashboardAnimalForm
from polls.services.auth.auth_views import PageAuthReminderView
from . import views
from .services.auth import auth_views

from .modules.dashboard.animal_views import AnimalDelete, AnimalCreate, AnimalList, AnimalUpdate

# API TEMP
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class UserPostList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]


# API REST ///

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

    # REST API
    url(r'^api/users', UserPostList.as_view()),
]
