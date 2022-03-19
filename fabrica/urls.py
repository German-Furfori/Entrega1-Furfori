from django.urls import path
from .views import ingresar_maquina, ingresar_producto, ingresar_trabajador, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('ingresar_trabajador', ingresar_trabajador, name='ingresar_trabajador'),
    path('ingresar_maquina', ingresar_maquina, name='ingresar_maquina'),
    path('ingresar_producto', ingresar_producto, name='ingresar_producto'),

]
