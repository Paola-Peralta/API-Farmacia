from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.shortcuts import get_object_or_404
from apps.movimientos.facturas.models import Factura, DetalleFactura
from apps.catalogos.productos.models import Producto
from apps.catalogos.clientes.models import Clientes
from apps.catalogos.tipoFactura.models import TipoFacturas
from apps.movimientos.facturas.Api.serializers import FacturaSerializer
from drf_yasg.utils import swagger_auto_schema

class FacturaApiView(APIView):
    
    @swagger_auto_schema(request_body=FacturaSerializer)
    def post(self,request):
        serializer = FacturaSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    codigo = serializer.validated_data.get('codigo')
                    fecha = serializer.validated_data.get('fecha')
                    iva = serializer.validated_data.get('iva')
                    descuento = serializer.validated_data.get('descuento')
                    cliente = get_object_or_404(Clientes,id=serializer.validated_data.get('clienteId').id)
                    tipoFactura = get_object_or_404(TipoFacturas,id=serializer.validated_data.get('tipoFacturaId').id)
                    detalle_data = serializer.validated_data.get('detalles')

                    factura = Factura.objects.create(codigo=codigo, fecha=fecha, iva=iva, descuento= descuento,clienteId=cliente, tipoFacturaId =tipoFactura)
                    iva = 0
                    descuento = 0

                    for detalles_data in detalle_data:
                        producto = get_object_or_404(Producto, id=detalles_data['producto'].id)
                        cantidad = detalles_data['cantidad']

                        if producto.cantidad < cantidad:
                            return Response(
                                {"Error": f"Stock insuficiente para el producto: {producto.nombreProducto}"},
                                status=status.HTTP_400_BAD_REQUEST
                            )
                        producto.cantidad -= cantidad
                        producto.save()

                        DetalleFactura.objects.create(
                            factura=factura,
                            producto=producto,
                            cantidad=cantidad,
                            precio=detalles_data['precio']                           
                        )
                    factura.save()

                    facturaSerializer = FacturaSerializer(factura)
                    return Response(facturaSerializer.data, status=status.HTTP_201_CREATED)
                
            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
