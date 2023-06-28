from django.contrib import admin
from .models import Articulo

# Register your models here.

class  ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre','seccion')
    list_filter = ('seccion','created')
    readonly_fields = ('created','updated')


admin.site.register(Articulo, ArticuloAdmin)