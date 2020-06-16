from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django import forms
# ---importamos nuestras estruras ---------------
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm
#_________________ PARA USER ________________________________
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView,LogoutView
#_________________ PARA API ________________________________
from .serializers import ProductoSerializer
from rest_framework import generics

#_____________________________________________________________
class API_objects(generics.ListCreateAPIView):
        queryset = Producto.objects.all()
        serializer_class = ProductoSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Producto.objects.all()
        serializer_class = ProductoSerializer

# Create your views here.

#login


def registerView(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})


#login
def proveedor_list(request):
    return render(request, 'app/proveedor_list.html', {})

#logout
def logout(request):
    if request.method=='POST':
        form = LogoutView(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})



def index(request):
    return render(request, 'app/index.html', {})


def quienes(request):
    return render(request, 'app/quienes.html', {})


def nba(request):
    return render(request, 'app/nba.html', {})

def inicio(request):
    return render(request, 'registration/inicio.html', {})


def finalFantasy(request):
    return render(request, 'app/finalFantasy.html', {})


def blairWitch(request):
    return render(request, 'app/blairWitch.html', {})

#--------------ingresar producto
@login_required
def ingresarProducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if(form.is_valid):
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/ingresarProducto')
    else:
        form = ProductoForm()
        return render(request, 'app/ingresarProducto.html', {'formProducto': form})

#--------------ingresar proveedor
@login_required
def ingresarProveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if(form.is_valid):
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/ingresarProveedor')
    else:
        form = ProveedorForm()
        return render(request, 'app/ingresarProveedor.html', {'formProveedor': form})


        
#------------------editar productos
@login_required
def editarProducto(request, producto_id):
    # Recuperamos el objeto asociado al id
    instancia = Producto.objects.get(id=producto_id)
    # creamos un formulario que contenta los datos del registros recuperado
    form = ProductoForm(instance=instancia)

    #Comprobamos que sea enviado el formulario
    
    if request.method =="POST":
        form= ProductoForm(request.POST, instance= instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "app/editarProducto.html",{'form':form})
         
@login_required   
def borrarProducto(request, producto_id):
    instancia = Producto.objects.get(id=producto_id)
    instancia.delete()
    return redirect("/listarProductosFull")   #--> al raiz de las páginas


#------------------editar proveedores
@login_required
def editarProveedor(request, proveedor_id):
    # Recuperamos el objeto asociado al id
    instancia = Proveedor.objects.get(id=proveedor_id)
    # creamos un formulario que contenta los datos del registros recuperado
    form = ProveedorForm(instance=instancia)

    #Comprobamos que sea enviado el formulario
    
    if request.method =="POST":
        form= ProveedorForm(request.POST, instance= instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "app/editarProveedor.html",{'form':form})
         
@login_required   
def borrarProveedor(request, proveedor_id):
    instancia = Proveedor.objects.get(id=proveedor_id)
    instancia.delete()
    return redirect("/listarProveedoresFull")   #--> al raiz de las páginas


# ------------------listar Proveedores
@login_required
def listarProveedores(request):
    proveedor = Proveedor.objects.all()
    rut = ""

    if request.POST.get('rut'):
        rut = request.POST.get('rut')
        proveedor = proveedor.filter(rut=rut)

    if request.POST.get('nombre'):
        nombre = request.POST.get('nombre')
        proveedor = proveedor.filter(nombre=nombre)

    return render(request, "app/listarProveedores.html", {'proveedor': proveedor})






@login_required
def listarProveedoresFull(request):
    proveedor = Proveedor.objects.all()
    rut = ""

    if request.POST.get('rut'):
        rut = request.POST.get('rut')
        proveedor = proveedor.filter(rut=rut)

    if request.POST.get('nombre'):
        nombre = request.POST.get('nombre')
        proveedor = proveedor.filter(nombre=nombre)

    return render(request, "app/listarProveedoresFull.html", {'proveedor': proveedor})
    
    
    
    
# ------------------filtros
@login_required
def listarProductos(request):
    producto = Producto.objects.all()
    precio = 0  # Filtro por defecto

    if request.POST.get('precio'):
        precio = int(request.POST.get('precio'))
        producto = producto.filter(precio__exact=precio)

    if request.POST.get('clasificacion'):
        clasificacion = request.POST.get('clasificacion')
        producto = producto.filter(clasificacion__exact=clasificacion)

    return render(request, "app/listarProductos.html", {'producto': producto})



@login_required
def listarProductosFull(request):
    producto = Producto.objects.all()
    precio = 0  # Filtro por defecto

    if request.POST.get('precio'):
        precio = int(request.POST.get('precio'))
        producto = producto.filter(precio__exact=precio)

    if request.POST.get('clasificacion'):
        clasificacion = request.POST.get('clasificacion')
        producto = producto.filter(clasificacion__exact=clasificacion)

    return render(request, "app/listarProductosFull.html", {'producto': producto})



# @login_required
# def listarProductos(request):
#     # creamos una variable que será colección y carga TODOS los registros
#     producto = Producto.objects.all()
#     # renderizamos la colección en el template: listar_carreras.html
#     return render(request, "app/listarProductos.html",
#                   {'producto': producto})
