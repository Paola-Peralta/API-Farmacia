from django.contrib import admin
from apps.movimientos.compras.models import Compra, DetallesCompras

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'fecha', 'proveedorId', 'tipoDeCompraId']

#DETALLE COMPRA
@admin.register(DetallesCompras)
class DetalleComprasAdmin(admin.ModelAdmin):
    list_display = ('compra', 'producto', 'cantidad', 'precio')
    search_fields = ('compra__codigo', 'producto__nombreProducto')