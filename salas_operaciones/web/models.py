from django.db import models

# Create your models here.
class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=6)
    tamano = models.IntegerField()
    descripcion = models.CharField(max_length=100)

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    contacto_dueno = models.CharField(max_length=45)
    especie = models.CharField(max_length=45)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=128)
    created = models.DateField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class Procedimiento(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    user = models.ForeignKey(User, models.DO_NOTHING)
    mascota = models.ForeignKey(Mascota, models.DO_NOTHING)
    sala = models.ForeignKey(Sala, models.DO_NOTHING)