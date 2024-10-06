from django.db import models

class Examen(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    costo = models.FloatField(verbose_name='Costo Examén')
    
    class Meta:
        verbose_name_plural = 'Examenes'

    def __str__(self) -> str:
        return f"{self.codigo} - {self.descripcion} - {self.costo}"

