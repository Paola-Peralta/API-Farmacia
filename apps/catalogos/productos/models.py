from django.db import models
from apps.catalogos.catalogos.models import Categoria
from apps.catalogos.catalogos.models import Presentaciones
from apps.catalogos.catalogos.models import Medidas

class Producto(models.Model):
    codigoProducto = models.CharField(verbose_name='Código', max_length=30, unique=True)
    nombreProducto = models.CharField(verbose_name='Nombre', max_length=100)
    cantidad = models.IntegerField(verbose_name= 'Cantidad')
    fechaVencimiento = models.DateField(verbose_name= 'Fecha vencimiento', max_length= 200)
    precio = models.FloatField(verbose_name= 'Precio')
    categoria = models.ForeignKey(Categoria, verbose_name = 'Categoria', on_delete=models.PROTECT )
    medidas = models.ForeignKey(Medidas, verbose_name='Unidas de Medidas', on_delete= models.PROTECT )
    presentaciones = models.ForeignKey(Presentaciones, verbose_name= 'Presentaciones', on_delete=models.PROTECT )
    
    class Meta:
        verbose_name_plural = 'Producto'
        
    
    def __str__(self):
        return f"{self.codigoProducto} - {self.nombreProducto}"

