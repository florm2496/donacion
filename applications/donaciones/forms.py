from django import forms
from .models import Donacion



class edForm(forms.ModelForm):
    class Meta:
        model=Donacion
        fields=[
            'contacto',
            'detalle',
            'categoria',
        ]

        