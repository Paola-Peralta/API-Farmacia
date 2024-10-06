from django.db import models
from apps.administracionExamenes.examenes.models import Examen

class Resultado(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    examen = models.ForeignKey(Examen,verbose_name='Examen', on_delete=models.PROTECT )

    class Meta:
        verbose_name_plural = 'Resultados'
            
    def __str__(self):
        return f"{self.codigo} - {self.descripcion} "
