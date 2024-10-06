from django.contrib import admin
from apps.administracionExamenes.consultas.models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'clienteId']
    list_display = ['codigo', 'fecha', 'clienteId']