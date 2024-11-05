
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_detallefactura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles', to='facturas.factura', verbose_name='Factura'),
        ),
    ]
