from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from apps.catalogos.clientes.models import Clientes
from apps.catalogos.clientes.Api.serializers import ClientesSerializer
from apps.seguridad.permissions import CustomPermission
from rest_framework.permissions import IsAuthenticated
from config.utils.Pagination import PaginationMixin
import logging.handlers
#from drf_yasg import openapi

# Configura el logger
logger = logging.getLogger(__name__)

class ClientesApiView(PaginationMixin,APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Clientes

    #Vistar para listar o crear clientes
    @swagger_auto_schema(response={200: ClientesSerializer(many=True)})
    def get(self, request):

        logger.info("GET request to list all cliente")
        cliente = Clientes.objects.all().order_by('id')
        page = self.paginate_queryset(cliente,request)

        if page is not None:
            serializer = ClientesSerializer(page, many=True)
            logger.info("Paginated response for cliente")
            return self.get_paginated_response(serializer.data)


        
        serializer = ClientesSerializer(cliente, many=True)
        logger.error("Returning all cliente without pagination")
        return Response(serializer.data)   
        
    @swagger_auto_schema(request_body=ClientesSerializer, response={201: ClientesSerializer})
    def post(self, request):


        logger.info("POST request to create a new cliente")

        """
        # Crear un nuevo cliente.
        # """
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("cliente created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create cliente: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClienteDetails(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Clientes
    #Para obtener, actualizar y eliminar un cliente especifico

    @swagger_auto_schema(responses={200: ClientesSerializer})
    def get(self, request, pk):
           
        try:
            clientes = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response ({'Error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientesSerializer(clientes)
        return Response(serializer.data)
    
    
    
    @swagger_auto_schema(request_body=ClientesSerializer, responses={201: ClientesSerializer})
    def put(self, request, pk):

        logger.info("PUT request to update cliente with ID: %s", pk)

        try:
            clientes = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response ({'Error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, clientes)
        
        serializer = ClientesSerializer(clientes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("cliente updated successfully with ID: %s", pk)
            return Response(serializer.data)
        
        logger.error("Failed to update cliente with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=ClientesSerializer, responses={201: ClientesSerializer})
    def patch(self, request, pk):


        logger.info("PATCH request to partially update cliente with ID: %s", pk)

        try:
            clientes = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response({'Error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, clientes)
        
        serializer = ClientesSerializer(clientes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("cliente partially updated successfully with ID: %s", pk)
            return Response(serializer.data)
        logger.error("Failed to partially update cliente with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(response={204: 'No content'})
    def delete(self, request, pk):

        logger.info("DELETE request to delete cliente with ID: %s", pk)

        try:
            clientes = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response ({'Error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, clientes)
        
        clientes.delete()
        logger.info("cliente deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
