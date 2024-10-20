from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from apps.catalogos.proveedores.models import Proveedores
from apps.catalogos.proveedores.Api.serializers import ProveedoresSerializer


class ProveedoresApiView(APIView):
    
    #Vistar para listar o crear clientes
    @swagger_auto_schema(response={200: ProveedoresSerializer(many=True)})
    def get(self, request):
        proveedores = Proveedores.objects.all()
        serializer = ProveedoresSerializer(proveedores, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ProveedoresSerializer, response={201: ProveedoresSerializer})
    def post(self, request):
        """
        # Crear un nuevo proveedor.
        # """
        serializer = ProveedoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProveedoresDetails(APIView):
    #Para obtener, actualizar y eliminar un proveedor especifico

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

        try:
            proveedores = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response ({'Error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProveedoresSerializer(proveedores, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=ProveedoresSerializer, responses={201: ProveedoresSerializer})
    def patch(self, request, pk):
        try:
            proveedores = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response({'Error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProveedoresSerializer(proveedores, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(response={204: 'No content'})
    def delete(self, request, pk):
        try:
            proveedores = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response ({'Error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        proveedores.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)