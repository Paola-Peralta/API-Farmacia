from django.db import models

class Estado(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    tipoEstado = models.CharField(verbose_name='Tipo de estado', max_length=50)

    class Meta:
        verbose_name_plural = 'Tipo de estado'

    def __str__(self):
        return f"{self.codigo}-{self.tipoEstado}"

