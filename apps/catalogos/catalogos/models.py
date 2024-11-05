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

class Departamento(models.Model):
    codigo = models.CharField(verbose_name='Departamento', max_length=10, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)

    class Meta:
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
    
class Municipio(models.Model):
    codigo = models.CharField(verbose_name='Municipio', max_length=10, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    departamento = models.ForeignKey(Departamento, verbose_name= ("Departamento"), on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
    
class Sucursal(models.Model):
    codigo = models.CharField(verbose_name='Código de sucursal', max_length=10, unique=True)
    nombre = models.CharField(verbose_name='Nombre de farmacia', max_length=50)
    municipio = models.ForeignKey(Municipio,verbose_name='Municipio', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Sucursales'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"