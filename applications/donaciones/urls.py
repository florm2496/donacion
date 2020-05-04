#
from django.urls import path
from . import views

app_name = "donaciones_app"

urlpatterns = [
   path(
        'home_don/', 
        views.HomeDonaciones.as_view(),
        name='home_donaciones',
    ), 
    path(
        'add_donacion/', 
        views.addDonacion.as_view(),
        name='add_donacion',
    ), 

    
]