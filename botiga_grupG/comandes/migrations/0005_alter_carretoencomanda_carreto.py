# Generated by Django 5.0.3 on 2024-05-08 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreto', '0008_remove_carreto_metodo_pago'),
        ('comandes', '0004_remove_carretoencomanda_id_carreto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carretoencomanda',
            name='carreto',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='carreto.carreto'),
        ),
    ]
