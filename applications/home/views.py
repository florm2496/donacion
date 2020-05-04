import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse


from django.views.generic import (
    TemplateView,CreateView
)
from applications.entrada.models import Entry
from .models import Home 
from applications.donaciones.models import Donacion
#from applications.donaciones.forms import DonacionForm
from .forms import SuscripcionForm , ContactForm
class HomePage(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        #cargamos el home
        context["home"]=Home.objects.latest('created')


        context["portada"]=Entry.objects.entrada_en_portada()

        context["entradas_home"]=Entry.objects.entrada_en_home()
        
        context["entradas_recientes"]=Entry.objects.entradas_recientes()
        
        context["form"]=SuscripcionForm


        #context["donacion"]=DonacionForm

        return context

class SaveSuscripcion(CreateView):
    form_class=SuscripcionForm
    success_url= 'index'

class ContactView(CreateView):
    form_class= ContactForm
    success_url='index'
