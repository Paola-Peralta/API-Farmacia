# Generated by Django 4.2 on 2024-10-27 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Departamento')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Municipio')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogos.departamento', verbose_name='Departamento')),
            ],
            options={
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código de sucursal')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de farmacia')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogos.municipio', verbose_name='Municipio')),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
            },
        ),
    ]
