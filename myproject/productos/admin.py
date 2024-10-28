from django.contrib import admin
from .models import Fabrica, Producto

class FabricaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'f_vencimiento', 'fabrica')
    list_filter = ('nombre', 'fabrica')

admin.site.register(Fabrica, FabricaAdmin)
admin.site.register(Producto, ProductoAdmin)