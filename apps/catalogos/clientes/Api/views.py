from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from apps.catalogos.clientes.models import Clientes
from apps.catalogos.clientes.Api.serializers import ClientesSerializer
#from drf_yasg import openapi

class ClientesApiView(APIView):

    #Vistar para listar o crear clientes
    @swagger_auto_schema(response={200: ClientesSerializer(many=True)})
    def get(self, request):
        clientes = Clientes.objects.all()
        serializer = ClientesSerializer(clientes, many=True)
        return Response(serializer.data)   
        
    @swagger_auto_schema(request_body=ClientesSerializer, response={201: ClientesSerializer})
    def post(self, request):
        """
        # Crear un nuevo cliente.
        # """
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClienteDetails(APIView):
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

        try:
            clientes = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response ({'Error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClientesSerializer(clientes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=ClientesSerializer, responses={201: ClientesSerializer})
    def patch(self, request, pk):
        try:
            clientes = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response({'Error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClientesSerializer(clientes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(response={204: 'No content'})
    def delete(self, request, pk):
        try:
            clientes = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response ({'Error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        clientes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
