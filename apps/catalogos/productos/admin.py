from django.contrib import admin
from apps.catalogos.productos.models import Producto

@admin.register (Producto)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'codigoProducto']
    list_display = ['codigoProducto', 'nombreProducto', 'cantidad','fechaVencimiento','precio', 'categoria', 'medidas', 'presentaciones']

