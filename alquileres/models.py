from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.nombre


class Propiedad(models.Model):
    descripcion = models.CharField(max_length=500)
    precioDiario = models.IntegerField()
    imagen = models.ImageField(upload_to='image', max_length=100)
    titulo = models.CharField(max_length=50)
    maximoHabitantes = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Propiedades"

    def __str__(self):
        return self.titulo


class Reserva(models.Model):
    total = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(blank=True, null=True, max_length=50)
    apellido = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=200)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.PROTECT, blank=False, null=False)
    fechaReserva = models.DateField(blank=False, null=False, auto_now=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class fechaAlquiler(models.Model):
    fecha = models.DateField()
    propiedad = models.ForeignKey(Propiedad, null=True, blank=True, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name_plural = "FechasAlquiler"
