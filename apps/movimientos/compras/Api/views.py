from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.movimientos.compras.models import Compra
from apps.movimientos.compras.Api.serializers import CompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer