from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, PresentacionesViewSet, MedidasViewSet
from .views import *

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'presentaciones', PresentacionesViewSet, basename ='presentaciones')
router.register(r'medidas', MedidasViewSet, basename='medidas')

urlpatterns = [
    path('', include(router.urls)),
]