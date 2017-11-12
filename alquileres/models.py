from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=200, unique=True)


class Propiedad(models.Model):
    descripcion = models.CharField(max_length=500)
    precioDiario = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField()
    titulo = models.CharField(max_length=50)
    numeroFicha = models.IntegerField()
    maximoHabitantes = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


class fechaAlquiler(models.Model):
    fecha = models.DateField()
    propiedad = models.ForeignKey(Propiedad, null=True, blank=True, on_delete=models.CASCADE)
    mail = models.EmailField()


class Huesped(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)


class Reserva(models.Model):
    numeroReserva = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    huesped = models.ForeignKey(Huesped, null=True, blank=True, on_delete=models.CASCADE)
    fechaReserva = models.ForeignKey(fechaAlquiler, null=True, blank=True, on_delete=models.CASCADE)