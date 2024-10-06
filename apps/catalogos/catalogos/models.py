from django.db import models

# Categoria
class Categoria(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=10, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categoria'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"


#Presentaciones
class Presentaciones(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=10, unique= True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=100)

    class Meta:
        verbose_name_plural = 'Presentaciones'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
    
#UNIDAD DE MEDIDA
class Medidas(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=10, unique= True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=100)

    class Meta:
        verbose_name_plural = 'Unidad de medidas'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
