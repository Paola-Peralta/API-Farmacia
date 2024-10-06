from django.db import models

#Clientes
class Clientes(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=10, unique=True)
    nombres = models.CharField(verbose_name='Nombres', max_length=50)
    primerApellido = models.CharField(verbose_name='Primer Apellido', max_length=50)
    segundoApellido = models.CharField(verbose_name='Segundo Apellido', max_length=50)
    direccion = models.CharField(verbose_name='Dirección', max_length=50)
    telefono = models.CharField(verbose_name='Teléfono', max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Registro de clientes'

    def __str__(self):
        return f"{self.codigo} - {self.nombres}-{self.primerApellido} - {self.segundoApellido} - {self.direccion} - {self.telefono}"