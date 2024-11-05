from rest_framework.serializers import ModelSerializer, CharField
from apps.administracionExamenes.resultado.models import Resultado, ResultadoExamen

class DetalleResuladoSerializer(ModelSerializer):
    detalleExamenConsulta = CharField(source='detalleExamen.consulta', read_only=True)
    estado_nombre = CharField(source='estado.tipoEstado', read_only = True)
    class Meta:
        model= ResultadoExamen
        fields=['detalleExamen','detalleExamenConsulta','valor','estado','estado_nombre']


class ResultadoSerializer(ModelSerializer):
    examen_nombre = CharField(source='examen.descripcion', read_only=True)
    detalles = DetalleResuladoSerializer(many=True)
    class Meta:
        model= Resultado
        fields=['codigo','descripcion','examen','examen_nombre', 'detalles']
