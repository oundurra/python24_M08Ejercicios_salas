from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 

# Create your views here.
def index(request):
    
    #noticias = getLikesByUser(request.user.id)

    return render(request, 'index.html', {})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to a homepage or another page after successful registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def procedimientos(request):
    None

def agendar(request):
    None
