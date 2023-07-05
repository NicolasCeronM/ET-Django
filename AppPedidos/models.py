from django.db import models
from django.contrib.auth import get_user_model
from App.models import Articulo
from django.db.models import F,Sum, FloatField
# Create your models here.

User = get_user_model()

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='pedidos')
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()

    def __str__(self):

        return str(self.id)
    

    class Meta:
        db_table = 'pedidos' #Como se va a ver en la basen de datos
        verbose_name ='pedido'
        verbose_name_plural ='pedidos'

class DetallePedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='detalle_pedido')
    producto = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):

        return f'{self.cantidad} unidades de {self.producto.nombre}, '
    
    class Meta:
        db_table = 'detalle_pedido' #Como se va a ver en la basen de datos
        verbose_name ='detalle_pedido'
        verbose_name_plural ='detalle_pedidos'
