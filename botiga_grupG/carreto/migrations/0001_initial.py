# Generated by Django 5.0.3 on 2024-04-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carreto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('importe', models.DecimalField(decimal_places=3, max_digits=5)),
                ('metodo_pago', models.CharField(choices=[('paypal', 'paypal'), ('tarjeta', 'tarjeta'), ('transferencia', 'transferencia')], max_length=30)),
            ],
        )
    ]