from django import forms

from .models import Suscripcion , Contact
from django.urls import reverse, reverse_lazy 
from django.http import HttpResponseRedirect
class SuscripcionForm(forms.ModelForm):
    class Meta:
        model=Suscripcion
        fields=(
            'email',
        )
        widgets={
        'email': forms.EmailInput(
            attrs={
                'placeholder':'correo electronico',
        
            }

        ),
    }


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=(
        'fullname',
        'email',
        'message',
        
        )
    def clean_email(self):
        email=self.cleaned_data['email']
        if '@' not in email or email=='':
            valido=False
            return valido