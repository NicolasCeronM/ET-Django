from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Articulo(models.Model):

    imagen = models.ImageField(upload_to='articulos/')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    precio = models.IntegerField()  
    seccion = models.CharField( max_length=30)
    stock = models.IntegerField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'articulo'
        verbose_name_plural = 'articulos'
    
class Direccion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='direcciones')
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    numero = models.IntegerField()
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    cod_postal = models.CharField(max_length=20,null=True, blank=True)