from django import forms
from django.forms import ModelForm
from .models import Contacto

class ContactForm(forms.ModelForm):
    class Meta:

        model = Contacto
        fields = ["correo_electronico","nombre","asunto"]
    