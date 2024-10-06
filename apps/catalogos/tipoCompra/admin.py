from django.contrib import admin
from apps.catalogos.tipoCompra.models import TipoCompras
#TIPO DE COMPRA
@admin.register(TipoCompras)
class TipocompraAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'descripcion']