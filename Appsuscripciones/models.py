from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Plan(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Plan {self.nombre}, con precio de ${self.precio} al mes'
    
    class Meta:
        db_table = 'plan' #Como se va a ver en la basen de datos
        verbose_name = 'plan'
        verbose_name_plural = 'planes'

class Suscripcion(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suscripcion')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'El usuario{self.user.first_name} tiene el plan {self.plan.nombre} con un valor de {self.plan.precio}'
    
    class Meta:
        db_table = 'detalle_suscripcion' #Como se va a ver en la basen de datos
        verbose_name = 'suscripcion'
        verbose_name_plural = 'suscripciones'