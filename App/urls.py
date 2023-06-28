from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [

    path('',views.index, name='index'),
    path('juguetes/',views.juguestes, name='juguetes'),
    path('medicamentos/',views.medicamentos, name='medicamentos'),
    path('comida/',views.comida,name='comida'),
    path('ropa/',views.ropa, name='ropa'),
    path('login/',auth_view.LoginView.as_view(template_name ='registration/login.html'), name='login'),
    path('registrar/',views.registrar, name='registrar'),
    path('plan/',views.suscripcion, name='plan'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)