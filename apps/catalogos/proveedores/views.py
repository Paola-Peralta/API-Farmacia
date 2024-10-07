from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.catalogos import proveedores
from apps.catalogos.proveedores.models import Proveedores
from apps.catalogos.proveedores.serializers import ProveedoresSerializer

class ProveedoresApiView(APIView):
    def get(self, request):
        serializer = ProveedoresSerializer(ProveedoresSerializer.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)    
    
    def post(self, request):
        serializer=ProveedoresSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)
    
    def put(self, request, pk):
        try:
            proveedores = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "proveedor no encontrado"})
        
        serializer = ProveedoresSerializer(proveedores, data=request.data)        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def delete(self, request, pk):
        try:
            proveedores = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "proveedor no encontrado"})
    
        proveedores.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        try:
            proveedores = Proveedores.objects.get(pk=pk)
        except proveedores.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "proveedor no encontrado"})
    
        serialize = ProveedoresSerializer(proveedores, data=request.data, partial=True)  # Permite actualizar solo los campos proporcionados
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(status=status.HTTP_200_OK, data=serialize.data)
