from django.contrib import admin
from apps.administracionExamenes.examenes.models import Examen

@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'descripcion']
    list_display = ['codigo', 'descripcion', 'costo'] 

