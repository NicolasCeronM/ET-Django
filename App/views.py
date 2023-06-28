from django.shortcuts import render, redirect
from .models import Articulo
from django.contrib.auth import logout
from .forms import CustomUserForm
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request,'ProyectoEtApp/index.html')


def juguestes(request):

    articulo = Articulo.objects.all()

    return render(request, 'ProyectoEtApp/juguestes.html',{'articulos':articulo})


def medicamentos(request):

    articulo = Articulo.objects.all()
    return render(request, 'ProyectoEtApp/medicamentos.html',{'articulos':articulo})

def comida(request):
    articulo = Articulo.objects.all()
    return render(request, 'ProyectoEtApp/comida.html',{'articulos':articulo})

def ropa(request):
    articulo = Articulo.objects.all()
    return render(request,'ProyectoEtApp/ropa.html',{'articulos':articulo})

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