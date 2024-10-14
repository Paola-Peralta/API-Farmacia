from django.urls import path
from .views import DetalleFacturaApiView

app_name = 'detalleCompra'

urlpatterns = [
    path('', DetalleFacturaApiView.as_view(), name='detalleFactura'),
]
