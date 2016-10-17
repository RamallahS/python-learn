from django.conf.urls import url

from super.views import PageAngularApp

urlpatterns = [
    url(r'', PageAngularApp.as_view())
]
