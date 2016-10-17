from django.template.loader_tags import register
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from polls.models import Animal

# Forms classes
from django import forms


class AnimalForm(forms.ModelForm):
    name = forms.CharField(min_length=2)
    animal_kind = forms.Select()

    class Meta:
        model = Animal
        fields = ['name', 'animal_kind']


# Filters
# Пример регистрации и использования фильтров
@register.filter(is_safe=True)
def label_with_classes(value, arg):
    return value.label_tag(attrs={'class': arg})

# Views classes

class AnimalMixin(object):
    model = Animal
    success_url = reverse_lazy('animals.list')


class AnimalList(AnimalMixin, ListView):
    pass


class AnimalCreate(AnimalMixin, CreateView):
    form_class = AnimalForm
    # fields = ['name', 'animal_kind']


class AnimalUpdate(AnimalMixin, UpdateView):
    form_class = AnimalForm
    # fields = ['name', 'animal_kind']


class AnimalDelete(AnimalMixin, DeleteView):
    pass
