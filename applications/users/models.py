from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    LOCALIDAD_CHOICES = (
        ('SM', 'San Miguel de Tucuman'),
        ('YB', 'Yerba Buena'),
        ('C', 'El cadillal'),
        ('BD','Banda de Rio Sali'),
        ('VN','Villa Nougues'),
        ('F' ,'Famailla'),
        ('L' ,'Lules'),
        ('T','Trancas'),
        ('LT' , 'Las Talitas'),
        ('M','Monteros'),
        ('CP','Concepcion'),
        ('A','Aguilares'),
        ('JBA' ,'Juan Bautista Alberdi'),
        
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField('Nombres', max_length=100)
    ocupation = models.CharField(
        'Ocupacion',
        max_length=30, 
        blank=True
    )
    genero = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    localidad=models.CharField(
        max_length=10,
        choices=LOCALIDAD_CHOICES, default=''
    )
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )
   
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def get_short_name(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name
