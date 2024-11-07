from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from apps.catalogos.productos.models import Producto
from apps.catalogos.productos.Api.serializers import ProductoSerializer
from apps.seguridad.permissions import CustomPermission
from rest_framework.permissions import IsAuthenticated

class ProductoApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Producto


    @swagger_auto_schema(response={200: ProductoSerializer(many=True)})
    def get(self, request):
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ProductoSerializer, response={201: ProductoSerializer})
    def post(self, request):
        """
        # Crear un nuevo producto.
        # """
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            warning_message = getattr(serializer, 'warning_message', None)  # Obtener mensaje de advertencia, si existe
            serializer.save()

            # Enviar advertencia en la respuesta si el producto está cerca de vencer
            response_data = serializer.data
            if warning_message:
                response_data['advertencia'] = warning_message

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoDetails(APIView):
    #Para obtener, actualizar y eliminar un producto especifico

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Producto

    @swagger_auto_schema(responses={200: ProductoSerializer})
    def get(self, request, pk):
           
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response ({'Error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(request_body=ProductoSerializer, responses={201: ProductoSerializer})
    def put(self, request, pk):

        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response ({'Error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, producto) 
        
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            warning_message = getattr(serializer, 'warning_message', None)
            serializer.save()
            response_data = serializer.data
            if warning_message:
                response_data['advertencia'] = warning_message
                
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=ProductoSerializer, responses={201: ProductoSerializer})
    def patch(self, request, pk):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'Error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, producto) 
        
        serializer = ProductoSerializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(response={204: 'No content'})
    def delete(self, request, pk):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response ({'Error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, producto) 
        
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)