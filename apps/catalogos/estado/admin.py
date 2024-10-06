from django.contrib import admin
from apps.catalogos.estado.models import Estado

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'tipoEstado']
