# Generated by Django 5.0.3 on 2024-05-08 16:08


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cataleg', '0005_rename_tipus_producte_productes_tipus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productes',
            old_name='tipus',
            new_name='tipus_producte',
        ),
    ]
