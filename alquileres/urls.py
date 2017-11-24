from django.conf.urls import url
from alquileres.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^propiedad/(?P<propiedadid>\d+)$', detail, name="dpto"),
    url(r'^propiedad/(?P<propiedadid>\d+)/alquilar$', reservaPropiedad, name="form")
]
