from django.shortcuts import render
from django.http import Http404
from alquileres.models import Propiedad


# Create your views here.
def index(request):
    propiedades = Propiedad.objects.all()
    contexto = {'propiedades': propiedades}
    return render(request, 'alquileres/index.html', contexto)


def detail(request, propiedadid):
    try:
        dpto = Propiedad.objects.get(id=propiedadid)
    except Propiedad.DoesNotExist:
        raise Http404("La propiedad ingresada no existe")
    return render(request, 'propiedad/' + str(propiedadid) +'.html', {'dpto': dpto})
