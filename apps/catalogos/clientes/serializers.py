from rest_framework.serializers import ModelSerializer
from apps.catalogos.clientes.models import Clientes

class ClientesSerializer(ModelSerializer):
    class Meta:
        model = Clientes
        fields = ['codigo', 'nombres', 'primerApellido','segundoApellido','direccion','telefono']