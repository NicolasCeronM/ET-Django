from django.db import models
from App.models import Articulo

# Create your models here.

class Descuento(models.Model):

    producto = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='descuento')
    pct = models.IntegerField()
    fec_ini = models.DateField()
    fec_ter = models.DateField()

    def __str__(self):
        return f'{self.producto} tiene un descuento de {self.pct}%'
    
    class Meta:
        db_table = 'descuento' #Como se va a ver en la basen de datos
        verbose_name ='descuento'
        verbose_name_plural ='descuentos'