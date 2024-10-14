from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.movimientos.compras.Api.views import CompraViewSet
from .views import *

router = DefaultRouter()
router.register(r'compras', CompraViewSet, basename='compras')
urlpatterns = [
    path('', include(router.urls)),
]