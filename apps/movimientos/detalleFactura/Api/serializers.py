from rest_framework.serializers import ModelSerializer
from apps.movimientos.detalleFactura.models import DetalleFactura

class DetalleFacturaSerializer(ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = ['factura', 'producto', 'cantidad', 'precio']