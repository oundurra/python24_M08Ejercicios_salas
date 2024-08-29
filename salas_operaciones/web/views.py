from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 
from .models import User
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def index(request):
    procedimientos = Procedimiento.objects.all()

    return render(request, 'index.html', {"procedimientos":procedimientos})

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

@login_required
def add_procedimiento(request):
    if request.method == 'POST':
        form = ProcedimientoForm(request.POST)
        if form.is_valid():
            procedimiento = form.instance

            #Validar que la sala y el horario están libres
            proc = Procedimiento.objects.filter(
                     Q(hora_inicio__range=(procedimiento.hora_inicio, procedimiento.hora_fin)) | Q(hora_fin__range=(procedimiento.hora_inicio, procedimiento.hora_fin))
                    ,sala=procedimiento.sala
                    ,fecha=procedimiento.fecha) | Procedimiento.objects.filter(
                     Q(hora_inicio__range=(procedimiento.hora_inicio, procedimiento.hora_fin)) | Q(hora_fin__range=(procedimiento.hora_inicio, procedimiento.hora_fin))
                    ,user=User.objects.get(id = request.user.id)
                    ,fecha=procedimiento.fecha)

            #proc = Procedimiento.objects.filter(Q(hora_inicio__range=(procedimiento.hora_inicio, procedimiento.hora_fin)) | Q(hora_fin__range=(procedimiento.hora_inicio, procedimiento.hora_fin)))

            if not proc:
                messages.success(request, "Sala agendada correctamente.")
                procedimiento.user = User.objects.get(id = request.user.id)
                procedimiento.save()
            else:
                messages.warning(request, "No se pudo agendar la sala.")
            
            return redirect('home')  # Redirect to a homepage or another page after successful registration
    else:
        form = ProcedimientoForm()

    return render(request, 'procedimiento.html', {'form': form})

def del_procedimiento(request,id):
    Procedimiento.objects.get(id=id).delete()
    messages.success(request, "Procedimiento eliminado correctamente.")
    return redirect('home')
