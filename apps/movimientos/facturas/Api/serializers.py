from rest_framework.serializers import ModelSerializer, CharField
from apps.movimientos.facturas.models import Factura, DetalleFactura

class DetalleFacturaSerializer(ModelSerializer):
    producto_nombre = CharField(source='producto.nombreProducto', read_only=True)
    class Meta:
        model = DetalleFactura
        fields = ['producto','producto_nombre','cantidad','precio']

class FacturaSerializer(ModelSerializer):
    detalles = DetalleFacturaSerializer(many= True)
    cliente_nombre = CharField(source='clienteId.nombres', read_only = True)
    tipo_factura = CharField(source='tipoFacturaId.descripcion', read_only = True)

    class Meta:
        model = Factura
        fields = ['codigo', 'fecha', 'iva', 'descuento','clienteId','cliente_nombre','tipoFacturaId','tipo_factura','detalles']


