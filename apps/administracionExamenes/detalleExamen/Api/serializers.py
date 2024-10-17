from rest_framework.serializers import ModelSerializer 
from apps.administracionExamenes.detalleExamen.models import DetallesExamen

class DetalleExamenSerializer(ModelSerializer):
    class Meta:
        model = DetallesExamen
        fields = ['examen', 'consulta', 'fechaEntrega' , 'precio']