from django.shortcuts import render,redirect
from .carro import Carro
from App.models import Articulo
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def agregar_producto(request,producto_id):

    carro = Carro(request)

    producto = Articulo.objects.get(id=producto_id)

    carro.agregar(producto = producto)

    return redirect("dashboard:carro")

def eliminiar_producto(request,producto_id):

    carro = Carro(request)

    producto = Articulo.objects.get(id=producto_id)

    carro.eliminar(producto = producto)

    return redirect("index")

def restar_producto(request,producto_id):

    carro = Carro(request)

    producto = Articulo.objects.get(id=producto_id)

    carro.restar_producto(producto = producto)

    return redirect("dashboard:carro")

def limpiar_carro(request):

    carro = Carro(request)
    carro.limpiar_carro()

    return redirect("index")