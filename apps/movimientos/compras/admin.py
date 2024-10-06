from django.contrib import admin
from apps.movimientos.compras.models import Compra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'fecha', 'proveedorId', 'tipoDeCompraId']

