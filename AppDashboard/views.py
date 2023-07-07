from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from App.models import Direccion
from django.contrib import messages
from django.contrib.auth.models import User
from App.models import Direccion
from AppPedidos.models import Pedido, DetallePedido
from Appsuscripciones.models import Plan, Suscripcion
from AppCarro.context_processor import importe_total_carro
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
@login_required
def dash_usuario(request):

    pedido = Pedido.objects.filter(user=request.user)
    detalle = DetallePedido.objects.filter(user=request.user)
    cant_pedido = pedido.count()


    direc = Direccion.objects.filter(user=request.user) 
    cant_direc = direc.count()

    ctx = {
        'direc':direc,
        'cant_direc':cant_direc,

        'pedido': pedido,
        'detalle_pedido': detalle,
        'cant_pedido':cant_pedido,
    }

    return render (request,'Dashboards/datos_usuario.html',ctx)

@login_required
def dash_carro(request):
    user = User.objects.get(id=request.user.id)
    suscripciones = user.suscripcion.all()    

    total = importe_total_carro(request)
    importe_total = total['importe_total_carro']
    toal_total=importe_total

    for suscripcion in suscripciones:
        if request.user.id == suscripcion.user.id:
            importe_total = round(importe_total - (importe_total * 15) / 100)
            toal_total = importe_total
            break

    data = {
        'suscripciones': suscripciones,
        'toal_total': toal_total,
    }

    return render(request, 'Dashboards/carro.html',data)

@login_required
def dash_direc(request):

    user = User.objects.get(id=request.user.id)
    direcciones = user.direcciones.all() 

    ctx = {'direc':direcciones}
    return render(request,'Dashboards/direcciones.html',ctx)

def craer_direc(request):

    if request.method !='POST':
        messages.success(request,'Error')
        return render(request,'Dashboards/direcciones.html')
    else:
        usuario = request.user
        newDireccion = Direccion(
      
            user = usuario,
            nombre = request.POST.get('nuevoNombre'),
            direccion = request.POST.get('direc'),
            numero = request.POST.get('regNum'),
            region = request.POST.get('regRegion'),
            comuna = request.POST.get('regComuna'),
            cod_postal = request.POST['cpostalComuna']

        )
        newDireccion.save()

        messages.success(request,'Direccion agregada correctamente')

        return redirect(to='dashboard:direcciones')

def eliminar_direc(request,id):

    direccion = get_object_or_404(Direccion,id=id)
    direccion.delete()

    messages.success(request,'Eliminado correctamente')
    return redirect(to='dashboard:direcciones')

def direc_edit(request, id):
    if id != "":
        direc = Direccion.objects.get(id = id)
        context = {"direc": direc}
        return render(request, "Dashboards/direccion_modificar.html", context)
    else:
        context = {"mensaje": "Error, usuario no encontrado"}
        return render(request, "dash_admin/productos.html", context)
    
def modificar_direc(request,id):

    
    if request.method != 'POST':
        return render(request,'Dashboards/direccion_modificar.html')
    else:
        usuario = request.user

        objDireccion = usuario.direcciones.get(id = id)
      
        #objDireccion.user = usuario,
        objDireccion.nombre = request.POST['nuevoNombre']
        objDireccion.direccion = request.POST['direc']
        objDireccion.numero = request.POST['regNum']
        objDireccion.region = request.POST['regRegion']
        objDireccion.comuna = request.POST.get('regComuna')
        objDireccion.cod_postal = request.POST['cpostalComuna']
        objDireccion.save()

        messages.success(request,'Direccion modificada correctamente')

        return redirect(to='dashboard:direcciones')


@login_required
def dash_compras(request):

    return render(request,'Dashboards/compras.html')

def suscripcion_user(request):

    user = User.objects.get(id=request.user.id)
    suscripciones = user.suscripcion.all()

    planes = Plan.objects.all()
    if suscripciones:
        for i in suscripciones:
            fecha_siguiente_mes = i.created_at + relativedelta(months=1) 
    else:
        fecha_siguiente_mes = 0
        
        
    data = {
        'planes':planes,
        'suscripciones': suscripciones,
        'fecha_siguiente_mes':fecha_siguiente_mes,
    }

    return render(request,'suscripcion/suscripcion.html',data)

def nueva_suscripcion(request,id):

    newSuscripcion = Suscripcion.objects.create(
        user = request.user,
        plan_id = id,
        created_at = datetime.now()
    )

    newSuscripcion.save()

    return redirect(to='dashboard:suscripcion')

def eliminar_suscripcion(request,id):

    suscripcion = get_object_or_404(Suscripcion,id=id)
    suscripcion.delete()

    messages.success(request,'Suscripcion cancelada')

    return redirect(to='dashboard:suscripcion')


@login_required
def salir(request):

    logout(request)

    return redirect('index')