
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_detallescompras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallescompras',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles', to='compras.compra', verbose_name='Compra'),
        ),
    ]
