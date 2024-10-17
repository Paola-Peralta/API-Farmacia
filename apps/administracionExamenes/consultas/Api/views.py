from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.administracionExamenes.consultas.models import Consulta
from apps.administracionExamenes.consultas.Api.serializers import ConsultaSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer