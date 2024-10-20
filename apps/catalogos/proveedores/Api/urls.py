from django.urls import path
from .views import ProveedoresApiView, ProveedoresDetails

app_name = 'proveedores'

urlpatterns = [
    path('', ProveedoresApiView.as_view(), name='proveedores'),
    path('<int:pk>/', ProveedoresDetails.as_view()),
]