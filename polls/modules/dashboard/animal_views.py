from django.urls import reverse_lazy
from django.views.generic import DeleteView

from polls.models import Animal


class AnimalDelete(DeleteView):
    model = Animal
    success_url = reverse_lazy('dashboard.index')
