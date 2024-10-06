from django.contrib import admin
from apps.movimientos.facturas.models import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'fecha', 'iva', 'descuento', 'clienteId', 'tipoFacturaId']
