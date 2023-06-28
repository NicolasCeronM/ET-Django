from django.contrib import admin
from .models import DetallePedido, Pedido

# Register your models here.

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
admin.site.register(DetallePedido)
