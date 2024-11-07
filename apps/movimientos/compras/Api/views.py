from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction
from apps.movimientos.compras.models import Compra, DetallesCompras
from apps.catalogos.productos.models import Producto
from apps.catalogos.proveedores.models import Proveedores
from apps.catalogos.catalogos.models import Sucursal
from apps.catalogos.tipoCompra.models import TipoCompras
from apps.movimientos.compras.Api.serializers import CompraSerializer
from drf_yasg.utils import swagger_auto_schema
from apps.seguridad.permissions import CustomPermission
from rest_framework.permissions import IsAuthenticated

class CompraApiView(APIView):

    #Metodo get para obtener una compra
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Compra

    @swagger_auto_schema(response={200: CompraSerializer(many=True)}) 
    def get(self, request):
        compras = Compra.objects.all()
        serializer = CompraSerializer(compras, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
                    sucursal = get_object_or_404(Sucursal, id=serializer.validated_data.get('sucursal').id)
                    detalle_data = serializer.validated_data.get('detalles')
                                                           
                    compra = Compra.objects.create(codigo=codigo, fecha=fecha, proveedorId=proveedores, tipoDeCompraId=tipoCompra, sucursal=sucursal)

                    #detalle_data = serializer.validated_data.get('detalles')
                    for detalles_data in detalle_data:
                        producto = get_object_or_404(Producto, id=detalles_data['producto'].id)
                        cantidad = detalles_data['cantidad']

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
    
class CompraDetails(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Compra

    @swagger_auto_schema(request_body=CompraSerializer)
    def put(self, request, pk):
        # Validar si el pk de la compra se ha proporcionado
        if not pk:
            return Response({"Error": "Se requiere el ID de la compra para actualizar."}, status=status.HTTP_400_BAD_REQUEST)
        
        compra = get_object_or_404(Compra, pk=pk)
        serializer = CompraSerializer(compra, data=request.data)

        self.check_object_permissions(request, compra)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Obtener y actualizar los datos de la compra
                    codigo = serializer.validated_data.get('codigo')
                    fecha = serializer.validated_data.get('fecha')
                    proveedores = get_object_or_404(Proveedores, id=serializer.validated_data.get('proveedorId').id)
                    tipoCompra = get_object_or_404(TipoCompras, id=serializer.validated_data.get('tipoDeCompraId').id)
                    sucursal = get_object_or_404(Sucursal, id=serializer.validated_data.get('sucursal').id)
                    detalle_data = serializer.validated_data.get('detalles')

                    # Actualizar la información básica de la compra
                    compra.codigo = codigo
                    compra.fecha = fecha
                    compra.proveedorId = proveedores
                    compra.tipoDeCompraId = tipoCompra
                    compra.sucursal = sucursal

                    # Eliminar los detalles actuales y ajustar el stock
                    DetallesCompras.objects.filter(compra=compra).delete()

                    for detalles_data in detalle_data:
                        producto = get_object_or_404(Producto, id=detalles_data['producto'].id)
                        cantidad = detalles_data['cantidad']

                        # Crear un nuevo detalle de compra con los datos actualizados
                        DetallesCompras.objects.create(
                            compra=compra,
                            producto=producto,
                            cantidad=cantidad,
                            precio=detalles_data['precio']
                        )

                    compra.save()

                    compra_serializer = CompraSerializer(compra)
                    return Response(compra_serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)