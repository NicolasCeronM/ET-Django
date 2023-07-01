from django.shortcuts import render
from .models import Plan

# Create your views here.

def suscripcion(request):

    planes = Plan.objects.all()

    data = {
        'planes':planes
    }

    return render(request,'suscripcion.html', data)
