from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializers
from drf_yasg.utils import swagger_auto_schema

class UserCreateView(APIView):
    @swagger_auto_schema(request_body=UserCreateSerializers)
    def post(self, request):
        serializer = UserCreateSerializers(data=request.data)

        #Validar datos
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensaje": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)
        
        #En caso de error retornar las validaciones
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
