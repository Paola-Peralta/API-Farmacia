# Generated by Django 4.2 on 2024-10-06 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallesCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='compras.compra', verbose_name='Compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name_plural': 'Detalle Compras',
            },
        ),
    ]
