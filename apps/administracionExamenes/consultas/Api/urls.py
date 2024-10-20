from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.administracionExamenes.consultas.Api.views import ConsultaViewSet
from .views import *

router = DefaultRouter()
router.register(r'consultas', ConsultaViewSet, basename='consultas')
urlpatterns = [
    path('', include(router.urls)),
]