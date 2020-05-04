from django.shortcuts import render
from .forms import edForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy 
from django.http import HttpResponseRedirect
# Create your views here.
from django.views.generic import (
    TemplateView,CreateView,ListView
)
#from applications.donaciones.models import Donacion
from .models import Donacion
#from .forms import DonacionForm


class HomeDonaciones(TemplateView):
    model=Donacion
    template_name='donaciones/home_donaciones.html'

class addDonacion(LoginRequiredMixin ,CreateView):
    model=Donacion
    template_name='donaciones/add_donacion.html'
    form_class=edForm
    login_url=reverse_lazy('users_app:user-login')

   
    def form_valid(self, form):
    

        Donacion.objects.crear_donacion(
        form.cleaned_data['contacto'],
        form.cleaned_data['detalle'],
        form.cleaned_data['categoria'],
        self.request.user.id,
        )
        return super(addDonacion, self).form_valid(form)
        