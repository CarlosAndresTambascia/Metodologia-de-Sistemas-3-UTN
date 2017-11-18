from django.shortcuts import render
from django.http import HttpResponse
from alquileres.models import Propiedad


# Create your views here.
def index(request):
    propiedades = Propiedad.objects.all()
    contexto = {'propiedades':propiedades}
    return render(request, 'alquileres/index.html', contexto)