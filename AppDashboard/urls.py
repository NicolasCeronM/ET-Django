from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [

    path('',views.dash_usuario, name='dashboard'),
    path('carro/',views.dash_carro, name='carro'),
    path('direcciones/',views.dash_direc, name='direcciones'),
    path('crear_direc/',views.craer_direc, name='crear_direc'),
    path('eliminar_direc/<id>/',views.eliminar_direc,name='eliminar_direc'),
    path('editar_direc/<id>/', views.direc_edit, name='editar_direc'),
    path('modificar_direc/<id>/', views.modificar_direc, name='modificar_direc'),
    path('compras/',views.dash_compras,name='compras'),
    path('salir/',views.salir,name='salir'),

]