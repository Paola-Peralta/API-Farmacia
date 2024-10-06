from django.db import models
from apps.catalogos.productos.models import Producto
from apps.movimientos.facturas.models import Factura

class DetalleFactura(models.Model):
    #models.CASCADE significa que en el caso que se elimine una factura todos los detalles relacionados tambien se eleminaran
    factura = models.ForeignKey(Factura, verbose_name='Factura', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.PROTECT)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.FloatField(verbose_name='Precio')

    class Meta:
        verbose_name_plural = 'Detalle Facturas'

    def __str__(self):
        return f"Factura: {self.factura.codigo}, Producto: {self.producto.nombreProducto}, Cantidad: {self.cantidad}, Precio: {self.precio}"


