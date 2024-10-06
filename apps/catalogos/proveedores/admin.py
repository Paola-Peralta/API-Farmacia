from django.contrib import admin
from apps.catalogos.proveedores.models import Proveedores

@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'telefono']
    list_display = ['codigo', 'nombres', 'primerApellido', 'segundoApellido','email', 'direccion', 'telefono' ]
