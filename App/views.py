from django.shortcuts import render, redirect
from .models import Articulo
from django.contrib.auth import logout
from .forms import CustomUserForm
from django.contrib.auth import authenticate
from django.contrib import messages
from AppDescuento.models import Descuento

# Create your views here.

def index(request):

    descuentos = Descuento.objects.all()
    productos = Articulo.objects.all()

    for producto in productos:
        for descuento in descuentos:
            if producto == descuento.producto:
                producto.precio = round(producto.precio - (producto.precio * descuento.pct) / 100)


    data ={
        'descuentos': descuentos,
        'productos':productos
    }


    return render(request,'ProyectoEtApp/index.html', data)


def juguestes(request):

    productos = Articulo.objects.all()
    descuentos = Descuento.objects.all()

    for producto in productos:
        for descuento in descuentos:
            if producto == descuento.producto:
                producto.precio = round(producto.precio - (producto.precio * descuento.pct) / 100)

    data = {
        'descuentos': descuentos,
        'productos':productos
    }


    return render(request, 'ProyectoEtApp/juguestes.html',data)


def medicamentos(request):

    productos = Articulo.objects.all()
    descuentos = Descuento.objects.all()

    for producto in productos:
        for descuento in descuentos:
            if producto == descuento.producto:
                producto.precio = round(producto.precio - (producto.precio * descuento.pct) / 100)

    data = {
        'descuentos': descuentos,
        'productos':productos
    }
    return render(request, 'ProyectoEtApp/medicamentos.html',data)

def comida(request):
    productos = Articulo.objects.all()
    descuentos = Descuento.objects.all()

    for producto in productos:
        for descuento in descuentos:
            if producto == descuento.producto:
                producto.precio = round(producto.precio - (producto.precio * descuento.pct) / 100)

    data = {
        'descuentos': descuentos,
        'productos':productos
    }

    return render(request, 'ProyectoEtApp/comida.html',data)

def ropa(request):
    productos = Articulo.objects.all()
    descuentos = Descuento.objects.all()

    for producto in productos:
        for descuento in descuentos:
            if producto == descuento.producto:
                producto.precio = round(producto.precio - (producto.precio * descuento.pct) / 100)

    data = {
        'descuentos': descuentos,
        'productos':productos
    }

    return render(request,'ProyectoEtApp/ropa.html',data)

def login(request):
    pass

def registrar(request):

    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':

        formulario = CustomUserForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            #Autenticar usuario
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            messages.success(request,'Creado correctamente')
            return redirect(to='login')
        data['form'] = formulario
        

    return render(request,'registration/registrar.html', data)

def suscripcion(request):


    return render(request,'ProyectoEtApp/suscripcion.html')