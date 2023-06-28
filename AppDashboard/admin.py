from django.contrib import admin
from App.models import Direccion

# Register your models here.

class DireccionAdmin(admin.ModelAdmin):
    list_display =('user','direccion','region','comuna')

admin.site.register(Direccion,DireccionAdmin)
