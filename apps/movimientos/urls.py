from django.urls import path, include

urlpatterns = [
    path('compras/', include('apps.movimientos.compras.Api.urls')),
    path('facturas/', include('apps.movimientos.facturas.Api.urls')),
    path('detalleCompra/', include('apps.movimientos.detalleCompra.Api.urls')),
    path('detalleFactura/', include('apps.movimientos.detalleFactura.Api.urls')),
]