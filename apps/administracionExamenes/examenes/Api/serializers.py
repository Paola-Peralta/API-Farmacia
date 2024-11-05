from rest_framework.serializers import ModelSerializer, CharField
from apps.administracionExamenes.examenes.models import Examen, DetallesExamen

#Serializer de la clase DetalleExamen
class DetalleExamenSerializer(ModelSerializer):
    consulta_codigo = CharField(source='consulta.codigo', read_only=True)
    class Meta:
        model = DetallesExamen
        fields = ['consulta','consulta_codigo','fechaEntrega','precio']

#Serializador del examen
class ExamenSerializer(ModelSerializer):
    detalles = DetalleExamenSerializer(many=True)
    class Meta:
        model = Examen
        fields = ['codigo','descripcion','detalles']