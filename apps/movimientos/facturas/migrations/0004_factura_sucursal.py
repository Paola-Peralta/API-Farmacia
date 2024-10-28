# Generated by Django 4.2 on 2024-10-27 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_departamento_municipio_sucursal'),
        ('facturas', '0003_alter_detallefactura_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='sucursal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='catalogos.sucursal', verbose_name='Sucursal'),
            preserve_default=False,
        ),
    ]
