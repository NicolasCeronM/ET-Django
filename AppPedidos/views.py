from django.shortcuts import render,redirect
from .models import Pedido,DetallePedido
from AppCarro.carro import Carro
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django. utils.html import strip_tags
from django.contrib.auth.models import User
from AppCarro.context_processor import importe_total_carro
from Appsuscripciones.models import Suscripcion


# Create your views here.

def pedidos(request):

    pedido = Pedido.objects.filter(user=request.user)
    detalle = DetallePedido.objects.filter(user=request.user)

    ctx = {
        'pedido': pedido,
        'detalle_pedido': detalle,
    }
    return render(request,'Dashboards/compras.html',ctx)

def procesar_pedido(request):

    suscripciones = Suscripcion.objects.all()

    total = importe_total_carro(request)
    importe_total = total['importe_total_carro']

    for suscripcion in suscripciones:
        if request.user.id == suscripcion.user.id:
            importe_total = round(importe_total - (importe_total * 15) / 100)
            break
            

    pedido = Pedido.objects.create(user=request.user,total=importe_total)
    carro = Carro(request)

    detalle_pedido = list()

    for key,value in carro.carro.items():

        detalle_pedido.append(DetallePedido(

            user = request.user,
            producto_id = key,
            pedido = pedido,
            cantidad = value['cantidad'],
        ))


    DetallePedido.objects.bulk_create(detalle_pedido)
                           
    enviar_mail(
        pedido=pedido,
        detalle_pedido = detalle_pedido,
        nombreusuario=request.user.username,
        emailusuario = request.user.email,
        total = importe_total_carro(request)

    )

    pedido = Pedido.objects.filter(user=request.user)
    detalle = DetallePedido.objects.filter(user=request.user)

    ctx = {
        'pedido': pedido,
        'detalle_pedido': detalle,
    }


    messages.success(request,'El pedido se a enviado correctamente')

    return redirect(to='pedido:pedidos')


def enviar_mail(**kwargs):

    asunto = 'Gracias por el pedido'

    ctx = {
        'pedido': kwargs.get('pedido'),
        'detalle_pedido': kwargs.get('detalle_pedido'),
        'nombreusuario':kwargs.get('nombreusuario'),
        'total': kwargs.get('total'),
    }

    mensaje =render_to_string('pedido/pedido.html',ctx)

    mensaje_texto = strip_tags(mensaje)
    from_email='nicolas134b@gmail.com'
    to= kwargs.get('emailusuario')

    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)

