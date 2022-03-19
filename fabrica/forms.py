from django import forms


class IngresarTrabajador(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    telefono = forms.IntegerField()
    email = forms.EmailField(max_length=30)
    

class IngresarMaquina(forms.Form):
    tipo_de_maquina = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    
    
class IngresarProducto(forms.Form):
    producto = forms.CharField(max_length=20)
    cantidad_en_stock = forms.IntegerField()
    
    
class BuscarTrabajador(forms.Form):
    apellido = forms.CharField(label="Ingrese el apellido del trabajador", max_length=20)