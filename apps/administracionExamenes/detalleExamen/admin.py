from django.contrib import admin
from apps.administracionExamenes.detalleExamen.models import DetallesExamen

#DETALLE COMPRA
@admin.register(DetallesExamen)
class DetalleExamenAdmin(admin.ModelAdmin):
    #search_fields = ('consulta_clienteId')
    list_display = ('examen', 'consulta', 'fechaEntrega', 'precio')