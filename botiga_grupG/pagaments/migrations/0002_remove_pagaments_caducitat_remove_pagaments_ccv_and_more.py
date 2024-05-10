# Generated by Django 5.0.3 on 2024-05-08 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreto', '0009_remove_carreto_id_user'),
        ('pagaments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagaments',
            name='caducitat',
        ),
        migrations.RemoveField(
            model_name='pagaments',
            name='ccv',
        ),
        migrations.RemoveField(
            model_name='pagaments',
            name='num_tarjeta',
        ),
        migrations.AddField(
            model_name='pagaments',
            name='Carreto',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='carreto.carreto'),
        ),
        migrations.AddField(
            model_name='pagaments',
            name='metodo_pago',
            field=models.CharField(choices=[('paypal', 'paypal'), ('tarjeta', 'tarjeta'), ('transferencia', 'transferencia')], default='tarjeta', max_length=30),
        ),
        migrations.DeleteModel(
            name='Usuari',
        ),
    ]