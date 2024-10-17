from rest_framework.serializers import ModelSerializer 
from apps.administracionExamenes.consultas.models import Consulta

class ConsultaSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['codigo', 'fecha', 'clienteId']