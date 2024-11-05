from django.urls import path, include
from apps.movimientos.compras.Api.views import CompraApiView, CompraDetails

app_name = 'compras'
urlpatterns = [
    path('', CompraApiView.as_view(), name='compras'),
    path('<int:pk>/', CompraDetails.as_view()),
]