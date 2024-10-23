from django.db import models
from apps.catalogos.proveedores.models import Proveedores
from apps.catalogos.tipoCompra.models import TipoCompras
from apps.catalogos.productos.models import Producto

class Compra(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    fecha = models.DateField(verbose_name= 'Fecha')
    proveedorId = models.ForeignKey(Proveedores, verbose_name='Proveedor', on_delete=models.PROTECT)
    tipoDeCompraId = models.ForeignKey(TipoCompras, verbose_name='Tipo de compra', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Compras'
    
    def __str__(self):
        return f"{self.codigo}-{self.fecha}"
    

#DETALLE DE COMPRA 
class DetallesCompras(models.Model):
    compra = models.ForeignKey(Compra, related_name='detalles', verbose_name='Compra', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.PROTECT)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.FloatField(verbose_name='Precio')

    class Meta:
        verbose_name_plural = 'Detalle Compras'

    def __str__(self):
        return f"Compras: {self.compra.codigo}, Producto: {self.producto.nombreProducto}, Cantidad: {self.cantidad}, Precio: {self.precio}"