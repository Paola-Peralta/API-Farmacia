from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from apps.catalogos.proveedores.models import Proveedores
from apps.catalogos.proveedores.Api.serializers import ProveedoresSerializer
from apps.seguridad.permissions import CustomPermission
from rest_framework.permissions import IsAuthenticated
from config.utils.Pagination import PaginationMixin
import logging.handlers


# Configura el logger
logger = logging.getLogger(__name__)


class ProveedoresApiView(PaginationMixin,APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Proveedores
    
    #Vistar para listar o crear clientes
    @swagger_auto_schema(response={200: ProveedoresSerializer(many=True)})
    def get(self, request):

        logger.info("GET request to list all proveedores")
        proveedores = Proveedores.objects.all().order_by('id')
        page = self.paginate_queryset(proveedores,request)

        if page is not None:
            serializer = ProveedoresSerializer(page, many=True)
            logger.info("Paginated response for proveedores")
            return self.get_paginated_response(serializer.data)

        serializer = ProveedoresSerializer(proveedores, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ProveedoresSerializer, response={201: ProveedoresSerializer})
    def post(self, request):

        logger.info("POST request to create a new proveedores")

        """
        # Crear un nuevo proveedor.
        # """
        serializer = ProveedoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("proveedores created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create proveedores: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProveedoresDetails(APIView):
    #Para obtener, actualizar y eliminar un proveedor especifico

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Proveedores

    @swagger_auto_schema(responses={200: ProveedoresSerializer})
    def get(self, request, pk):
           
        try:
            proveedores = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response ({'Error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProveedoresSerializer(proveedores)
        return Response(serializer.data)
    
    
    
    @swagger_auto_schema(request_body=ProveedoresSerializer, responses={201: ProveedoresSerializer})
    def put(self, request, pk):

        logger.info("PUT request to update proveedores with ID: %s", pk)

        try:
            proveedores = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response ({'Error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, proveedoresroveedores)
        
        serializer = ProveedoresSerializer(proveedores, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("proveedores updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to update proveedores with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=ProveedoresSerializer, responses={201: ProveedoresSerializer})
    def patch(self, request, pk):

        logger.info("PATCH request to partially update proveedores with ID: %s", pk)

        try:
            proveedores = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response({'Error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, proveedores)

        serializer = ProveedoresSerializer(proveedores, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("proveedores partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update proveedores with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(response={204: 'No content'})
    def delete(self, request, pk):

        logger.info("DELETE request to delete proveedores with ID: %s", pk)

        try:
            proveedores = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response ({'Error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, proveedores)
        
        proveedores.delete()
        logger.info("proveedores deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)