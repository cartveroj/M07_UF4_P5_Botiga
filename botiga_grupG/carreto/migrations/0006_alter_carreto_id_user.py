# Generated by Django 5.0.3 on 2024-05-03 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreto', '0005_remove_productoencarreto_metodo_pago_and_more'),
        ('pagaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreto',
            name='id_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='pagaments.usuari'),
        ),
    ]
