#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        'index/', 
        views.HomePage.as_view(),
        name='index',
    ),  
    path('savesuscripcion' , views.SaveSuscripcion.as_view(),
    name='addsuscripcion'),
    path('contactform' , views.ContactView.as_view(),
    name='contactform'),
]
