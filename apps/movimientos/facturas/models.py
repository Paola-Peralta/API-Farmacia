from django.db import models
from apps.catalogos.clientes.models import Clientes
from apps.catalogos.tipoFactura.models import TipoFacturas

class Factura(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    fecha = models.DateField(verbose_name='Fecha Factura')
    iva = models.FloatField(verbose_name='Iva', max_length=50)
    descuento = models.FloatField(verbose_name='Descuento', max_length=50)
    clienteId = models.ForeignKey(Clientes, verbose_name='Cliente', on_delete=models.PROTECT)
    tipoFacturaId = models.ForeignKey(TipoFacturas, verbose_name='Tipo factura', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return f"{self.codigo}-{self.fecha}-{self.iva}-{self.descuento}"
