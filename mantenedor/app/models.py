from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


# Create your models here.


class Proveedor(models.Model):

    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=50)
    region = models.CharField(max_length=50, blank=True, null=True)
    comuna = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    sku = models.IntegerField()
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=30)
    clasificacion = models.CharField(max_length=30)
    precio = models.IntegerField()
    disponible = models.IntegerField()

    def __str__(self):
        return self.nombre
