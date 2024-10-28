from django.db import models
from apps.administracionExamenes.consultas.models import Consulta

class Examen(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    #costo = models.FloatField(verbose_name='Costo Examén')
    
    class Meta:
        verbose_name_plural = 'Examenes'

    def __str__(self) -> str:
        return f"{self.codigo} - {self.descripcion} "

 # Create your models here.
class DetallesExamen(models.Model):
    examen = models.ForeignKey(Examen, related_name='detalles', verbose_name='Examen', on_delete=models.PROTECT)
    consulta = models.ForeignKey(Consulta, verbose_name='Consulta', on_delete=models.PROTECT)
    fechaEntrega = models.DateField(verbose_name='Fecha entrega')
    precio = models.FloatField(verbose_name='Precio')

    class Meta:
        verbose_name_plural = 'Detalle de Examenes'

    def __str__(self):
        return f"examen: {self.examen.descripcion}, consulta: {self.consulta.clienteId}, fechaEntrega: {self.fechaEntrega}, Precio: {self.precio}"
