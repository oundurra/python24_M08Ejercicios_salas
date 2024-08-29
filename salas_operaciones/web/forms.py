from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Procedimiento

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')

        labels = {
            'username':'EMail',
            'first_name':'Nombre'
        }

class ProcedimientoForm(forms.ModelForm):
    class Meta:
        model = Procedimiento
        fields = ('id', 'fecha', 'hora_inicio', 'hora_fin', 'mascota', 'sala')

        labels = {
            'hora_inicio':'Inicio',
            'hora_fin':'Fin'
        }
