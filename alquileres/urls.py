from django.conf.urls import url
from alquileres.views import *
from . import views

urlpatterns = [
    url(r'^$', index),
    url(r'^propiedad/(?P<propiedadid>\d+)$', detail, name="dpto"),
    url(r'^alquileres/reservaPropiedad/', views.reservaPropiedad, name='reservaPropiedad'),
    url(r'^reservaPropiedad/([0-9]+)/$', views.reservaExitosa, name='reservaExitosa'),

]
