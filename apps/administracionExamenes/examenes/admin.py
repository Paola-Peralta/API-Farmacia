from django.contrib import admin
from apps.administracionExamenes.examenes.models import Examen, DetallesExamen

@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'descripcion']
    list_display = ['codigo', 'descripcion', 'costo'] 

 #DETALLE EXAMEN
@admin.register(DetallesExamen)
class DetalleExamenAdmin(admin.ModelAdmin):
    #search_fields = ('consulta_clienteId')
    list_display = ('examen', 'consulta', 'fechaEntrega', 'precio')