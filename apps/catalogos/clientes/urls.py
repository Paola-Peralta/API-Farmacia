from django.urls import path
from .views import ClientesApiView

app_name = 'clientes'

urlpatterns = [
    path('', ClientesApiView.as_view(), name='clientes'),
    path('<int:pk>/', ClientesApiView.as_view(), name='clientes-update'),  # Para PUT
]
