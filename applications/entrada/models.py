from django.db import models

# Create your models here.
from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from .managers import EntryManager
# Create your models here.
class Category(TimeStampedModel):
    short_name =models.CharField(
        'nombre corto',
        max_length=15,
        unique=True
    )
    name=models.CharField(
        'nombre',
        max_length=30
    )
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name=models.CharField(
        'nombre',
        max_length=30
    )
class Entry(TimeStampedModel):
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    categoria=models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag=models.ManyToManyField(Tag)
    title=models.CharField(
        'titulo',
        max_length=200

    )
    resumen=models.TextField('Resumen')
    contenido=RichTextUploadingField('contenido')
    public=models.BooleanField(default=False)
    image=models.ImageField(
        'Imagen',
        upload_to='Entry',
    )
    portada=models.BooleanField(default=False)
    in_home=models.BooleanField(default=False)
    slug=models.SlugField(editable=False , max_length=300)

    objects = EntryManager()
    
    class Meta:
        verbose_name='Entrada'
        verbose_name_plural='Entradas'
    def __str__(self):
        return self.title