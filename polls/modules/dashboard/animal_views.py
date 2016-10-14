from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from polls.models import Animal


class AnimalMixin(object):
    model = Animal
    success_url = reverse_lazy('animals.list')


class AnimalList(AnimalMixin, ListView):
    pass


class AnimalCreate(AnimalMixin, CreateView):
    fields = ['name']


class AnimalUpdate(AnimalMixin, UpdateView):
    fields = ['name']


class AnimalDelete(AnimalMixin, DeleteView):
    pass
