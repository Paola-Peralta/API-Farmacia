from django.contrib import admin
from apps.catalogos.clientes.models import Clientes

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'telefono']
    list_display = ['codigo', 'nombres', 'primerApellido', 'segundoApellido', 'direccion', 'telefono' ]
