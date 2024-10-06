from django.contrib import admin
from apps.movimientos.detalleFactura.models import DetalleFactura

#DETALLE FACTURA
@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad', 'precio')
    search_fields = ('factura__codigo', 'producto__nombreProducto')
    #list_filter = ('factura', 'producto')