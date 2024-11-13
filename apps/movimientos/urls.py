from django.urls import path, include

urlpatterns = [
    path('compras/', include('apps.movimientos.compras.Api.urls' )),
    path('facturas/', include('apps.movimientos.facturas.Api.urls')),
]