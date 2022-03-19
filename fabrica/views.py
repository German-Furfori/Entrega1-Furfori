from django.shortcuts import render

def inicio(request):
    return render(request, 'fabrica/index.html', {})

def ingresar_trabajador(request):
    
    
    return render(request, 'fabrica/ingresar_trabajador.html', {})