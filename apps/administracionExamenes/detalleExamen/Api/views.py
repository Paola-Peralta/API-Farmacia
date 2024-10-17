from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.administracionExamenes.detalleExamen.models import DetallesExamen
from apps.administracionExamenes.detalleExamen.Api.serializers import DetalleExamenSerializer

class DetallesExamenViewSet(ModelViewSet):
    queryset = DetallesExamen.objects.all()
    serializer_class = DetalleExamenSerializer