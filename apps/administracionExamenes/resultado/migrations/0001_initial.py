# Generated by Django 4.2 on 2024-10-06 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('examenes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30, unique=True, verbose_name='Código')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('examen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='examenes.examen', verbose_name='Examen')),
            ],
            options={
                'verbose_name_plural': 'Resultados',
            },
        ),
    ]
