from django.contrib import admin
from apps.administracionExamenes.resultado.models import Resultado, ResultadoExamen

@admin.register(Resultado)
class ConsultaAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'descripcion', 'examen']

@admin.register(ResultadoExamen)
class ResultadoExamenAdmin(admin.ModelAdmin):
    list_display = ['detalleExamen', 'resultado', 'valor', 'estado']