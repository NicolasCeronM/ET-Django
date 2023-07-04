from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "admin_page"

urlpatterns = [
    #Paginas principales
    path('', views.inicio, name='inicio'),
    path('usuarios/',views.usuarios,name='usuarios'),
    path('productos/',views.productos, name='productos'),
    path('descuentos/',views.descuento, name='descuentos'), 
    path('planes/',views.planes, name='planes'),
    #Acciones
    path('editar/<id>/',views.user_edit, name='editar'),
    path('modificar/<id>/',views.modificar_producto, name='modificar'),
    path('eliminar/<id>/',views.eliminar, name='eliminar'),
    path('eliminar_user/<id>/',views.eliminar_usuario, name='eliminar_user'),
    #Acciones de descuento
    path('nuevo_descuento/', views.nuevo_descuento, name='nuevo_descuento'),
    path('eliminar_descuento/<id>/',views.eliminar_descuento, name='eliminar_descuento'),
    #Acciones de planes mensuales
    path('eliminar_plan/<id>/', views.eliminar_plan,name='eliminar_plan'),
    #Cerrar sesion
    path('salir',views.salir, name='salir'),
]
