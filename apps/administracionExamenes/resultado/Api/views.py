from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import transaction
from apps.administracionExamenes.resultado.Api.serializers import DetalleResuladoSerializer, ResultadoSerializer
from apps.administracionExamenes.examenes.models import Examen, DetallesExamen
from apps.catalogos.estado.models import Estado
from apps.administracionExamenes.resultado.models import Resultado, ResultadoExamen
from drf_yasg.utils import swagger_auto_schema

class ResultadoApiView(APIView):
    @swagger_auto_schema(response={200: ResultadoSerializer(many=True)})
    def get(self, request):
        resultados = Resultado.objects.all()  # Asegúrate de que estás obteniendo instancias de Resultado
        serializer = ResultadoSerializer(resultados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=ResultadoSerializer)
    def post(self, request):
        serializer = ResultadoSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Crear el Resultado
                    resultado = Resultado.objects.create(
                        codigo=serializer.validated_data['codigo'],
                        descripcion=serializer.validated_data['descripcion'],
                        examen=get_object_or_404(Examen, id=serializer.validated_data['examen'].id)
                    )

                    # Procesar los detalles del resultado, si están presentes en la solicitud
                    detalles_data = serializer.validated_data.get('detalles', [])
                    for detalle_data in detalles_data:
                        detalle_examen = get_object_or_404(DetallesExamen, id=detalle_data['detalleExamen'].id)
                        estado = get_object_or_404(Estado, id=detalle_data['estado'].id)
                        ResultadoExamen.objects.create(
                            detalleExamen=detalle_examen,
                            resultado=resultado,
                            valor=detalle_data['valor'],
                            estado=estado
                        )

                    # Serializar y devolver el resultado creado
                    resultado_serializer = ResultadoSerializer(resultado)
                    return Response(resultado_serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResultadoDetails(APIView):
    @swagger_auto_schema(request_body=ResultadoSerializer)
    def put(self, request, pk):
        resultado = get_object_or_404(Resultado, pk=pk)
        serializer = ResultadoSerializer(resultado, data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Actualizar el Resultado
                    resultado.codigo = serializer.validated_data['codigo']
                    resultado.descripcion = serializer.validated_data['descripcion']
                    resultado.examen = get_object_or_404(Examen, id=serializer.validated_data['examen'].id)
                    resultado.save()

                    # Eliminar los detalles existentes antes de agregar nuevos
                    ResultadoExamen.objects.filter(resultado=resultado).delete()

                    # Procesar los nuevos detalles del resultado, si están presentes en la solicitud
                    detalles_data = serializer.validated_data.get('detalles', [])
                    for detalle_data in detalles_data:
                        detalle_examen = get_object_or_404(DetallesExamen, id=detalle_data['detalleExamen'].id)
                        estado = get_object_or_404(Estado, id=detalle_data['estado'].id)
                        ResultadoExamen.objects.create(
                            detalleExamen=detalle_examen,
                            resultado=resultado,
                            valor=detalle_data['valor'],
                            estado=estado
                        )

                    # Serializar y devolver el resultado actualizado
                    resultado_serializer = ResultadoSerializer(resultado)
                    return Response(resultado_serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)