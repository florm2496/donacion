from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    about = models.CharField( max_length=50)
    email = models.EmailField('email de contacto' , blank=True , null=True)
    phone = models.CharField(max_length=50)

    class Meta:
        verbose_name='Pagina principal'
        verbose_name_plural='Pagina principal'

    def __str__(self):
        return self.title
    
class Suscripcion(TimeStampedModel):
    email = models.EmailField('email de contacto' , blank=True , null=True)
    
    class Meta:
        verbose_name='Suscriptor'
        verbose_name_plural='Suscriptores'

    def __str__(self):
        return self.email

class Contact(TimeStampedModel):
    fullname = models.CharField('Nombres', max_length=50 , null=True)

    email=models.CharField('email' , max_length=20,null=True)
    message=models.TextField(null=True)

    class Meta:
        verbose_name='Contacto'
        verbose_name_plural='Mensajes'

    def __str__(self):
        return self.fullname
