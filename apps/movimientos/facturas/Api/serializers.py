from rest_framework.serializers import ModelSerializer
from apps.movimientos.facturas.models import Factura

class FacturaSerializer(ModelSerializer):
    class Meta:
        model = Factura
        fields = ['codigo', 'fecha', 'iva', 'descuento', 'clienteId', 'tipoFacturaId']