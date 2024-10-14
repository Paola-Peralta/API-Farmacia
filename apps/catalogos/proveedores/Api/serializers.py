from rest_framework.serializers import ModelSerializer
from apps.catalogos.proveedores.models import Proveedores

class ProveedoresSerializer(ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ['codigo', 'nombres', 'primerApellido','segundoApellido','email','direccion','telefono']