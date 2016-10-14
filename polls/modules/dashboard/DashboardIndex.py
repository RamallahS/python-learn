from django.shortcuts import render
from django.views.generic import TemplateView

from polls.models import Animal


class DashboardIndex(TemplateView):
    template_name = 'dashboard.index.html'

    def get(self, request, *args, **kwargs):
        animals = Animal.objects.all()
        return render(request, self.template_name, {"animals": animals})


class DashboardAnimalForm(TemplateView):
    template_name = 'dashboard.animals.form.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
