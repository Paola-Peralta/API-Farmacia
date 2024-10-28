from rest_framework.serializers import ModelSerializer
from apps.catalogos.productos.models import Producto
from datetime import datetime, timedelta
from rest_framework import serializers

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigoProducto', 'nombreProducto','cantidad','fechaVencimiento','precio','categoria','medidas','presentaciones']

        def validate_fechaVencimiento(self, value):
            # Obtener la fecha actual
            fecha_actual = datetime.now().date()
            
            # Calcular los límites de tiempo para las advertencias y restricciones
            limite_un_mes = fecha_actual + timedelta(days=30)
            limite_dos_meses = fecha_actual + timedelta(days=60)
            
            # Validación para fecha de vencimiento menor a un mes
            if value <= limite_un_mes:
                raise serializers.ValidationError("No se puede registrar un producto que vence en menos de un mes.")
            
            # Advertencia para fecha de vencimiento menor a dos meses
            elif value <= limite_dos_meses:
                self.warning_message = "Advertencia: El producto tiene menos de dos meses para su vencimiento."
            
            return value