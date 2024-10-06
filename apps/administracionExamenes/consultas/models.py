from django.db import models
from apps.catalogos.clientes.models import Clientes
class Consulta(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    fecha = models.DateField(verbose_name='Fecha de consulta')
    clienteId = models.ForeignKey(Clientes, verbose_name='Cliente', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f"{self.codigo}-{self.fecha}"
