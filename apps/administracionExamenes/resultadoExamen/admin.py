from django.contrib import admin
from apps.administracionExamenes.resultadoExamen.models import ResultadoExamen

@admin.register(ResultadoExamen)
class ResultadoExamenAdmin(admin.ModelAdmin):
    list_display = ['detalleExamen', 'resultado', 'valor', 'estado']