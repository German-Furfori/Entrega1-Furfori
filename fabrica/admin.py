from django.contrib import admin

from fabrica.models import Maquina, Producto, Trabajador

admin.site.register(Trabajador)
admin.site.register(Producto)
admin.site.register(Maquina)

