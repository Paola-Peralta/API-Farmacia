from django.contrib import admin
from apps.movimientos.detalleCompra.models import DetallesCompras

#DETALLE COMPRA
@admin.register(DetallesCompras)
class DetalleComprasAdmin(admin.ModelAdmin):
    list_display = ('compra', 'producto', 'cantidad', 'precio')
    search_fields = ('compra__codigo', 'producto__nombreProducto')
    #list_filter = ('compra', 'producto')
