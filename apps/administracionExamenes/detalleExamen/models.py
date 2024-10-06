from django.db import models
from apps.administracionExamenes.consultas.models import Consulta
from apps.administracionExamenes.examenes.models import Examen

# Create your models here.
class DetallesExamen(models.Model):
    examen = models.ForeignKey(Examen, verbose_name='Examen', on_delete=models.PROTECT)
    consulta = models.ForeignKey(Consulta, verbose_name='Consulta', on_delete=models.PROTECT)
    fechaEntrega = models.DateField(verbose_name='Fecha entrega')
    precio = models.FloatField(verbose_name='Precio')

    class Meta:
        verbose_name_plural = 'Detalle de Examenes'

    def __str__(self):
        return f"examen: {self.examen.descripcion}, consulta: {self.consulta.clienteId}, fechaEntrega: {self.fechaEntrega}, Precio: {self.precio}"
