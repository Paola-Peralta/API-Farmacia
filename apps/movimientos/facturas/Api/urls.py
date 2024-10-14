from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.movimientos.facturas.Api.views import FacturaViewSet
from .views import *

router = DefaultRouter()
router.register(r'facturas', FacturaViewSet, basename='facturas')

urlpatterns = [
    path('', include(router.urls)),
]