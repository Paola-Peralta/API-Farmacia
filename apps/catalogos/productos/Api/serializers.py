from rest_framework.serializers import ModelSerializer
from apps.catalogos.productos.models import Producto

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigoProducto', 'nombreProducto','cantidad','fechaVencimiento','precio','categoria','medidas','presentaciones']