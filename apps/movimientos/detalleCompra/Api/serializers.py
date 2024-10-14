from rest_framework.serializers import ModelSerializer
from apps.movimientos.detalleCompra.models import DetallesCompras

class DetalleComprasSerializer(ModelSerializer):
    class Meta:
        model = DetallesCompras
        fields = ['compra', 'producto', 'cantidad', 'precio']