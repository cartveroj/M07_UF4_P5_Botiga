from django.db import models
from enum import Enum
# Create your models here.

class Carreto(models.Model):
    tipo_pago =[
        ("paypal","paypal"),
        ("tarjeta","tarjeta"),
        ("transferencia","transferencia")
    ]
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()
    importe = models.DecimalField(max_digits=5, decimal_places=3)
    metodo_pago = models.CharField(max_length=30, choices=tipo_pago)