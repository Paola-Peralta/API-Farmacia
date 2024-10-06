from django.db import models
from apps.catalogos.productos.models import Producto
from apps.movimientos.compras.models import Compra

#DETALLE DE COMPRA 
class DetallesCompras(models.Model):
    compra = models.ForeignKey(Compra, verbose_name='Compra', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.PROTECT)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.FloatField(verbose_name='Precio')

    class Meta:
        verbose_name_plural = 'Detalle Compras'

    def __str__(self):
        return f"Compras: {self.compra.codigo}, Producto: {self.producto.nombreProducto}, Cantidad: {self.cantidad}, Precio: {self.precio}"
