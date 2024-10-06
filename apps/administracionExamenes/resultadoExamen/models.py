from django.db import models
from apps.administracionExamenes.detalleExamen.models import DetallesExamen
from apps.catalogos.estado.models import Estado
from apps.administracionExamenes.resultado.models import Resultado

class ResultadoExamen(models.Model):
    detalleExamen = models.ForeignKey(DetallesExamen, verbose_name='Detalle de Examen', on_delete=models.PROTECT)
    resultado = models.ForeignKey(Resultado,verbose_name='Resultado', on_delete=models.PROTECT)
    valor = models.FloatField(verbose_name='Valor' )
    estado = models.ForeignKey(Estado, verbose_name='Estado', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Resultados de Examenes'
            
    def __str__(self):
        return f"{self.detalleExamen} - {self.resultado} - {self.valor} -{self.estado} "


