from django.db import models
from django.forms import CharField, EmailField, IntegerField


class Trabajador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, TEL: {self.telefono}, email: {self.email}"


class Maquina(models.Model):
    tipo_de_maquina = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.tipo_de_maquina} {self.marca}"
    
    
class Producto(models.Model):
    producto = models.CharField(max_length=20)
    cantidad_en_stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.producto}, stock: {self.cantidad_en_stock}"
