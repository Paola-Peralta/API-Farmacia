from django.db import models
from apps.administracionExamenes.examenes.models import Examen
from apps.administracionExamenes.examenes.models import DetallesExamen
from apps.catalogos.estado.models import Estado

class Resultado(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    examen = models.ForeignKey(Examen,verbose_name='Examen', on_delete=models.PROTECT )

    class Meta:
        verbose_name_plural = 'Resultados'
            
    def __str__(self):
        return f"{self.codigo} - {self.descripcion} "

class ResultadoExamen(models.Model):
    detalleExamen = models.ForeignKey(DetallesExamen, verbose_name='Detalle de Examen', on_delete=models.PROTECT)
    resultado = models.ForeignKey(Resultado,verbose_name='Resultado', on_delete=models.PROTECT)
    valor = models.FloatField(verbose_name='Valor' )
    estado = models.ForeignKey(Estado, verbose_name='Estado', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Resultados de Examenes'
            
    def __str__(self):
        return f"{self.detalleExamen} - {self.resultado} - {self.valor} -{self.estado}"
