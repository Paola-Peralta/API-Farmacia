from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import transaction
from apps.administracionExamenes.examenes.Api.serializers import ExamenSerializer
from apps.administracionExamenes.examenes.models import Examen, DetallesExamen
from apps.administracionExamenes.consultas.models import Consulta
from drf_yasg.utils import swagger_auto_schema
from apps.seguridad.permissions import CustomPermission
from rest_framework.permissions import IsAuthenticated
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configura el logger
logger = logging.getLogger(__name__)

class ExamenApiView(PaginationMixin,APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Examen

    @swagger_auto_schema(response={200: ExamenSerializer(many=True)})
    def get(self,request):

        logger.info("GET request to list all examen")
        examen = Examen.objects.all().order_by('id')
        page = self.paginate_queryset(examen,request)

        if page is not None:
            serializer = ExamenSerializer(page, many=True)
            logger.info("Paginated response for examen")
            return self.get_paginated_response(serializer.data)

        serializer = ExamenSerializer(examen, many=True)
        logger.error("Returning all examen without pagination")
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=ExamenSerializer)
    def post(self, request):

        logger.info("POST request to create a new examen")

        serializer = ExamenSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Crear el Examen
                    examen = Examen.objects.create(
                        codigo=serializer.validated_data['codigo'],
                        descripcion=serializer.validated_data['descripcion']
                        
                    )

                    # Procesar los detalles del examen
                    detalles_data = serializer.validated_data.get('detalles', [])
                    for detalle_data in detalles_data:
                        consulta = get_object_or_404(Consulta, id=detalle_data['consulta'].id)
                        DetallesExamen.objects.create(
                            examen=examen,
                            consulta=consulta,
                            fechaEntrega=detalle_data['fechaEntrega'],
                            precio=detalle_data['precio']
                            
                        )

                    # Serializar y devolver el examen creado
                    examen_serializer = ExamenSerializer(examen)
                    return Response(examen_serializer.data, status=status.HTTP_201_CREATED)
                

            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        logger.error("Failed to create examen: %s", serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExamenDetails(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Examen

    @swagger_auto_schema(request_body=ExamenSerializer)
    def put(self, request, pk):

        logger.info("PUT request to update examen with ID: %s", pk)

        examen = get_object_or_404(Examen, pk=pk)
        serializer = ExamenSerializer(examen, data=request.data)

        self.check_object_permissions(request, examen)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Actualizar datos del Examen
                    examen.codigo = serializer.validated_data['codigo']
                    examen.descripcion = serializer.validated_data['descripcion']
                    examen.save()
                    logger.info("examen updated successfully with ID: %s", pk)

                    # Actualizar detalles del examen
                    detalles_data = serializer.validated_data.get('detalles', [])
                    DetallesExamen.objects.filter(examen=examen).delete()
                    for detalle_data in detalles_data:
                        consulta = get_object_or_404(Consulta, id=detalle_data['consulta'].id)
                        DetallesExamen.objects.create(
                            examen=examen,
                            consulta=consulta,
                            fechaEntrega=detalle_data['fechaEntrega'],
                            precio=detalle_data['precio']
                        )

                    # Serializar y devolver el examen actualizado
                    examen_serializer = ExamenSerializer(examen)
                    return Response(examen_serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        logger.error("Failed to update examen with ID: %s. Errors: %s", pk, serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)