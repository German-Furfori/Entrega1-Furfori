from django.shortcuts import render

from fabrica.forms import IngresarMaquina, IngresarProducto, IngresarTrabajador
from fabrica.models import Maquina, Producto, Trabajador

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
    
    return render(request, 'fabrica/ingresar.html', {"formulario": formulario})

def ingresar_maquina(request):
    if request.method == 'POST':
        formulario = IngresarMaquina(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Maquina(tipo_de_maquina=data['tipo_de_maquina'], marca=data['marca'])
            nuevo_curso.save()
            
    formulario = IngresarMaquina()
    
    return render(request, 'fabrica/ingresar.html', {"formulario": formulario})

def ingresar_producto(request):
    if request.method == 'POST':
        formulario = IngresarProducto(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Producto(producto=data['producto'], cantidad_en_stock=data['cantidad_en_stock'])
            nuevo_curso.save()
            
    formulario = IngresarProducto()
    
    return render(request, 'fabrica/ingresar.html', {"formulario": formulario})