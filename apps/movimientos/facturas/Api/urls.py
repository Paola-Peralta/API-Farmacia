from django.urls import path, include
from apps.movimientos.facturas.Api.views import FacturaApiView

app_name = 'facturas'
urlpatterns = [
    path('', FacturaApiView.as_view(), name='facturas'),
]