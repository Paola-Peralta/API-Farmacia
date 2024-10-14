from rest_framework.serializers import ModelSerializer
from apps.catalogos.catalogos.models import Categoria, Presentaciones, Medidas

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['codigo', 'descripcion']

class PresentacionesSerializer(ModelSerializer):
    class Meta:
        model = Presentaciones
        fields = ['codigo','descripcion']

class MedidasSerializer(ModelSerializer):
    class Meta:
        model = Medidas
        fields = ['codigo','descripcion']