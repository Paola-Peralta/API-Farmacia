from django.contrib import admin
from apps.administracionExamenes.resultado.models import Resultado

@admin.register(Resultado)
class ConsultaAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'descripcion', 'examen']

