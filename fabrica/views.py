from django.shortcuts import render

from fabrica.forms import IngresarTrabajador
from fabrica.models import Trabajador

def inicio(request):
    return render(request, 'fabrica/index.html', {})

def ingresar_trabajador(request):
    if request.method == 'POST':
        formulario = IngresarTrabajador(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Trabajador(nombre=data['nombre'], apellido=data['apellido'], telefono=data['telefono'], email=data['email'])
            nuevo_curso.save()
            
    formulario = IngresarTrabajador()
    
    return render(request, 'fabrica/ingresar_trabajador.html', {"formulario": formulario})

def ingresar_maquina(request):
    
    
    return render(request, 'fabrica/ingresar_maquina.html', {})

def ingresar_producto(request):
    
    
    return render(request, 'fabrica/ingresar_producto.html', {})