from django.db import models
from apps.catalogos.clientes.models import Clientes
from apps.catalogos.tipoFactura.models import TipoFacturas
from apps.catalogos.productos.models import Producto

#MODELO FACTURA
class Factura(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    fecha = models.DateField(verbose_name='Fecha Factura')
    iva = models.FloatField(verbose_name='Iva', max_length=50)
    descuento = models.FloatField(verbose_name='Descuento', max_length=50)
    clienteId = models.ForeignKey(Clientes, verbose_name='Cliente', on_delete=models.PROTECT)
    tipoFacturaId = models.ForeignKey(TipoFacturas, verbose_name='Tipo factura', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return f"{self.codigo}-{self.fecha}-{self.iva}-{self.descuento}"

#MODELO DETALLE FACTURA
class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, verbose_name='Factura', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.PROTECT)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.FloatField(verbose_name='Precio')

    class Meta:
        verbose_name_plural = 'Detalle Facturas'

    def __str__(self):
        return f"Factura: {self.factura.codigo}, Producto: {self.producto.nombreProducto}, Cantidad: {self.cantidad}, Precio: {self.precio}"