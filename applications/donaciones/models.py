from django.db import models
from applications.users.models import User
from ckeditor.fields import RichTextField
from django.conf import settings
from .managers import DonacionManager


class Categoria(models.Model):
    nombre = models.CharField( max_length=50)
    def __str__(self):
        return str(self.id) + '-' + self.nombre


class Donacion(models.Model):

    categoria=models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria_donacion'
    )
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_donador'
    )
    contacto=models.CharField(max_length=25)
    detalle=RichTextField()

    class Meta:

        verbose_name = 'donacion'
        verbose_name_plural = 'donaciones'

    def __str__(self):
        return str(self.categoria) 
