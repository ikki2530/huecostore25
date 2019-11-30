from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre',)

class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ['nombresProveedor', 'apellidosProveedor', 'correo']
    list_display = ('nombresProveedor', 'apellidosProveedor', 'correo', 'fecha_creacion')


admin.site.register(Categoria, CategoriaAdmin) #CategoriaAdmin agrega el buscador
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto)
