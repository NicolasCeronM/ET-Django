from django.urls import path
from . import views

app_name = "suscripciones"

urlpatterns = [

    path('',views.suscripcion, name='suscripciones'),
]