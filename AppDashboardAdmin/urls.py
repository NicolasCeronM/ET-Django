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
    #Acciones
    path('editar/<id>/',views.user_edit, name='editar'),
    path('modificar/<id>/',views.modificar_producto, name='modificar'),
    path('eliminar/<id>/',views.eliminar, name='eliminar'),
    path('eliminar_user/<id>/',views.eliminar_usuario, name='eliminar_user'),
    path('salir',views.salir, name='salir'),
]
