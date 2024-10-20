from django.contrib import admin
from apps.movimientos.facturas.models import Factura, DetalleFactura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'fecha', 'iva', 'descuento', 'clienteId', 'tipoFacturaId']

#DETALLE FACTURA
@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad', 'precio')
    search_fields = ('factura__codigo', 'producto__nombreProducto')