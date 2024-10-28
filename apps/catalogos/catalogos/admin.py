from django.contrib import admin
from apps.catalogos.catalogos.models import Categoria
from apps.catalogos.catalogos.models import Presentaciones
from apps.catalogos.catalogos.models import Medidas
from apps.catalogos.catalogos.models import Municipio
from apps.catalogos.catalogos.models import Departamento
from apps.catalogos.catalogos.models import Sucursal

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

#Departamento
@admin.register (Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'descripcion']
    list_display = ['codigo', 'descripcion' ]

#Municipio
@admin.register (Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'descripcion']
    list_display = ['codigo', 'descripcion','departamento']


#CATALOGOS
@admin.register (Sucursal)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'nombre']
    list_display = ['codigo', 'nombre','municipio' ]
