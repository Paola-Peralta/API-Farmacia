from rest_framework.serializers import ModelSerializer 
from apps.administracionExamenes.examenes.models import Examen

class ExamenSerializer(ModelSerializer):
    class Meta:
        model = Examen
        fields = ['codigo', 'descripcion', 'costo']