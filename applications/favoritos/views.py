from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .models import Favoritos ,Entry
from django.http import HttpResponseRedirect

from django.views.generic import(
    ListView,View
)
class UserFav(LoginRequiredMixin ,ListView):
    template_name='favoritos/perfil.html'
    context_object_name='entrada_user'
    login_url=reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favoritos.objects.entradas_user(self.request.user)


class AddFavoritos(View):
    def post(self , request , *args , **kwargs):
        usuario=self.request.user
        entrada=Entry.objects.get(id=self.kwargs['pk'])
        
        Favoritos.objects.create(
            user=usuario,
            entry=entrada
        )
        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil'
            )
        )