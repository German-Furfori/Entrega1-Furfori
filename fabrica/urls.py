from django.urls import path
from .views import ingresar_trabajador, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('ingresar_trabajador', ingresar_trabajador, name='ingresar_trabajador')
]
