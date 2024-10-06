from django.contrib import admin
from apps.catalogos.catalogos.models import Categoria
from apps.catalogos.catalogos.models import Presentaciones
from apps.catalogos.catalogos.models import Medidas

#CATALOGOS
@admin.register (Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'descripcion']
    list_display = ['codigo', 'descripcion' ]

#PRESENTACIONES
@admin.register (Presentaciones)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'descripcion']
    list_display = ['codigo', 'descripcion' ]

#UNIDAD DE MEDIDA
@admin.register (Medidas)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'descripcion']
    list_display = ['id','codigo', 'descripcion' ]
