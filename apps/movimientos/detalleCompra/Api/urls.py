from django.urls import path
from .views import DetalleCompraApiView

app_name = 'detalleCompra'

urlpatterns = [
    path('', DetalleCompraApiView.as_view(), name='detalleCompra'),
]
