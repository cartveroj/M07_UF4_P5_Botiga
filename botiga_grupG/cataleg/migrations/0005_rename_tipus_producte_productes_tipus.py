# Generated by Django 5.0.3 on 2024-04-19 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cataleg', '0004_rename_tipus_productes_tipus_producte'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productes',
            old_name='tipus_producte',
            new_name='tipus',
        ),
    ]