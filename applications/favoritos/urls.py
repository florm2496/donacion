#
from django.urls import path
from . import views

app_name = "favoritos_app"

urlpatterns = [
  path(
      'perfil/',
      views.UserFav.as_view(),
      name='perfil',
  ),
  path(
      'addFAV/<pk>/',
      views.AddFavoritos.as_view(),
      name='addFAV',
  ),
  

]