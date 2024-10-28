from django.urls import path, include
from apps.movimientos.facturas.Api.views import FacturaApiView, FacturaDetails

app_name = 'facturas'
urlpatterns = [
    path('', FacturaApiView.as_view(), name='facturas'),
    path('<int:pk>/', FacturaDetails.as_view()),  # Para PUT
]