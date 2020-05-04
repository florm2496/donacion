from django.db import models
from django.conf import settings
# Create your models here.
from model_utils.models import TimeStampedModel
from applications.entrada.models import Entry
from .managers import FavoritosManager

class Favoritos(TimeStampedModel):
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favoritos',
        on_delete=models.CASCADE
    )
    entry=models.ForeignKey(
        Entry,
        related_name='entry_favoritos',
        on_delete=models.CASCADE
    )
    objects=FavoritosManager()

    class Meta:
        unique_together=('user' , 'entry')
        verbose_name='entrada favorita'
        verbose_name_plural='entradas favoritas'

    def __str__(self):
        return self.entry.title
