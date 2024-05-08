# Generated by Django 5.0.3 on 2024-04-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreto', '0002_remove_carreto_cantidad_remove_carreto_id_producto_and_more'),
        ('cataleg', '0004_rename_tipus_productes_tipus_producte'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreto',
            name='productos',
            field=models.ManyToManyField(through='carreto.ProductoEnCarreto', to='cataleg.productes'),
        ),
    ]
