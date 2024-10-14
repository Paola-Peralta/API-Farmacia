from django.urls import path
from .views import ProveedoresApiView

app_name = 'proveedores'

urlpatterns = [
    path('', ProveedoresApiView.as_view(), name='proveedores'),
    path('<int:pk>/', ProveedoresApiView.as_view(), name='proveedores-update'),
]