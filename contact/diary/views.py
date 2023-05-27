from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from diary.models import *
from django.urls import *
from django.db.models import QuerySet

# Create your views here.


class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 5

#metodo para buscar una consulta
    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return Contact.objects.filter(name__icontains=q)

        return super().get_queryset()


class ContactCreateView(generic.CreateView):
    model = Contact
    fields = ('name', 'email', 'birth', 'phone', 'avatar')
    success_url = reverse_lazy('diarylist')


class ContactUpdateView(generic.UpdateView):
    model = Contact
    fields = ('name', 'email', 'birth', 'phone', 'avatar')
    success_url = reverse_lazy('diarylist')


class ContactDeleteView(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('diarylist')
