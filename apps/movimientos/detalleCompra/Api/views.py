from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from apps.movimientos import detalleCompra
from apps.movimientos.detalleCompra.models import DetallesCompras
from apps.movimientos.detalleCompra.Api.serializers import DetalleComprasSerializer
from drf_yasg import openapi

class DetalleCompraApiView(APIView):
    def get(self, request):
        serializer = DetalleComprasSerializer(DetallesCompras.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)
    
    @swagger_auto_schema(request_body=DetalleComprasSerializer)
    def post(self, request):
        """
        Crear un nuevo detallecompra.
        """
        serializer = DetalleComprasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)