from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.administracionExamenes.examenes.models import Examen
from apps.administracionExamenes.examenes.Api.serializers import ExamenSerializer

class ExamenViewSet(ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer