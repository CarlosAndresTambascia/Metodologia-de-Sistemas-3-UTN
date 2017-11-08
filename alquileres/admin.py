from django.contrib import admin
from .models import Ciudad, Propiedad, fechaAlquiler, Huesped, Reserva

# Register your models here.

admin.site.register(Ciudad)
admin.site.register(Propiedad)
admin.site.register(fechaAlquiler)
admin.site.register(Huesped)
admin.site.register(Reserva)