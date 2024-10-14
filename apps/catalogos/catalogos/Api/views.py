from rest_framework.viewsets import ModelViewSet
from apps.catalogos.catalogos.models import Categoria, Presentaciones, Medidas
from apps.catalogos.catalogos.Api.serializers import CategoriaSerializer, PresentacionesSerializer, MedidasSerializer

#Un ViewSet que maneja las operaciones CRUD para el modelo Departamento.
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

#Un ViewSet que maneja las operaciones CRUD para el modelo Presentaciones.
class PresentacionesViewSet(ModelViewSet):
    queryset = Presentaciones.objects.all()
    serializer_class = PresentacionesSerializer

#Un ViewSet que maneja las operaciones CRUD para el modelo Medidas.
class MedidasViewSet(ModelViewSet):
    queryset = Medidas.objects.all()
    serializer_class = MedidasSerializer