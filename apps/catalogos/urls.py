from django.urls import path, include

urlpatterns = [
    path('clientes/', include('apps.catalogos.clientes.Api.urls')),
    path('proveedores/', include('apps.catalogos.proveedores.Api.urls')),
    path('catalogos/', include('apps.catalogos.catalogos.Api.urls')),
]
