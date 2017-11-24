import datetime

from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import Http404

from alquileres.forms import reservaForm
from alquileres.models import *


# Create your views here.
def index(request):
    ciudades = Ciudad.objects.all()
    if 'filter' in request.GET:
        filtrados = Propiedad.objects.all().filter(ciudad=request.GET['idCiudad'])
        contexto = {
            'propiedades': filtrados,
            'ciudades': ciudades
        }
        return render(request, 'alquileres/index.html', contexto)
    else:
        propiedades = Propiedad.objects.all()
        contexto = {
            'propiedades': propiedades,
            'ciudades': ciudades
        }
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
        dpto = Propiedad.objects.get(id=propiedadid)
        if (allowRent(request.POST['dateFrom'], request.POST['dateTo'])):
            huesped = Huesped(nombre=request.POST['nombre'], apellido=request.POST['apellido'])
            huesped.save()
            reserva = Reserva(fecha=datetime.datetime.now(), total=totalAPagar(request.POST['dateFrom'], request.POST['dateTo'], dpto), huesped=huesped)
            reserva.save()
            almacenaRangoFechas(parsearDate(request.POST['dateFrom']), parsearDate(request.POST['dateTo']), reserva, dpto)
            context = {
                'reserva': reserva,
                'dpto': dpto
            }
            messages.success(request, 'Reserva concretada con éxito, su total a pagar es de' +reserva.total)
        else:
            messages.error(request, 'Rango de fechas no habilitado')
            context = {
                'dpto': dpto
            }
            return render(request, 'alquileres/reservasForm.html', context)

        context = reservaForm(request.POST)
        if context.is_valid():
            context.save()
            return redirect('alquileres:index')
        else:
            context = reservaForm()

def parsearDate(dateString):
    return datetime.datetime.strptime(dateString, "%Y-%m-%d").date()


def almacenaRangoFechas(dateFrom, dateTo, reserva, dpto):
    while(dateFrom <= dateTo):
        rentalDate = fechaAlquiler.objects.create(fecha=dateFrom, reserva=reserva)
        rentalDate.dpto.add(dpto)
        rentalDate.save()
        dateFrom = dateFrom + datetime.timedelta(days=1)

def allowRent(dateFrom, dateTo):
    disponible = True
    rentalDates = fechaAlquiler.objects.filter(date__range=[dateFrom, dateTo], propiedad__isnull=False ).count()
    if rentalDates != 0:
        disponible = False
    return disponible

def totalAPagar(dateFrom, dateTo, dpto):
    rentalDates = fechaAlquiler.objects.filter(date__range=[dateFrom, dateTo], propiedad__isnull=False ).count()
    total = rentalDates * dpto.precioDiario
    return total