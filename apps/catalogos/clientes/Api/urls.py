from django.urls import path
from .views import ClientesApiView, ClienteDetails

app_name = 'clientes'

urlpatterns = [
    path('', ClientesApiView.as_view(), name='clientes'),
    path('<int:pk>/', ClienteDetails.as_view()),  # Para PUT
]
