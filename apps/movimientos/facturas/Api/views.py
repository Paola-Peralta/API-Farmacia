from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.shortcuts import get_object_or_404
from apps.movimientos.facturas.models import Factura, DetalleFactura
from apps.catalogos.productos.models import Producto
from apps.catalogos.clientes.models import Clientes
from apps.catalogos.catalogos.models import Sucursal
from apps.catalogos.tipoFactura.models import TipoFacturas
from apps.movimientos.facturas.Api.serializers import FacturaSerializer
from drf_yasg.utils import swagger_auto_schema

class FacturaApiView(APIView):
    
    # Método GET para obtener una factura específica o listar todas
    @swagger_auto_schema(responses={200: FacturaSerializer(many=True)})
    def get(self, request, pk=None):
        if pk:
            # Obtener una factura específica
            factura = get_object_or_404(Factura, pk=pk)
            serializer = FacturaSerializer(factura)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Listar todas las facturas
            facturas = Factura.objects.all()
            serializer = FacturaSerializer(facturas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
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
                    sucursal = get_object_or_404(Sucursal, id=serializer.validated_data.get('sucursal').id)
                    detalle_data = serializer.validated_data.get('detalles')

                    subtotal = 0
                    descuento = 0
                    iva = 0.10  # IVA del 10%

                    #Crear factura
                    factura = Factura.objects.create(
                        codigo=codigo,
                        fecha=fecha,
                        iva=iva, 
                        descuento= descuento,
                        clienteId=cliente, 
                        tipoFacturaId =tipoFactura, 
                        sucursal=sucursal)

                    for detalles_data in detalle_data:
                        producto = get_object_or_404(Producto, id=detalles_data['producto'].id)
                        cantidad = detalles_data['cantidad']
                        precio = detalles_data['precio']

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

                         # Actualizar subtotal
                        subtotal += cantidad * precio
                        
                        # Calcular IVA y aplicar descuento si corresponde
                    iva_total = subtotal * iva
                    if subtotal > 1000:
                        descuento = subtotal * 0.05  # Descuento del 5%

                    # Actualizar los valores de IVA y descuento en la factura
                    factura.iva = iva_total
                    factura.descuento = descuento
                    factura.save()

                    facturaSerializer = FacturaSerializer(factura)
                    return Response(facturaSerializer.data, status=status.HTTP_201_CREATED)
                
            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacturaDetails(APIView):

    @swagger_auto_schema(request_body=FacturaSerializer)
    def put(self, request, pk=None):
        # Validar si el pk de la factura se ha proporcionado
        if not pk:
            return Response({"Error": "Se requiere el ID de la factura para actualizar."}, status=status.HTTP_400_BAD_REQUEST)
        
        factura = get_object_or_404(Factura, pk=pk)
        serializer = FacturaSerializer(factura, data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Obtener y actualizar los datos de la factura
                    codigo = serializer.validated_data.get('codigo')
                    fecha = serializer.validated_data.get('fecha')
                    cliente = get_object_or_404(Clientes, id=serializer.validated_data.get('clienteId').id)
                    tipoFactura = get_object_or_404(TipoFacturas, id=serializer.validated_data.get('tipoFacturaId').id)
                    sucursal = get_object_or_404(Sucursal, id=serializer.validated_data.get('sucursal').id)
                    detalle_data = serializer.validated_data.get('detalles')

                    subtotal = 0
                    iva = 0.10  # IVA del 10%

                    # Actualizar la información básica de la factura
                    factura.codigo = codigo
                    factura.fecha = fecha
                    factura.clienteId = cliente
                    factura.tipoFacturaId = tipoFactura
                    factura.sucursal = sucursal

                    # Eliminar los detalles actuales y restablecer el stock
                    DetalleFactura.objects.filter(factura=factura).delete()

                    for detalles_data in detalle_data:
                        producto = get_object_or_404(Producto, id=detalles_data['producto'].id)
                        cantidad = detalles_data['cantidad']
                        precio = detalles_data['precio']

                        if producto.cantidad < cantidad:
                            return Response(
                                {"Error": f"Stock insuficiente para el producto: {producto.nombreProducto}"},
                                status=status.HTTP_400_BAD_REQUEST
                            )

                        producto.cantidad -= cantidad
                        producto.save()

                        # Crear un nuevo detalle de factura con los datos actualizados
                        DetalleFactura.objects.create(
                            factura=factura,
                            producto=producto,
                            cantidad=cantidad,
                            precio=precio
                        )

                        # Actualizar el subtotal
                        subtotal += cantidad * precio

                    # Recalcular el IVA y descuento si es necesario
                    iva_total = subtotal * iva
                    descuento = subtotal * 0.05 if subtotal > 1000 else 0  # Descuento del 5% si el subtotal > 1000

                    # Guardar los valores actualizados de IVA y descuento en la factura
                    factura.iva = iva_total
                    factura.descuento = descuento
                    factura.save()

                    factura_serializer = FacturaSerializer(factura)
                    return Response(factura_serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)