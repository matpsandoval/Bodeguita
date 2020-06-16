from django.contrib import admin
from .models import Proveedor, Producto
# Register your models here.

admin.site.register(Producto)
admin.site.register(Proveedor)
