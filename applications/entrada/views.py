from django.shortcuts import render
from django.views.generic import (
    TemplateView,CreateView,DetailView
)
from .models import Entry
# Create your views here.
class entradaDetail(DetailView):
    template_name='entrada/detalle_entrada.html'
    model= Entry
