from rest_framework.serializers import ModelSerializer 
from apps.movimientos.compras.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ['codigo', 'fecha', 'proveedorId', 'tipoDeCompraId']