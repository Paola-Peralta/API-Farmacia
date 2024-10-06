from django.contrib import admin
from apps.catalogos.tipoFactura.models import TipoFacturas

#TIPO DE FACTURA
@admin.register(TipoFacturas)
class TipocompraAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'descripcion']
