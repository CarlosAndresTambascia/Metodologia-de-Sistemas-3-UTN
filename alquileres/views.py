import datetime

from django.shortcuts import render, redirect
from django.http import Http404

from alquileres.forms import reservaForm
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
    return render(request, 'alquileres/oneHouse.html', {'dpto': dpto})


def reservaPropiedad(request, propiedadid):
    if request.method == 'GET':
        dpto = Propiedad.objects.get(id=propiedadid)
        form = reservaForm
        now = datetime.datetime.now
        context = {
            'dpto': dpto,
            'form': form,
            'now': now
        }
        return render(request, 'alquileres/reservasForm.html', context)

    if request.method == 'POST':
        context = reservaForm(request.POST)
        if context.is_valid():
            context.save()
            return redirect('alquileres:index')
        else:
            context = reservaForm()
        return render(request, 'alquileres/reservasForm.html', context)
