from django import forms
from .models import Producto, Proveedor



class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['rut', 'nombre',
                  'telefono', 'domicilio', 'region', 'comuna']
        labels = {'rut': 'Rut', 'nombre': 'Nombre Empresa', 'telefono': 'Teléfono', 'domicilio': 'Domicilio',
                  'region': 'Región', 'comuna': 'Comuna'}
        widgets = {'rut': forms.TextInput(attrs={'class': 'form-control'}),
                   'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                   'telefono': forms.TextInput(attrs={'class': 'form-control'}),
                   'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
                   'region': forms.TextInput(attrs={'class': 'form-control'}),
                   'comuna': forms.TextInput(attrs={'class': 'form-control'}), }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['proveedor', 'codigo', 'sku', 'nombre',
                  'descripcion', 'clasificacion', 'precio','disponible' ]
        labels = {'proveedor': 'Proveedor', 'codigo': 'Codigo EAN', 'sku': 'Codigo Interno', 'nombre': 'Nombre', 'descripcion': 'Descripcion Producto',
                  'clasificacion': 'Clasificación', 'precio': 'Precio Producto', 'disponible': 'Stock Disponible'}
        # widgets = {'codigo': forms.TextInput(attrs={'class': 'form-control'}),
        #            'sku': forms.TextInput(attrs={'class': 'form-control'}),
        #            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        #            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        #            'clasificacion': forms.TextInput(attrs={'class': 'form-control'}),
        #            'precio': forms.TextInput(attrs={'class': 'form-control'}), 
        #            'disponible': forms.TextInput(attrs={'class': 'form-control'}), }
