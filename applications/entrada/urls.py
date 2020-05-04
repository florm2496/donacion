from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path(
        'entradaDetail/<pk>/', 
        views.entradaDetail.as_view(),
        name='detalle_entrada',
    ),  
]
