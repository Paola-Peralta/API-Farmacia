from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction
from apps.movimientos.compras.models import Compra, DetallesCompras
from apps.catalogos.productos.models import Producto
from apps.catalogos.proveedores.models import Proveedores
from apps.catalogos.tipoCompra.models import TipoCompras
from apps.movimientos.compras.Api.serializers import CompraSerializer
from drf_yasg.utils import swagger_auto_schema

class CompraApiView(APIView):
    @swagger_auto_schema(request_body=CompraSerializer)
    def post(self, request):
        serializer = CompraSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    codigo = serializer.validated_data.get('codigo')
                    fecha = serializer.validated_data.get('fecha')
                    proveedores = get_object_or_404(Proveedores, id=serializer.validated_data.get('proveedorId').id)
                    tipoCompra = get_object_or_404(TipoCompras, id=serializer.validated_data.get('tipoDeCompraId').id)
                    detalle_data = serializer.validated_data.get('detalles')
                                                           
                    compra = Compra.objects.create(codigo=codigo, fecha=fecha, proveedorId=proveedores, tipoDeCompraId=tipoCompra)

                    #detalle_data = serializer.validated_data.get('detalles')
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

                        DetallesCompras.objects.create(
                            compra=compra,
                            producto=producto,
                            cantidad=cantidad,
                            precio=detalles_data['precio']                           
                        )
                    compra.save()

                    compraSerializer = CompraSerializer(compra)
                    return Response(compraSerializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)