from django import forms
from .models import Post

class propiedadPost (forms.ModelForm):
    class Meta:
        model = Post
        fields = ('descripcion', 'precioDiario', 'imagen','titulo', 'numeroFicha', 'maximoHabitantes', 'ciudad', 'usuario')
