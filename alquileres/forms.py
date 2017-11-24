from django import forms
from alquileres.models import Reserva


class reservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'numeroReserva',
            'total',
            'huesped',

        ]
        labels = {
            'numeroReserva': 'Numero Reserva',
            'total': 'Total',
            'huesped': 'Nombre del Huesped',
        }
        widgets = {
            'numeroReserva': forms.NumberInput(attrs={'class':'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'huesped': forms.TextInput(attrs={'class': 'form-control'}),
        }
