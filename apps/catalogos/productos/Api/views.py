from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from apps.catalogos.productos.models import Producto
from apps.catalogos.productos.Api.serializers import ProductoSerializer
from apps.seguridad.permissions import CustomPermission
from rest_framework.permissions import IsAuthenticated
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configura el logger
logger = logging.getLogger(__name__)

class ProductoApiView(PaginationMixin,APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Producto


    @swagger_auto_schema(response={200: ProductoSerializer(many=True)})
    def get(self, request):

        logger.info("GET request to list all producto")
        producto = Producto.objects.all().order_by('id')
        page = self.paginate_queryset(producto,request)

        if page is not None:
            serializer = ProductoSerializer(page, many=True)
            logger.info("Paginated response for resultado")
            return self.get_paginated_response(serializer.data)

        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ProductoSerializer, response={201: ProductoSerializer})
    def post(self, request):

        logger.info("POST request to create a new producto")
        """
        # Crear un nuevo producto.
        # """
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            warning_message = getattr(serializer, 'warning_message', None)  # Obtener mensaje de advertencia, si existe
            serializer.save()
            logger.info("producto created successfully")

            # Enviar advertencia en la respuesta si el producto está cerca de vencer
            response_data = serializer.data
            if warning_message:
                response_data['advertencia'] = warning_message

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create producto: %s", serializer.errors)
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

        logger.info("PUT request to update producto with ID: %s", pk)

        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response ({'Error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, producto) 
        
        
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            warning_message = getattr(serializer, 'warning_message', None)
            serializer.save()
            logger.info("Producto updated successfully with ID: %s", pk)
            response_data = serializer.data
            if warning_message:
                response_data['advertencia'] = warning_message
                
            return Response(serializer.data)
        logger.error("Failed to update producto with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=ProductoSerializer, responses={201: ProductoSerializer})
    def patch(self, request, pk):

        logger.info("PATCH request to partially update producto with ID: %s", pk)

        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'Error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, producto) 
        
        serializer = ProductoSerializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("producto partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        
        logger.error("Failed to partially update producto with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(response={204: 'No content'})
    def delete(self, request, pk):
        logger.info("DELETE request to delete producto with ID: %s", pk)
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response ({'Error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, producto) 
        
        producto.delete()
        logger.info("producto deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)