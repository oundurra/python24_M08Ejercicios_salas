from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')

        labels = {
            'username':'EMail',
            'first_name':'Nombre'
        }