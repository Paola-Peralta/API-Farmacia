from django.db import models

#Tipo DE COMPRA
class TipoCompras(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=10, unique=True)
    descripcion = models.CharField(verbose_name='Tipo de compra', max_length=50)

    class Meta:
        verbose_name_plural = 'Tipo de compras'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"