from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.administracionExamenes.detalleExamen.Api.views import DetallesExamenViewSet
from .views import *

router = DefaultRouter()
router.register(r'DetalleExamen', DetallesExamenViewSet, basename='DetalleExamen')
urlpatterns = [
    path('', include(router.urls)),
]