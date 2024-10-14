from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from apps.catalogos import proveedores
from apps.catalogos.proveedores.models import Proveedores
from apps.catalogos.proveedores.Api.serializers import ProveedoresSerializer


class ProveedoresApiView(APIView):
    def get(self, request):
        serializer = ProveedoresSerializer(Proveedores.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data) 
    
    @swagger_auto_schema(request_body=ProveedoresSerializer)
    def post(self, request):
        serializer=ProveedoresSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)