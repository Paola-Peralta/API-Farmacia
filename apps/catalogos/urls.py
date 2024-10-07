from django.urls import path, include

urlpatterns = [
    path('clientes/', include('apps.catalogos.clientes.urls')),
    path('proveedores/', include('apps.catalogos.proveedores.urls')),
]
