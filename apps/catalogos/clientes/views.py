from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.catalogos import clientes
from apps.catalogos.clientes.models import Clientes
from apps.catalogos.clientes.serializers import ClientesSerializer

class ClientesApiView(APIView):
    def get(self, request):
        serializer = ClientesSerializer(Clientes.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)    
    
    def post(self, request):
        serializer=ClientesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)
    
    def put(self, request, pk):
        try:
            cliente = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Cliente no encontrado"})
        
        serializer = ClientesSerializer(cliente, data=request.data)        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def delete(self, request, pk):
        try:
            clientes = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Cliente no encontrado"})
    
        clientes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        try:
            clientes = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Cliente no encontrado"})
    
        serialize = ClientesSerializer(clientes, data=request.data, partial=True)  # Permite actualizar solo los campos proporcionados
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(status=status.HTTP_200_OK, data=serialize.data)