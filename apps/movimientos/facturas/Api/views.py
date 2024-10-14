from rest_framework.viewsets import ModelViewSet
from apps.movimientos.facturas.models import Factura
from apps.movimientos.facturas.Api.serializers import FacturaSerializer

class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    