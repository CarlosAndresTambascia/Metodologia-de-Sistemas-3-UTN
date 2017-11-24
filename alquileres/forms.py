from django import forms
from alquileres.models import *


class reservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'numeroReserva',
            'huesped',

        ]
        labels = {
            'numeroReserva': 'Numero Reserva',
            'huesped': 'Nombre del Huesped',
        }
        widgets = {
            'numeroReserva': forms.NumberInput(attrs={'class':'form-control'}),
            'huesped': forms.TextInput(attrs={'class': 'form-control'}),
        }


class huespedForm (forms.ModelForm):
    class Meta:
        model = Huesped
        fields = [
            'nombre',
            'apellido',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }

