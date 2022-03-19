from django.shortcuts import render

from fabrica.forms import BuscarTrabajador, IngresarMaquina, IngresarProducto, IngresarTrabajador
from fabrica.models import Maquina, Producto, Trabajador

def inicio(request):
    return render(request, 'fabrica/index.html', {})

def ingresar_trabajador(request):
    if request.method == 'POST':
        formulario = IngresarTrabajador(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_trabajador = Trabajador(nombre=data['nombre'], apellido=data['apellido'], telefono=data['telefono'], email=data['email'])
            nuevo_trabajador.save()
            
    formulario = IngresarTrabajador()
    
    return render(request, 'fabrica/ingresar.html', {"formulario": formulario})

def ingresar_maquina(request):
    if request.method == 'POST':
        formulario = IngresarMaquina(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_maquina = Maquina(tipo_de_maquina=data['tipo_de_maquina'], marca=data['marca'])
            nueva_maquina.save()
            
    formulario = IngresarMaquina()
    
    return render(request, 'fabrica/ingresar.html', {"formulario": formulario})

def ingresar_producto(request):
    if request.method == 'POST':
        formulario = IngresarProducto(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_producto = Producto(producto=data['producto'], cantidad_en_stock=data['cantidad_en_stock'])
            nuevo_producto.save()
            
    formulario = IngresarProducto()
    
    return render(request, 'fabrica/ingresar.html', {"formulario": formulario})

def buscar_trabajador(request):
    trabajadores_buscados = []
    dato = request.GET.get('apellido', None)
    
    if dato is not None:
        trabajadores_buscados = Trabajador.objects.filter(apellido__icontains=dato)
        
    buscador = BuscarTrabajador()
    return render(request, 'fabrica/buscar.html', {'buscador': buscador, 'trabajadores_buscados': trabajadores_buscados, 'dato': dato})
