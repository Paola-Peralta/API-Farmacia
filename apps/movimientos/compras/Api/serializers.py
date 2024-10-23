from rest_framework.serializers import ModelSerializer, CharField

from apps.movimientos.compras.models import Compra, DetallesCompras

#Serializador de la clase DetalleCompras
class DetalleCompraSerializer(ModelSerializer):
    producto_nombre = CharField(source='producto.nombreProducto', read_only=True)
    class Meta:
        model = DetallesCompras
        fields = ['producto','cantidad','precio','producto_nombre']

#Serializador de la clase Compra
class CompraSerializer(ModelSerializer):
    detalles = DetalleCompraSerializer(many=True)
    proveedor_nombre = CharField(source='proveedorId.nombres', read_only = True)
    tipo_compra = CharField(source='tipoDeCompraId.descripcion',read_only = True)
    class Meta:
        model = Compra
        fields = ['codigo','fecha','proveedorId','proveedor_nombre','tipoDeCompraId', 'tipo_compra', 'detalles']