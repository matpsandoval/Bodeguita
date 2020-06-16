"""appCrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('ingresarProducto', include('app.urls')),
    path('ingresarProveedor', include('app.urls')),
    path('listarProductosFull', include('app.urls')),
    path('listarProveedoresFull', include('app.urls')),
    path('editarProducto/<int:producto_id>', include('app.urls')),
    path('editarProveedor/<int:proveedor_id>', include('app.urls')),
    path('borrarProducto/<int:producto_id>', include('app.urls')),
    path('borrarProveedor/<int:proveedor_id>', include('app.urls')),
    path('listarProductos', include('app.urls')),
    path('listarProveedores', include('app.urls')),
]
